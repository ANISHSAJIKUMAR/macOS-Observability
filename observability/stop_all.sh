#!/usr/bin/env bash
set -euo pipefail

OBS_BASE="${OBS_BASE:-$(cd "$(dirname "$0")" && pwd)}"
ENV_FILE="${OBS_ENV_FILE:-$OBS_BASE/.env}"
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
  "$HOME/Library/LaunchAgents/observability.net_connectivity.plist"
  "$HOME/Library/LaunchAgents/observability.mac_system_info.plist"
  "$HOME/Library/LaunchAgents/observability.launchd_metrics.plist"
  "$HOME/Library/LaunchAgents/observability.grafana_health.plist"
  "$HOME/Library/LaunchAgents/observability.prom_config_checksum.plist"
  "$HOME/Library/LaunchAgents/observability.battery_metrics.plist"
  "$HOME/Library/LaunchAgents/observability.vmware_fusion_metrics.plist"
)
for agent in "${LAUNCH_AGENTS[@]}"; do
  if [ -f "$agent" ]; then
    launchctl bootout "$USER_DOMAIN" "$agent" >/dev/null 2>&1 || true
  fi
done

log "Stopping Wi‑Fi LaunchDaemon (root) if available..."
if [ "$CAN_SUDO" -eq 1 ]; then
  if [ -f /Library/LaunchDaemons/observability.wdutil_metrics.plist ]; then
    $SUDO launchctl bootout system /Library/LaunchDaemons/observability.wdutil_metrics.plist || true
  fi
  if [ -f /Library/LaunchDaemons/observability.cpu_fan_metrics.plist ]; then
    $SUDO launchctl bootout system /Library/LaunchDaemons/observability.cpu_fan_metrics.plist || true
  fi
  if [ -f /Library/LaunchDaemons/observability.smart_metrics.plist ]; then
    $SUDO launchctl bootout system /Library/LaunchDaemons/observability.smart_metrics.plist || true
  fi
  if [ -f /Library/LaunchDaemons/observability.promtail.plist ]; then
    $SUDO launchctl bootout system /Library/LaunchDaemons/observability.promtail.plist || true
  fi
  if [ -f /Library/LaunchDaemons/observability.tshark_metrics.plist ]; then
    $SUDO launchctl bootout system /Library/LaunchDaemons/observability.tshark_metrics.plist || true
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
  curl -sf http://localhost:9090/-/ready >/dev/null && log "Prometheus still running" || log "Prometheus stopped"
  curl -sf http://localhost:9100/metrics >/dev/null && log "node_exporter still running" || log "node_exporter stopped"
  curl -sf http://localhost:3100/ready >/dev/null && log "Loki still running" || log "Loki stopped"
  curl -skf https://localhost:3000/api/health >/dev/null && log "Grafana still running" || log "Grafana stopped"
fi

log "All services stopped."