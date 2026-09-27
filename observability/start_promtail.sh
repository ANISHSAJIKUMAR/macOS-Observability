#!/usr/bin/env bash
# Start Promtail as LaunchDaemon (requires sudo)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PROMTAIL_PLIST="$SCRIPT_DIR/launchd/observability.promtail.plist"
DAEMON_DIR="/Library/LaunchDaemons"

echo "Starting Promtail for macOS Observatory..."
echo ""

# Check if promtail binary exists
if [ ! -f "$HOME/.local/bin/promtail" ]; then
    echo "❌ Promtail binary not found at: $HOME/.local/bin/promtail"
    echo ""
    echo "To install promtail:"
    echo "  brew install promtail"
    echo "  # Or download from: https://github.com/grafana/loki/releases"
    exit 1
fi

echo "✓ Promtail binary found"

# Update paths in plist
mkdir -p /tmp
TEMP_PLIST="/tmp/observability.promtail.plist.$$"
sed "s|PROJECT_ROOT_PLACEHOLDER|$PROJECT_ROOT|g" "$PROMTAIL_PLIST" > "$TEMP_PLIST"

echo "✓ Updated paths for current installation"
echo ""

# Install LaunchDaemon (requires sudo)
echo "Installing Promtail LaunchDaemon (requires sudo)..."
sudo cp "$TEMP_PLIST" "$DAEMON_DIR/observability.promtail.plist"
sudo chown root:wheel "$DAEMON_DIR/observability.promtail.plist"
sudo chmod 644 "$DAEMON_DIR/observability.promtail.plist"

echo "✓ LaunchDaemon installed"

# Load LaunchDaemon
echo "Loading LaunchDaemon..."
sudo launchctl bootstrap system "$DAEMON_DIR/observability.promtail.plist" 2>&1 || echo "Already loaded"

echo ""
echo "✅ Promtail started!"
echo ""
echo "Check status:"
echo "  sudo launchctl list | grep promtail"
echo ""
echo "Check logs:"
echo "  tail -f $PROJECT_ROOT/.local/var/log/promtail.log"
echo ""
