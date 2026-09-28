# Dashboard verification — September 28, 2026

All 11 live dashboards were queried through Grafana's datasource proxy, using
their actual Prometheus/Loki references and expanded dashboard variables.
646 query targets were checked: 605 returned results, 41 were unavailable, and
none returned a query error. Panel IDs are unique and datasource references resolve.
This is a current-state check, not a guarantee about future collection.

| Dashboard | Queries returning data | Unavailable queries |
| --- | ---: | ---: |
| `all-metrics-full` | 392 | 4 |
| `exec-summary` | 38 | 1 |
| `mac-info` | 30 | 0 |
| `mac-logs` | 14 | 0 |
| `mac-network` | 34 | 3 |
| `mac-security` | 8 | 9 |
| `mac-system-all` | 50 | 2 |
| `overview` | 24 | 0 |
| `prometheus-self` | 10 | 0 |
| `tshark-live` | 2 | 10 |
| `vmware-fusion` | 3 | 12 |

## Repairs

- Corrected Loki and VMware datasource UIDs, provisioned stable datasource IDs,
  fixed an escaped LogQL expression, and assigned unique panel IDs/ref IDs.
- Corrected system-info metric names; CPU core count now counts CPU series
  instead of treating an info label's constant value as the core count.
- Corrected the Prometheus checksum exporter to follow the project directory.
- Added Foundation thermal-state collection when powermetrics is unavailable.
- Added system_profiler fallback for Wi-Fi MCS.
- Removed artificial zero fallbacks for missing measurements; instant stat/table
  queries avoid retaining obsolete label sets as additional current values.
- Replaced stale packet samples with an honest failed-capture state, repaired
  the user's scheduled export log paths, and fixed fractional capture intervals.
- Added VMware discovery count, installation status and exporter age; no VMs
  are currently found in the configured/default folders.

## Remaining environmental limitations

- **Packet capture:** macOS denies this user access to `/dev/bpf0`. The exporter
  now runs every minute and reports `tshark_capture_success=0`; packet panels
  correctly show unavailable. An administrator must enable BPF capture access
  (for example, Wireshark's ChmodBPF installer) before live capture can work.
- **VMware:** Fusion is installed, but zero VMX files are discovered. VM-specific
  metrics require an actual VM; no virtual machine was created or started.
- **Storage:** `/Volumes/External-SSD` and `/Volumes/Time Machine` are not mounted.
- **Platform metrics:** macOS does not expose transmit-drop counts, Wi-Fi CCA/NSS,
  CPU temperature or fan RPM through the current unprivileged collectors.
  Thermal pressure, RSSI, SNR, transmit rate and MCS are available.
- **Prometheus notification metrics:** dropped notifications and queue length
  series are not currently exported by this installation.
- Log counts can legitimately be zero when no matching application/security
  events occur. These remain distinct from missing hardware measurements.

## Repeat the audit

Set `GRAFANA_PASSWORD` in your environment, then run:

```bash
python3 scripts/audit_dashboards.py > dashboard-audit.json
```

Optional: set `GRAFANA_URL` and `GRAFANA_USER`. The report contains query status
and series counts, not log contents. A nonzero exit indicates a query error or
invalid datasource/panel structure. Unavailable series are reported separately.
