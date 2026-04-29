---
title: "onDemandEntries"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:47.117Z"
content_hash: "7e06fc2cfd6530b515d3d5641c00f604d7f94ab8113a19f7ba92265483fe9832"
menu_path: ["onDemandEntries"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../mdxRs/index.md", "title": "mdxRs"}
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
