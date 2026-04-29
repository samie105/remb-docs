---
title: "bundlePagesRouterDependencies"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:19:47.873Z"
content_hash: "ec728391d9b2b7a923873fae80428148584c139654ad6518de758e620f96963e"
menu_path: ["bundlePagesRouterDependencies"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/basePath/index.md", "title": "basePath"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/compress/index.md", "title": "compress"}
---

# bundlePagesRouterDependencies

Last updated April 23, 2026

Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  bundlePagesRouterDependencies: true,
}
 
module.exports = nextConfig
```

Explicitly opt-out certain packages from being bundled using the [`serverExternalPackages`](../serverExternalPackages/index.md) option.

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | Moved from experimental to stable. Renamed from `bundlePagesExternals` to `bundlePagesRouterDependencies` |

Was this helpful?
