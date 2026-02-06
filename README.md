# Anish DevOps Lab

Personal DevOps workspace for my Mac. The primary project is a full local **observability** stack (metrics + logs + dashboards) built for interview demos and daily monitoring.

## Quick Start / Stop
Use these scripts to start or stop everything without deleting any data:

```bash
./stop_all.sh
./start_all.sh
./status_all.sh
```

## Observability Folder (Summary)
Location:
```
/Users/anishskumar/Anish-DevOps-Lab/observability
```

What it contains:
- Prometheus + Grafana configuration
- Loki + Promtail log pipeline
- node_exporter configuration
- Custom exporters (network, system info, launchd, Wi‑Fi, battery, thermal, SMART, tshark)
- Dashboard backups and documentation

Docs:
- Full setup, architecture, and demo flow:
  `/Users/anishskumar/Anish-DevOps-Lab/observability/README.md`

## Notes
- Grafana runs on HTTPS with a self‑signed certificate.
- Root LaunchDaemons (Wi‑Fi, SMART, fan/thermal, promtail, tshark) require sudo.
- Use `sudo -v` once per session if you want root exporters to start from `start_all.sh`.

## Folder Structure (Top Level)
- `observability/` — full monitoring stack (metrics + logs)
- `output/` — generated artifacts (screenshots/exports)
- `start_all.sh` / `stop_all.sh` — start/stop everything

## Demo Links (Quick Navigation)
- Overview: https://localhost:3000/d/overview/anish-laptop3a-overview
- Executive Summary: https://localhost:3000/d/exec-summary/executive-summary3a-anish-laptop
- System Health: https://localhost:3000/d/mac-system-all/mac-system3a-core-health
- Network & Wi‑Fi: https://localhost:3000/d/mac-network/mac-network3a-connectivity-and-wie28091-fi
- Live Capture (tshark): https://localhost:3000/d/tshark-live/mac-network3a-live-capture-tshark
- Logs: https://localhost:3000/d/mac-logs/mac-logs3a-system-apps-and-observability
- Security: https://localhost:3000/d/mac-security/mac-security3a-activity-and-risk-signals
- Prometheus Self‑Monitoring: https://localhost:3000/d/prometheus-self/prometheus3a-selfe28091-monitoring
- All Metrics Explorer: https://localhost:3000/d/all-metrics-full/all-metrics3a-live-explorer

## Health Checks (CLI)
```bash
curl -sf http://localhost:9090/-/ready
curl -sf http://localhost:9100/metrics | head -n 5
curl -sf http://localhost:3100/ready
curl -skf https://localhost:3000/api/health
```

## Useful Commands
```bash
# List service status
brew services list | egrep 'grafana|prometheus|loki|node_exporter'

# Restart core services
brew services restart node_exporter
brew services restart prometheus
brew services restart loki
brew services restart grafana

# Check LaunchAgent status (user)
launchctl print gui/$(id -u)/observability.net_connectivity

# Check LaunchDaemon status (root)
sudo launchctl print system/observability.wdutil_metrics
```
