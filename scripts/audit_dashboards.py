#!/usr/bin/env python3
"""Audit live Grafana queries through its datasource proxy; never print log contents."""
import base64
import concurrent.futures
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter

BASE = os.environ.get("GRAFANA_URL", "http://localhost:3000").rstrip("/")
AUTH = base64.b64encode((os.environ.get("GRAFANA_USER", "admin") + ":" + os.environ["GRAFANA_PASSWORD"]).encode()).decode()


def get(path):
    request = urllib.request.Request(BASE + path, headers={"Authorization": "Basic " + AUTH})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"HTTP {error.code}: {error.read().decode()[:300]}") from error


def panels(items):
    for panel in items:
        yield panel
        yield from panels(panel.get("panels", []))


def main():
    sources = get("/api/datasources")
    by_name = {s["name"]: s for s in sources}
    by_uid = {s["uid"]: s for s in sources}
    default = next(s for s in sources if s.get("isDefault"))
    jobs = []
    errors = []
    for item in get("/api/search?type=dash-db"):
        dashboard = get("/api/dashboards/uid/" + item["uid"])["dashboard"]
        variables = {v["name"]: v.get("allValue") or v.get("current", {}).get("value", "") for v in dashboard.get("templating", {}).get("list", [])}
        variables.update({"__rate_interval": "1m", "__interval": "1m", "__range": "1h"})
        ids = [p.get("id") for p in panels(dashboard["panels"])]
        if len(ids) != len(set(ids)) or None in ids:
            errors.append(item["uid"] + ": missing or duplicate panel IDs")
        for panel in panels(dashboard["panels"]):
            for target in panel.get("targets", []):
                if not target.get("expr") or target.get("hide"):
                    continue
                ds = target.get("datasource") or panel.get("datasource")
                source = by_uid.get(ds.get("uid")) if isinstance(ds, dict) else by_name.get(ds, default)
                if source is None:
                    errors.append(item["uid"] + ": missing datasource " + str(ds))
                    continue
                expr = target["expr"]
                for key, value in sorted(variables.items(), key=lambda pair: -len(pair[0])):
                    expr = expr.replace("${" + key + "}", str(value)).replace("$" + key, str(value))
                jobs.append((item["uid"], panel["title"], source, expr))

    def check(job):
        uid, title, source, expr = job
        prefix = "/api/datasources/proxy/uid/" + source["uid"]
        params = {"query": expr}
        if source["type"] == "loki":
            endpoint = "/loki/api/v1/query_range"
            params.update(start=str(int((time.time() - 3600) * 1e9)), end=str(int(time.time() * 1e9)), limit="1", step="60")
        else:
            endpoint = "/api/v1/query"
        result = {"dashboard": uid, "panel": title, "expr": expr}
        try:
            data = get(prefix + endpoint + "?" + urllib.parse.urlencode(params))
            if data.get("status") != "success":
                raise RuntimeError(str(data))
            rows = data.get("data", {}).get("result", [])
            result.update(status="ok" if rows else "unavailable", series=len(rows))
        except Exception as error:
            result.update(status="error", error=str(error))
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, jobs))
    report = {"checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "counts": dict(Counter(r["status"] for r in results)), "structural_errors": errors, "results": results}
    print(json.dumps(report, indent=2))
    return int(bool(errors) or any(r["status"] == "error" for r in results))


if __name__ == "__main__":
    raise SystemExit(main())
