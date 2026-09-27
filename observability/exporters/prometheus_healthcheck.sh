#!/usr/bin/env bash
# Prometheus Health Check & Auto-Restart Script
# Checks if Prometheus is healthy and restarts it if down
set -euo pipefail

LOG_FILE="${HOME}/Library/Logs/prometheus-healthcheck.log"
MAX_RESTART_ATTEMPTS=3
RESTART_COUNT_FILE="/tmp/prometheus_restart_count"
HEALTH_URL="http://localhost:9090/-/healthy"
RETRY_DELAY=5

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

get_restart_count() {
    if [ -f "$RESTART_COUNT_FILE" ]; then
        cat "$RESTART_COUNT_FILE"
    else
        echo "0"
    fi
}

increment_restart_count() {
    local count=$(get_restart_count)
    echo $((count + 1)) > "$RESTART_COUNT_FILE"
}

reset_restart_count() {
    echo "0" > "$RESTART_COUNT_FILE"
}

check_prometheus_health() {
    # Try to connect to Prometheus health endpoint
    if curl -sf --max-time 5 "$HEALTH_URL" >/dev/null 2>&1; then
        return 0  # Healthy
    else
        return 1  # Unhealthy
    fi
}

check_prometheus_process() {
    # Check if Prometheus process is running
    if lsof -i :9090 >/dev/null 2>&1; then
        return 0  # Running
    else
        return 1  # Not running
    fi
}

restart_prometheus() {
    local restart_count=$(get_restart_count)

    if [ "$restart_count" -ge "$MAX_RESTART_ATTEMPTS" ]; then
        log "ERROR: Max restart attempts ($MAX_RESTART_ATTEMPTS) reached. Manual intervention required."
        log "Please check: tail -50 ~/Library/Logs/Homebrew/prometheus/error.log"
        return 1
    fi

    log "WARNING: Prometheus is unhealthy. Attempting restart (attempt $((restart_count + 1))/$MAX_RESTART_ATTEMPTS)..."

    # Stop Prometheus
    brew services stop prometheus 2>&1 | tee -a "$LOG_FILE"
    sleep 2

    # Start Prometheus
    brew services start prometheus 2>&1 | tee -a "$LOG_FILE"
    sleep 5

    # Verify restart
    for i in {1..10}; do
        if check_prometheus_health; then
            log "SUCCESS: Prometheus restarted successfully and is now healthy"
            reset_restart_count
            return 0
        fi
        log "Waiting for Prometheus to start... (attempt $i/10)"
        sleep "$RETRY_DELAY"
    done

    increment_restart_count
    log "ERROR: Prometheus restart failed to restore health"
    return 1
}

# Main execution
main() {
    # First check if process is running
    if ! check_prometheus_process; then
        log "WARNING: Prometheus process not running (port 9090 not listening)"
        restart_prometheus
        exit $?
    fi

    # Process is running, check health endpoint
    if check_prometheus_health; then
        # Healthy - reset restart counter
        local current_count=$(get_restart_count)
        if [ "$current_count" -gt 0 ]; then
            log "INFO: Prometheus is healthy. Resetting restart counter."
            reset_restart_count
        fi
        log "INFO: Prometheus is healthy ✓"
        exit 0
    else
        # Unhealthy - attempt restart
        log "WARNING: Prometheus health check failed"
        restart_prometheus
        exit $?
    fi
}

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

# Run main function
main
