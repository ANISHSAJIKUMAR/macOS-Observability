# Screenshot Guide for Premium GitHub Presentation

This guide helps you capture the best screenshots to showcase the macOS Observatory.

## 📸 Screenshots to Capture

### 1. Grafana Dashboard (Primary Screenshot)
**URL**: http://localhost:3000

**What to capture**:
- Login screen showing clean UI
- Main dashboard with metrics
- System metrics panels (CPU, Memory, Disk)
- Custom macOS metrics (Battery, Network)

**Tips**:
- Use full screen (Cmd+Ctrl+F)
- Make window ~1600px wide for best quality
- Capture with Cmd+Shift+4, then Spacebar to capture window
- Save as: `screenshots/grafana-dashboard.png`

**Recommended dashboards to screenshot**:
1. **Overview Dashboard** - Main system health
2. **System Metrics** - CPU, Memory, Disk usage
3. **macOS Specific** - Battery, Network, VMware
4. **Logs View** - Loki log aggregation

### 2. Prometheus UI
**URL**: http://localhost:9090

**What to capture**:
- Main query interface with a sample query
- Targets page showing all exporters (http://localhost:9090/targets)
- Graph view with metrics

**Sample queries to show**:
```promql
# CPU usage
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory usage
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Battery level
mac_battery_charge_percent

# Network connectivity
mac_net_connectivity_status
```

### 3. Prometheus Targets
**URL**: http://localhost:9090/targets

**What to capture**:
- All targets showing as "UP" (green)
- Shows node_exporter, promtail, and custom exporters
- Save as: `screenshots/prometheus-targets.png`

### 4. Terminal - Setup Process
**What to capture**:
- Running `./setup.sh` successfully
- Output showing all services configured
- Clean, professional terminal with good colors

**Commands to screenshot**:
```bash
cd macos-observatory/observability
./setup.sh
# Capture the success output

./start_all.sh
# Capture services starting

./status_all.sh
# Capture status showing all services running
```

### 5. Architecture Diagram
Create or capture an architecture diagram showing:
- Grafana → Prometheus → Exporters
- Loki → Promtail → Logs
- Auto-restart health monitor

## 📁 Screenshot Organization

Create this structure:
```
macos-observatory/
├── screenshots/
│   ├── 1-grafana-main-dashboard.png
│   ├── 2-grafana-system-metrics.png
│   ├── 3-grafana-macos-metrics.png
│   ├── 4-prometheus-targets.png
│   ├── 5-prometheus-query.png
│   ├── 6-terminal-setup.png
│   ├── 7-terminal-status.png
│   └── architecture.png (optional)
```

## 🎨 Making Screenshots Look Premium

### Before Taking Screenshots:

1. **Clean up your desktop**
   - Hide desktop icons: `defaults write com.apple.finder CreateDesktop false; killall Finder`
   - Use a clean wallpaper

2. **Terminal appearance**
   - Use a nice theme (like Dracula, Nord, or Solarized)
   - Increase font size (14-16pt)
   - Use full screen or large window

3. **Browser**
   - Hide bookmarks bar
   - Zoom to 100%
   - Use full screen mode
   - Clear unnecessary tabs

4. **Grafana**
   - Use dark theme (looks more professional)
   - Set time range to show recent data (Last 6 hours)
   - Make sure panels have data

### Taking the Screenshot:

**Mac Screenshot Tips**:
- `Cmd + Shift + 4` then `Spacebar` = Window screenshot (with shadow)
- `Cmd + Shift + 4` = Select area
- `Cmd + Shift + 4` then `Spacebar` then hold `Option` = Window without shadow
- `Cmd + Shift + 3` = Full screen

**Recommended**: Window screenshots with shadow for a professional look

### After Taking Screenshots:

1. **Optimize images**:
```bash
# Install imagemagick if needed
brew install imagemagick

# Resize to max 1600px width (keeps quality, reduces file size)
for img in screenshots/*.png; do
  convert "$img" -resize 1600x\> "$img"
done
```

2. **Add to git**:
```bash
git add screenshots/
git commit -m "Add premium screenshots for GitHub presentation"
```

## 📝 What to Highlight in Each Screenshot

### Grafana Dashboard
- ✅ Multiple panels showing different metrics
- ✅ Professional dark theme
- ✅ Real data (not fake/empty)
- ✅ Time range selector visible
- ✅ Clean, organized layout

### Prometheus Targets
- ✅ All targets showing "UP" in green
- ✅ Multiple exporters (node_exporter + custom)
- ✅ Health check endpoint visible
- ✅ Last scrape time recent

### Terminal
- ✅ Successful setup output
- ✅ All checks passing (✓ symbols)
- ✅ Clear, readable font
- ✅ Professional color scheme

## 🎯 Screenshot Checklist

Before pushing to GitHub, ensure you have:

- [ ] Main Grafana dashboard (wide shot showing multiple panels)
- [ ] Grafana system metrics (CPU, Memory, Disk)
- [ ] Grafana macOS-specific metrics (Battery, Network)
- [ ] Prometheus targets page (all green/UP)
- [ ] Prometheus query example
- [ ] Terminal showing successful setup
- [ ] Terminal showing all services running
- [ ] (Optional) Architecture diagram

## 💡 Pro Tips

1. **Timing**: Take screenshots when you have interesting data
   - Let it run for a few hours to get graphs with curves
   - Show some activity (not flatlined metrics)

2. **Consistency**: Use the same window size for all browser screenshots

3. **Quality**: Always use PNG (not JPG) for UI screenshots

4. **Size**: Keep individual files under 500KB
   - GitHub README displays better with optimized images
   - Use: `pngquant screenshots/*.png` to compress

5. **Watermark**: Consider adding project name/logo to screenshots

## 🖼️ Example Screenshot Captions for README

```markdown
### Grafana Dashboard
![Grafana Main Dashboard](screenshots/grafana-main-dashboard.png)
*Real-time macOS system monitoring with custom metrics*

### Prometheus Targets
![Prometheus Targets](screenshots/prometheus-targets.png)
*All exporters healthy and collecting metrics*

### Quick Setup
![Terminal Setup](screenshots/terminal-setup.png)
*One-command setup with automatic configuration*
```

## 🎬 Next Steps

1. Capture all screenshots following this guide
2. Save them in `screenshots/` directory
3. Reference them in `README.md`
4. Push to GitHub with your commit
5. Verify they display correctly on GitHub

---

**Note**: GitHub displays images best at 1000-1600px width. Larger images are automatically scaled down, so optimize beforehand for faster loading.
