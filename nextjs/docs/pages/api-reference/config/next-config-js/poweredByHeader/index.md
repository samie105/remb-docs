---
title: "poweredByHeader"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:34.449Z"
content_hash: "c898139ea82512b6fd2ba1dde82a2ba78d87ee543e0a1455366fff7255d2c178"
menu_path: ["poweredByHeader"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)poweredByHeader

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
