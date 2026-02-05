#!/usr/bin/env python3
import json
import subprocess
import time
import os

OUTFILE = "/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/textfile/battery.prom"


def run_json(cmd):
    try:
        out = subprocess.check_output(cmd, text=True)
        return json.loads(out)
    except Exception:
        return {}


def run(cmd):
    try:
        return subprocess.check_output(cmd, text=True).strip()
    except Exception:
        return ""


def main():
    data = run_json(["/usr/sbin/system_profiler", "SPPowerDataType", "-json"])
    batt = None
    if isinstance(data, dict):
        items = data.get("SPPowerDataType", [])
        for it in items:
            if "sppower_battery_installed" in it or "sppower_battery_health" in it:
                batt = it
                break
    if batt is None:
        batt = {}

    # Power source
    power_line = run(["/usr/bin/pmset", "-g", "batt"])
    source = "Unknown"
    if "AC Power" in power_line:
        source = "AC"
    elif "Battery Power" in power_line:
        source = "Battery"

    percent = batt.get("sppower_battery_charge_percentage") or batt.get("sppower_battery_charge_percent")
    cycle = batt.get("sppower_battery_cycle_count")
    condition = batt.get("sppower_battery_health") or batt.get("sppower_battery_condition") or "Unknown"
    charging = batt.get("sppower_battery_is_charging")

    # Normalize numeric values
    def to_float(v):
        try:
            return float(str(v).replace('%',''))
        except Exception:
            return None

    percent_f = to_float(percent)
    cycle_f = to_float(cycle)
    charging_val = 1 if str(charging).lower() in ("yes", "true", "1") else 0

    lines = []
    lines.append("# HELP battery_charge_percent Battery charge percentage")
    lines.append("# TYPE battery_charge_percent gauge")
    if percent_f is not None:
        lines.append(f"battery_charge_percent {percent_f}")

    lines.append("# HELP battery_cycle_count Battery charge cycles")
    lines.append("# TYPE battery_cycle_count gauge")
    if cycle_f is not None:
        lines.append(f"battery_cycle_count {cycle_f}")

    lines.append("# HELP battery_is_charging Battery charging state (1=charging, 0=not)")
    lines.append("# TYPE battery_is_charging gauge")
    lines.append(f"battery_is_charging {charging_val}")

    # Condition label metric
    cond = str(condition).strip() or "Unknown"
    cond = cond.replace('"','').replace("\\","/")
    lines.append("# HELP battery_condition Battery health condition (label)")
    lines.append("# TYPE battery_condition gauge")
    lines.append(f'battery_condition{{state="{cond}"}} 1')

    # Power source label metric
    lines.append("# HELP battery_power_source Power source (label)")
    lines.append("# TYPE battery_power_source gauge")
    lines.append(f'battery_power_source{{source="{source}"}} 1')

    lines.append("# HELP battery_metrics_timestamp_seconds Export timestamp")
    lines.append("# TYPE battery_metrics_timestamp_seconds gauge")
    lines.append(f"battery_metrics_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
