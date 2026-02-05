# Promtail (Log Collector)

## Purpose
Tails system and app logs and ships them to Loki for Grafana to query.

## Files
- `promtail-config.yml` — Promtail scrape targets and labels
- `positions.yaml` — runtime offsets (generated, not committed)

## Apply Changes
```bash
sudo launchctl bootout system /Library/LaunchDaemons/com.local.promtail.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.local.promtail.plist
```

## Troubleshooting
- Promtail metrics: `http://localhost:9080/metrics`
