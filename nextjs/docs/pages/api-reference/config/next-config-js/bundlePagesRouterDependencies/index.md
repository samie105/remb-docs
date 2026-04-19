---
title: "bundlePagesRouterDependencies"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:21.676Z"
content_hash: "b1af599123adcca9102a8b5d8fda5e32c8a8eda319a7b5dff4d1e7515c765eb5"
menu_path: ["bundlePagesRouterDependencies"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/basePath/index.md", "title": "basePath"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/compress/index.md", "title": "compress"}
---

# bundlePagesRouterDependencies

Last updated April 15, 2026

Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  bundlePagesRouterDependencies: true,
}
 
module.exports = nextConfig
```

Explicitly opt-out certain packages from being bundled using the [`serverExternalPackages`](/docs/pages/api-reference/config/next-config-js/serverExternalPackages) option.

## Version History[](#version-history)

Version

Changes

`v15.0.0`

Moved from experimental to stable. Renamed from `bundlePagesExternals` to `bundlePagesRouterDependencies`

Was this helpful?

supported.

Send
