# macOS Observatory - Setup Guide

This guide helps you set up the observability lab on your Mac with automatic path configuration.

## Prerequisites

### 1. Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Required Services
```bash
brew install prometheus grafana loki node_exporter promtail
```

## Quick Setup

### Option 1: Automated Setup (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/ANISHSAJIKUMAR/macos-observatory.git
cd macos-observatory/observability
```

2. Run the setup script:
```bash
./setup.sh
```

This will:
- ✅ Detect your project path automatically
- ✅ Configure Prometheus with correct paths
- ✅ Install LaunchAgents for auto-restart monitoring
- ✅ Set up all custom exporters
- ✅ Clean up metadata files

3. Start all services:
```bash
./start_all.sh
```

4. Access the dashboards:
- **Grafana**: http://localhost:3000 (Login: admin/admin)
- **Prometheus**: http://localhost:9090
- **Loki**: http://localhost:3100

### Option 2: Manual Setup

If you prefer manual configuration:

1. Clone the repository:
```bash
git clone https://github.com/ANISHSAJIKUMAR/macos-observatory.git
cd macos-observatory
```

2. Set your project path:
```bash
export PROJECT_PATH="$(pwd)"
```

3. Update Prometheus args:
```bash
cat > /opt/homebrew/etc/prometheus.args <<EOF
--config.file $PROJECT_PATH/observability/prometheus/prometheus.yml
--web.listen-address=127.0.0.1:9090
--storage.tsdb.path /opt/homebrew/var/prometheus
--storage.tsdb.retention.time=14d
--storage.tsdb.retention.size=20GB
--web.enable-lifecycle
EOF
```

4. Start services:
```bash
cd observability
./start_all.sh
```

## What Gets Configured

### Dynamic Paths
The setup script automatically configures:

1. **Prometheus Configuration** (`/opt/homebrew/etc/prometheus.args`)
   - Points to your local project directory
   - No hardcoded user paths

2. **Prometheus Rules** (`prometheus/prometheus.yml`)
   - Uses relative paths for rule files
   - Works from any clone location

3. **LaunchAgents** (`~/Library/LaunchAgents/`)
   - Custom exporters with your project path
   - Auto-restart health check for Prometheus

4. **Health Check Script** (`exporters/prometheus_healthcheck.sh`)
   - Uses `$HOME` variable (already portable)
   - No hardcoded paths

## Services Included

### Core Services (via Homebrew)
- **Prometheus** (port 9090) - Metrics collection
- **Grafana** (port 3000) - Visualization dashboard
- **Loki** (port 3100) - Log aggregation
- **node_exporter** (port 9100) - System metrics
- **Promtail** (port 9080) - Log shipper

### Custom Exporters (via LaunchAgents)
- Battery metrics
- CPU/Fan metrics
- Network connectivity
- System information
- VMware Fusion metrics
- **Prometheus health check** (auto-restart)

## Managing Services

### Start All Services
```bash
cd observability
./start_all.sh
```

### Stop All Services
```bash
./stop_all.sh
```

### Check Status
```bash
./status_all.sh
```

### Restart Individual Service
```bash
brew services restart prometheus
brew services restart grafana
```

## Auto-Restart Feature

The setup includes automatic Prometheus monitoring:

- ✅ Checks health every 60 seconds
- ✅ Auto-restarts if unhealthy
- ✅ Max 3 restart attempts (prevents loops)
- ✅ Full logging for debugging

### Monitor Auto-Restart
```bash
# View live logs
tail -f ~/Library/Logs/prometheus-healthcheck.log

# Check LaunchAgent status
launchctl list | grep prometheus_healthcheck
```

### Disable/Enable Auto-Restart
```bash
# Disable
launchctl unload ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist

# Enable
launchctl load ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist
```

## Grafana Setup

### First Time Setup

1. Open Grafana:
```bash
open http://localhost:3000
```

2. Login:
   - Username: `admin`
   - Password: `admin`
   - Change password when prompted

3. Add Data Sources:

   **Prometheus:**
   - Go to: Configuration → Data Sources
   - Click: Add data source
   - Select: Prometheus
   - URL: `http://localhost:9090`
   - Click: Save & Test

   **Loki:**
   - Add data source
   - Select: Loki
   - URL: `http://localhost:3100`
   - Click: Save & Test

4. Import Dashboards:
   - Go to: Create → Import
   - Try these IDs:
     - `1860` - Node Exporter Full
     - `13639` - Node Exporter for Prometheus
     - `12486` - Loki Logs

## Troubleshooting

### Services Won't Start

1. Check if ports are in use:
```bash
lsof -i :9090  # Prometheus
lsof -i :3000  # Grafana
lsof -i :3100  # Loki
```

2. Check service logs:
```bash
tail -50 /opt/homebrew/var/log/prometheus.log
tail -50 /opt/homebrew/var/log/grafana.log
```

3. Re-run setup:
```bash
./setup.sh
./start_all.sh
```

### Prometheus Not Starting

1. Validate config:
```bash
promtool check config prometheus/prometheus.yml
```

2. Check rule files:
```bash
promtool check rules prometheus/rules/*.yml
```

3. View error log:
```bash
tail -50 /opt/homebrew/var/log/prometheus.err.log
```

### Re-configure for Different Path

If you move the project:

1. Run setup again:
```bash
cd macos-observatory/observability
./setup.sh
```

2. Restart services:
```bash
./stop_all.sh
sleep 2
./start_all.sh
```

## Uninstall

To completely remove the observability lab:

1. Stop all services:
```bash
cd observability
./stop_all.sh
```

2. Remove LaunchAgents:
```bash
rm ~/Library/LaunchAgents/observability.*.plist
```

3. Uninstall Homebrew services (optional):
```bash
brew uninstall prometheus grafana loki node_exporter promtail
```

4. Remove project directory:
```bash
cd ..
rm -rf macos-observatory
```

## For Developers

### Project Structure
```
macos-observatory/
├── observability/
│   ├── setup.sh                    # Auto-configuration script
│   ├── start_all.sh               # Start all services
│   ├── stop_all.sh                # Stop all services
│   ├── status_all.sh              # Check service status
│   ├── prometheus/
│   │   ├── prometheus.yml         # Prometheus config (relative paths)
│   │   └── rules/*.yml            # Alert/recording rules
│   ├── grafana/
│   │   └── grafana.ini            # Grafana config
│   ├── loki/
│   │   └── loki-local-config.yaml # Loki config
│   ├── exporters/
│   │   ├── prometheus_healthcheck.sh  # Auto-restart script
│   │   └── *.py                       # Custom Python exporters
│   └── launchd/
│       └── observability.*.plist      # LaunchAgent configs
└── SETUP.md                           # This file
```

### Adding Custom Metrics

1. Create your exporter script in `exporters/`
2. Create a LaunchAgent plist in `launchd/`
3. Re-run `./setup.sh` to install

### Modifying Prometheus Rules

1. Edit files in `prometheus/rules/`
2. Validate:
```bash
promtool check rules prometheus/rules/*.yml
```
3. Reload Prometheus:
```bash
curl -X POST http://localhost:9090/-/reload
```

## Support

- **Issues**: https://github.com/ANISHSAJIKUMAR/macos-observatory/issues
- **Documentation**: See README.md in project root

## Version
1.0 - Portable configuration with auto-setup

## Created
September 27, 2026
