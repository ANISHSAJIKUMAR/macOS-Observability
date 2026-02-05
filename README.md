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
