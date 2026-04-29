---
title: "generateEtags"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:26.581Z"
content_hash: "738447fd73678ba33e383c6f3a57e23dcda4c6956b76432261cd5cb2453bd967"
menu_path: ["generateEtags"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/generateBuildId/index.md", "title": "generateBuildId"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/headers/index.md", "title": "headers"}
---

# generateEtags

Last updated April 23, 2026

Next.js will generate [etags](https://en.wikipedia.org/wiki/HTTP_ETag) for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.

Open `next.config.js` and disable the `generateEtags` option:

next.config.js

```
module.exports = {
  generateEtags: false,
}
```

Was this helpful?
