---
title: "onDemandEntries"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:24.390Z"
content_hash: "a5e10cfde39f155cee59b3205b9efac187df96b5ff2489775ccc55c539982810"
menu_path: ["onDemandEntries"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../logging/index.md", "title": "logging"}
nav_next: {"path": "../optimizePackageImports/index.md", "title": "optimizePackageImports"}
---

# onDemandEntries

Last updated April 23, 2026

Next.js exposes some options that give you some control over how the server will dispose or keep in memory built pages in development.

To change the defaults, open `next.config.js` and add the `onDemandEntries` config:

next.config.js

```
module.exports = {
  onDemandEntries: {
    // period (in ms) where the server will keep pages in the buffer
    maxInactiveAge: 25 * 1000,
    // number of pages that should be kept simultaneously without being disposed
    pagesBufferLength: 2,
  },
}
```

Was this helpful?
