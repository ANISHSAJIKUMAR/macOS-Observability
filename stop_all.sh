#!/usr/bin/env bash
set -euo pipefail

# Non-interactive: do not prompt for sudo
SUDO="sudo -n"
CAN_SUDO=1
if ! $SUDO -v >/dev/null 2>&1; then
  CAN_SUDO=0
fi

log() { printf "[stop_all] %s\n" "$*"; }

log "Stopping LaunchAgents..."
launchctl unload ~/Library/LaunchAgents/com.local.net_connectivity.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.mac_system_info.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.launchd_metrics.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.grafana_health.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.prom_config_checksum.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.battery_metrics.plist || true

log "Stopping Wi‑Fi LaunchDaemon (root) if available..."
if [ "$CAN_SUDO" -eq 1 ]; then
  if [ -f /Library/LaunchDaemons/com.local.wdutil_metrics.plist ]; then
    $SUDO launchctl bootout system /Library/LaunchDaemons/com.local.wdutil_metrics.plist || true
  fi
  if [ -f /Library/LaunchDaemons/com.local.cpu_fan_metrics.plist ]; then
    $SUDO launchctl bootout system /Library/LaunchDaemons/com.local.cpu_fan_metrics.plist || true
  fi
  if [ -f /Library/LaunchDaemons/com.local.smart_metrics.plist ]; then
    $SUDO launchctl bootout system /Library/LaunchDaemons/com.local.smart_metrics.plist || true
  fi
else
  log "Skipping root LaunchDaemons (sudo -n not available)."
fi

log "Stopping core services in order..."
# Stop UI first, then storage, then exporters
brew services stop grafana || true
brew services stop prometheus || true
brew services stop node_exporter || true

log "Status checks..."
if command -v curl >/dev/null 2>&1; then
  curl -sf http://localhost:9090/-/ready >/dev/null && log "Prometheus still running" || log "Prometheus stopped"
  curl -sf http://localhost:9100/metrics >/dev/null && log "node_exporter still running" || log "node_exporter stopped"
  curl -skf https://localhost:3000/api/health >/dev/null && log "Grafana still running" || log "Grafana stopped"
fi

log "All services stopped."
