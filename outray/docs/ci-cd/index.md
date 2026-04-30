---
title: "CI/CD Integration"
source: "https://outray.dev/docs/ci-cd"
canonical_url: "https://outray.dev/docs/ci-cd"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:25:37.156Z"
content_hash: "24701b0134434bc1c435553caad2b2c4d74f752ec5a52afd5200463521d4f49f"
menu_path: ["CI/CD Integration"]
section_path: []
nav_prev: {"path": "outray/docs/teams/index.md", "title": "Teams & Organizations"}
nav_next: {"path": "outray/docs/observability/index.md", "title": "Observability"}
---

## CI/CD Integration

Automate tunnels in your CI/CD pipelines

OutRay is perfect for preview environments in CI/CD pipelines. By using API keys, you can automate tunnel creation without interactive login.

1.  **Generate API Key**: Go to your organization settings in the dashboard and generate a new API Key.
2.  **Store Secret**: Store the API key as a secret in your CI provider (e.g., `OUTRAY_API_KEY`).

Use the `--key` flag to authenticate the tunnel:

```
outray 3000 --key $OUTRAY_API_KEY
```

Here is a simple example of how to use OutRay in a GitHub Action:

```
steps:
  - name: Start Tunnel
    run: |
      npm install -g outray
      outray 3000 --key ${{ secrets.OUTRAY_API_KEY }} &
```
