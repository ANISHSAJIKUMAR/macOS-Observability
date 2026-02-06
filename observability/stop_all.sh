#!/usr/bin/env bash
set -euo pipefail

OBS_BASE="${OBS_BASE:-$(cd "$(dirname "$0")" && pwd)}"
ENV_FILE="${OBS_ENV_FILE:-$OBS_BASE/.env}"
LAUNCH_AGENTS_DIR="${LAUNCH_AGENTS_DIR:-$HOME/Library/LaunchAgents}"
LAUNCH_DAEMONS_DIR="${LAUNCH_DAEMONS_DIR:-/Library/LaunchDaemons}"
if [ -f "$ENV_FILE" ]; then
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
fi
# Non-interactive: do not prompt for sudo
SUDO="sudo -n"
CAN_SUDO=1
if ! $SUDO -v >/dev/null 2>&1; then
  CAN_SUDO=0
fi

log() { printf "[stop_all] %s\n" "$*"; }

log "Stopping LaunchAgents..."
USER_DOMAIN="gui/$(id -u)"
LAUNCH_AGENTS=(
  "${LAUNCH_AGENTS_DIR}/observability.net_connectivity.plist"
  "${LAUNCH_AGENTS_DIR}/observability.mac_system_info.plist"
  "${LAUNCH_AGENTS_DIR}/observability.launchd_metrics.plist"
  "${LAUNCH_AGENTS_DIR}/observability.grafana_health.plist"
  "${LAUNCH_AGENTS_DIR}/observability.prom_config_checksum.plist"
  "${LAUNCH_AGENTS_DIR}/observability.battery_metrics.plist"
  "${LAUNCH_AGENTS_DIR}/observability.vmware_fusion_metrics.plist"
)
for agent in "${LAUNCH_AGENTS[@]}"; do
  if [ -f "$agent" ]; then
    launchctl bootout "$USER_DOMAIN" "$agent" >/dev/null 2>&1 || true
  fi
done

log "Stopping Wi‑Fi LaunchDaemon (root) if available..."
if [ "$CAN_SUDO" -eq 1 ]; then
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.wdutil_metrics.plist" ]; then
    $SUDO launchctl bootout system "${LAUNCH_DAEMONS_DIR}/observability.wdutil_metrics.plist" || true
  fi
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.cpu_fan_metrics.plist" ]; then
    $SUDO launchctl bootout system "${LAUNCH_DAEMONS_DIR}/observability.cpu_fan_metrics.plist" || true
  fi
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.smart_metrics.plist" ]; then
    $SUDO launchctl bootout system "${LAUNCH_DAEMONS_DIR}/observability.smart_metrics.plist" || true
  fi
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.promtail.plist" ]; then
    $SUDO launchctl bootout system "${LAUNCH_DAEMONS_DIR}/observability.promtail.plist" || true
  fi
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.tshark_metrics.plist" ]; then
    $SUDO launchctl bootout system "${LAUNCH_DAEMONS_DIR}/observability.tshark_metrics.plist" || true
  fi
else
  log "Skipping root LaunchDaemons (sudo -n not available)."
fi

log "Stopping core services in order..."
# Stop UI first, then storage, then exporters
brew services stop grafana || true
brew services stop loki || true
brew services stop prometheus || true
brew services stop node_exporter || true

log "Status checks..."
if command -v curl >/dev/null 2>&1; then
  if curl -sf http://localhost:9090/-/ready >/dev/null; then
    log "Prometheus still running"
  else
    log "Prometheus stopped"
  fi
  if curl -sf http://localhost:9100/metrics >/dev/null; then
    log "node_exporter still running"
  else
    log "node_exporter stopped"
  fi
  if curl -sf http://localhost:3100/ready >/dev/null; then
    log "Loki still running"
  else
    log "Loki stopped"
  fi
  if curl -skf https://localhost:3000/api/health >/dev/null; then
    log "Grafana still running"
  else
    log "Grafana stopped"
  fi
fi

log "All services stopped."
