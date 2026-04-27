---
title: "httpAgentOptions"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:33.414Z"
content_hash: "18451cf5ea855cea03e69a8934f3f16c5b95c84f175974b69a0135ed970d3719"
menu_path: ["httpAgentOptions"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)httpAgentOptions

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
