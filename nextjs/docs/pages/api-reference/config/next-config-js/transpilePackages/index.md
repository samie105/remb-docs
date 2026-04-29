---
title: "transpilePackages"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:55.436Z"
content_hash: "1aaa785c95644676fad5f25d2b242a3e5e15061f8ee9120351fffbe876509e00"
menu_path: ["transpilePackages"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/trailingSlash/index.md", "title": "trailingSlash"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/turbopack/index.md", "title": "turbopack"}
---

# transpilePackages

Last updated April 23, 2026

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

| Version | Changes |
| --- | --- |
| `v13.0.0` | `transpilePackages` added. |

Was this helpful?
