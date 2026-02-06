# Grafana Dashboard Schema

This is a **minimal JSON schema** used by CI to validate that dashboard JSON files
are well-formed and contain the most important structural keys.

Why minimal?
- Grafana dashboard JSON varies by version and plugin.
- A permissive schema avoids false failures while still catching broken JSON.

CI uses this file via `ajv-cli`:
```
observability/grafana/schema/dashboard.schema.json
```
