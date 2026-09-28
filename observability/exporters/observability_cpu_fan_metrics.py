#!/usr/bin/env python3
import logging
import os
import plistlib
import subprocess
import time

from observability_env import get_textfile_dir, load_env

load_env()

OUTFILE = os.path.join(get_textfile_dir(), "cpu_fan.prom")


def run_powermetrics_plist():
    try:
        p = subprocess.run(
            ["/usr/bin/powermetrics", "-n", "1", "--show-all", "-f", "plist"],
            capture_output=True,
            check=False,
        )
        return p.stdout or b""
    except Exception:
        logging.getLogger(__name__).exception("Metric collection failed")
        return b""


def main():
    raw = run_powermetrics_plist()
    data = {}
    if raw:
        try:
            data = plistlib.loads(raw)
        except Exception:
            logging.getLogger(__name__).exception("Metric collection failed")
            data = {}

    lines = []
    has_powermetrics = 1 if data else 0

    lines.append("# HELP powermetrics_available powermetrics plist available (1=yes, 0=no)")
    lines.append("# TYPE powermetrics_available gauge")
    lines.append(f"powermetrics_available {has_powermetrics}")
    cpu_temp = None
    fan_rpm = None

    # Thermal pressure (Nominal, Moderate, Heavy, Critical)
    thermal = data.get("thermal_pressure") if data else None
    if not thermal:
        # Foundation exposes thermal pressure without root-only powermetrics.
        try:
            result = subprocess.run(
                ["/usr/bin/osascript", "-l", "JavaScript", "-e",
                 'ObjC.import("Foundation"); $.NSProcessInfo.processInfo.thermalState'],
                capture_output=True, text=True, timeout=10, check=True,
            )
            thermal = {0: "Nominal", 1: "Moderate", 2: "Heavy", 3: "Critical"}.get(
                int(result.stdout.strip())
            )
        except (OSError, ValueError, subprocess.SubprocessError):
            thermal = None
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

    lines.append("# HELP cpu_temperature_c CPU temperature in Celsius (if available)")
    lines.append("# TYPE cpu_temperature_c gauge")
    if cpu_temp is not None:
        lines.append(f"cpu_temperature_c {cpu_temp}")

    lines.append("# HELP cpu_temperature_available CPU temperature metric availability (1=yes, 0=no)")
    lines.append("# TYPE cpu_temperature_available gauge")
    lines.append(f"cpu_temperature_available {1 if cpu_temp is not None else 0}")

    lines.append("# HELP fan_speed_rpm Fan speed in RPM (if available)")
    lines.append("# TYPE fan_speed_rpm gauge")
    if fan_rpm is not None:
        lines.append(f"fan_speed_rpm {fan_rpm}")

    lines.append("# HELP fan_speed_available Fan speed metric availability (1=yes, 0=no)")
    lines.append("# TYPE fan_speed_available gauge")
    lines.append(f"fan_speed_available {1 if fan_rpm is not None else 0}")

    lines.append("# HELP cpu_fan_metrics_timestamp_seconds Export timestamp")
    lines.append("# TYPE cpu_fan_metrics_timestamp_seconds gauge")
    lines.append(f"cpu_fan_metrics_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
