# Prometheus Rules

## Purpose
This folder contains **recording rules** to precompute common metrics so dashboards load faster.

## Files
- `recording.yml` — recording rules for CPU, memory, filesystem, and network

## What the Rules Do
- `job:node_cpu_usage_percent:rate5m` → CPU usage %
- `job:node_memory_used_percent` → RAM usage %
- `job:node_filesystem_used_percent` → Disk usage % (all mounts)
- `job:node_network_receive_bps` → RX throughput (bytes/sec)
- `job:node_network_transmit_bps` → TX throughput (bytes/sec)
- `job:net_ping_loss_percent` → ping loss % (recorded)

## Safe Changes
- Add new rules for frequently used queries
- Change `interval` if you want faster/slower updates

## Apply Changes
```bash
brew services restart prometheus
```
