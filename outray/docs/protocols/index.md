---
title: "TCP & UDP Tunnels"
source: "https://outray.dev/docs/protocols"
canonical_url: "https://outray.dev/docs/protocols"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:27:16.765Z"
content_hash: "0fa177beb1eaae753a7c7e703bff3dc6bd2b95d4c01dabf83cfda87cbc9f9c3f"
menu_path: ["TCP & UDP Tunnels"]
section_path: []
nav_prev: {"path": "outray/docs/express-plugin/index.md", "title": "Express Plugin"}
nav_next: {"path": "outray/docs/cli-reference/index.md", "title": "CLI Reference"}
---

## TCP & UDP Tunnels

Open non-HTTP services over TCP or UDP with the OutRay CLI.

OutRay can tunnel raw TCP and UDP traffic so you can share things like SSH, databases, syslog, or game servers.

```
outray tcp 22 --remote-port 2222
```

**What happens**

-   We try to bind the requested remote port; if it’s taken, you’ll see the assigned port in the output.
-   External TCP clients connect to the assigned port; traffic is piped to your local port.

**Flags that matter**

-   `<port>`: local TCP service to forward to.
-   `--remote-port <port>` (optional): ask for a specific public port in the TCP pool (defaults 20000-30000). If it’s busy, we assign another.

```
outray udp 514 --remote-port 1514
```

**What happens**

-   We try to bind the requested UDP port; if busy, you’ll get the assigned port (UDP pool defaults 30001-40000).
-   External UDP packets to the assigned port are forwarded to your local UDP service; your responses are relayed back.

**Flags that matter**

-   `<port>` (positional): local UDP service to forward to.
-   `--remote-port <port>` (optional): ask for a specific public port in the UDP pool.

-   **Port already in use**: retry without `--remote-port` to let OutRay pick one, or choose another.
-   **No responses (UDP)**: ensure your local service replies; the CLI relays responses automatically once it receives them.
