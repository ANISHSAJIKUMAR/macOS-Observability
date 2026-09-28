#!/usr/bin/env python3
import hashlib
import os
import time

from observability_env import get_obs_base, get_textfile_dir, load_env

load_env()

OUTFILE = os.path.join(get_textfile_dir(), "prom_config_checksum.prom")
FILES = [os.path.join(get_obs_base(), "prometheus", name) for name in
         ("prometheus.yml", "prometheus.args", "rules/recording.yml")]



def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    lines = []
    lines.append("# HELP prom_config_checksum Prometheus config file checksum")
    lines.append("# TYPE prom_config_checksum gauge")

    for path in FILES:
        if not os.path.exists(path):
            continue
        checksum = sha256(path)
        label_path = path.replace("\\", "\\\\")
        lines.append(f'prom_config_checksum{{file="{label_path}",sha256="{checksum}"}} 1')

    lines.append("# HELP prom_config_checksum_timestamp_seconds Export timestamp")
    lines.append("# TYPE prom_config_checksum_timestamp_seconds gauge")
    lines.append(f"prom_config_checksum_timestamp_seconds {time.time()}")

    tmp = OUTFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, OUTFILE)


if __name__ == "__main__":
    main()
