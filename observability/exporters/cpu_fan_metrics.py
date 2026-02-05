#!/usr/bin/env python3
import subprocess
import time
import os
import plistlib

OUTFILE = "/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/textfile/cpu_fan.prom"


def run_powermetrics_plist():
    try:
        out = subprocess.check_output(["/usr/bin/powermetrics", "-n", "1", "--show-all", "-f", "plist"], stderr=subprocess.STDOUT)
        return out
    except Exception:
        return b""


def main():
    raw = run_powermetrics_plist()
    if not raw:
        return

    try:
        data = plistlib.loads(raw)
    except Exception:
        return

    lines = []

    # Thermal pressure (Nominal, Moderate, Heavy, Critical)
    thermal = data.get("thermal_pressure")
    if thermal:
        state = str(thermal)
        mapping = {"Nominal": 0, "Moderate": 1, "Heavy": 2, "Critical": 3}
        level = mapping.get(state, -1)
        lines.append("# HELP cpu_thermal_pressure_level Thermal pressure level (0=Nominal,1=Moderate,2=Heavy,3=Critical)")
        lines.append("# TYPE cpu_thermal_pressure_level gauge")
        if level >= 0:
            lines.append(f"cpu_thermal_pressure_level {level}")

        lines.append("# HELP cpu_thermal_pressure_state Thermal pressure state label")
        lines.append("# TYPE cpu_thermal_pressure_state gauge")
        lines.append(f'cpu_thermal_pressure_state{{state="{state}"}} 1')

    lines.append("# HELP cpu_fan_metrics_timestamp_seconds Export timestamp")
    lines.append("# TYPE cpu_fan_metrics_timestamp_seconds gauge")
    lines.append(f"cpu_fan_metrics_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
