#!/usr/bin/env python3
import glob
import logging
import os
import re
import subprocess
import time

from observability_env import get_textfile_dir, load_env

load_env()

OUTFILE = os.path.join(get_textfile_dir(), "vmware_fusion.prom")

DEFAULT_VMRUN = "/Applications/VMware Fusion.app/Contents/Library/vmrun"


def run(cmd):
    try:
        p = subprocess.run(cmd, check=False, capture_output=True, text=True)
    except Exception:
        logging.getLogger(__name__).exception("Metric collection failed")
        return ""
    if p.returncode != 0:
        return ""
    return p.stdout


def find_vmrun():
    if os.path.exists(DEFAULT_VMRUN):
        return DEFAULT_VMRUN
    # fallback: try mdfind
    out = run(["/usr/bin/mdfind", "kMDItemFSName == 'vmrun'" ])
    for line in out.splitlines():
        if line.endswith("/vmrun") and os.path.exists(line):
            return line
    return None


def parse_vmx(path):
    info = {}
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"')
                info[k] = v
    except Exception:
        logging.getLogger(__name__).exception("Metric collection failed")
        return info
    return info


def vm_name_from_vmx(path, vmx_info):
    name = vmx_info.get("displayName")
    if name:
        return name
    return os.path.splitext(os.path.basename(path))[0]


def list_running_vms(vmrun):
    out = run([vmrun, "list"])
    vms = []
    for line in out.splitlines():
        if line.startswith("Total running VMs"):
            continue
        line = line.strip()
        if line:
            vms.append(line)
    return vms


def get_guest_ip(vmrun, vmx_path):
    out = run([vmrun, "getGuestIPAddress", vmx_path])
    ip = out.strip()
    if ip and re.match(r"\d+\.\d+\.\d+\.\d+", ip):
        return ip
    return ""


def find_vmx_from_processes():
    # map vmx_path -> (cpu, rss_mb)
    out = run(["/bin/ps", "-axo", "pid,%cpu,rss,command"])
    usage = {}
    for line in out.splitlines():
        if "vmware-vmx" not in line:
            continue
        # find vmx path in command
        m = re.search(r"(/[^\s]+\.vmx)", line)
        if not m:
            continue
        vmx = m.group(1)
        parts = line.split(None, 3)
        if len(parts) < 4:
            continue
        try:
            cpu = float(parts[1])
            rss_kb = float(parts[2])
        except Exception:
            logging.getLogger(__name__).exception("Metric collection failed")
            continue
        rss_mb = rss_kb / 1024.0
        usage[vmx] = (cpu, rss_mb)
    return usage


def vmdk_info(vmx_path, vmx_info):
    vmdks = []
    for k, v in vmx_info.items():
        if k.endswith(".fileName") and v.endswith(".vmdk"):
            vmdks.append(v)
    sizes = []
    base = os.path.dirname(vmx_path)
    for v in vmdks:
        p = v if os.path.isabs(v) else os.path.join(base, v)
        if os.path.exists(p):
            try:
                sizes.append(os.path.getsize(p))
            except Exception:
                logging.getLogger(__name__).exception("Metric collection failed")
    return sum(sizes)


def count_snapshots(vmx_path):
    base = os.path.dirname(vmx_path)
    count = 0
    for ext in ("*.vmsn", "*.vmss"):
        count += len(glob.glob(os.path.join(base, ext)))
    return count


def main():
    vmrun = find_vmrun()

    running = set(list_running_vms(vmrun)) if vmrun else set()
    usage = find_vmx_from_processes()

    # Find all VMX files in default Fusion locations
    vmx_files = []
    home = os.path.expanduser("~")
    candidates = [
        os.path.join(home, "Virtual Machines.localized"),
        os.path.join(home, "Documents", "Virtual Machines.localized"),
        os.path.join(home, "Documents", "Virtual Machines"),
    ]
    for c in candidates:
        if os.path.isdir(c):
            vmx_files.extend(glob.glob(os.path.join(c, "**", "*.vmx"), recursive=True))

    # Also include any running VMX not in default locations
    for vmx in running:
        if vmx not in vmx_files:
            vmx_files.append(vmx)

    lines = [
        "# TYPE vmware_fusion_available gauge",
        f"vmware_fusion_available {int(bool(vmrun))}",
        "# TYPE vmware_fusion_vm_count gauge",
        f"vmware_fusion_vm_count {len(set(vmx_files))}",
    ]
    lines.append("# HELP vmware_fusion_vm_running VM running state (1=running, 0=stopped)")
    lines.append("# TYPE vmware_fusion_vm_running gauge")
    lines.append("# HELP vmware_fusion_vm_cpu_percent VM CPU usage percent (from vmware-vmx process)")
    lines.append("# TYPE vmware_fusion_vm_cpu_percent gauge")
    lines.append("# HELP vmware_fusion_vm_mem_mb VM memory RSS in MB (from vmware-vmx process)")
    lines.append("# TYPE vmware_fusion_vm_mem_mb gauge")
    lines.append("# HELP vmware_fusion_vm_config_vcpus VM configured vCPU count")
    lines.append("# TYPE vmware_fusion_vm_config_vcpus gauge")
    lines.append("# HELP vmware_fusion_vm_config_mem_mb VM configured memory (MB)")
    lines.append("# TYPE vmware_fusion_vm_config_mem_mb gauge")
    lines.append("# HELP vmware_fusion_vm_vmdk_bytes Total VMDK size bytes")
    lines.append("# TYPE vmware_fusion_vm_vmdk_bytes gauge")
    lines.append("# HELP vmware_fusion_vm_snapshot_count Snapshot count")
    lines.append("# TYPE vmware_fusion_vm_snapshot_count gauge")
    lines.append("# HELP vmware_fusion_vm_guest_tools Guest tools/IP availability (1=yes, 0=no)")
    lines.append("# TYPE vmware_fusion_vm_guest_tools gauge")

    for vmx in sorted(set(vmx_files)):
        info = parse_vmx(vmx)
        name = vm_name_from_vmx(vmx, info)
        vcpus = info.get("numvcpus")
        mem = info.get("memsize")
        vmdk_bytes = vmdk_info(vmx, info)
        snaps = count_snapshots(vmx)

        cpu, rss_mb = usage.get(vmx, (None, None))
        is_running = 1 if vmx in running else 0

        guest_ip = ""
        tools_ok = 0
        if is_running:
            guest_ip = get_guest_ip(vmrun, vmx)
            if guest_ip:
                tools_ok = 1

        def esc(v):
            return str(v).replace("\\", r"\\").replace("\n", r"\n").replace('"', r'\\"')

        labels = f'{{vm_name="{esc(name)}",vmx_path="{esc(vmx)}",guest_ip="{esc(guest_ip)}"}}'
        lines.append(f"vmware_fusion_vm_running{labels} {is_running}")
        if cpu is not None:
            lines.append(f"vmware_fusion_vm_cpu_percent{labels} {cpu}")
        if rss_mb is not None:
            lines.append(f"vmware_fusion_vm_mem_mb{labels} {rss_mb}")
        if vcpus:
            try:
                lines.append(f"vmware_fusion_vm_config_vcpus{labels} {float(vcpus)}")
            except Exception:
                logging.getLogger(__name__).exception("Metric collection failed")
        if mem:
            try:
                lines.append(f"vmware_fusion_vm_config_mem_mb{labels} {float(mem)}")
            except Exception:
                logging.getLogger(__name__).exception("Metric collection failed")
        lines.append(f"vmware_fusion_vm_vmdk_bytes{labels} {vmdk_bytes}")
        lines.append(f"vmware_fusion_vm_snapshot_count{labels} {snaps}")
        lines.append(f"vmware_fusion_vm_guest_tools{labels} {tools_ok}")

    lines.append("# HELP vmware_fusion_metrics_timestamp_seconds Export timestamp")
    lines.append("# TYPE vmware_fusion_metrics_timestamp_seconds gauge")
    lines.append(f"vmware_fusion_metrics_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
