# VMware Fusion Monitoring

## Purpose
Provides host-side monitoring for VMware Fusion VMs on this Mac.

## What It Collects
- VM running state
- CPU usage per VM (vmware-vmx process)
- Memory RSS per VM
- Configured vCPU and memory from .vmx
- VMDK size (capacity usage)
- Snapshot count
- Guest Tools detection (via guest IP)

## Exporter
- Script: `/Users/anishskumar/Anish-DevOps-Lab/observability/exporters/observability_vmware_fusion_metrics.py`
- Output: `/Users/anishskumar/Anish-DevOps-Lab/observability/node_exporter/textfile/vmware_fusion.prom`

## LaunchAgent
- `/Users/anishskumar/Library/LaunchAgents/observability.vmware_fusion_metrics.plist`

## Dashboard
- `VMware Fusion: VM Health`
- URL: `https://localhost:3000/d/vmware-fusion/vmware-fusion3a-vm-health`

## Notes
- Guest OS metrics are not collected by default.
  To collect guest metrics, install an agent inside the VM (node_exporter, telegraf, or OpenTelemetry).
- If VMDK size shows 0, the disk path is not discoverable from the .vmx file.
