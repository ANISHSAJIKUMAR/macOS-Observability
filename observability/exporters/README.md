# Custom Exporters

## Purpose
These scripts emit Prometheus metrics into the textfile directory for node_exporter.

## Files & Behavior
- `observability_battery_metrics.py`
  - Battery charge %, cycle count, charger connected
  - Battery health max capacity %, condition label, power source
- `observability_net_connectivity_metrics.py`
  - Pings public targets
  - Exposes latency and loss
- `observability_mac_system_info_metrics.py`
  - Exposes identity and hardware facts (CPU, memory, OS, IP, SSID)
- `observability_launchd_metrics.py`
  - Lists running launchd jobs
- `observability_cpu_fan_metrics.py`
  - Thermal pressure level/state (proxy for CPU heat)
  - Availability flags for CPU temperature and fan speed (some Macs do not expose these)
- `observability_smart_metrics.py`
  - Disk SMART overall health
  - Disk SMART status via diskutil (Verified/Not Supported)
- `observability_grafana_health_metrics.py`
  - Checks Grafana API health (up/down)
- `observability_prom_config_checksum.py`
  - Calculates SHA256 checksums of Prometheus config files
- `observability_wdutil_metrics.py`
  - Wi‑Fi RSSI, noise, SNR, link rate, CCA, MCS, NSS
  - Adds `wifi_metrics_source` to show data source (wdutil/system_profiler)
- `observability_tshark_metrics.py`
  - Live packet capture metrics (throughput, top talkers, protocol mix)
  - Requires root (LaunchDaemon)
  - Requires root (LaunchDaemon)
- `observability_vmware_fusion_metrics.py`
  - VMware Fusion VM inventory and host-side metrics (CPU/RAM, snapshots, disk size)

## What You Can Change
- Targets in `observability_net_connectivity_metrics.py`
- Fields emitted in `observability_mac_system_info_metrics.py`
- Sampling interval via launchd `StartInterval`

## Apply Changes
```bash
launchctl unload ~/Library/LaunchAgents/observability.net_connectivity.plist
launchctl unload ~/Library/LaunchAgents/observability.mac_system_info.plist
launchctl unload ~/Library/LaunchAgents/observability.launchd_metrics.plist
launchctl load ~/Library/LaunchAgents/observability.net_connectivity.plist
launchctl load ~/Library/LaunchAgents/observability.mac_system_info.plist
launchctl load ~/Library/LaunchAgents/observability.launchd_metrics.plist
sudo launchctl bootout system /Library/LaunchDaemons/observability.wdutil_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.wdutil_metrics.plist
```

## Troubleshooting
- Check the textfile directory for `.prom` files
- Ensure scripts are executable: `chmod +x *.py`
