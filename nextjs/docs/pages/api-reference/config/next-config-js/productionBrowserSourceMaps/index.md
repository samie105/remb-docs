---
title: "productionBrowserSourceMaps"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:34.880Z"
content_hash: "6fb8b61857e4ce473c43c670a388c82b44fabff57290fad6f791b9ced8f424bf"
menu_path: ["productionBrowserSourceMaps"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../poweredByHeader/index.md", "title": "poweredByHeader"}
nav_next: {"path": "../proxyClientMaxBodySize/index.md", "title": "experimental.proxyClientMaxBodySize"}
---

# productionBrowserSourceMaps

Last updated April 23, 2026

Source Maps are enabled by default during development. During production builds, they are disabled to prevent you leaking your source on the client, unless you specifically opt-in with the configuration flag.

Next.js provides a configuration flag you can use to enable browser source map generation during the production build:

next.config.js

```
module.exports = {
  productionBrowserSourceMaps: true,
}
```

When the `productionBrowserSourceMaps` option is enabled, the source maps will be output in the same directory as the JavaScript files. Next.js will automatically serve these files when requested.

-   Adding source maps can increase `next build` time
-   Increases memory usage during `next build`

Was this helpful?
