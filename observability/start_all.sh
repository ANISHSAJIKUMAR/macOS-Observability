#!/usr/bin/env bash
set -euo pipefail

OBS_BASE="${OBS_BASE:-$(cd "$(dirname "$0")" && pwd)}"
ENV_FILE="${OBS_ENV_FILE:-$OBS_BASE/.env}"
LAUNCH_AGENTS_DIR="${LAUNCH_AGENTS_DIR:-$HOME/Library/LaunchAgents}"
LAUNCH_DAEMONS_DIR="${LAUNCH_DAEMONS_DIR:-/Library/LaunchDaemons}"
PROMTAIL_BIN="${PROMTAIL_BIN:-$HOME/.local/bin/promtail}"
if [ -f "$ENV_FILE" ]; then
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
fi
# Non-interactive: do not prompt for sudo
SUDO="sudo -n"
CAN_SUDO=1
if ! $SUDO -v > /dev/null 2>&1; then
  CAN_SUDO=0
fi

log() { printf "[start_all] %s\n" "$*"; }

log "Starting core services in order..."
# Start metrics first, then storage, then UI
brew services start node_exporter
brew services start prometheus
brew services start loki
brew services start grafana

log "Starting LaunchAgents..."
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
    launchctl bootout "$USER_DOMAIN" "$agent" > /dev/null 2>&1 || true
    launchctl bootstrap "$USER_DOMAIN" "$agent"
  fi
done

log "Starting Wi‑Fi LaunchDaemon (root) if available..."
if [ "$CAN_SUDO" -eq 1 ]; then
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.wdutil_metrics.plist" ]; then
    $SUDO launchctl bootstrap system "${LAUNCH_DAEMONS_DIR}/observability.wdutil_metrics.plist" || true
  fi
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.cpu_fan_metrics.plist" ]; then
    $SUDO launchctl bootstrap system "${LAUNCH_DAEMONS_DIR}/observability.cpu_fan_metrics.plist" || true
  fi
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.smart_metrics.plist" ]; then
    $SUDO launchctl bootstrap system "${LAUNCH_DAEMONS_DIR}/observability.smart_metrics.plist" || true
  fi
  if [ -x "$PROMTAIL_BIN" ] && [ -f "${LAUNCH_DAEMONS_DIR}/observability.promtail.plist" ]; then
    $SUDO launchctl bootstrap system "${LAUNCH_DAEMONS_DIR}/observability.promtail.plist" || true
  elif [ -f "${LAUNCH_DAEMONS_DIR}/observability.promtail.plist" ]; then
    log "Skipping promtail LaunchDaemon (binary missing at $PROMTAIL_BIN)."
  fi
  if [ -f "${LAUNCH_DAEMONS_DIR}/observability.tshark_metrics.plist" ]; then
    $SUDO launchctl bootstrap system "${LAUNCH_DAEMONS_DIR}/observability.tshark_metrics.plist" || true
  fi
else
  log "Skipping root LaunchDaemons (sudo -n not available)."
fi

log "Reloading Prometheus rules..."
if command -v curl > /dev/null 2>&1; then
  curl -sf -X POST http://localhost:9090/-/reload > /dev/null || true
fi

log "Status checks..."
if command -v curl > /dev/null 2>&1; then
  if curl -sf http://localhost:9090/-/ready > /dev/null; then
    log "Prometheus ready"
  else
    log "Prometheus not ready"
  fi
  if curl -sf http://localhost:9100/metrics > /dev/null; then
    log "node_exporter OK"
  else
    log "node_exporter not responding"
  fi
  LOKI_OK=0
  for _ in {1..10}; do
    if curl -sf http://localhost:3100/ready > /dev/null; then
      LOKI_OK=1
      break
    fi
    sleep 1
  done
  if [ "$LOKI_OK" -eq 1 ]; then
    log "Loki OK"
  else
    log "Loki not responding"
  fi
  # Grafana is HTTPS now
  if curl -skf https://localhost:3000/api/health > /dev/null; then
    log "Grafana OK"
  else
    log "Grafana not responding"
  fi
fi

log "All services started."
