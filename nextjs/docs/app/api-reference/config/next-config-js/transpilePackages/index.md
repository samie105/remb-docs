---
title: "transpilePackages"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:34.594Z"
content_hash: "3e35eec4f5cefd9d552265b0e701c930749de2a6316282ced34d0f4667ee19a3"
menu_path: ["transpilePackages"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../trailingSlash/index.md", "title": "trailingSlash"}
nav_next: {"path": "../turbopack/index.md", "title": "turbopack"}
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
