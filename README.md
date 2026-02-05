# Anish DevOps Lab

This is my personal DevOps workspace. The main project here is **observability** for my Mac laptop.

## Quick Start / Stop
Use these scripts to stop or start everything without deleting anything:

```bash
./stop_all.sh
./start_all.sh
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
- Custom exporters (network, system info, launchd, Wi‑Fi)
- Dashboard backups and documentation

Docs:
- Full setup and architecture are documented in:
  `/Users/anishskumar/Anish-DevOps-Lab/observability/README.md`

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
