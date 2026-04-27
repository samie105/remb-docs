---
title: "pageExtensions"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:53.948Z"
content_hash: "78757cad08c89d6ac43928b5255bfea724300a59967e4eb88154190e3566a5c4"
menu_path: ["pageExtensions"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)pageExtensions

# pageExtensions

Last updated April 23, 2026

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

Was this helpful?
