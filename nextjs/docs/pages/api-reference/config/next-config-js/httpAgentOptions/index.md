---
title: "httpAgentOptions"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:49.067Z"
content_hash: "0cbe4fd35e36b0e5320e38c3c95824491ada7a54b18f64a57c13de03f3368acf"
menu_path: ["httpAgentOptions"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/headers/index.md", "title": "headers"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/images/index.md", "title": "images"}
---

# httpAgentOptions

Last updated April 15, 2026

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

supported.

Send
