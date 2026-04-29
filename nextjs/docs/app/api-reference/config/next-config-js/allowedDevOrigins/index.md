---
title: "allowedDevOrigins"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:05:44.048Z"
content_hash: "0026449986d763e6659700ba5e67fd910a822082356b9067c138892cac80954e"
menu_path: ["allowedDevOrigins"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../adapterPath/index.md", "title": "adapterPath"}
nav_next: {"path": "../appDir/index.md", "title": "appDir"}
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
