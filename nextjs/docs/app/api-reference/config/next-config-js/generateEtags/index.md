---
title: "generateEtags"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:34.360Z"
content_hash: "ec3ab52efc2e72a6de16975ca4f0bd9326de1a8809925fff9d661388372ee0c9"
menu_path: ["generateEtags"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/generateBuildId/index.md", "title": "generateBuildId"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/headers/index.md", "title": "headers"}
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

[Previous

generateBuildId

](/docs/app/api-reference/config/next-config-js/generateBuildId)

[Next

headers

](/docs/app/api-reference/config/next-config-js/headers)

Was this helpful?

supported.

Send


