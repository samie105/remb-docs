---
title: "Reserved Subdomains"
source: "https://outray.dev/docs/reserved-subdomains"
canonical_url: "https://outray.dev/docs/reserved-subdomains"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:24:32.246Z"
content_hash: "3e297a413180ec22b8fbab4f775d12c1465f55e273638ccf701d379407f624f9"
menu_path: ["Reserved Subdomains"]
section_path: []
nav_prev: {"path": "outray/docs/opening-a-tunnel/index.md", "title": "Opening a Tunnel"}
nav_next: {"path": "outray/docs/password-protection/index.md", "title": "Password Protection"}
---

## Reserved Subdomains

How to use persistent subdomains for your tunnels

By default, OutRay assigns a random subdomain to your tunnel each time you start it. However, for many use cases (like webhooks or OAuth callbacks), you need a consistent URL.

You can request a specific subdomain using the `--subdomain` flag:

```
outray 3000 --subdomain my-app
```

If the subdomain is available, your public URL will be `https://my-app.tunnel.outray.app`.

Subdomains are reserved for your organization. Once you successfully use a subdomain, it is linked to your organization, and no other user can claim it.
