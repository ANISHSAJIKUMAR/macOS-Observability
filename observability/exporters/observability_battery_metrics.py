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
    batt = {}
    charge_info = {}
    health_info = {}
    model_info = {}
    charger_info = {}
    if isinstance(data, dict):
        items = data.get("SPPowerDataType", [])
        # Try to find the most detailed battery dict
        for it in items:
            if "sppower_battery_charge_info" in it:
                charge_info = it.get("sppower_battery_charge_info", {})
            if "sppower_battery_health_info" in it:
                health_info = it.get("sppower_battery_health_info", {})
            if "sppower_battery_model_info" in it:
                model_info = it.get("sppower_battery_model_info", {})
            if "sppower_battery_charger_connected" in it or "sppower_battery_is_charging" in it:
                charger_info = it
            if any(k in it for k in ("sppower_battery_health", "sppower_battery_cycle_count", "sppower_battery_charge_percentage")):
                batt = it

    # Flatten useful fields
    if charge_info:
        batt.update(charge_info)
    if health_info:
        batt.update(health_info)
    if model_info:
        batt.update(model_info)
    if charger_info:
        batt.update(charger_info)

    # Power source
    power_line = run(["/usr/bin/pmset", "-g", "batt"])
    source = "Unknown"
    if "AC Power" in power_line:
        source = "AC"
    elif "Battery Power" in power_line:
        source = "Battery"

    percent = (
        batt.get("sppower_battery_charge_percentage")
        or batt.get("sppower_battery_charge_percent")
        or batt.get("sppower_battery_state_of_charge")
    )
    cycle = batt.get("sppower_battery_cycle_count")
    condition = batt.get("sppower_battery_health") or batt.get("sppower_battery_condition") or "Unknown"
    charging = batt.get("sppower_battery_is_charging")
    charger_connected = batt.get("sppower_battery_charger_connected")
    health_max_capacity = batt.get("sppower_battery_health_maximum_capacity")  # e.g. "81%"

    # Prefer parsing percent from pmset output
    if power_line:
        # e.g. " -InternalBattery-0 (id=...) 87%; discharging; ..."
        import re
        m = re.search(r"(\d+)%", power_line)
        if m:
            percent = m.group(1)

    # Normalize numeric values
    def to_float(v):
        try:
            return float(str(v).replace('%',''))
        except Exception:
            return None

    percent_f = to_float(percent)
    cycle_f = to_float(cycle)
    health_max_f = to_float(health_max_capacity)
    if percent_f is None:
        percent_f = 0
    if cycle_f is None:
        cycle_f = 0
    if health_max_f is None:
        health_max_f = 0
    charging_val = 1 if str(charging).lower() in ("yes", "true", "1") else 0
    charger_connected_val = 1 if str(charger_connected).lower() in ("yes", "true", "1") else 0

    lines = []
    lines.append("# HELP battery_charge_percent Battery charge percentage")
    lines.append("# TYPE battery_charge_percent gauge")
    if percent_f is not None:
        lines.append(f"battery_charge_percent {percent_f}")

    lines.append("# HELP battery_cycle_count Battery charge cycles")
    lines.append("# TYPE battery_cycle_count gauge")
    if cycle_f is not None:
        lines.append(f"battery_cycle_count {cycle_f}")

    lines.append("# HELP battery_health_max_capacity_percent Battery maximum capacity health (%)")
    lines.append("# TYPE battery_health_max_capacity_percent gauge")
    lines.append(f"battery_health_max_capacity_percent {health_max_f}")

    lines.append("# HELP battery_charger_connected Charger connected (1=yes, 0=no)")
    lines.append("# TYPE battery_charger_connected gauge")
    lines.append(f"battery_charger_connected {charger_connected_val}")

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
