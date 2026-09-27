#!/usr/bin/env bash
# Stop Promtail LaunchDaemon (requires sudo)

set -euo pipefail

DAEMON_DIR="/Library/LaunchDaemons"
PLIST_FILE="$DAEMON_DIR/observability.promtail.plist"

echo "Stopping Promtail..."
echo ""

if [ ! -f "$PLIST_FILE" ]; then
    echo "⚠️  Promtail LaunchDaemon not installed"
    exit 0
fi

# Unload LaunchDaemon
echo "Unloading LaunchDaemon (requires sudo)..."
sudo launchctl bootout system "$PLIST_FILE" 2>&1 || echo "Already unloaded"

# Remove plist
echo "Removing LaunchDaemon..."
sudo rm -f "$PLIST_FILE"

echo ""
echo "✅ Promtail stopped and removed!"
echo ""
