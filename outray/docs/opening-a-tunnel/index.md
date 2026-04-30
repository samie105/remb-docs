---
title: "Opening a Tunnel"
source: "https://outray.dev/docs/opening-a-tunnel"
canonical_url: "https://outray.dev/docs/opening-a-tunnel"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:24:32.107Z"
content_hash: "a4a1f0902609edc91bde4c439fd40767bd2fa9a7d5b7a0e0f799add94ae50d9b"
menu_path: ["Opening a Tunnel"]
section_path: []
nav_prev: {"path": "outray/docs/authentication/index.md", "title": "Authentication"}
nav_next: {"path": "outray/docs/reserved-subdomains/index.md", "title": "Reserved Subdomains"}
---

## Opening a Tunnel

How to expose your local server to the internet

Once you are authenticated, you can start exposing your local services to the internet.

To expose a local server running on a specific port (e.g., 3000), simply run:

```
outray 3000
```

You will see an output similar to this:

```
Connecting to OutRay...
Linked to your local port 3000
Tunnel ready: https://random-name.tunnel.outray.app
Keep this running to keep your tunnel active.
```

Now, anyone with the public URL can access your local server.

For managing multiple tunnels, you can use a TOML configuration file. Create an `outray/config.toml` file in your project directory:

```
[tunnel.web]
protocol = "http"
local_port = 3000

[tunnel.api]
protocol = "http"
local_port = 8000
```

Then start all tunnels at once:

```
outray start
```

You can validate your config file before starting:

```
outray validate-config
```

See the [CLI Reference](https://outray.dev/docs/reference/cli-reference#configuration-files) for complete configuration options.

OutRay provides a real-time view of requests and responses in your terminal. As requests come in, you will see the method, path, and status code.

To stop the tunnel, simply press `Ctrl+C` in your terminal. This will close the connection and the public URL will no longer be accessible.
