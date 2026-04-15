#!/usr/bin/env python3
import subprocess
import time
import platform
import socket
import os
from observability_env import load_env, get_textfile_dir
load_env()

OUTFILE = os.path.join(get_textfile_dir(), "mac_system_info.prom")


def run(cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        return ""
    return p.stdout.strip()


def get_ip():
    # Prefer Wi‑Fi (en0) then en1
    for iface in ["en0", "en1"]:
        ip = run(["/usr/sbin/ipconfig", "getifaddr", iface])
        if ip:
            return ip
    return ""


def get_router():
    out = run(["/usr/sbin/netstat", "-rn"])
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0] == "default":
            return parts[1]
    return ""


def get_wifi_ssid():
    out = run(["/usr/sbin/networksetup", "-getairportnetwork", "en0"])
    # "Current Wi-Fi Network: SSID" or "You are not associated..."
    if ":" in out:
        return out.split(":", 1)[1].strip()
    return ""

def get_hw_model():
    return run(["/usr/sbin/sysctl", "-n", "hw.model"])

def get_cpu_brand():
    # Apple Silicon typically returns a brand string here
    return run(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"]) or ""

def get_cpu_cores():
    return run(["/usr/sbin/sysctl", "-n", "hw.ncpu"])

def get_mem_bytes():
    return run(["/usr/sbin/sysctl", "-n", "hw.memsize"])

def format_bytes_to_gb(val):
    try:
        b = float(val)
    except Exception:
        return val
    gb = b / (1024 ** 3)
    return f"{gb:.1f} GB"


def main():
    hostname = socket.gethostname()
    os_version = run(["/usr/bin/sw_vers", "-productVersion"])
    os_build = run(["/usr/bin/sw_vers", "-buildVersion"])
    kernel = platform.release()
    arch = platform.machine()
    ip = get_ip()
    router = get_router()
    ssid = get_wifi_ssid()
    hw_model = get_hw_model()
    cpu_brand = get_cpu_brand()
    cpu_cores = get_cpu_cores()
    mem_bytes = get_mem_bytes()
    mem_human = format_bytes_to_gb(mem_bytes)

    labels = {
        "hostname": hostname,
        "os_version": os_version,
        "os_build": os_build,
        "kernel": kernel,
        "arch": arch,
        "hw_model": hw_model,
        "cpu_brand": cpu_brand,
        "cpu_cores": cpu_cores,
        "mem_bytes": mem_human,
        "primary_ip": ip,
        "router": router,
        "wifi_ssid": ssid,
    }

    # Escape label values
    def esc(v):
        return v.replace("\\", r"\\").replace("\n", r"\\n").replace('"', r'\\"')

    label_str = ",".join([f'{k}="{esc(v)}"' for k, v in labels.items()])

    lines = []
    lines.append("# HELP mac_system_info Static system info as labels")
    lines.append("# TYPE mac_system_info gauge")
    lines.append(f"mac_system_info{{{label_str}}} 1")
    lines.append("# HELP mac_system_kv System info key/value pairs")
    lines.append("# TYPE mac_system_kv gauge")
    for k, v in labels.items():
        lines.append(f'mac_system_kv{{key="{esc(k)}",value="{esc(v)}"}} 1')
    lines.append("# HELP mac_system_info_timestamp_seconds Export timestamp")
    lines.append("# TYPE mac_system_info_timestamp_seconds gauge")
    lines.append(f"mac_system_info_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
