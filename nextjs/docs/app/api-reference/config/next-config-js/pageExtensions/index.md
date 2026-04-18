---
title: "pageExtensions"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:04.908Z"
content_hash: "1ff2a4246c5c319dbfa8f6d085b9921305c890852bdedb6aebffecf0619d92d3"
menu_path: ["pageExtensions"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/output/index.md", "title": "output"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/poweredByHeader/index.md", "title": "poweredByHeader"}
---

# pageExtensions

Last updated April 15, 2026

By default, Next.js accepts files with the following extensions: `.tsx`, `.ts`, `.jsx`, `.js`. This can be modified to allow other extensions like markdown (`.md`, `.mdx`).

next.config.js

```
const withMDX = require('@next/mdx')()
 
/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
}
 
module.exports = withMDX(nextConfig)
```

[Previous

output

](/docs/app/api-reference/config/next-config-js/output)

[Next

poweredByHeader

](/docs/app/api-reference/config/next-config-js/poweredByHeader)

Was this helpful?

supported.

Send
