#!/usr/bin/env bash
# Setup script for DevOps Observability Lab
# Makes the project work on any Mac with dynamic paths

set -euo pipefail

# Get the absolute path to the project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OBSERVABILITY_DIR="$SCRIPT_DIR"

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║     DevOps Observability Lab - Setup Script                      ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""
echo "Project root: $PROJECT_ROOT"
echo "Observability dir: $OBSERVABILITY_DIR"
echo ""

# Check prerequisites
echo "📋 Checking prerequisites..."
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Please install: https://brew.sh"
    exit 1
fi
echo "✓ Homebrew installed"

# Check for required services
for service in prometheus grafana loki node_exporter; do
    if brew list "$service" &>/dev/null; then
        echo "✓ $service installed"
    else
        echo "⚠️  $service not installed. Run: brew install $service"
    fi
done

echo ""
echo "🔧 Configuring Prometheus with dynamic paths..."

# Update Prometheus brew service args
PROM_ARGS_FILE="/opt/homebrew/etc/prometheus.args"
if [ -f "$PROM_ARGS_FILE" ]; then
    cat > "$PROM_ARGS_FILE" <<EOF
--config.file $OBSERVABILITY_DIR/prometheus/prometheus.yml
--web.listen-address=127.0.0.1:9090
--storage.tsdb.path /opt/homebrew/var/prometheus
--storage.tsdb.retention.time=14d
--storage.tsdb.retention.size=20GB
--storage.tsdb.min-block-duration=2h
--storage.tsdb.max-block-duration=24h
--web.enable-lifecycle
EOF
    echo "✓ Updated Prometheus config path: $OBSERVABILITY_DIR/prometheus/prometheus.yml"
else
    echo "⚠️  Prometheus args file not found. Run: brew install prometheus"
fi

# Update prometheus.yml with dynamic paths
PROM_CONFIG="$OBSERVABILITY_DIR/prometheus/prometheus.yml"
if [ -f "$PROM_CONFIG" ]; then
    # Create a backup
    cp "$PROM_CONFIG" "$PROM_CONFIG.bak"

    # Update rule_files path to be relative
    sed -i.tmp "s|rule_files:.*|rule_files:|" "$PROM_CONFIG"
    sed -i.tmp "s|  - /Users/.*/rules/\*\.yml|  - $OBSERVABILITY_DIR/prometheus/rules/*.yml|" "$PROM_CONFIG"
    rm -f "$PROM_CONFIG.tmp"

    echo "✓ Updated Prometheus rule_files path"
else
    echo "⚠️  prometheus.yml not found at $PROM_CONFIG"
fi

# Update LaunchAgents with dynamic paths
echo ""
echo "🚀 Configuring LaunchAgents..."

# Update prometheus health check LaunchAgent
HEALTHCHECK_PLIST="$OBSERVABILITY_DIR/launchd/observability.prometheus_healthcheck.plist"
if [ -f "$HEALTHCHECK_PLIST" ]; then
    # Update the script path in the plist
    sed -i.bak "s|<string>/Users/[^<]*/Projects/Active/devops-observability-lab/|<string>$PROJECT_ROOT/|g" "$HEALTHCHECK_PLIST"
    echo "✓ Updated prometheus_healthcheck.plist"
fi

# Update health check script paths (for logging)
HEALTHCHECK_SCRIPT="$OBSERVABILITY_DIR/exporters/prometheus_healthcheck.sh"
if [ -f "$HEALTHCHECK_SCRIPT" ]; then
    echo "✓ Health check script found (uses \$HOME variable, already portable)"
fi

# Install/Update LaunchAgents
echo ""
echo "📦 Installing LaunchAgents..."
for plist in "$OBSERVABILITY_DIR/launchd"/observability.*.plist; do
    if [ -f "$plist" ]; then
        plist_name=$(basename "$plist")
        # Update paths in plist before copying
        sed "s|/Users/[^/]*/Projects/Active/devops-observability-lab/|$PROJECT_ROOT/|g" "$plist" > "$HOME/Library/LaunchAgents/$plist_name"

        # Reload the LaunchAgent
        launchctl unload "$HOME/Library/LaunchAgents/$plist_name" 2>/dev/null || true
        launchctl load "$HOME/Library/LaunchAgents/$plist_name"
        echo "  ✓ Installed $plist_name"
    fi
done

echo ""
echo "🧹 Cleaning up metadata files..."
find "$OBSERVABILITY_DIR" -name "._*" -type f -delete 2>/dev/null || true
echo "✓ Removed macOS metadata files"

echo ""
echo "📊 Configuring Grafana provisioning..."

# Create provisioning directories if they don't exist
mkdir -p "$OBSERVABILITY_DIR/grafana/provisioning/datasources"
mkdir -p "$OBSERVABILITY_DIR/grafana/provisioning/dashboards"
echo "✓ Created provisioning directories"

# Create datasource provisioning config
cat > "$OBSERVABILITY_DIR/grafana/provisioning/datasources/prometheus.yml" <<EOF
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://localhost:9090
    isDefault: true
    editable: true
    jsonData:
      timeInterval: 15s
EOF
echo "✓ Created Prometheus datasource config"

# Create dashboard provisioning config
cat > "$OBSERVABILITY_DIR/grafana/provisioning/dashboards/dashboards.yml" <<EOF
apiVersion: 1

providers:
  - name: 'macOS Observatory Dashboards'
    orgId: 1
    folder: ''
    type: file
    disableDeletion: false
    updateIntervalSeconds: 10
    allowUiUpdates: true
    options:
      path: $OBSERVABILITY_DIR/grafana/dashboards
      foldersFromFilesStructure: false
EOF
echo "✓ Created dashboard provisioning config"

# Update brew Grafana config to use provisioning
BREW_GRAFANA_CONFIG="/opt/homebrew/etc/grafana/grafana.ini"
if [ -f "$BREW_GRAFANA_CONFIG" ]; then
    # Backup original config
    sudo cp "$BREW_GRAFANA_CONFIG" "$BREW_GRAFANA_CONFIG.backup" 2>/dev/null || true

    # Check if provisioning path already set
    if ! grep -q "^provisioning = " "$BREW_GRAFANA_CONFIG"; then
        # Add provisioning path after [paths] section
        sudo sed -i.tmp "/^\[paths\]/a\\
provisioning = $OBSERVABILITY_DIR/grafana/provisioning
" "$BREW_GRAFANA_CONFIG" 2>/dev/null || echo "⚠️  Could not update Grafana config (needs sudo)"
        sudo rm -f "$BREW_GRAFANA_CONFIG.tmp" 2>/dev/null || true
        echo "✓ Updated Grafana config with provisioning path"
    else
        echo "✓ Grafana provisioning already configured"
    fi
fi

# Reset Grafana admin password to default
echo ""
echo "🔐 Resetting Grafana admin password..."
if brew services list | grep -q "grafana.*started"; then
    brew services stop grafana >/dev/null 2>&1
    sleep 2
fi

# Reset password using grafana-cli
/opt/homebrew/opt/grafana/bin/grafana cli \
    --homepath /opt/homebrew/opt/grafana/share/grafana \
    --config /opt/homebrew/etc/grafana/grafana.ini \
    admin reset-admin-password admin >/dev/null 2>&1 || echo "⚠️  Could not reset password (might be first time setup)"

echo "✓ Grafana password set to: admin"

echo ""
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║                  ✅ Setup Complete!                              ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""
echo "📊 Next steps:"
echo ""
echo "1. Start all services:"
echo "   ./start_all.sh"
echo ""
echo "2. Check status:"
echo "   ./status_all.sh"
echo ""
echo "3. Access Grafana:"
echo "   open http://localhost:3000"
echo "   👤 Login: admin / admin"
echo "   📊 11 dashboards auto-loaded!"
echo ""
echo "4. Access Prometheus:"
echo "   open http://localhost:9090"
echo ""
echo "📝 Note: Paths are now configured for this machine:"
echo "   $PROJECT_ROOT"
echo ""
echo "💡 Auto-restart monitoring is active!"
echo "   Monitor: tail -f ~/Library/Logs/prometheus-healthcheck.log"
echo ""
