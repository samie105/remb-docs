---
title: "https - Node documentation"
source: "https://docs.deno.com/api/node/https/"
canonical_url: "https://docs.deno.com/api/node/https/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:54.889Z"
content_hash: "968ee27491da63cfc9656d736af16f2ed6cded2d41c464dc25bf85ec318754b3"
menu_path: ["https - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/http/index.md", "title": "http - Node documentation"}
nav_next: {"path": "deno/deno/api/node/http2/index.md", "title": "http2 - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:https";
```

HTTPS is the HTTP protocol over TLS/SSL. In Node.js this is implemented as a separate module.

### Classes [#](#Classes)

c

[Agent](.././https/~/Agent "Agent")

An `Agent` object for HTTPS similar to `http.Agent`. See [request](.././https/~/request) for more information.

*   [options](.././https/~/Agent#property_options)

### Functions [#](#Functions)

f

[createServer](.././https/~/createServer "createServer")

Or

f

[get](.././https/~/get "get")

Like `http.get()` but for HTTPS.

f

[request](.././https/~/request "request")

Makes a request to a secure web server.

### Interfaces [#](#Interfaces)

I

[AgentOptions](.././https/~/AgentOptions "AgentOptions")

No documentation available

*   [maxCachedSessions](.././https/~/AgentOptions#property_maxcachedsessions)

c

I

[Server](.././https/~/Server "Server")

No documentation available

*   [addListener](.././https/~/Server#method_addlistener_0)
*   [closeAllConnections](.././https/~/Server#method_closeallconnections_0)
*   [closeIdleConnections](.././https/~/Server#method_closeidleconnections_0)
*   [emit](.././https/~/Server#method_emit_0)
*   [on](.././https/~/Server#method_on_0)
*   [once](.././https/~/Server#method_once_0)
*   [prependListener](.././https/~/Server#method_prependlistener_0)
*   [prependOnceListener](.././https/~/Server#method_prependoncelistener_0)

### Type Aliases [#](<#Type Aliases>)

T

[RequestOptions](.././https/~/RequestOptions "RequestOptions")

No documentation available

T

[ServerOptions](.././https/~/ServerOptions "ServerOptions")

No documentation available

### Variables [#](#Variables)

v

[globalAgent](.././https/~/globalAgent "globalAgent")

No documentation available

