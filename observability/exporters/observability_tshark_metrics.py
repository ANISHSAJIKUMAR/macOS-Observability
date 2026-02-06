#!/usr/bin/env python3
import os
import re
import subprocess
import time
from observability_env import load_env, get_textfile_dir
load_env()

OUTFILE = os.path.join(get_textfile_dir(), "tshark.prom")

IFACE = os.environ.get("TS_IFACE", "en0")
DURATION = int(os.environ.get("TS_DURATION", "5"))
TOP_N = int(os.environ.get("TS_TOP_N", "5"))


def run_tshark():
    cmd = [
        "/opt/homebrew/bin/tshark",
        "-i", IFACE,
        "-a", f"duration:{DURATION}",
        "-q",
        "-z", "io,stat,1",
        "-z", "conv,ip",
        "-z", "io,phs",
    ]
    return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)

def run_tshark_security():
    filters = [
        "tcp.flags.syn==1 && tcp.flags.ack==0",
        "tcp.flags.reset==1",
        "tcp.flags.fin==1",
        "tcp.analysis.retransmission",
        "tcp.analysis.fast_retransmission",
        "tcp.analysis.lost_segment",
        "tcp.analysis.out_of_order",
        "tcp.analysis.duplicate_ack",
        "tcp.analysis.zero_window",
        "tcp.analysis.zero_window_probe",
        "tcp.analysis.zero_window_probe_ack",
        "dns",
        "tls",
        "http",
        "ssh",
        "arp",
        "icmp",
        "udp.port==443",  # QUIC / HTTP3
        "mdns",
        "stun",
    ]
    cmd = [
        "/opt/homebrew/bin/tshark",
        "-i", IFACE,
        "-a", f"duration:{DURATION}",
        "-q",
    ]
    for flt in filters:
        cmd += ["-z", f"io,stat,0,{flt}"]
    return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)


def parse_size(val: str) -> float:
    if val is None:
        return 0.0
    val = val.replace("\u00a0", " ").replace(",", "").strip()
    m = re.search(r"([0-9.]+)\s*([kMG]?B)?", val)
    if not m:
        return 0.0
    num = float(m.group(1))
    unit = m.group(2) or "B"
    mult = 1.0
    if unit == "kB":
        mult = 1000.0
    elif unit == "MB":
        mult = 1000.0 ** 2
    elif unit == "GB":
        mult = 1000.0 ** 3
    return num * mult


def parse_io_stats(text: str):
    frames = 0
    bytes_ = 0
    for line in text.splitlines():
        m = re.search(r"\|\s*\d+\s*<>\s*\d+\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|", line)
        if m:
            try:
                frames += int(m.group(1))
                bytes_ += int(m.group(2))
            except Exception:
                continue
    return frames, bytes_


def parse_conversations(text: str):
    conv = []
    for line in text.splitlines():
        if "<->" not in line:
            continue
        m = re.search(
            r"^(\S+)\s+<->\s+(\S+)\s+(\d+)\s+([0-9.]+\s*[kMG]?B)\s+(\d+)\s+([0-9.]+\s*[kMG]?B)\s+(\d+)\s+([0-9.]+\s*[kMG]?B)",
            line.strip(),
        )
        if not m:
            continue
        try:
            src, dst = m.group(1), m.group(2)
            frames_total = int(m.group(7))
            bytes_total = parse_size(m.group(8))
        except Exception:
            continue
        conv.append((bytes_total, frames_total, src, dst))
    conv.sort(reverse=True, key=lambda x: x[0])
    return conv[:TOP_N]


def parse_protocols(text: str):
    protos = []
    for line in text.splitlines():
        m = re.search(r"^\s*([A-Za-z0-9_\-]+)\s+frames:(\d+)\s+bytes:(\d+)", line)
        if not m:
            continue
        proto = m.group(1)
        if proto in ("frame", "eth"):
            continue
        try:
            frames = int(m.group(2))
            bytes_ = int(m.group(3))
        except Exception:
            continue
        protos.append((proto, frames, bytes_))
    return protos

def parse_security_stats(text: str):
    # Parses multiple IO Statistics sections with Col 1: <filter>
    stats = {}
    current_filter = None
    for line in text.splitlines():
        m = re.search(r"Col\s+1:\s+(.+)$", line)
        if m:
            current_filter = m.group(1).replace("|", "").strip()
            continue
        if current_filter and re.search(r"<>", line) and "|" in line:
            # line: | 0.000 <> 3.003 |  10 | 1200 |
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 3:
                try:
                    frames = int(parts[1])
                    bytes_ = int(parts[2])
                    stats[current_filter] = (frames, bytes_)
                except Exception:
                    pass
            current_filter = None
    return stats


def main():
    lines = []
    lines.append("# HELP tshark_capture_success Whether tshark capture succeeded (1=yes, 0=no)")
    lines.append("# TYPE tshark_capture_success gauge")

    try:
        output = run_tshark()
        sec_output = run_tshark_security()
        frames, bytes_ = parse_io_stats(output)
        conv = parse_conversations(output)
        protos = parse_protocols(output)
        sec = parse_security_stats(sec_output)
        duration = max(DURATION, 1)

        lines.append("tshark_capture_success 1")
        lines.append("# HELP tshark_capture_frames_total Frames captured in the sampling window")
        lines.append("# TYPE tshark_capture_frames_total gauge")
        lines.append(f"tshark_capture_frames_total {frames}")

        lines.append("# HELP tshark_capture_bytes_total Bytes captured in the sampling window")
        lines.append("# TYPE tshark_capture_bytes_total gauge")
        lines.append(f"tshark_capture_bytes_total {bytes_}")

        lines.append("# HELP tshark_capture_pps Packets per second (approx)")
        lines.append("# TYPE tshark_capture_pps gauge")
        lines.append(f"tshark_capture_pps {frames / duration:.2f}")

        lines.append("# HELP tshark_capture_bps Bytes per second (approx)")
        lines.append("# TYPE tshark_capture_bps gauge")
        lines.append(f"tshark_capture_bps {bytes_ / duration:.2f}")

        lines.append("# HELP tshark_conv_bytes_total Bytes by top IP conversation")
        lines.append("# TYPE tshark_conv_bytes_total gauge")
        lines.append("# HELP tshark_conv_frames_total Frames by top IP conversation")
        lines.append("# TYPE tshark_conv_frames_total gauge")
        for bytes_total, frames_total, src, dst in conv:
            lines.append(f'tshark_conv_bytes_total{{src="{src}",dst="{dst}",iface="{IFACE}"}} {bytes_total}')
            lines.append(f'tshark_conv_frames_total{{src="{src}",dst="{dst}",iface="{IFACE}"}} {frames_total}')

        lines.append("# HELP tshark_proto_frames_total Frames by protocol (hierarchy)")
        lines.append("# TYPE tshark_proto_frames_total gauge")
        lines.append("# HELP tshark_proto_bytes_total Bytes by protocol (hierarchy)")
        lines.append("# TYPE tshark_proto_bytes_total gauge")
        for proto, fcount, bcount in protos:
            lines.append(f'tshark_proto_frames_total{{proto="{proto}",iface="{IFACE}"}} {fcount}')
            lines.append(f'tshark_proto_bytes_total{{proto="{proto}",iface="{IFACE}"}} {bcount}')

        lines.append("# HELP tshark_sec_frames_total Security-related frames by filter")
        lines.append("# TYPE tshark_sec_frames_total gauge")
        lines.append("# HELP tshark_sec_bytes_total Security-related bytes by filter")
        lines.append("# TYPE tshark_sec_bytes_total gauge")
        for flt, (fcount, bcount) in sec.items():
            flt_label = flt.replace("\\\\", "\\\\").replace("\"", "'")
            lines.append(f'tshark_sec_frames_total{{filter="{flt_label}",iface="{IFACE}"}} {fcount}')
            lines.append(f'tshark_sec_bytes_total{{filter="{flt_label}",iface="{IFACE}"}} {bcount}')

    except Exception as e:
        lines.append("tshark_capture_success 0")
        try:
            import sys
            sys.stderr.write(f"tshark_metrics error: {e}\\n")
        except Exception:
            pass

    lines.append("# HELP tshark_metrics_timestamp_seconds Export timestamp")
    lines.append("# TYPE tshark_metrics_timestamp_seconds gauge")
    lines.append(f"tshark_metrics_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()