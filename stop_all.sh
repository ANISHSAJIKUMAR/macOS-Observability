#!/usr/bin/env bash
set -euo pipefail

echo "Stopping LaunchAgents..."
launchctl unload ~/Library/LaunchAgents/com.local.net_connectivity.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.mac_system_info.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.launchd_metrics.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.grafana_health.plist || true
launchctl unload ~/Library/LaunchAgents/com.local.prom_config_checksum.plist || true

if [ -f /Library/LaunchDaemons/com.local.wdutil_metrics.plist ]; then
  echo "Stopping Wi-Fi LaunchDaemon (root)..."
  sudo launchctl bootout system /Library/LaunchDaemons/com.local.wdutil_metrics.plist || true
fi

echo "Stopping core services..."
brew services stop grafana || true
brew services stop prometheus || true
brew services stop node_exporter || true

echo "All services stopped."
