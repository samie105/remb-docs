---
title: "mdxRs"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:55.154Z"
content_hash: "c6bbb435615ebda2071c1187027541dc214681f42d95eb43e28cff0ccf1b4b85"
menu_path: ["mdxRs"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/logging/index.md", "title": "logging"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/onDemandEntries/index.md", "title": "onDemandEntries"}
---

# mdxRs

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

For experimental use with `@next/mdx`. Compiles MDX files using the new Rust compiler.

next.config.js

```
const withMDX = require('@next/mdx')()
 
/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['ts', 'tsx', 'mdx'],
  experimental: {
    mdxRs: true,
  },
}
 
module.exports = withMDX(nextConfig)
```

[Previous

logging

](/docs/app/api-reference/config/next-config-js/logging)

[Next

onDemandEntries

](/docs/app/api-reference/config/next-config-js/onDemandEntries)

Was this helpful?

supported.

Send




