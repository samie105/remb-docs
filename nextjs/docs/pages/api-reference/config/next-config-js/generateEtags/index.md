---
title: "generateEtags"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:44.330Z"
content_hash: "4f81a928408900fbcfd9850cb0a9f3818bb80db9de89cdb5fdb02ec9c277f367"
menu_path: ["generateEtags"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/generateBuildId/index.md", "title": "generateBuildId"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/headers/index.md", "title": "headers"}
---

# generateEtags

Last updated April 15, 2026

Next.js will generate [etags](https://en.wikipedia.org/wiki/HTTP_ETag) for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.

Open `next.config.js` and disable the `generateEtags` option:

next.config.js

```
module.exports = {
  generateEtags: false,
}
```

Was this helpful?

supported.

Send




