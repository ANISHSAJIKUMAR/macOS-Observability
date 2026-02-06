#!/usr/bin/env bash
set -euo pipefail

OBS_BASE="${OBS_BASE:-$(cd "$(dirname "$0")" && pwd)}"
ENV_FILE="${OBS_ENV_FILE:-$OBS_BASE/.env}"
if [ -f "$ENV_FILE" ]; then
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
fi
log() { printf "[status] %s\n" "$*"; }

SUDO="sudo -n"
CAN_SUDO=1
if ! $SUDO -v >/dev/null 2>&1; then
  CAN_SUDO=0
fi

log "Core services (brew)"
if command -v brew >/dev/null 2>&1; then
  brew services list | egrep 'grafana|prometheus|loki|node_exporter' || true
else
  log "brew not found"
fi

log "HTTP health checks"
if command -v curl >/dev/null 2>&1; then
  curl -sf http://localhost:9090/-/ready >/dev/null && log "Prometheus ready" || log "Prometheus not ready"
  curl -sf http://localhost:9100/metrics >/dev/null && log "node_exporter OK" || log "node_exporter not responding"
  curl -sf http://localhost:3100/ready >/dev/null && log "Loki ready" || log "Loki not ready"
  curl -skf https://localhost:3000/api/health >/dev/null && log "Grafana OK" || log "Grafana not responding"
fi

log "Prometheus targets"
if command -v curl >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY'
import json, subprocess, sys
try:
    raw = subprocess.check_output(['curl','-sf','http://localhost:9090/api/v1/targets'])
except Exception:
    print('targets unavailable')
    sys.exit(0)
try:
    j=json.loads(raw)
except Exception:
    print('targets unavailable')
    sys.exit(0)
active=j.get('data',{}).get('activeTargets',[])
print('targets', len(active))
for t in active:
    if t.get('health')!='up':
        print('DOWN', t.get('labels',{}).get('job'), t.get('scrapeUrl'), t.get('lastError'))
PY
fi

log "LaunchAgents (user)"
USER_DOMAIN="gui/$(id -u)"
for svc in \
  observability.net_connectivity \
  observability.mac_system_info \
  observability.launchd_metrics \
  observability.grafana_health \
  observability.prom_config_checksum \
  observability.battery_metrics
  observability.vmware_fusion_metrics
  do
    launchctl print "$USER_DOMAIN/$svc" 2>/dev/null | awk '/state =|last exit code =/' | head -n 2 | sed "s/^/[agent] $svc /" || true
  done

log "LaunchDaemons (root)"
if [ "$CAN_SUDO" -eq 1 ]; then
  for svc in \
    observability.wdutil_metrics \
    observability.cpu_fan_metrics \
    observability.smart_metrics \
    observability.promtail \
    observability.tshark_metrics
    do
      $SUDO launchctl print system/$svc 2>/dev/null | awk '/state =|last exit code =/' | head -n 2 | sed "s/^/[daemon] $svc /" || true
    done
else
  log "root checks skipped (sudo -n not available)"
fi

log "Textfile exporter freshness"
TEXTDIR="${TEXTFILE_DIR:-$OBS_BASE/node_exporter/textfile}"
if command -v python3 >/dev/null 2>&1; then
  python3 - <<PY
import os, time, glob
text_dir="$TEXTDIR"
now=time.time()
stale=[]
for fp in sorted(glob.glob(text_dir+'/*.prom')):
    age=now-os.stat(fp).st_mtime
    if age>300:
        stale.append((os.path.basename(fp), int(age)))
print('stale', stale)
PY
fi

log "Done"