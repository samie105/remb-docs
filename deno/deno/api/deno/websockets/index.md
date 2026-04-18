---
title: "WebSockets - Deno documentation"
source: "https://docs.deno.com/api/deno/websockets"
canonical_url: "https://docs.deno.com/api/deno/websockets"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:29.971Z"
content_hash: "f5872df1bc4a7b34f742d052fe522c04569fa5a4f003cbf439a416294cbf14e1"
menu_path: ["WebSockets - Deno documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/deno/testing/index.md", "title": "Testing - Deno documentation"}
nav_next: {"path": "deno/deno/api/deno/all_symbols/index.md", "title": "All Symbols - Deno documentation"}
---

### Functions [#](#Functions)

f

[Deno.upgradeWebSocket](./././~/Deno.upgradeWebSocket "Deno.upgradeWebSocket")

Upgrade an incoming HTTP request to a WebSocket.

### Interfaces [#](#Interfaces)

I

[Deno.UpgradeWebSocketOptions](./././~/Deno.UpgradeWebSocketOptions "Deno.UpgradeWebSocketOptions")

Options which can be set when performing a [`Deno.upgradeWebSocket`](./././~/Deno.upgradeWebSocket) upgrade of a `Request`

*   [idleTimeout](./././~/Deno.UpgradeWebSocketOptions#property_idletimeout)
*   [protocol](./././~/Deno.UpgradeWebSocketOptions#property_protocol)

I

[Deno.WebSocketUpgrade](./././~/Deno.WebSocketUpgrade "Deno.WebSocketUpgrade")

The object that is returned from a [`Deno.upgradeWebSocket`](./././~/Deno.upgradeWebSocket) request.

*   [response](./././~/Deno.WebSocketUpgrade#property_response)
*   [socket](./././~/Deno.WebSocketUpgrade#property_socket)

