# Anish Laptop Observability (Complete Guide)

Single source of truth for the full local monitoring stack on this Mac.
Includes configuration, dashboards, exporters, and demo flow.

## Tech Stack
- Prometheus (metrics storage)
- Grafana (dashboards + visualization)
- Loki (log storage)
- Promtail (log collector)
- node_exporter (system metrics)
- Custom Python exporters (network, system info, launchd, Wi‑Fi, battery, thermal, SMART, Grafana health, tshark)
- launchd / LaunchDaemon (scheduling & background services)

## UI & Performance Tuning
- Grafana uses HTTPS locally with a self‑signed certificate.
- Data proxy timeout: 30s
- Query concurrency limits set to reduce CPU usage
- Remote cache enabled (database)
- Minimum dashboard refresh interval: 10s
- Overview dashboard is the default landing page

## Quick Start
```bash
# Start everything (services + exporters)
./start_all.sh

# Stop everything
./stop_all.sh

# Status (services + exporters)
./status_all.sh

# If you need root LaunchDaemons to start, run once per terminal session:
sudo -v
```

## Core Service Commands
```bash
# Status
brew services list | egrep 'grafana|prometheus|loki|node_exporter'

# Restart a single service
brew services restart prometheus

# Restart all core services
brew services restart node_exporter
brew services restart prometheus
brew services restart loki
brew services restart grafana
```

## Service URLs
- Prometheus: http://localhost:9090
- Grafana: https://localhost:3000
- node_exporter: http://localhost:9100/metrics
- Loki: http://localhost:3100

## High‑Level Architecture
```mermaid
graph TD
  A["Mac OS (system metrics)"] --> B["node_exporter (http://localhost:9100)"]
  A --> C["Custom exporters (scripts)"]
  C --> D["Textfile collector (.prom files)"]
  D --> B
  B --> E["Prometheus (http://localhost:9090)"]
  C --> E
  E --> F["Grafana (https://localhost:3000)"]
  G["launchd (user agents)"] --> C
  H["LaunchDaemons (root) for Wi‑Fi/SMART/Fan/Promtail/tshark"] --> C
  E --> I["Retention: 14 days / 20 GB cap"]
  F --> J["Dashboards: System / Network / Info / Executive"]
  A --> K["Promtail (log collector)"]
  K --> L["Loki (http://localhost:3100)"]
  L --> F
```

## Dashboard Inventory
Grafana folder: **Anish Laptop**

- **VMware Fusion: VM Health** — VM inventory, CPU/RAM usage, snapshots, VMDK size
- **Mac System: Core Health** — CPU, memory, disk usage (AnishSSD + Time Machine), disk I/O
- **Mac Network: Connectivity & Wi‑Fi** — throughput, errors/drops, ping health, Wi‑Fi signal/rates
- **Mac Network: Live Capture (tshark)** — live traffic analysis (top talkers, protocol mix)
- **Mac Info: Identity & Status** — system identity, key specs, running launchd jobs
- **Mac Logs: System & Apps** — system/app logs via Loki
- **Mac Security: Activity & Risk Signals** — security‑focused log signals and user activity
- **Mac Security: Activity & Risk Signals** now includes live tshark capture panels (SYN/RST/retrans/DNS/TLS)
- **All Metrics: Live Explorer** — all active Prometheus metrics (live only)
- **Executive Summary: Anish Laptop** — high‑level health view for demos/interviews
- **Anish Laptop: Overview** — navigation hub + quick KPIs
- **Prometheus: Self‑Monitoring** — scrape health, TSDB, WAL, config checksum
- **Mac System: Core Health** now includes battery health, thermal pressure, and SMART disk health panels

Dashboard exports:
```
/Users/anishskumar/Anish-DevOps-Lab/observability/grafana/dashboards/
```

## Retention Policy
Prometheus keeps **14 days** of data with a **20 GB** cap.
Loki keeps **14 days** of logs.

## Secrets and Git Safety
- No actual secrets were found in this folder (only commented examples in `grafana.ini`).
- A `.gitignore` was added at `/Users/anishskumar/Anish-DevOps-Lab/.gitignore` to prevent accidental commits of sensitive local config.
- If you ever add credentials (Grafana admin password, OAuth secrets, API tokens), keep them in local files or environment variables and **do not commit** them.

## Start/Stop Order
- Start: `node_exporter` → `prometheus` → `loki` → `grafana` → exporters
- Stop: `grafana` → `loki` → `prometheus` → `node_exporter` → exporters

## Key Paths
```
/Users/anishskumar/Anish-DevOps-Lab/observability/prometheus/prometheus.yml
/Users/anishskumar/Anish-DevOps-Lab/observability/prometheus/prometheus.args
/Users/anishskumar/Anish-DevOps-Lab/observability/grafana/grafana.ini
/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/node_exporter.args
/Users/anishskumar/Anish-DevOps-Lab/observability/exporters/
/Users/anishskumar/Anish-DevOps-Lab/observability/launchd/
/Users/anishskumar/Anish-DevOps-Lab/observability/loki/loki-config.yml
/Users/anishskumar/Anish-DevOps-Lab/observability/promtail/promtail-config.yml
```

## Directory Map
- `grafana/` — Grafana config + dashboard backups
- `prometheus/` — Prometheus config + rules
- `node_exporter/` — node_exporter args + textfile output
- `exporters/` — custom metric exporters (Python)
- `launchd/` — LaunchAgents/Daemons for exporters
- `loki/` — Loki config (log storage)
- `promtail/` — Promtail config (log collection)
- `migration/` — Docker + new‑Mac setup files

## Permissions & Launchd
- `start_all.sh` uses `launchctl bootstrap/bootout` (preferred on modern macOS).
- Root exporters (Wi‑Fi, SMART, fan/thermal, promtail, tshark) require sudo.
- Run `sudo -v` once per terminal session before `./start_all.sh` if you want root services to start without prompts.

## Launchd Commands
```bash
# User agents (metrics exporters)
launchctl print gui/$(id -u)/observability.net_connectivity
launchctl print gui/$(id -u)/observability.mac_system_info

# Root daemons (Wi‑Fi/SMART/fan/promtail/tshark)
sudo launchctl print system/observability.wdutil_metrics
sudo launchctl print system/observability.smart_metrics
```

## Troubleshooting
- **No data in Grafana**: check Prometheus and node_exporter are running and `http://localhost:9100/metrics` works.
- **Wi‑Fi panels empty**: ensure the root LaunchDaemon is loaded and `observability_wdutil_metrics.py` runs with sudo. Wi‑Fi metrics use `wdutil` and `system_profiler` (airport is not used).
- **Exporter metrics missing**: verify the textfile directory is correct and readable.
- **Logs missing**: confirm Loki and promtail are running and the Loki datasource is healthy in Grafana.

## Common Changes
- Change data retention in `prometheus.args`
- Add scrape targets in `prometheus.yml`
- Add or remove dashboards in Grafana and re‑export JSON
- UI improvements: KPI strip, thresholds, sparklines, “What to Watch” panels, Overview dashboard

---

See folder‑level READMEs for details.



## Showcase Flow (UI Walkthrough)
Use this order to demo the system in interviews or walkthroughs:

1. **Overview** — landing page and navigation hub
   - https://localhost:3000/d/overview/anish-laptop3a-overview
   - What it shows: overall health KPIs, quick links to all dashboards

2. **Executive Summary** — high‑level story for non‑technical audience
   - https://localhost:3000/d/exec-summary/executive-summary3a-anish-laptop
   - What it shows: top KPIs, health checks, and key risk signals

3. **System Health** — core CPU, memory, disk, battery, thermal
   - https://localhost:3000/d/mac-system-all/mac-system3a-core-health
   - What it shows: system resource health + battery and SMART status

4. **Network & Wi‑Fi** — connectivity and quality
   - https://localhost:3000/d/mac-network/mac-network3a-connectivity-and-wie28091-fi
   - What it shows: throughput, errors/drops, ping, Wi‑Fi signal/rates

5. **Live Capture (tshark)** — packet‑level live analysis
   - https://localhost:3000/d/tshark-live/mac-network3a-live-capture-tshark
   - What it shows: top talkers, protocol mix, live packet flow

6. **Logs** — system/app/observability logs
   - https://localhost:3000/d/mac-logs/mac-logs3a-system-apps-and-observability
   - What it shows: readable log streams with filters and keyword search

7. **Security** — risk signals from logs + live packet signals
   - https://localhost:3000/d/mac-security/mac-security3a-activity-and-risk-signals
   - What it shows: auth failures, privilege activity, Wi‑Fi security, tshark signals

8. **Prometheus Self‑Monitoring** — data plane health
   - https://localhost:3000/d/prometheus-self/prometheus3a-selfe28091-monitoring
   - What it shows: scrape health, TSDB usage, WAL/ingestion status

9. **All Metrics Explorer** — raw metrics for deep‑dive
   - https://localhost:3000/d/all-metrics-full/all-metrics3a-live-explorer
   - What it shows: full live metric list and raw panels

## Metrics & Logs Reference
- /Users/anishskumar/Anish-DevOps-Lab/observability/METRICS_AND_LOGS.md

## Quick Health Checks
```bash
curl -sf http://localhost:9090/-/ready
curl -sf http://localhost:9100/metrics | head -n 5
curl -sf http://localhost:3100/ready
curl -skf https://localhost:3000/api/health
```

## Final Notes
- Dashboard layouts are compacted to avoid empty space.
- Log dashboards are tagged `logs` for easy search.
- Overview page is the default home with pinned links.

## Showcase Screenshots (Non‑Sensitive)
These images intentionally **exclude** logs, security, network, tshark, and identity dashboards.

### Overview
![Overview](docs/screenshots/overview.png)

### Executive Summary
![Executive Summary](docs/screenshots/executive-summary.png)

### Mac System: Core Health
![Mac System Core Health](docs/screenshots/mac-system-core-health.png)

### Prometheus: Self‑Monitoring
![Prometheus Self Monitoring](docs/screenshots/prometheus-self.png)


## VMware Fusion Monitoring
- Dashboard: https://localhost:3000/d/vmware-fusion/vmware-fusion3a-vm-health
- Exporter: /Users/anishskumar/Anish-DevOps-Lab/observability/exporters/observability_vmware_fusion_metrics.py
- LaunchAgent: /Users/anishskumar/Library/LaunchAgents/observability.vmware_fusion_metrics.plist


## VMware Folder
- /Users/anishskumar/Anish-DevOps-Lab/observability/vmware/README.md


## Output Folder
- /Users/anishskumar/Anish-DevOps-Lab/observability/output
  (Screenshots, renders, and exported artifacts)
