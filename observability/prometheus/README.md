# Prometheus Configuration (Full Detail)

## Files
- `prometheus.yml` — scrape configuration (targets + jobs)
- `prometheus.args` — runtime flags used by Homebrew service

## prometheus.yml (Line‑by‑Line)
```
/Users/anishskumar/Anish-DevOps-Lab/observability/prometheus/prometheus.yml
```

Current contents and explanations:

```yaml
global:
  scrape_interval: 15s
```
- **global**: global defaults for all scrape jobs.
- **scrape_interval: 15s**: scrape targets every 15 seconds.

```yaml
scrape_configs:
  - job_name: "prometheus"
    static_configs:
    - targets: ["localhost:9090"]
```
- **job_name: prometheus**: the self‑scrape job for Prometheus.
- **targets: ["localhost:9090"]**: scrape the local Prometheus server.

```yaml
  - job_name: "node_exporter"
    static_configs:
    - targets: ["localhost:9100"]
```
- **job_name: node_exporter**: scrape system metrics from node_exporter.
- **targets: ["localhost:9100"]**: the node_exporter HTTP endpoint.

## prometheus.args (Line‑by‑Line)
```
/Users/anishskumar/Anish-DevOps-Lab/observability/prometheus/prometheus.args
```

Current values and meanings:
```
--config.file /Users/anishskumar/Anish-DevOps-Lab/observability/prometheus/prometheus.yml
```
- Use this Prometheus config file.

```
--web.listen-address=127.0.0.1:9090
```
- Prometheus listens only on localhost.

```
--storage.tsdb.path /opt/homebrew/var/prometheus
```
- Prometheus stores TSDB data here.

```
--storage.tsdb.retention.time=14d
```
- Keep only 14 days of data.

```
--storage.tsdb.retention.size=20GB
```
- Limit total storage to 20 GB.

```
--storage.tsdb.min-block-duration=2h
```
- Block compaction lower bound (smaller blocks).

```
--storage.tsdb.max-block-duration=24h
```
- Block compaction upper bound (larger blocks).

## Safe Changes
- Add new scrape jobs in `prometheus.yml`
- Adjust retention time/size in `prometheus.args`
- Add or edit rules in `rules/recording.yml`
- Add or edit alerts in `rules/alerts.yml`

## Apply Changes
```bash
brew services restart prometheus
```

## Troubleshooting
- Check targets: `http://localhost:9090/targets`
- Check Prometheus health: `http://localhost:9090/-/healthy`
 - Check active rules: `http://localhost:9090/rules`
