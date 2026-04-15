# Grafana Configuration (Full Detail)

## Files
- `grafana.ini` — local Grafana config (not committed)
- `grafana.ini.template` — committed template of the current config
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

## HTTPS (Self‑Signed)
Grafana is configured for local HTTPS using a self‑signed certificate:
```
/Users/anishskumar/Anish-DevOps-Lab/observability/grafana/certs/localhost.crt
/Users/anishskumar/Anish-DevOps-Lab/observability/grafana/certs/localhost.key
```
Browser will show a warning the first time; accept the certificate for local use.

## Key Settings (Quick Reference)
- `http_port = 3000` → Grafana listens on port 3000
- `protocol = https` → HTTPS enabled locally
- `cert_file` / `cert_key` → local TLS certificate and key
- `dataproxy.timeout = 30` → data source query timeout (seconds)
- `query.concurrent_query_limit = 20` → limits mixed query concurrency
- `datasources.concurrent_query_count = 5` → limits datasource concurrency
- `default_theme = dark` → dark UI theme by default
- `default_home_dashboard_path` → Overview dashboard is the landing page
- `remote_cache.type = database` + `encryption = true` → cached data stored safely
- `data = /opt/homebrew/var/lib/grafana` → data storage
- `logs = /opt/homebrew/var/log/grafana` → log directory
- `plugins = /opt/homebrew/var/lib/grafana/plugins` → plugin directory
- Loki datasource added for log search

## Safe Changes
- Change `http_port`
- Enable plugins
- Update security/auth sections

## Apply Changes
```bash
brew services restart grafana
```

## Troubleshooting
- Health check: `https://localhost:3000/api/health`
- Logs: `/opt/homebrew/var/log/grafana`
