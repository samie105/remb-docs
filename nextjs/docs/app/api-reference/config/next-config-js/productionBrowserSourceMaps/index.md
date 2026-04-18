---
title: "productionBrowserSourceMaps"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:09.884Z"
content_hash: "768f6bad8ec8601fa6f2631ae33b622e0def386a31536ec0f00d44a30ee4cdb7"
menu_path: ["productionBrowserSourceMaps"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/poweredByHeader/index.md", "title": "poweredByHeader"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize/index.md", "title": "proxyClientMaxBodySize"}
---

# productionBrowserSourceMaps

Last updated April 15, 2026

Source Maps are enabled by default during development. During production builds, they are disabled to prevent you leaking your source on the client, unless you specifically opt-in with the configuration flag.

Next.js provides a configuration flag you can use to enable browser source map generation during the production build:

next.config.js

```
module.exports = {
  productionBrowserSourceMaps: true,
}
```

When the `productionBrowserSourceMaps` option is enabled, the source maps will be output in the same directory as the JavaScript files. Next.js will automatically serve these files when requested.

*   Adding source maps can increase `next build` time
*   Increases memory usage during `next build`

[Previous

poweredByHeader

](/docs/app/api-reference/config/next-config-js/poweredByHeader)

[Next

proxyClientMaxBodySize

](/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize)

Was this helpful?

supported.

Send


