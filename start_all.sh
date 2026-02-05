#!/usr/bin/env bash
set -euo pipefail

echo "Starting core services..."
brew services start prometheus
brew services start grafana
brew services start node_exporter

echo "Starting LaunchAgents..."
launchctl load ~/Library/LaunchAgents/com.local.net_connectivity.plist
launchctl load ~/Library/LaunchAgents/com.local.mac_system_info.plist
launchctl load ~/Library/LaunchAgents/com.local.launchd_metrics.plist
launchctl load ~/Library/LaunchAgents/com.local.grafana_health.plist
launchctl load ~/Library/LaunchAgents/com.local.prom_config_checksum.plist

if [ -f /Library/LaunchDaemons/com.local.wdutil_metrics.plist ]; then
  echo "Starting Wi-Fi LaunchDaemon (root)..."
  sudo launchctl bootstrap system /Library/LaunchDaemons/com.local.wdutil_metrics.plist
fi

echo "All services started."
