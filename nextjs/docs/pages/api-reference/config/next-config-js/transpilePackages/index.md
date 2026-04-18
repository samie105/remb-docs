---
title: "transpilePackages"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:21:31.123Z"
content_hash: "ab801542e40d7e27a1609f0c40705cb843646324eac1a482b8b16ce0581c36a6"
menu_path: ["transpilePackages"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/trailingSlash/index.md", "title": "trailingSlash"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/turbopack/index.md", "title": "turbopack"}
---

# transpilePackages

Last updated April 15, 2026

Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`). This replaces the `next-transpile-modules` package.

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  transpilePackages: ['package-name'],
}
 
module.exports = nextConfig
```

## Version History[](#version-history)

Version

Changes

`v13.0.0`

`transpilePackages` added.

Was this helpful?

supported.

Send




