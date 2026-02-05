# Grafana Configuration (Full Detail)

## Files
- `grafana.ini` — main Grafana config
- `grafana.ini.annotated.md` — line‑by‑line explanation of the current config
- `dashboards/` — dashboard JSON backups

## grafana.ini (Line‑by‑Line)
```
/Users/anishskumar/Anish-DevOps-Lab/observability/grafana/grafana.ini
```

Full annotation:
```
/Users/anishskumar/Anish-DevOps-Lab/observability/grafana/grafana.ini.annotated.md
```

## Key Settings (Quick Reference)
- `http_port = 3000` → Grafana listens on port 3000
- `data = /opt/homebrew/var/lib/grafana` → data storage
- `logs = /opt/homebrew/var/log/grafana` → log directory
- `plugins = /opt/homebrew/var/lib/grafana/plugins` → plugin directory

## Safe Changes
- Change `http_port`
- Enable plugins
- Update security/auth sections

## Apply Changes
```bash
brew services restart grafana
```

## Troubleshooting
- Health check: `http://localhost:3000/api/health`
- Logs: `/opt/homebrew/var/log/grafana`
