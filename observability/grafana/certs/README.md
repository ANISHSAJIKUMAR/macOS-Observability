# Grafana TLS Certificates

## Purpose
Local HTTPS certificates for Grafana.

## Files
- `localhost.crt`
- `localhost.key` (generate locally; do not commit)

## Notes
- Self-signed, local only.
- Regenerate the key and certificate locally if you need a fresh TLS pair.
- The private key must stay out of git.
