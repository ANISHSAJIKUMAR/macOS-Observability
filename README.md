# Anish DevOps Lab (Root)

[![CI](https://github.com/ANISHSAJIKUMAR/anish-devops-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/ANISHSAJIKUMAR/anish-devops-lab/actions/workflows/ci.yml)
[![Last Release](https://img.shields.io/github/v/release/ANISHSAJIKUMAR/anish-devops-lab)](https://github.com/ANISHSAJIKUMAR/anish-devops-lab/releases)
[![License: Proprietary](https://img.shields.io/badge/license-proprietary-red)](https://github.com/ANISHSAJIKUMAR/anish-devops-lab)

**Owner:** Anish Kumar (change `OWNER_NAME` in `observability/.env`)

This repository hosts my personal DevOps workspace. The active project is **Observability** for **macOS (Mac)**.

## Go To Project
- Main project folder: `/Users/anishskumar/Anish-DevOps-Lab/observability` (macOS only)
- Full setup guide: `/Users/anishskumar/Anish-DevOps-Lab/observability/README.md`

## Common Commands
Run from the root or any folder:
```bash
./observability/start_all.sh
./observability/stop_all.sh
./observability/status_all.sh
```

## Notes
- Root folder is kept minimal on purpose.
- All project scripts, configs, dashboards, and outputs live under `observability/`.
- This setup is built and tested for macOS. Linux/Windows require different service managers and paths.


## CI/CD (GitHub Actions)
- Validates YAML/JSON, shell scripts, exporters, and Prometheus config.
- Workflow: `.github/workflows/ci.yml`
