---
title: "https - Node documentation"
source: "https://docs.deno.com/api/node/https/"
canonical_url: "https://docs.deno.com/api/node/https/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:07:51.441Z"
content_hash: "ce3526946e35a189442ae43c979c966b05f9553e999b26e9edc302f3b41ca4af"
menu_path: ["https - Node documentation"]
section_path: []
content_language: "en"
---
### Usage in Deno

```typescript
import * as mod from "node:https";
```

HTTPS is the HTTP protocol over TLS/SSL. In Node.js this is implemented as a separate module.

c

[Agent](.././https/~/Agent "Agent")

An `Agent` object for HTTPS similar to `http.Agent`. See [request](.././https/~/request) for more information.

-   [options](.././https/~/Agent#property_options)

f

[createServer](.././https/~/createServer "createServer")

Or

f

[get](.././https/~/get "get")

Like `http.get()` but for HTTPS.

f

[request](.././https/~/request "request")

Makes a request to a secure web server.

I

[AgentOptions](.././https/~/AgentOptions "AgentOptions")

No documentation available

-   [maxCachedSessions](.././https/~/AgentOptions#property_maxcachedsessions)

c

I

[Server](.././https/~/Server "Server")

No documentation available

-   [addListener](.././https/~/Server#method_addlistener_0)
-   [closeAllConnections](.././https/~/Server#method_closeallconnections_0)
-   [closeIdleConnections](.././https/~/Server#method_closeidleconnections_0)
-   [emit](.././https/~/Server#method_emit_0)
-   [on](.././https/~/Server#method_on_0)
-   [once](.././https/~/Server#method_once_0)
-   [prependListener](.././https/~/Server#method_prependlistener_0)
-   [prependOnceListener](.././https/~/Server#method_prependoncelistener_0)

T

[RequestOptions](.././https/~/RequestOptions "RequestOptions")

No documentation available

T

[ServerOptions](.././https/~/ServerOptions "ServerOptions")

No documentation available

v

[globalAgent](.././https/~/globalAgent "globalAgent")

No documentation available
