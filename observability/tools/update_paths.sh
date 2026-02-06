#!/usr/bin/env bash
set -euo pipefail

OBS_BASE="${OBS_BASE:-$(cd "$(dirname "$0")/.." && pwd)}"
ENV_FILE="${OBS_ENV_FILE:-$OBS_BASE/.env}"
if [ -f "$ENV_FILE" ]; then
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
fi

if [ -z "${OBS_BASE:-}" ]; then
  echo "OBS_BASE not set" >&2
  exit 1
fi

python3 - <<PY
import os
from pathlib import Path

obs_base = os.environ.get('OBS_BASE')
if not obs_base:
    raise SystemExit('OBS_BASE not set')

root = Path(obs_base)
paths = list((root / 'launchd').glob('observability.*.plist'))
paths += [root / 'prometheus' / 'prometheus.yml', root / 'prometheus' / 'prometheus.args', root / 'node_exporter' / 'node_exporter.args']
paths += list((root / 'exporters').glob('observability_*.py'))

old_bases = [
    '/Users/anishskumar/Anish-DevOps-Lab/observability',
    str(root)
]

for p in paths:
    if not p.exists():
        continue
    data = p.read_text()
    for old in set(old_bases):
        if old and old in data:
            data = data.replace(old, obs_base)
    p.write_text(data)

print('Updated paths in config files to', obs_base)
PY

echo "Copying LaunchAgents/Daemons..."
cp -f "$OBS_BASE/launchd"/*.plist "$HOME/Library/LaunchAgents/" 2>/dev/null || true
if command -v sudo >/dev/null 2>&1; then
  sudo cp -f "$OBS_BASE/launchd"/*.plist /Library/LaunchDaemons/ 2>/dev/null || true
fi

echo "Done."
