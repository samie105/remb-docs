---
title: "Custom Domains"
source: "https://outray.dev/docs/custom-domains"
canonical_url: "https://outray.dev/docs/custom-domains"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:25:04.520Z"
content_hash: "45450dbc914a7658d6050523d72b015e99357037755cbdff0f47fd7b2111fb1d"
menu_path: ["Custom Domains"]
section_path: []
nav_prev: {"path": "outray/docs/password-protection/index.md", "title": "Password Protection"}
nav_next: {"path": "outray/docs/teams/index.md", "title": "Teams & Organizations"}
---

## Custom Domains

Use your own domain names for tunnels

OutRay allows you to white-label your tunnels by using your own domain names. Instead of `random-name.tunnel.outray.app`, you can use `api.yourcompany.com`.

1.  **Add Domain**: Go to the **Domains** section in your dashboard and add your domain (e.g., `tunnel.yourcompany.com`).
2.  **DNS Configuration**: Create a CNAME record in your DNS provider pointing to `edge.outray.app`.
3.  **Verification**: OutRay will automatically verify the DNS record and issue an SSL certificate.

Once your domain is verified, you can use it with the `--domain` flag:

```
outray 3000 --domain tunnel.yourcompany.com
```
