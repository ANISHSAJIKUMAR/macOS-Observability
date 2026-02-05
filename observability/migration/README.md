# Migration & Containerization

This folder provides a **ready-to-use Docker setup** plus instructions for running the stack on a **new Mac** without Docker.

## A) Docker (Containerized)

### 1. Requirements
- Docker Desktop
- `docker compose` (included with Docker Desktop)

### 2. Start
```bash
cd /Users/anishskumar/Anish-DevOps-Lab/observability/migration

docker compose up -d
```

### 3. URLs
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- node_exporter: http://localhost:9100/metrics
- Loki: http://localhost:3100 (if enabled)
- tshark live capture: dashboard only (requires root daemon on macOS)

### 4. Notes
- Grafana in Docker uses **HTTP** (no HTTPS by default).
- Dashboards are auto-provisioned into folder **Anish Laptop**.
- Default Grafana creds (change immediately):
  - user: `admin`
  - pass: `changeme`

### 5. Stop
```bash
docker compose down
```

---

## B) New Mac (Non‑Docker, permanent setup)

### 1. Requirements
- Homebrew installed

### 2. Install
```bash
brew install prometheus grafana node_exporter smartmontools loki promtail wireshark
```

Note: `wireshark` installs `tshark` (CLI) which is required for the Live Capture dashboard.

### 3. Copy configs
Clone the repo and keep it in:
```
~/Anish-DevOps-Lab
```

Ensure these paths exist:
```
~/Anish-DevOps-Lab/observability
```

### 4. Update paths (user-specific)
If your username is not `anishskumar`, replace paths in configs:
```
/Users/anishskumar/Anish-DevOps-Lab → /Users/<your_user>/Anish-DevOps-Lab
```

Files to update:
- `observability/prometheus/prometheus.yml`
- `observability/prometheus/prometheus.args`
- `observability/node_exporter/node_exporter.args`
- `observability/launchd/*.plist`
- `observability/exporters/*.py`

### 5. Start services
```bash
brew services start prometheus
brew services start grafana
brew services start node_exporter
brew services start loki
```

### 6. Load launchd jobs
```bash
launchctl load ~/Library/LaunchAgents/observability.net_connectivity.plist
launchctl load ~/Library/LaunchAgents/observability.mac_system_info.plist
launchctl load ~/Library/LaunchAgents/observability.launchd_metrics.plist
launchctl load ~/Library/LaunchAgents/observability.grafana_health.plist
launchctl load ~/Library/LaunchAgents/observability.prom_config_checksum.plist
launchctl load ~/Library/LaunchAgents/observability.battery_metrics.plist

# root daemons (Wi‑Fi / SMART / Thermal)
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.wdutil_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.cpu_fan_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.smart_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.promtail.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.tshark_metrics.plist
```

### 7. Verify
```bash
curl http://localhost:9090/-/ready
curl http://localhost:9100/metrics
curl http://localhost:3100/ready
```

---

## Notes
- Docker version is **for demo/testing** only.
- The non‑Docker setup is the **recommended permanent install** on macOS.
