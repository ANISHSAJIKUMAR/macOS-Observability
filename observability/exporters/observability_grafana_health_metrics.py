#!/usr/bin/env python3
import json
import ssl
import urllib.request
import time
import os
from observability_env import load_env, get_textfile_dir
load_env()

OUTFILE = os.path.join(get_textfile_dir(), "grafana_health.prom")
URLS = ["https://localhost:3000/api/health", "http://localhost:3000/api/health"]


def fetch_health():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    for url in URLS:
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, context=ctx, timeout=5) as r:
                data = json.load(r)
                return 1, data
        except Exception:
            continue
    return 0, {}


def main():
    up, data = fetch_health()
    status = data.get("database", "")
    version = data.get("version", "")

    def esc(v: str) -> str:
        return v.replace("\\", r"\\").replace("\n", r"\\n").replace('"', r'\\"')

    labels = []
    if status:
        labels.append(f'database="{esc(status)}"')
    if version:
        labels.append(f'version="{esc(version)}"')
    label_str = "{" + ",".join(labels) + "}" if labels else ""

    lines = []
    lines.append("# HELP grafana_up Grafana API health reachable (1=up, 0=down)")
    lines.append("# TYPE grafana_up gauge")
    lines.append(f"grafana_up{label_str} {up}")
    lines.append("# HELP grafana_health_timestamp_seconds Export timestamp")
    lines.append("# TYPE grafana_health_timestamp_seconds gauge")
    lines.append(f"grafana_health_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
