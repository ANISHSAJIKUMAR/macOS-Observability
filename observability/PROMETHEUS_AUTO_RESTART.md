# Prometheus Auto-Restart Health Check

## Overview
Automatic health monitoring and restart system for Prometheus to ensure continuous operation.

## Features

### 1. **Automatic Health Monitoring**
- Checks Prometheus every 60 seconds
- Tests both process status (port 9090) and HTTP health endpoint
- Logs all checks and actions

### 2. **Smart Auto-Restart**
- Automatically restarts Prometheus if unhealthy
- Maximum 3 restart attempts to prevent restart loops
- 5-second retry delay between checks
- Resets restart counter when service is healthy

### 3. **Comprehensive Logging**
- Main log: `~/Library/Logs/prometheus-healthcheck.log`
- Stdout: `~/Library/Logs/prometheus-healthcheck-stdout.log`
- Stderr: `~/Library/Logs/prometheus-healthcheck-stderr.log`

## How It Works

```
Every 60 seconds:
  ├─ Check if Prometheus process is running (port 9090)
  │  └─ If not running → Restart
  ├─ Check HTTP health endpoint (http://localhost:9090/-/healthy)
  │  └─ If unhealthy → Restart
  └─ If healthy → Reset restart counter
```

## Components

### 1. Health Check Script
Location: `observability/exporters/prometheus_healthcheck.sh`

Functions:
- `check_prometheus_health()` - Tests HTTP health endpoint
- `check_prometheus_process()` - Verifies process is running
- `restart_prometheus()` - Restarts via brew services
- Smart retry logic with exponential backoff

### 2. LaunchAgent
Location: `observability/launchd/observability.prometheus_healthcheck.plist`

Configuration:
- Runs every 60 seconds (StartInterval: 60)
- Runs at system load (RunAtLoad: true)
- Background process (doesn't block)

## Manual Control

### Check Status
```bash
# View recent health checks
tail -20 ~/Library/Logs/prometheus-healthcheck.log

# Run health check manually
~/Projects/Active/macos-observatory/observability/exporters/prometheus_healthcheck.sh

# Check LaunchAgent status
launchctl list | grep prometheus_healthcheck
```

### Enable/Disable
```bash
# Disable auto-restart
launchctl unload ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist

# Enable auto-restart
launchctl load ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist
```

### Reset Restart Counter
```bash
rm /tmp/prometheus_restart_count
```

## Configuration

### Adjust Check Interval
Edit `observability.prometheus_healthcheck.plist`:
```xml
<key>StartInterval</key>
<integer>60</integer>  <!-- Change to desired seconds -->
```

Then reload:
```bash
launchctl unload ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist
launchctl load ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist
```

### Adjust Restart Attempts
Edit `prometheus_healthcheck.sh`:
```bash
MAX_RESTART_ATTEMPTS=3  # Change to desired number
RETRY_DELAY=5           # Seconds between retries
```

## Logs & Monitoring

### View Live Logs
```bash
# Watch health check activity
tail -f ~/Library/Logs/prometheus-healthcheck.log

# View last 50 lines
tail -50 ~/Library/Logs/prometheus-healthcheck.log
```

### Log Format
```
[2026-09-27 17:30:00] INFO: Prometheus is healthy ✓
[2026-09-27 17:31:00] WARNING: Prometheus health check failed
[2026-09-27 17:31:00] WARNING: Prometheus is unhealthy. Attempting restart (attempt 1/3)...
[2026-09-27 17:31:15] SUCCESS: Prometheus restarted successfully and is now healthy
```

## Safety Features

1. **Restart Limit**: Maximum 3 attempts to prevent restart loops
2. **Cooldown Period**: 5-second delay between restart attempts
3. **Process Verification**: Checks both process and HTTP health
4. **Graceful Restart**: Uses `brew services` for clean restarts
5. **Log Rotation**: System handles log rotation automatically

## Troubleshooting

### Health Check Not Running
```bash
# Check LaunchAgent status
launchctl list | grep prometheus_healthcheck

# Reload LaunchAgent
launchctl unload ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist
launchctl load ~/Library/LaunchAgents/observability.prometheus_healthcheck.plist
```

### Max Restarts Reached
```bash
# Check what's wrong
tail -50 ~/Library/Logs/Homebrew/prometheus/error.log

# Reset counter after fixing
rm /tmp/prometheus_restart_count

# Manual restart
brew services restart prometheus
```

### Script Permissions
```bash
chmod +x ~/Projects/Active/macos-observatory/observability/exporters/prometheus_healthcheck.sh
```

## Integration with Observability Stack

This health check runs alongside other custom exporters:
- Battery metrics
- Network connectivity
- VMware Fusion metrics
- Grafana health
- System info

All managed via LaunchAgents in `observability/launchd/`

## Benefits

✓ **Automatic Recovery**: No manual intervention for transient issues
✓ **Continuous Monitoring**: Ensures Prometheus stays operational
✓ **Smart Retry Logic**: Prevents restart loops
✓ **Comprehensive Logging**: Easy troubleshooting
✓ **Zero Downtime Goal**: Restarts within 15-20 seconds
✓ **Lightweight**: Minimal resource usage (runs every 60s)

## Created
September 27, 2026

## Version
1.0
