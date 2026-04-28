---
title: "typedRoutes"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:44.734Z"
content_hash: "823e2b4af552a369335987b364b1404ef231319faa4eb4fb6ed22dcc3009fb60"
menu_path: ["typedRoutes"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/turbopackIgnoreIssue/index.md", "title": "turbopack.ignoreIssue"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/typescript/index.md", "title": "typescript"}
---

# typedRoutes

Last updated April 23, 2026

> **Note**: This option has been marked as stable, so you should use `typedRoutes` instead of `experimental.typedRoutes`.

Support for [statically typed links](/docs/app/api-reference/config/typescript#statically-typed-links). This feature requires using TypeScript in your project.

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  typedRoutes: true,
}
 
module.exports = nextConfig
```

Was this helpful?
