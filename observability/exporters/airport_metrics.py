#!/usr/bin/env python3
import subprocess
import time

AIRPORT = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
OUTFILE = "/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/textfile/airport.prom"

def escape_label_value(v: str) -> str:
    return v.replace("\\", r"\\").replace("\n", r"\\n").replace('"', r'\\"')


def parse_airport(output: str):
    data = {}
    for line in output.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
    return data


def to_float(value: str):
    try:
        return float(value)
    except Exception:
        return None


def main():
    try:
        out = subprocess.check_output([AIRPORT, "-I"], text=True)
    except Exception:
        return

    data = parse_airport(out)

    ssid = data.get("SSID", "")
    bssid = data.get("BSSID", "")
    channel = data.get("channel", "")
    rssi = to_float(data.get("agrCtlRSSI", ""))
    noise = to_float(data.get("agrCtlNoise", ""))
    tx_rate = to_float(data.get("lastTxRate", ""))
    max_rate = to_float(data.get("maxRate", ""))
    mcs = to_float(data.get("MCS", ""))
    auth = data.get("link auth", "")

    labels = []
    if ssid:
        labels.append(f'ssid="{escape_label_value(ssid)}"')
    if bssid:
        labels.append(f'bssid="{escape_label_value(bssid)}"')
    if channel:
        labels.append(f'channel="{escape_label_value(channel)}"')
    if auth:
        labels.append(f'auth="{escape_label_value(auth)}"')

    label_str = "{" + ",".join(labels) + "}" if labels else ""

    lines = []
    lines.append("# HELP airport_wifi_rssi_dbm Wi-Fi signal strength (dBm)")
    lines.append("# TYPE airport_wifi_rssi_dbm gauge")
    if rssi is not None:
        lines.append(f"airport_wifi_rssi_dbm{label_str} {rssi}")

    lines.append("# HELP airport_wifi_noise_dbm Wi-Fi noise level (dBm)")
    lines.append("# TYPE airport_wifi_noise_dbm gauge")
    if noise is not None:
        lines.append(f"airport_wifi_noise_dbm{label_str} {noise}")

    lines.append("# HELP airport_wifi_snr_db Signal-to-noise ratio (dB)")
    lines.append("# TYPE airport_wifi_snr_db gauge")
    if rssi is not None and noise is not None:
        lines.append(f"airport_wifi_snr_db{label_str} {rssi - noise}")

    lines.append("# HELP airport_wifi_tx_rate_mbps Current TX rate (Mbps)")
    lines.append("# TYPE airport_wifi_tx_rate_mbps gauge")
    if tx_rate is not None:
        lines.append(f"airport_wifi_tx_rate_mbps{label_str} {tx_rate}")

    lines.append("# HELP airport_wifi_max_rate_mbps Max supported rate (Mbps)")
    lines.append("# TYPE airport_wifi_max_rate_mbps gauge")
    if max_rate is not None:
        lines.append(f"airport_wifi_max_rate_mbps{label_str} {max_rate}")

    lines.append("# HELP airport_wifi_mcs Modulation and coding scheme (MCS)")
    lines.append("# TYPE airport_wifi_mcs gauge")
    if mcs is not None:
        lines.append(f"airport_wifi_mcs{label_str} {mcs}")

    # Always emit a timestamp so we can check freshness
    lines.append("# HELP airport_wifi_metrics_timestamp_seconds Export timestamp")
    lines.append("# TYPE airport_wifi_metrics_timestamp_seconds gauge")
    lines.append(f"airport_wifi_metrics_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    # Atomic replace
    import os
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
