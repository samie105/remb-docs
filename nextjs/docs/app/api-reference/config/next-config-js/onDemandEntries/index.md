---
title: "onDemandEntries"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:59.064Z"
content_hash: "e99dc374967d592b0cf375469a0ddc867e6a3afdda33a747018d0136f325f5cf"
menu_path: ["onDemandEntries"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/mdxRs/index.md", "title": "mdxRs"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/optimizePackageImports/index.md", "title": "optimizePackageImports"}
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

[Previous

mdxRs

](/docs/app/api-reference/config/next-config-js/mdxRs)

[Next

optimizePackageImports

](/docs/app/api-reference/config/next-config-js/optimizePackageImports)

Was this helpful?

supported.

Send
