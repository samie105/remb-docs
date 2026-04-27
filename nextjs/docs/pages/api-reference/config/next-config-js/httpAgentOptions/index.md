---
title: "httpAgentOptions"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:15.757Z"
content_hash: "43e7d4dcedfc44215be1b82ba41510e74371c14af64bcbe3950165fcaf0783f4"
menu_path: ["httpAgentOptions"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)httpAgentOptions

# httpAgentOptions

Last updated April 23, 2026

In Node.js versions prior to 18, Next.js automatically polyfills `fetch()` with [undici](/docs/architecture/supported-browsers#polyfills) and enables [HTTP Keep-Alive](https://developer.mozilla.org/docs/Web/HTTP/Headers/Keep-Alive) by default.

To disable HTTP Keep-Alive for all `fetch()` calls on the server-side, open `next.config.js` and add the `httpAgentOptions` config:

next.config.js

```
module.exports = {
  httpAgentOptions: {
    keepAlive: false,
  },
}
```

Was this helpful?
