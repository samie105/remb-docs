---
title: "allowedDevOrigins"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:15.234Z"
content_hash: "ec1a140361c4d534fb7794be6fc50876fa577c1b72f2bd5fb0f6b582b735a270"
menu_path: ["allowedDevOrigins"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/adapterPath/index.md", "title": "adapterPath"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/assetPrefix/index.md", "title": "assetPrefix"}
---

# allowedDevOrigins

Last updated April 15, 2026

Next.js blocks cross-origin requests to dev-only assets and endpoints during development by default to prevent unauthorized access.

To configure a Next.js application to allow requests from origins other than the hostname the server was initialized with (`localhost` by default), use the `allowedDevOrigins` config option.

`allowedDevOrigins` lets you set additional origins that can request the dev server in development mode. For example, to use `local-origin.dev` instead of only `localhost`, open `next.config.js` and add the `allowedDevOrigins` config:

next.config.js

```
module.exports = {
  allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
}
```

Was this helpful?

supported.

Send
