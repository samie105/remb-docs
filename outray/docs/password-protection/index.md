---
title: "Password Protection"
source: "https://outray.dev/docs/password-protection"
canonical_url: "https://outray.dev/docs/password-protection"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:25:04.721Z"
content_hash: "f0bf1e1aacf05d6fe192825c46a195d5ec299d99b4219539cb77ae7e85d06ca1"
menu_path: ["Password Protection"]
section_path: []
nav_prev: {"path": "outray/docs/reserved-subdomains/index.md", "title": "Reserved Subdomains"}
nav_next: {"path": "outray/docs/custom-domains/index.md", "title": "Custom Domains"}
---

## Password Protection

Restrict access to your tunnels with password authentication

Password protection lets you restrict access to your HTTP tunnels using [Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#basic_authentication_scheme). When enabled, anyone visiting your tunnel URL will be prompted for a password before they can access the underlying service.

Password-protected tunnels are available on **paid plans** (Ray, Beam, and Pulse). [View pricing →](https://outray.dev/pricing)

Use the `--password` flag when starting an HTTP tunnel:

```
outray 3000 --password mysecretpassword
```

Visitors will see a browser-native login prompt. Enter any username (it is ignored) and the password you specified.

You can also set a password in your `outray/config.toml`:

```
[tunnel.web]
protocol = "http"
local_port = 3000
password = "mysecretpassword"
```

Then start all tunnels as usual:

```
outray start
```

1.  When a tunnel is opened with a password, the server stores the password in the tunnel's metadata.
2.  Every incoming HTTP request is checked for a valid `Authorization` header.
3.  If the header is missing or the credentials are wrong, the server responds with **401 Unauthorized** and a `WWW-Authenticate: Basic` header, which triggers the browser's native login dialog.
4.  Once the correct password is supplied, the request is forwarded to your local service as normal.

If you are calling a password-protected tunnel from code (e.g., `curl`, `fetch`, or a webhook provider), include the credentials in the request:

```
curl -u :mysecretpassword https://my-tunnel.tunnel.outray.app/api/health
```

Or with an explicit `Authorization` header:

```
curl -H "Authorization: Basic $(echo -n ':mysecretpassword' | base64)" \
  https://my-tunnel.tunnel.outray.app/api/health
```

The username field is ignored — only the password is checked. You can pass any value (or leave it empty as shown above).

-   **Webhook testing** — prevent unauthorized payloads from reaching your dev server.
-   **Staging previews** — share a tunnel with your team without exposing it publicly.
-   **Client demos** — give a client temporary access without opening the tunnel to the entire internet.
