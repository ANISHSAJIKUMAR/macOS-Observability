# launchd Jobs (Full Detail)

## LaunchAgents (user)
- `com.local.net_connectivity.plist`
- `com.local.mac_system_info.plist`
- `com.local.launchd_metrics.plist`
- `com.local.grafana_health.plist`
- `com.local.prom_config_checksum.plist`
- `com.local.battery_metrics.plist`

## LaunchDaemon (root)
- `com.local.wdutil_metrics.plist`
- `com.local.cpu_fan_metrics.plist`
- `com.local.smart_metrics.plist`
- `com.local.promtail.plist`
- `com.local.tshark_metrics.plist`

## Example Plist (Line‑by‑Line)
```
<key>Label</key>                 # Unique job name
<string>com.local.net_connectivity</string>

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
launchctl unload ~/Library/LaunchAgents/com.local.net_connectivity.plist
launchctl unload ~/Library/LaunchAgents/com.local.mac_system_info.plist
launchctl unload ~/Library/LaunchAgents/com.local.launchd_metrics.plist
launchctl unload ~/Library/LaunchAgents/com.local.grafana_health.plist
launchctl load ~/Library/LaunchAgents/com.local.net_connectivity.plist
launchctl load ~/Library/LaunchAgents/com.local.mac_system_info.plist
launchctl load ~/Library/LaunchAgents/com.local.launchd_metrics.plist
launchctl load ~/Library/LaunchAgents/com.local.grafana_health.plist
sudo launchctl bootout system /Library/LaunchDaemons/com.local.wdutil_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.local.wdutil_metrics.plist
sudo launchctl bootout system /Library/LaunchDaemons/com.local.cpu_fan_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.local.cpu_fan_metrics.plist
sudo launchctl bootout system /Library/LaunchDaemons/com.local.smart_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.local.smart_metrics.plist
sudo launchctl bootout system /Library/LaunchDaemons/com.local.promtail.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.local.promtail.plist
sudo launchctl bootout system /Library/LaunchDaemons/com.local.tshark_metrics.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.local.tshark_metrics.plist
```
