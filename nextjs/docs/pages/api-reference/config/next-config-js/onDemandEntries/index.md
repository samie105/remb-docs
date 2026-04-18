---
title: "onDemandEntries"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:59.463Z"
content_hash: "23f98f2342026cd82472cd49329fe8b3888565457535fefa37f12178ff94f69a"
menu_path: ["onDemandEntries"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/logging/index.md", "title": "logging"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/optimizePackageImports/index.md", "title": "optimizePackageImports"}
---

# onDemandEntries

Last updated April 15, 2026

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

supported.

Send




