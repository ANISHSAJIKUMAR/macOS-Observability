#!/usr/bin/env python3
import subprocess
import time
import os
import re

OUTFILE = "/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/textfile/smart.prom"


def list_disks():
    try:
        out = subprocess.check_output(["/usr/sbin/diskutil", "list"], text=True)
    except Exception:
        return []
    disks = []
    for line in out.splitlines():
        m = re.match(r"/dev/(disk\d+)", line.strip())
        if m:
            disks.append(m.group(1))
    # unique
    return list(dict.fromkeys(disks))


def smartctl(device):
    try:
        out = subprocess.check_output(["/opt/homebrew/sbin/smartctl", "-a", f"/dev/{device}"], text=True, stderr=subprocess.STDOUT)
        return out
    except Exception:
        return ""


def main():
    lines = []
    lines.append("# HELP smart_device_ok SMART overall health status (1=OK, 0=BAD)")
    lines.append("# TYPE smart_device_ok gauge")

    for dev in list_disks():
        out = smartctl(dev)
        if not out:
            continue
        ok = None
        for line in out.splitlines():
            if "SMART overall-health self-assessment test result" in line or "SMART Health Status" in line:
                if "PASSED" in line or "OK" in line:
                    ok = 1
                else:
                    ok = 0
                break
        if ok is not None:
            lines.append(f'smart_device_ok{{device="{dev}"}} {ok}')

    lines.append("# HELP smart_metrics_timestamp_seconds Export timestamp")
    lines.append("# TYPE smart_metrics_timestamp_seconds gauge")
    lines.append(f"smart_metrics_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
