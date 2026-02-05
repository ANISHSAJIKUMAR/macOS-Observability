# Custom Exporters

## Purpose
These scripts emit Prometheus metrics into the textfile directory for node_exporter.

## Files & Behavior
- `battery_metrics.py`
  - Battery charge %, cycle count, charger connected
  - Battery health max capacity %, condition label, power source
- `net_connectivity_metrics.py`
  - Pings public targets
  - Exposes latency and loss
- `mac_system_info_metrics.py`
  - Exposes identity and hardware facts (CPU, memory, OS, IP, SSID)
- `launchd_metrics.py`
  - Lists running launchd jobs
- `cpu_fan_metrics.py`
  - Thermal pressure level/state (proxy for CPU heat)
  - Availability flags for CPU temperature and fan speed (some Macs do not expose these)
- `smart_metrics.py`
  - Disk SMART overall health
  - Disk SMART status via diskutil (Verified/Not Supported)
- `grafana_health_metrics.py`
  - Checks Grafana API health (up/down)
- `prom_config_checksum.py`
  - Calculates SHA256 checksums of Prometheus config files
- `wdutil_metrics.py`
  - Wi‑Fi RSSI, noise, SNR, link rate, CCA, MCS, NSS
  - Adds `wifi_metrics_source` to show data source (wdutil/system_profiler)
  - Requires root (LaunchDaemon)

## What You Can Change
- Targets in `net_connectivity_metrics.py`
- Fields emitted in `mac_system_info_metrics.py`
- Sampling interval via launchd `StartInterval`

## Apply Changes
```bash
launchctl unload ~/Library/LaunchAgents/com.local.net_connectivity.plist
launchctl unload ~/Library/LaunchAgents/com.local.mac_system_info.plist
launchctl unload ~/Library/LaunchAgents/com.local.launchd_metrics.plist
launchctl load ~/Library/LaunchAgents/com.local.net_connectivity.plist
launchctl load ~/Library/LaunchAgents/com.local.mac_system_info.plist
launchctl load ~/Library/LaunchAgents/com.local.launchd_metrics.plist
sudo launchctl bootout system /Library/LaunchDaemons/com.local.wdutil_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.local.wdutil_metrics.plist
```

## Troubleshooting
- Check the textfile directory for `.prom` files
- Ensure scripts are executable: `chmod +x *.py`
