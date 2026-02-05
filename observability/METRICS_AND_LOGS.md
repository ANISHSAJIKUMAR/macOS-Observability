# Metrics and Logs Reference

This file documents the main **metrics scraped** and the **log sources** shipped into Loki.
It’s intended as a quick reference for what each metric/log is used for.

## Prometheus Metrics (Primary)

### System (node_exporter)
- `node_cpu_seconds_total` — CPU time by core and mode. Used to compute CPU usage %.
- `node_memory_total_bytes` — Total RAM. Used for memory usage calculations.
- `node_memory_free_bytes` — Free RAM. Used to compute used memory %.
- `node_filesystem_size_bytes` — Filesystem total size per mount. Used for disk capacity.
- `node_filesystem_avail_bytes` — Filesystem available bytes. Used for disk usage %.
- `node_disk_read_bytes_total` — Disk read throughput.
- `node_disk_written_bytes_total` — Disk write throughput.
- `node_network_receive_bytes_total` — Network RX throughput.
- `node_network_transmit_bytes_total` — Network TX throughput.
- `node_network_receive_errs_total` — RX errors (network health).
- `node_network_transmit_errs_total` — TX errors (network health).
- `node_network_receive_drop_total` — RX drops (congestion / driver issues).
- `node_network_transmit_drop_total` — TX drops.

### Custom System Metrics
- `net_ping_latency_ms` — Ping latency to public targets. Indicates connectivity quality.
- `net_ping_loss_percent` — Packet loss to public targets. Indicates network stability.
- `mac_system_info_*` — Identity/spec fields (host, OS version, CPU model, memory, IP, SSID). Used for system inventory panels.
- `launchd_jobs_running_total` — Count of active launchd jobs. Used to spot abnormal spikes.

### Battery & Power
- `battery_charge_percent` — Battery % remaining.
- `battery_cycle_count` — Battery health (age indicator).
- `battery_health_max_capacity_percent` — Maximum capacity vs new (battery wear).
- `battery_is_charging` — Charging state (1/0).
- `battery_charger_connected` — Power adapter connected (1/0).
- `battery_power_source` — Label metric for AC vs Battery.
- `battery_condition` — Label metric for health state (Good/Service Recommended).

### Thermal / Hardware
- `cpu_thermal_pressure_level` — Thermal pressure (Nominal → Critical).
- `cpu_thermal_pressure_state` — Label version of thermal state.
- `cpu_temperature_available` — Whether CPU temp is readable (1/0).
- `fan_speed_available` — Whether fan RPM is readable (1/0).

### Disk SMART
- `smart_device_supported` — Whether SMART is supported.
- `smart_device_ok` — SMART health (1 OK / 0 Bad).
- `smart_status_verified` — diskutil SMART verified (1 OK).
- `smart_status_label` — Label metric for SMART status (Verified / Not Supported).

### Wi‑Fi Metrics
- `wifi_rssi_dbm` — Wi‑Fi signal strength (dBm).
- `wifi_noise_dbm` — Wi‑Fi noise (dBm).
- `wifi_snr_db` — Signal‑to‑noise ratio (quality indicator).
- `wifi_tx_rate_mbps` — Current transmit rate.
- `wifi_max_rate_mbps` — Max supported rate (if available).
- `wifi_mcs` — Modulation and coding scheme.
- `wifi_cca_percent` — Channel busy %. Higher = congestion.
- `wifi_nss` — Spatial streams count.
- `wifi_metrics_source` — Source of Wi‑Fi metrics (wdutil/system_profiler).

### tshark Live Capture
- `tshark_capture_success` — Whether capture succeeded (1/0).
- `tshark_capture_frames_total` — Frames captured in sampling window.
- `tshark_capture_bytes_total` — Bytes captured in sampling window.
- `tshark_capture_pps` — Packets per second (approx).
- `tshark_capture_bps` — Bytes per second (approx).
- `tshark_conv_bytes_total` — Bytes per IP conversation (top talkers).
- `tshark_conv_frames_total` — Frames per IP conversation.
- `tshark_proto_frames_total` — Frames by protocol (UDP/TCP/ARP/etc).
- `tshark_proto_bytes_total` — Bytes by protocol.
- `tshark_sec_frames_total` — Security filters (SYN, reset, retransmission, DNS/ARP/ICMP) frames.
- `tshark_sec_bytes_total` — Security filter bytes.

## Prometheus Recording Rules (Derived)
- `job:node_cpu_usage_percent:rate5m` — 5m CPU usage %.
- `job:node_memory_used_percent` — Memory usage %.
- `job:node_filesystem_used_percent` — Filesystem used %.
- `job:node_filesystem_used_gb` — Used disk in GB.
- `job:node_filesystem_avail_gb` — Available disk in GB.
- `job:node_network_receive_mb_s` — RX MB/s.
- `job:node_network_transmit_mb_s` — TX MB/s.

## Logs Shipped to Loki (Readable)

### System Logs
- `/var/log/system.log` — Core system events.
- `/var/log/wifi.log` — Wi‑Fi association/disconnect/auth events.
- `/var/log/install.log` — Package install/upgrade activity.
- `/var/log/fsck_apfs.log` — APFS filesystem checks.
- `/var/log/fsck_apfs_error.log` — Filesystem check errors.
- `/var/log/fsck_hfs.log` — HFS filesystem checks.
- `/var/log/shutdown_monitor.log` — Shutdown and reboot tracking.
- `/var/log/com.apple.xpc.launchd/*` — service launches and daemon activity.
- `/var/log/powermanagement/*` — power/sleep events.

### Diagnostic / Crash Logs
- `/Library/Logs/DiagnosticReports/*` — System crash/diagnostic reports.
- `/Users/anishskumar/Library/Logs/DiagnosticReports/*` — User app crash reports.

### App Logs (User)
- `/Users/anishskumar/Library/Logs/*/*.log`
- `/Users/anishskumar/Library/Logs/*/*.txt`

### Observability Logs
- `/opt/homebrew/var/log/grafana/*.log`
- `/opt/homebrew/var/log/prometheus*.log`
- `/opt/homebrew/var/log/node_exporter*.log`

## Notes
- Some metrics (e.g., CPU temperature, fan RPM) may be unavailable on Apple Silicon.
- Binary logs (legacy `.asl`, Wi‑Fi analytics `.out`) are excluded because they render unreadable.
