---
title: "poweredByHeader"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:56.395Z"
content_hash: "29dffdf2a7dcda8b8f3dacd79b5f92235a5fd589be711af09b57dd2242067fc0"
menu_path: ["poweredByHeader"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../pageExtensions/index.md", "title": "pageExtensions"}
nav_next: {"path": "../productionBrowserSourceMaps/index.md", "title": "productionBrowserSourceMaps"}
---

# poweredByHeader

Last updated April 23, 2026

By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:

next.config.js

```
module.exports = {
  poweredByHeader: false,
}
```

Was this helpful?
