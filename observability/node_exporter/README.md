# node_exporter Configuration (Full Detail)

## Files
- `node_exporter.args`

## node_exporter.args (Line‑by‑Line)
```
/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/node_exporter.args
```

Current values:
```
--collector.textfile.directory=/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/textfile
```
- Enables the textfile collector and points to the directory where custom exporters write `.prom` files.

## Safe Changes
- Add/remove node_exporter collectors via flags
- Change textfile directory (must also update exporter scripts)

## Apply Changes
```bash
brew services restart node_exporter
```
