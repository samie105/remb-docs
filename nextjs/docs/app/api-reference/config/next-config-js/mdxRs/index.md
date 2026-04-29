---
title: "mdxRs"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:45.364Z"
content_hash: "787c6e5855058372ea51356b47f0db7ecc67160a78558d6ff17091e3a6c4e896"
menu_path: ["mdxRs"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/logging/index.md", "title": "logging"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/onDemandEntries/index.md", "title": "onDemandEntries"}
---

# mdxRs

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

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

Was this helpful?
