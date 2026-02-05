#!/usr/bin/env bash
set -euo pipefail

# Non-interactive: do not prompt for sudo
SUDO="sudo -n"
CAN_SUDO=1
if ! $SUDO -v >/dev/null 2>&1; then
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
launchctl load ~/Library/LaunchAgents/observability.net_connectivity.plist
launchctl load ~/Library/LaunchAgents/observability.mac_system_info.plist
launchctl load ~/Library/LaunchAgents/observability.launchd_metrics.plist
launchctl load ~/Library/LaunchAgents/observability.grafana_health.plist
launchctl load ~/Library/LaunchAgents/observability.prom_config_checksum.plist
launchctl load ~/Library/LaunchAgents/observability.battery_metrics.plist
launchctl load ~/Library/LaunchAgents/observability.airport_metrics.plist

log "Starting Wi‑Fi LaunchDaemon (root) if available..."
if [ "$CAN_SUDO" -eq 1 ]; then
  if [ -f /Library/LaunchDaemons/observability.wdutil_metrics.plist ]; then
    $SUDO launchctl bootstrap system /Library/LaunchDaemons/observability.wdutil_metrics.plist || true
  fi
  if [ -f /Library/LaunchDaemons/observability.cpu_fan_metrics.plist ]; then
    $SUDO launchctl bootstrap system /Library/LaunchDaemons/observability.cpu_fan_metrics.plist || true
  fi
  if [ -f /Library/LaunchDaemons/observability.smart_metrics.plist ]; then
    $SUDO launchctl bootstrap system /Library/LaunchDaemons/observability.smart_metrics.plist || true
  fi
  if [ -f /Library/LaunchDaemons/observability.promtail.plist ]; then
    $SUDO launchctl bootstrap system /Library/LaunchDaemons/observability.promtail.plist || true
  fi
  if [ -f /Library/LaunchDaemons/observability.tshark_metrics.plist ]; then
    $SUDO launchctl bootstrap system /Library/LaunchDaemons/observability.tshark_metrics.plist || true
  fi
else
  log "Skipping root LaunchDaemons (sudo -n not available)."
fi

log "Reloading Prometheus rules..."
if command -v curl >/dev/null 2>&1; then
  curl -sf -X POST http://localhost:9090/-/reload >/dev/null || true
fi

log "Status checks..."
if command -v curl >/dev/null 2>&1; then
  curl -sf http://localhost:9090/-/ready >/dev/null && log "Prometheus ready" || log "Prometheus not ready"
  curl -sf http://localhost:9100/metrics >/dev/null && log "node_exporter OK" || log "node_exporter not responding"
  curl -sf http://localhost:3100/ready >/dev/null && log "Loki OK" || log "Loki not responding"
  # Grafana is HTTPS now
  curl -skf https://localhost:3000/api/health >/dev/null && log "Grafana OK" || log "Grafana not responding"
fi

log "All services started."
