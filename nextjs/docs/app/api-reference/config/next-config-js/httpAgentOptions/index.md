---
title: "httpAgentOptions"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:42.927Z"
content_hash: "68aa3fdc4630900847005d7f0993682ed9de0a883b6652c64d9a2be889cacc61"
menu_path: ["httpAgentOptions"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/htmlLimitedBots/index.md", "title": "htmlLimitedBots"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/images/index.md", "title": "images"}
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

[Previous

htmlLimitedBots

](/docs/app/api-reference/config/next-config-js/htmlLimitedBots)

[Next

images

](/docs/app/api-reference/config/next-config-js/images)

Was this helpful?

supported.

Send


