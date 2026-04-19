---
title: "productionBrowserSourceMaps"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:21:11.188Z"
content_hash: "6294a825dee57442d9188a31e30341df21cf460b7b96c74f3288c66d01dbd6c2"
menu_path: ["productionBrowserSourceMaps"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/poweredByHeader/index.md", "title": "poweredByHeader"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize/index.md", "title": "experimental.proxyClientMaxBodySize"}
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

Was this helpful?

supported.

Send
