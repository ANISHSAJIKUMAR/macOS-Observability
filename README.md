# 🔭 macOS Observatory

[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey?logo=apple)](https://www.apple.com/macos/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Prometheus](https://img.shields.io/badge/prometheus-v3.15-orange?logo=prometheus)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/grafana-latest-blue?logo=grafana)](https://grafana.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub stars](https://img.shields.io/github/stars/ANISHSAJIKUMAR/macos-observatory?style=social)](https://github.com/ANISHSAJIKUMAR/macos-observatory/stargazers)

> **Your complete macOS observation platform.** Production-grade monitoring with Prometheus, Grafana, Loki, and 100+ custom macOS metrics. Monitor CPU, memory, disk, network, battery health, temperature, and more with beautiful dashboards and automatic alerting.

**Perfect for:** DevOps Engineers • SREs • Mac Power Users • Developers • System Administrators • Learning Observability

---

## 🚀 Quick Start (3 Steps)

```bash
# 1. Install dependencies
brew install prometheus grafana loki node_exporter promtail

# 2. Clone and setup
git clone https://github.com/ANISHSAJIKUMAR/macos-observatory.git
cd macos-observatory/observability
./setup.sh

# 3. Start monitoring
./start_all.sh
```

**That's it!** Open http://localhost:3000 (admin/admin) and start monitoring your Mac.

---

## ✨ Why This Project?

### 🎯 **Built Specifically for macOS**
Unlike generic monitoring solutions, this includes **macOS-specific metrics**:
- 🔋 Battery health, charge cycles, and temperature
- 🌡️ CPU/GPU temperature and fan speed
- 📱 System information and architecture
- 🖥️ VMware Fusion VM monitoring
- 📡 WiFi signal strength and connectivity

### ⚡ **Production-Ready Features**
- 🤖 **Auto-restart monitoring** - Prometheus self-heals automatically
- 🎨 **Beautiful dashboards** - Pre-configured Grafana visualizations
- 📊 **100+ metrics** - System, network, battery, temperature, custom
- 🔔 **Smart alerting** - Get notified before issues become problems
- 🚀 **One-command setup** - No complex configuration needed

### 💎 **Zero Hassle**
- ✅ **Portable** - Works on any Mac, any directory
- ✅ **No hardcoded paths** - Dynamic configuration
- ✅ **Well documented** - Complete guides included
- ✅ **Community driven** - Open source and extensible

---

## 📸 Screenshots

### Grafana Dashboard
![Grafana Dashboard](screenshots/grafana-dashboard.png)
*Real-time macOS system monitoring with custom metrics*

### Prometheus Targets
![Prometheus Targets](screenshots/prometheus-targets.png)
*All exporters healthy and collecting metrics*

### CPU & Memory Monitoring
![System Metrics](screenshots/system-metrics.png)
*Track CPU, memory, disk, and network usage over time*

---

## 🎯 What You Can Monitor

<table>
<tr>
<td width="33%">

### 💻 **System Metrics**
- CPU usage & load average
- Memory & swap usage
- Disk space & I/O
- Network traffic & errors
- Process count & uptime

</td>
<td width="33%">

### 🍎 **macOS Specific**
- Battery health & cycles
- CPU/GPU temperature
- Fan speed (RPM & %)
- WiFi signal strength
- System architecture
- VMware Fusion VMs

</td>
<td width="33%">

### 🔧 **Advanced**
- LaunchAgent status
- Service health checks
- Log aggregation (Loki)
- Custom Python metrics
- Alert rules
- Auto-restart monitoring

</td>
</tr>
</table>

**📊 Total: 100+ Metrics Available** - [See full catalog →](METRICS_CATALOG.md)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     🌐 Grafana UI (Port 3000)               │
│              Beautiful dashboards & visualizations           │
└────────────────┬────────────────────────────────────────────┘
                 │
       ┌─────────┴──────────┐
       ▼                    ▼
┌──────────────┐    ┌──────────────┐
│  Prometheus  │    │     Loki     │
│  (Port 9090) │    │  (Port 3100) │
│ Metrics DB   │    │   Logs DB    │
└──────┬───────┘    └──────┬───────┘
       │                   │
       ▼                   ▼
┌─────────────────┐  ┌─────────────────┐
│ node_exporter   │  │    Promtail     │
│ System Metrics  │  │   Log Shipper   │
└────────┬────────┘  └─────────────────┘
         │
    ┌────┴─────┬─────────┬──────────┐
    ▼          ▼         ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│Battery │ │CPU/Fan │ │Network │ │VMware  │
│Metrics │ │Metrics │ │Check   │ │Metrics │
└────────┘ └────────┘ └────────┘ └────────┘

         🤖 Auto-Restart Health Monitor
         Checks Prometheus every 60s
```

---

## 📋 Features Comparison

| Feature | macOS Observatory | Prometheus Only | Grafana Cloud | Apple Activity Monitor |
|---------|:------------------------:|:---------------:|:-------------:|:----------------------:|
| **macOS Battery Metrics** | ✅ | ❌ | ❌ | ⚠️ Basic |
| **CPU Temperature** | ✅ | ❌ | ❌ | ❌ |
| **Historical Data** | ✅ 14 days | ✅ Custom | ✅ Paid | ❌ |
| **Custom Dashboards** | ✅ Grafana | ❌ | ✅ | ❌ |
| **Auto-Restart** | ✅ | ❌ | N/A | N/A |
| **One-Command Setup** | ✅ | ❌ | ❌ | ✅ |
| **Alerting** | ✅ | ✅ | ✅ | ❌ |
| **Log Aggregation** | ✅ Loki | ❌ | ✅ | ❌ |
| **100% Free** | ✅ | ✅ | ⚠️ Limited | ✅ |
| **Portable Config** | ✅ | ❌ | N/A | N/A |

---

## 🚀 Installation

### Prerequisites

- macOS 11.0 (Big Sur) or later
- [Homebrew](https://brew.sh) package manager
- 2GB free disk space
- Internet connection

### Step-by-Step Setup

#### 1. Install Homebrew Services
```bash
brew install prometheus grafana loki node_exporter promtail
```

#### 2. Clone Repository
```bash
git clone https://github.com/ANISHSAJIKUMAR/macos-observatory.git
cd macos-observatory
```

#### 3. Run Setup Script
```bash
cd observability
./setup.sh
```

The setup script will:
- ✅ Detect your project path automatically
- ✅ Configure Prometheus with correct paths
- ✅ Install 13 LaunchAgents for custom metrics
- ✅ Set up auto-restart monitoring
- ✅ Clean up metadata files

#### 4. Start Services
```bash
./start_all.sh
```

#### 5. Access Dashboards

- **Grafana**: http://localhost:3000 (Login: admin/admin)
- **Prometheus**: http://localhost:9090
- **Loki**: http://localhost:3100

**🎉 You're monitoring your Mac!**

---

## 📊 Available Metrics

### System Metrics (node_exporter)

**CPU:**
- `node_cpu_seconds_total` - CPU time by mode
- `node_load1`, `node_load5`, `node_load15` - Load averages

**Memory:**
- `node_memory_MemTotal_bytes` - Total RAM
- `node_memory_MemAvailable_bytes` - Available RAM
- `node_memory_SwapTotal_bytes` - Swap size

**Disk:**
- `node_filesystem_size_bytes` - Disk capacity
- `node_filesystem_avail_bytes` - Free space
- `node_disk_read_bytes_total` - Read I/O
- `node_disk_written_bytes_total` - Write I/O

**Network:**
- `node_network_receive_bytes_total` - Bytes received
- `node_network_transmit_bytes_total` - Bytes sent

### macOS-Specific Metrics

**Battery:**
- `mac_battery_charge_percent` - Current charge (0-100%)
- `mac_battery_capacity_percent` - Battery health (0-100%)
- `mac_battery_cycle_count` - Charge cycles
- `mac_battery_temperature_celsius` - Battery temp (°C)
- `mac_battery_time_remaining_minutes` - Time until empty

**Temperature & Fan:**
- `mac_cpu_temperature_celsius` - CPU die temperature
- `mac_gpu_temperature_celsius` - GPU temperature
- `mac_fan_speed_rpm` - Fan speed in RPM
- `mac_fan_speed_percent` - Fan speed percentage

**Network:**
- `mac_net_connectivity_status` - Internet reachable (1=up, 0=down)
- `mac_net_connectivity_latency_ms` - Ping latency
- `mac_net_wifi_signal_strength` - WiFi signal (dBm)

**System:**
- `mac_system_uptime_seconds` - macOS uptime
- `mac_system_processes_total` - Total processes

**VMware Fusion:**
- `mac_vmware_vm_count` - Number of VMs
- `mac_vmware_vm_running` - Running VMs
- `mac_vmware_vm_memory_mb` - VM memory allocated

**📖 [Complete Metrics Catalog →](METRICS_CATALOG.md)** - 100+ metrics with examples

---

## 🎨 Example Queries

### CPU Usage
```promql
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

### Memory Usage
```promql
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
```

### Disk Space Used
```promql
100 - ((node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) * 100)
```

### Battery Health
```promql
mac_battery_capacity_percent
```

### Network Traffic (MB/s)
```promql
rate(node_network_receive_bytes_total{device="en0"}[5m]) / 1024 / 1024
```

---

## 🤖 Auto-Restart Feature

Unique feature: **Prometheus automatically restarts if it becomes unhealthy!**

- ✅ Checks health every 60 seconds
- ✅ Auto-restarts on failure (max 3 attempts)
- ✅ Smart retry logic prevents loops
- ✅ Comprehensive logging for debugging

### Monitor Health Checks
```bash
tail -f ~/Library/Logs/prometheus-healthcheck.log
```

### Disable/Enable
```bash
# Disable
launchctl unload ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist

# Enable
launchctl load ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist
```

**📖 [Auto-Restart Documentation →](observability/PROMETHEUS_AUTO_RESTART.md)**

---

## 🛠️ Management Commands

```bash
cd observability

# Start all services
./start_all.sh

# Stop all services
./stop_all.sh

# Check status
./status_all.sh

# View logs
tail -f ~/Library/Logs/prometheus-healthcheck.log
```

### Individual Service Control
```bash
# Start/stop/restart
brew services start prometheus
brew services stop grafana
brew services restart loki

# Check status
brew services list
```

---

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Complete setup guide with troubleshooting
- **[METRICS_CATALOG.md](METRICS_CATALOG.md)** - All 100+ metrics with examples
- **[PROMETHEUS_AUTO_RESTART.md](observability/PROMETHEUS_AUTO_RESTART.md)** - Auto-restart feature
- **[SCREENSHOT_GUIDE.md](SCREENSHOT_GUIDE.md)** - How to capture screenshots
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines

---

## 🎯 Use Cases

### For DevOps Engineers
- Monitor Mac build machines and CI/CD runners
- Track resource usage during deployments
- Alert on infrastructure issues
- Historical performance analysis

### For Developers
- Monitor local development environment
- Track resource-intensive applications
- Debug performance bottlenecks
- Learn observability best practices

### For System Administrators
- Monitor fleet of Mac computers
- Battery health tracking for laptops
- Temperature monitoring for thermal issues
- Proactive maintenance alerts

### For Students & Learners
- Learn Prometheus, Grafana, and Loki
- Understand monitoring and alerting
- Practice PromQL queries
- Build custom dashboards

---

## 🔧 Customization

### Add Custom Metrics

1. Create a Python exporter in `observability/exporters/`
2. Create a LaunchAgent plist in `observability/launchd/`
3. Run `./setup.sh` to install

**Example:**
```python
#!/usr/bin/env python3
# observability/exporters/my_custom_metrics.py

def collect_metrics():
    return "my_metric{label=\"value\"} 42\n"

if __name__ == "__main__":
    print(collect_metrics())
```

### Add Alert Rules

Edit `observability/prometheus/rules/*.yml`:

```yaml
- alert: HighCPU
  expr: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 90
  for: 5m
  annotations:
    summary: "CPU usage above 90%"
```

### Import Grafana Dashboards

1. Go to http://localhost:3000
2. Click **+** → **Import**
3. Enter dashboard ID:
   - `1860` - Node Exporter Full
   - `13639` - Node Exporter for Prometheus
   - `12486` - Loki Logs

---

## 🐛 Troubleshooting

### Services Won't Start

```bash
# Check what's using ports
lsof -i :9090  # Prometheus
lsof -i :3000  # Grafana

# Re-run setup
cd observability
./setup.sh
./start_all.sh
```

### Prometheus Not Starting

```bash
# Check config
promtool check config observability/prometheus/prometheus.yml

# View error log
tail -50 /opt/homebrew/var/log/prometheus.err.log

# Manual start test
prometheus --config.file=observability/prometheus/prometheus.yml
```

### Grafana Not Loading

```bash
# Check if running
brew services list | grep grafana

# Check logs
tail -50 /opt/homebrew/var/log/grafana.log

# Restart
brew services restart grafana
```

**📖 [Full Troubleshooting Guide →](SETUP.md#troubleshooting)**

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly on macOS
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Ideas for Contributions

- 🎨 New Grafana dashboards
- 📊 Additional macOS metrics exporters
- 🔔 More alert rule examples
- 📖 Documentation improvements
- 🐛 Bug fixes
- 🌍 Translations

---

## ⭐ Show Your Support

If this project helped you, please consider:

- ⭐ **Star this repository** on GitHub
- 🐦 **Share on Twitter/X** with #DevOps #Monitoring
- 📝 **Write a blog post** about your experience
- 💬 **Share in communities** (Reddit, HackerNews, etc.)
- 🤝 **Contribute** improvements

---

## 📊 Project Stats

- **100+ metrics** available out of the box
- **13 custom exporters** for macOS
- **14 days** metric retention (configurable)
- **< 5 minutes** to full setup
- **100% portable** - works on any Mac
- **Auto-restart** monitoring included
- **MIT License** - completely free

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Created by**: ANISHSAJIKUMAR

- GitHub: [@ANISHSAJIKUMAR](https://github.com/ANISHSAJIKUMAR)
- LinkedIn: [Connect with me](https://linkedin.com/in/anishskumar)

---

## 🙏 Acknowledgments

- **Prometheus** - Amazing metrics collection system
- **Grafana** - Beautiful visualization platform
- **Loki** - Simple yet powerful log aggregation
- **Homebrew** - Making macOS package management easy
- **Open Source Community** - For making this possible

---

## 🔗 Related Projects

- [Prometheus](https://prometheus.io/) - Official Prometheus
- [Grafana](https://grafana.com/) - Official Grafana
- [node_exporter](https://github.com/prometheus/node_exporter) - System metrics exporter
- [Loki](https://grafana.com/oss/loki/) - Log aggregation system

---

## 🏷️ Keywords

`prometheus` `grafana` `loki` `observability` `monitoring` `macos` `devops` `sre` `metrics` `dashboards` `alerting` `homebrew` `node-exporter` `system-monitoring` `battery-monitoring` `cpu-temperature` `network-monitoring` `mac-monitoring` `infrastructure-monitoring` `performance-monitoring` `real-time-monitoring` `time-series` `launchagent` `auto-restart` `health-check` `portable` `open-source`

---

<div align="center">

**Made with ❤️ for the DevOps community**

[![GitHub stars](https://img.shields.io/github/stars/ANISHSAJIKUMAR/macos-observatory?style=social)](https://github.com/ANISHSAJIKUMAR/macos-observatory/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ANISHSAJIKUMAR/macos-observatory?style=social)](https://github.com/ANISHSAJIKUMAR/macos-observatory/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/ANISHSAJIKUMAR/macos-observatory?style=social)](https://github.com/ANISHSAJIKUMAR/macos-observatory/watchers)

**⭐ Star this repo if you find it helpful!**

[Report Bug](https://github.com/ANISHSAJIKUMAR/macos-observatory/issues) · [Request Feature](https://github.com/ANISHSAJIKUMAR/macos-observatory/issues) · [Contribute](CONTRIBUTING.md)

</div>
