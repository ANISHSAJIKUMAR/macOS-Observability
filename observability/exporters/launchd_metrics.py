#!/usr/bin/env python3
import subprocess
import time
import os

OUTFILE = "/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/textfile/launchd.prom"


def run(cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        return ""
    return p.stdout


def main():
    out = run(["/bin/launchctl", "list"])
    lines = out.splitlines()
    # Expected columns: PID	Status	Label
    # Skip header if present
    jobs = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("PID"):
            continue
        parts = line.split(None, 2)
        if len(parts) < 3:
            continue
        pid_str, status_str, label = parts
        try:
            pid = int(pid_str) if pid_str != "-" else 0
        except Exception:
            pid = 0
        try:
            status = int(status_str)
        except Exception:
            status = 0
        jobs.append((label, pid, status))

    def esc(v: str) -> str:
        return v.replace("\\", r"\\").replace("\n", r"\\n").replace('"', r'\\"')

    out_lines = []
    out_lines.append("# HELP launchd_job_running Launchd job running (1) or not (0)")
    out_lines.append("# TYPE launchd_job_running gauge")
    out_lines.append("# HELP launchd_job_pid Launchd job PID (0 if not running)")
    out_lines.append("# TYPE launchd_job_pid gauge")
    out_lines.append("# HELP launchd_job_status Launchd job last exit status")
    out_lines.append("# TYPE launchd_job_status gauge")

    for label, pid, status in jobs:
        l = esc(label)
        out_lines.append(f'launchd_job_running{{label="{l}"}} {1 if pid > 0 else 0}')
        out_lines.append(f'launchd_job_pid{{label="{l}"}} {pid}')
        out_lines.append(f'launchd_job_status{{label="{l}"}} {status}')

    out_lines.append("# HELP launchd_jobs_total Total launchd jobs")
    out_lines.append("# TYPE launchd_jobs_total gauge")
    out_lines.append(f"launchd_jobs_total {len(jobs)}")

    out_lines.append("# HELP launchd_metrics_timestamp_seconds Export timestamp")
    out_lines.append("# TYPE launchd_metrics_timestamp_seconds gauge")
    out_lines.append(f"launchd_metrics_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
