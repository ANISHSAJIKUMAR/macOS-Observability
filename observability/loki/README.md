# Loki (Log Storage)

## Purpose
Local log storage so Grafana can search system/app/observability logs.

## Files
- `loki-config.yml` — Loki config (storage, retention, ports)

## Apply Changes
```bash
brew services restart loki
```

## Troubleshooting
- Loki health: `http://localhost:3100/ready`
- Loki metrics: `http://localhost:3100/metrics`
