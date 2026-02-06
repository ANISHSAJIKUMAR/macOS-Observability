#!/usr/bin/env python3
import subprocess
import time
import re
import os
import json

OUTFILE = "/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/textfile/wifi.prom"


def run(cmd):
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception:
        return ""
    if p.returncode != 0:
        return ""
    return p.stdout


def parse_kv(text):
    data = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
    return data


def run_system_profiler_wifi():
    try:
        raw = subprocess.check_output(["/usr/sbin/system_profiler", "SPAirPortDataType", "-json"], text=True)
        data = json.loads(raw)
    except Exception:
        return {}
    try:
        iface = data["SPAirPortDataType"][0]["spairport_airport_interfaces"][0]
        current = iface.get("spairport_current_network_information", {})
        signal_noise = current.get("spairport_signal_noise", "")
        rate = current.get("spairport_network_rate", "")
        return {"signal_noise": signal_noise, "rate": rate}
    except Exception:
        return {}


def to_float(val):
    if val is None:
        return None
    try:
        return float(val)
    except Exception:
        m = re.search(r"[-+]?[0-9]*\.?[0-9]+", str(val))
        if m:
            try:
                return float(m.group(0))
            except Exception:
                return None
    return None


def main():
    out = run(["/usr/bin/wdutil", "info"])
    if not out:
        return
    data = parse_kv(out)

    ssid = data.get("SSID", "")
    bssid = data.get("BSSID", "")
    channel = data.get("Channel", data.get("channel", ""))
    security = data.get("Security", "")
    phy = data.get("PHY Mode", data.get("PHY", ""))
    rssi = to_float(data.get("RSSI", data.get("agrCtlRSSI", "")))
    noise = to_float(data.get("Noise", data.get("agrCtlNoise", "")))
    tx_rate = to_float(data.get("Tx Rate", data.get("lastTxRate", "")))
    max_rate = to_float(data.get("Max Rate", data.get("maxRate", "")))
    mcs = to_float(data.get("MCS Index", data.get("MCS", "")))
    cca = to_float(data.get("CCA", ""))
    nss = to_float(data.get("NSS", ""))

    source = "wdutil"
    # Some macOS builds report RSSI as 0 via wdutil. Fall back to system_profiler.
    if rssi is None or rssi == 0:
        sp = run_system_profiler_wifi()
        sig = sp.get("signal_noise", "")
        # format: "-35 dBm / -95 dBm"
        if sig and "/" in sig:
            parts = sig.split("/")
            if len(parts) >= 2:
                rssi = to_float(parts[0])
                noise = to_float(parts[1])
                source = "system_profiler"
        rate = sp.get("rate")
        if rate:
            tx_rate = to_float(rate)

    def esc(v: str) -> str:
        return v.replace("\\", r"\\").replace("\n", r"\\n").replace('"', r'\\"')

    labels = []
    if ssid:
        labels.append(f'ssid="{esc(ssid)}"')
    if bssid:
        labels.append(f'bssid="{esc(bssid)}"')
    if channel:
        labels.append(f'channel="{esc(channel)}"')
    if security:
        labels.append(f'security="{esc(security)}"')
    if phy:
        labels.append(f'phy="{esc(phy)}"')
    label_str = "{" + ",".join(labels) + "}" if labels else ""

    lines = []
    lines.append("# HELP wifi_rssi_dbm Wi-Fi signal strength (dBm)")
    lines.append("# TYPE wifi_rssi_dbm gauge")
    if rssi is not None:
        lines.append(f"wifi_rssi_dbm{label_str} {rssi}")

    lines.append("# HELP wifi_noise_dbm Wi-Fi noise level (dBm)")
    lines.append("# TYPE wifi_noise_dbm gauge")
    if noise is not None:
        lines.append(f"wifi_noise_dbm{label_str} {noise}")

    lines.append("# HELP wifi_snr_db Signal-to-noise ratio (dB)")
    lines.append("# TYPE wifi_snr_db gauge")
    if rssi is not None and noise is not None:
        lines.append(f"wifi_snr_db{label_str} {rssi - noise}")

    lines.append("# HELP wifi_tx_rate_mbps Current TX rate (Mbps)")
    lines.append("# TYPE wifi_tx_rate_mbps gauge")
    if tx_rate is not None:
        lines.append(f"wifi_tx_rate_mbps{label_str} {tx_rate}")

    lines.append("# HELP wifi_max_rate_mbps Max supported rate (Mbps)")
    lines.append("# TYPE wifi_max_rate_mbps gauge")
    if max_rate is not None:
        lines.append(f"wifi_max_rate_mbps{label_str} {max_rate}")

    lines.append("# HELP wifi_mcs Modulation and coding scheme (MCS)")
    lines.append("# TYPE wifi_mcs gauge")
    if mcs is not None:
        lines.append(f"wifi_mcs{label_str} {mcs}")

    lines.append("# HELP wifi_cca_percent Clear channel assessment busy percent")
    lines.append("# TYPE wifi_cca_percent gauge")
    if cca is not None:
        lines.append(f"wifi_cca_percent{label_str} {cca}")

    lines.append("# HELP wifi_nss Number of spatial streams")
    lines.append("# TYPE wifi_nss gauge")
    if nss is not None:
        lines.append(f"wifi_nss{label_str} {nss}")

    lines.append("# HELP wifi_metrics_timestamp_seconds Export timestamp")
    lines.append("# TYPE wifi_metrics_timestamp_seconds gauge")
    lines.append(f"wifi_metrics_timestamp_seconds {time.time()}")

    lines.append("# HELP wifi_metrics_source Wi-Fi metrics source (wdutil or system_profiler)")
    lines.append("# TYPE wifi_metrics_source gauge")
    lines.append(f'wifi_metrics_source{{source="{source}"}} 1')

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
