import logging
import os


def _parse_env_file(path: str) -> dict:
    data = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"')
                data[k] = v
    except Exception:
        logging.getLogger(__name__).exception("Metric collection failed")
        return data
    return data


def load_env():
    env_path = os.getenv("OBS_ENV_FILE")
    if not env_path:
        env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
    data = _parse_env_file(env_path)

    # First pass: set raw values if not already set
    for k, v in data.items():
        os.environ.setdefault(k, v)

    # Second pass: expand variables like ${OBS_BASE}
    for k, v in data.items():
        expanded = os.path.expandvars(os.environ.get(k, v))
        os.environ[k] = expanded


def get_obs_base() -> str:
    return os.environ.get("OBS_BASE") or os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def get_textfile_dir() -> str:
    return os.environ.get("TEXTFILE_DIR") or os.path.join(get_obs_base(), "node_exporter", "textfile")
