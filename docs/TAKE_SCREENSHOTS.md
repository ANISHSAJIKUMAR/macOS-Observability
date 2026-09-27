# Refresh the Grafana screenshots

Start the stack from `observability/` with `./start_all.sh`, then check the
service health with `./status_all.sh`. Open http://localhost:3000 and sign in
with your configured credentials. Use HTTPS instead if TLS is enabled.

## Capture live dashboards

Use a 1600-pixel-wide browser viewport (1100–1500 pixels tall), dark theme, and a recent time range with
real samples. Wait for the panels to finish loading. Grafana kiosk mode
(`&kiosk` in the URL) hides navigation without changing dashboard data.

| Dashboard UID | Repository image |
| --- | --- |
| `overview` | `docs/screenshots/overview.png` |
| `mac-system-all` | `docs/screenshots/mac-system-core-health.png` |
| `prometheus-self` | `docs/screenshots/prometheus-self.png` |
| `exec-summary` | `docs/screenshots/executive-summary.png` |

For example: `http://localhost:3000/d/overview?from=now-15m&to=now&kiosk`.
Capture the browser viewport as PNG. Inspect each image for readable labels,
loaded charts, and accidental personal information. Preserve genuine missing-data
or unavailable-hardware indicators; do not fabricate values for screenshots.

## Publish

The [README](../README.md) uses relative links to the tracked PNG files. Commit
both the README and images together; local absolute paths and localhost image
URLs cannot render on GitHub. Match filename spelling and case exactly.

After pushing, open the GitHub README and each image to verify rendering.
