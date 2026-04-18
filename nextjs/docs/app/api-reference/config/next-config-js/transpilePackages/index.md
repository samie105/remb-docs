---
title: "transpilePackages"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:47.705Z"
content_hash: "2a1b2989d2b24caebfe4deed5d4efe566449600c6eb610af0ccadcdf56e6afb6"
menu_path: ["transpilePackages"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/trailingSlash/index.md", "title": "trailingSlash"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/turbopack/index.md", "title": "turbopack"}
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

[Previous

trailingSlash

](/docs/app/api-reference/config/next-config-js/trailingSlash)

[Next

turbopack

](/docs/app/api-reference/config/next-config-js/turbopack)

Was this helpful?

supported.

Send




