#!/usr/bin/env python3
import subprocess
import time
import os
import re
from observability_env import load_env, get_textfile_dir
load_env()

OUTFILE = os.path.join(get_textfile_dir(), "smart.prom")


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


def diskutil_smart_status(device):
    try:
        out = subprocess.check_output(["/usr/sbin/diskutil", "info", device], text=True)
    except Exception:
        return ""
    for line in out.splitlines():
        if "SMART Status:" in line:
            return line.split(":", 1)[1].strip()
    return ""


def main():
    lines = []
    lines.append("# HELP smart_device_ok SMART overall health status (1=OK, 0=BAD)")
    lines.append("# TYPE smart_device_ok gauge")
    lines.append("# HELP smart_device_supported SMART support available (1=YES, 0=NO)")
    lines.append("# TYPE smart_device_supported gauge")
    lines.append("# HELP smart_status_verified SMART status verified via diskutil (1=Verified)")
    lines.append("# TYPE smart_status_verified gauge")
    lines.append("# HELP smart_status_label SMART status label (diskutil)")
    lines.append("# TYPE smart_status_label gauge")

    disks = list_disks()
    if not disks:
        lines.append('smart_device_supported{device="none"} 0')
    for dev in disks:
        out = smartctl(dev)
        if not out:
            status = diskutil_smart_status(dev)
            if status:
                supported = 1
                ok = 1 if status.lower() == "verified" else 0
                verified = 1 if status.lower() == "verified" else 0
                lines.append(f'smart_device_supported{{device="{dev}"}} {supported}')
                lines.append(f'smart_device_ok{{device="{dev}"}} {ok}')
                lines.append(f'smart_status_verified{{device="{dev}"}} {verified}')
                lines.append(f'smart_status_label{{device="{dev}",status="{status}"}} 1')
            else:
                lines.append(f'smart_device_supported{{device="{dev}"}} 0')
            continue
        if "SMART support is: Unavailable" in out:
            status = diskutil_smart_status(dev)
            if status:
                supported = 1
                ok = 1 if status.lower() == "verified" else 0
                verified = 1 if status.lower() == "verified" else 0
                lines.append(f'smart_device_supported{{device="{dev}"}} {supported}')
                lines.append(f'smart_device_ok{{device="{dev}"}} {ok}')
                lines.append(f'smart_status_verified{{device="{dev}"}} {verified}')
                lines.append(f'smart_status_label{{device="{dev}",status="{status}"}} 1')
            else:
                lines.append(f'smart_device_supported{{device="{dev}"}} 0')
            continue
        lines.append(f'smart_device_supported{{device="{dev}"}} 1')
        ok = None
        for line in out.splitlines():
            if "SMART overall-health self-assessment test result" in line or "SMART Health Status" in line:
                if "PASSED" in line or "OK" in line:
                    ok = 1
                else:
                    ok = 0
                break
        if ok is None:
            ok = 0
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
