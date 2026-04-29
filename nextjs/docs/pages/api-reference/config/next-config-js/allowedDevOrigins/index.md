---
title: "allowedDevOrigins"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:19:41.460Z"
content_hash: "7e9bf64cb6d8dcdde433146a3da8082d339b56a47b90025783e3e35ce901856a"
menu_path: ["allowedDevOrigins"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../adapterPath/index.md", "title": "adapterPath"}
nav_next: {"path": "../assetPrefix/index.md", "title": "assetPrefix"}
---

# allowedDevOrigins

Last updated April 23, 2026

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
