# launchd Jobs (Full Detail)

## LaunchAgents (user)
- `observability.net_connectivity.plist`
- `observability.mac_system_info.plist`
- `observability.launchd_metrics.plist`
- `observability.grafana_health.plist`
- `observability.prom_config_checksum.plist`
- `observability.battery_metrics.plist`

## LaunchDaemon (root)
- `observability.wdutil_metrics.plist`
- `observability.cpu_fan_metrics.plist`
- `observability.smart_metrics.plist`
- `observability.promtail.plist`
- `observability.tshark_metrics.plist`

## Example Plist (Line‑by‑Line)
```
<key>Label</key>                 # Unique job name
<string>observability.net_connectivity</string>

<key>ProgramArguments</key>      # Executable path and args
<array>
  <string>.../exporters/net_connectivity_metrics.py</string>
</array>

<key>StartInterval</key>         # How often to run (seconds)
<integer>30</integer>

<key>RunAtLoad</key>             # Run immediately on load
<true/>

<key>StandardOutPath</key>       # stdout log file
<string>/tmp/net_connectivity.out</string>

<key>StandardErrorPath</key>     # stderr log file
<string>/tmp/net_connectivity.err</string>
```

## Safe Changes
- Adjust `StartInterval`
- Update exporter path in `ProgramArguments`

## Apply Changes
```bash
launchctl unload ~/Library/LaunchAgents/observability.net_connectivity.plist
launchctl unload ~/Library/LaunchAgents/observability.mac_system_info.plist
launchctl unload ~/Library/LaunchAgents/observability.launchd_metrics.plist
launchctl unload ~/Library/LaunchAgents/observability.grafana_health.plist
launchctl load ~/Library/LaunchAgents/observability.net_connectivity.plist
launchctl load ~/Library/LaunchAgents/observability.mac_system_info.plist
launchctl load ~/Library/LaunchAgents/observability.launchd_metrics.plist
launchctl load ~/Library/LaunchAgents/observability.grafana_health.plist
sudo launchctl bootout system /Library/LaunchDaemons/observability.wdutil_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.wdutil_metrics.plist
sudo launchctl bootout system /Library/LaunchDaemons/observability.cpu_fan_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.cpu_fan_metrics.plist
sudo launchctl bootout system /Library/LaunchDaemons/observability.smart_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.smart_metrics.plist
sudo launchctl bootout system /Library/LaunchDaemons/observability.promtail.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.promtail.plist
sudo launchctl bootout system /Library/LaunchDaemons/observability.tshark_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/observability.tshark_metrics.plist
```
