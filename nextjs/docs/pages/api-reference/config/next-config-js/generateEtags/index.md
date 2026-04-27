---
title: "generateEtags"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:11.163Z"
content_hash: "c479f3a9f780adb8f7a7816ade15f4f0a4fdb7820bad0fc0cf04adfded8c9873"
menu_path: ["generateEtags"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)generateEtags

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
