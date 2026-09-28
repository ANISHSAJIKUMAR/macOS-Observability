#!/usr/bin/env python3
import os
import re
import subprocess
import time

from observability_env import get_textfile_dir, load_env

load_env()

OUTFILE = os.path.join(get_textfile_dir(), "net_connectivity.prom")

TARGETS = ["1.1.1.1", "8.8.8.8"]
IFACES = ["en0", "en1"]


def run(cmd):
    return subprocess.run(cmd, check=False, capture_output=True, text=True)


def ping_stats(target: str):
    # macOS ping summary: rtt min/avg/max/mdev = 10.123/12.345/15.678/0.500 ms
    # packet loss line: 3 packets transmitted, 3 packets received, 0.0% packet loss
    p = run(["/sbin/ping", "-c", "3", "-t", "2", target])
    out = p.stdout
    loss = None
    avg = None
    for line in out.splitlines():
        if "packet loss" in line:
            m = re.search(r"([0-9.]+)% packet loss", line)
            if m:
                loss = float(m.group(1))
        if "rtt min/avg/max" in line or "round-trip min/avg/max" in line:
            m = re.search(r"=\s*([0-9.]+)/([0-9.]+)/([0-9.]+)/([0-9.]+)\s*ms", line)
            if m:
                avg = float(m.group(2))
    return loss, avg


def iface_up(iface: str):
    p = run(["/sbin/ifconfig", iface])
    if p.returncode != 0:
        return None
    for line in p.stdout.splitlines():
        if "status:" in line:
            return 1.0 if "active" in line else 0.0
    return None


def main():
    lines = []
    lines.append("# HELP net_ping_loss_percent Packet loss percentage")
    lines.append("# TYPE net_ping_loss_percent gauge")
    lines.append("# HELP net_ping_latency_ms Average ping latency (ms)")
    lines.append("# TYPE net_ping_latency_ms gauge")

    for target in TARGETS:
        loss, avg = ping_stats(target)
        if loss is not None:
            lines.append(f"net_ping_loss_percent{{target=\"{target}\"}} {loss}")
        if avg is not None:
            lines.append(f"net_ping_latency_ms{{target=\"{target}\"}} {avg}")

    lines.append("# HELP net_iface_up Interface link state (1=up, 0=down)")
    lines.append("# TYPE net_iface_up gauge")
    for iface in IFACES:
        up = iface_up(iface)
        if up is not None:
            lines.append(f"net_iface_up{{iface=\"{iface}\"}} {up}")

    lines.append("# HELP net_connectivity_timestamp_seconds Export timestamp")
    lines.append("# TYPE net_connectivity_timestamp_seconds gauge")
    lines.append(f"net_connectivity_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
