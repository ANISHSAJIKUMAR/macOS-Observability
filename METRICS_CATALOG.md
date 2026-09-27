# Complete Metrics Catalog

This document lists all metrics available in the macOS Observatory. Use these in Grafana dashboards and Prometheus queries.

## 📊 System Metrics (node_exporter)

### CPU Metrics

| Metric | Description | Type | Example Query |
|--------|-------------|------|---------------|
| `node_cpu_seconds_total` | CPU time spent in each mode | Counter | `rate(node_cpu_seconds_total{mode="user"}[5m])` |
| `node_load1` | 1-minute load average | Gauge | `node_load1` |
| `node_load5` | 5-minute load average | Gauge | `node_load5` |
| `node_load15` | 15-minute load average | Gauge | `node_load15` |

**CPU Usage Percentage:**
```promql
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

### Memory Metrics

| Metric | Description | Type | Unit |
|--------|-------------|------|------|
| `node_memory_MemTotal_bytes` | Total memory | Gauge | Bytes |
| `node_memory_MemAvailable_bytes` | Available memory | Gauge | Bytes |
| `node_memory_MemFree_bytes` | Free memory | Gauge | Bytes |
| `node_memory_Cached_bytes` | Cached memory | Gauge | Bytes |
| `node_memory_Buffers_bytes` | Buffer memory | Gauge | Bytes |
| `node_memory_SwapTotal_bytes` | Total swap | Gauge | Bytes |
| `node_memory_SwapFree_bytes` | Free swap | Gauge | Bytes |

**Memory Usage Percentage:**
```promql
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
```

**Swap Usage:**
```promql
(1 - (node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes)) * 100
```

### Disk Metrics

| Metric | Description | Type | Labels |
|--------|-------------|------|--------|
| `node_filesystem_size_bytes` | Filesystem size | Gauge | device, mountpoint |
| `node_filesystem_avail_bytes` | Available space | Gauge | device, mountpoint |
| `node_filesystem_free_bytes` | Free space | Gauge | device, mountpoint |
| `node_disk_read_bytes_total` | Bytes read | Counter | device |
| `node_disk_written_bytes_total` | Bytes written | Counter | device |
| `node_disk_io_time_seconds_total` | I/O time | Counter | device |

**Disk Usage Percentage:**
```promql
100 - ((node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) * 100)
```

**Disk I/O Rate:**
```promql
rate(node_disk_read_bytes_total[5m])
rate(node_disk_written_bytes_total[5m])
```

### Network Metrics

| Metric | Description | Type | Labels |
|--------|-------------|------|--------|
| `node_network_receive_bytes_total` | Bytes received | Counter | device |
| `node_network_transmit_bytes_total` | Bytes transmitted | Counter | device |
| `node_network_receive_packets_total` | Packets received | Counter | device |
| `node_network_transmit_packets_total` | Packets sent | Counter | device |
| `node_network_receive_errs_total` | Receive errors | Counter | device |
| `node_network_transmit_errs_total` | Transmit errors | Counter | device |

**Network Throughput:**
```promql
rate(node_network_receive_bytes_total{device="en0"}[5m])
rate(node_network_transmit_bytes_total{device="en0"}[5m])
```

### System Metrics

| Metric | Description | Type |
|--------|-------------|------|
| `node_boot_time_seconds` | System boot time | Gauge |
| `node_time_seconds` | Current system time | Gauge |
| `node_procs_running` | Running processes | Gauge |
| `node_procs_blocked` | Blocked processes | Gauge |

**System Uptime:**
```promql
time() - node_boot_time_seconds
```

## 🍎 macOS-Specific Metrics

### Battery Metrics

| Metric | Description | Type | Range |
|--------|-------------|------|-------|
| `mac_battery_charge_percent` | Current battery charge | Gauge | 0-100 |
| `mac_battery_capacity_percent` | Battery health | Gauge | 0-100 |
| `mac_battery_cycle_count` | Charge cycles | Gauge | 0+ |
| `mac_battery_time_remaining_minutes` | Time until empty | Gauge | Minutes |
| `mac_battery_temperature_celsius` | Battery temp | Gauge | °C |
| `mac_battery_voltage_volts` | Battery voltage | Gauge | Volts |
| `mac_battery_amperage_ma` | Current draw | Gauge | mA |
| `mac_battery_is_charging` | Charging status | Gauge | 0/1 |
| `mac_battery_is_plugged` | AC power connected | Gauge | 0/1 |

**Battery Health Alert:**
```promql
mac_battery_capacity_percent < 80
```

**Low Battery Warning:**
```promql
mac_battery_charge_percent < 20 and mac_battery_is_plugged == 0
```

### CPU Temperature & Fan Metrics

| Metric | Description | Type | Unit |
|--------|-------------|------|------|
| `mac_cpu_temperature_celsius` | CPU die temperature | Gauge | °C |
| `mac_cpu_proximity_temp_celsius` | CPU proximity temp | Gauge | °C |
| `mac_gpu_temperature_celsius` | GPU temperature | Gauge | °C |
| `mac_fan_speed_rpm` | Fan speed | Gauge | RPM |
| `mac_fan_speed_percent` | Fan speed percentage | Gauge | 0-100 |

**Thermal Alert:**
```promql
mac_cpu_temperature_celsius > 85
```

### Network Connectivity Metrics

| Metric | Description | Type | Value |
|--------|-------------|------|-------|
| `mac_net_connectivity_status` | Internet reachable | Gauge | 1=up, 0=down |
| `mac_net_connectivity_latency_ms` | Ping latency | Gauge | Milliseconds |
| `mac_net_dns_resolution_status` | DNS working | Gauge | 1=ok, 0=fail |
| `mac_net_gateway_reachable` | Gateway accessible | Gauge | 1=up, 0=down |
| `mac_net_wifi_signal_strength` | WiFi signal | Gauge | -100 to 0 dBm |
| `mac_net_wifi_noise` | WiFi noise level | Gauge | dBm |
| `mac_net_wifi_channel` | WiFi channel | Gauge | Number |

**Connectivity Issues:**
```promql
mac_net_connectivity_status == 0
mac_net_connectivity_latency_ms > 100
```

### System Information Metrics

| Metric | Description | Type |
|--------|-------------|------|
| `mac_system_info` | OS version info | Info |
| `mac_system_uptime_seconds` | macOS uptime | Gauge |
| `mac_system_processes_total` | Total processes | Gauge |
| `mac_system_users_logged_in` | Logged-in users | Gauge |
| `mac_system_architecture` | CPU architecture | Info |

### VMware Fusion Metrics

| Metric | Description | Type |
|--------|-------------|------|
| `mac_vmware_vm_count` | Number of VMs | Gauge |
| `mac_vmware_vm_running` | Running VMs | Gauge |
| `mac_vmware_vm_memory_mb` | VM memory allocated | Gauge |
| `mac_vmware_vm_cpu_count` | VM CPU count | Gauge |
| `mac_vmware_vm_status` | VM power state | Gauge |

### LaunchAgent Status Metrics

| Metric | Description | Type | Labels |
|--------|-------------|------|--------|
| `mac_launchd_service_status` | Service status | Gauge | service, label |
| `mac_launchd_service_pid` | Service PID | Gauge | service |
| `mac_launchd_service_exit_code` | Last exit code | Gauge | service |
| `mac_launchd_service_uptime_seconds` | Service uptime | Gauge | service |

## 🔍 Prometheus Self-Monitoring

| Metric | Description | Type |
|--------|-------------|------|
| `prometheus_build_info` | Prometheus version | Info |
| `prometheus_tsdb_storage_blocks_bytes` | Storage size | Gauge |
| `prometheus_tsdb_head_series` | Series in memory | Gauge |
| `prometheus_tsdb_head_samples_appended_total` | Samples appended | Counter |
| `prometheus_http_requests_total` | HTTP requests | Counter |
| `prometheus_target_scrapes_total` | Scrapes performed | Counter |
| `prometheus_target_scrape_duration_seconds` | Scrape duration | Summary |
| `up` | Target up status | Gauge |

**Prometheus Health:**
```promql
up{job="prometheus"} == 1
prometheus_tsdb_storage_blocks_bytes < 10e9
```

## 📝 Log Metrics (Loki)

### Log Streams

| Stream | Description | Labels |
|--------|-------------|--------|
| `{job="system"}` | System logs | host, level |
| `{job="application"}` | App logs | app, level |
| `{filename=~".+"}` | File-based logs | filename, job |

### Common Log Queries

**Error logs in last hour:**
```logql
{job="system"} |= "error" [1h]
```

**Count by level:**
```logql
sum by (level) (count_over_time({job="system"}[1h]))
```

**Failed service starts:**
```logql
{job="system"} |= "failed to start"
```

## 🎯 Useful Dashboard Queries

### Top 10 Queries for Dashboards

#### 1. CPU Usage Over Time
```promql
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

#### 2. Memory Usage Percentage
```promql
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
```

#### 3. Disk Space Used
```promql
100 - ((node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) * 100)
```

#### 4. Network Traffic
```promql
rate(node_network_receive_bytes_total{device="en0"}[5m]) / 1024 / 1024
rate(node_network_transmit_bytes_total{device="en0"}[5m]) / 1024 / 1024
```

#### 5. Battery Status
```promql
mac_battery_charge_percent
mac_battery_capacity_percent
```

#### 6. System Temperature
```promql
mac_cpu_temperature_celsius
mac_gpu_temperature_celsius
```

#### 7. Process Count
```promql
node_procs_running
```

#### 8. Load Average
```promql
node_load1
node_load5
node_load15
```

#### 9. Disk I/O
```promql
rate(node_disk_read_bytes_total[5m]) / 1024 / 1024
rate(node_disk_written_bytes_total[5m]) / 1024 / 1024
```

#### 10. Connectivity Status
```promql
mac_net_connectivity_status
mac_net_connectivity_latency_ms
```

## 🚨 Alert Examples

### Critical Alerts

**High CPU Usage:**
```yaml
- alert: HighCPUUsage
  expr: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 90
  for: 5m
  annotations:
    summary: "High CPU usage detected"
```

**Low Memory:**
```yaml
- alert: LowMemory
  expr: (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) < 0.1
  for: 5m
  annotations:
    summary: "Less than 10% memory available"
```

**Disk Almost Full:**
```yaml
- alert: DiskAlmostFull
  expr: (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) < 0.1
  for: 10m
  annotations:
    summary: "Less than 10% disk space remaining"
```

**Service Down:**
```yaml
- alert: ServiceDown
  expr: up == 0
  for: 1m
  annotations:
    summary: "Service {{ $labels.job }} is down"
```

**Battery Health:**
```yaml
- alert: BatteryHealthLow
  expr: mac_battery_capacity_percent < 70
  annotations:
    summary: "Battery health degraded"
```

## 📈 Metric Retention

Default retention: **14 days**

Storage usage: ~1-2 GB for 14 days of metrics at default scrape intervals.

## 🔄 Scrape Intervals

| Target | Interval | Timeout |
|--------|----------|---------|
| Prometheus | 15s | 10s |
| node_exporter | 15s | 10s |
| Custom exporters | 60s | 30s |

## 📚 References

- [Prometheus Query Examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)
- [PromQL Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Grafana Dashboards](https://grafana.com/grafana/dashboards/)
- [Node Exporter Metrics](https://github.com/prometheus/node_exporter)

---

**Total Metrics Available:** 100+ metrics across system, network, battery, temperature, and custom categories.

**New Metrics:** Easily add custom Python exporters in `observability/exporters/` directory.
