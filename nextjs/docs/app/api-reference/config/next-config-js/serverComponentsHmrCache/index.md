---
title: "serverComponentsHmrCache"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:34.490Z"
content_hash: "7a380f7d603b61326b3e535d929d5960e5f4c58d00e73132a97649e572614a4c"
menu_path: ["serverComponentsHmrCache"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/serverActions/index.md", "title": "serverActions"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/serverExternalPackages/index.md", "title": "serverExternalPackages"}
---

# serverComponentsHmrCache

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.

By default, the HMR cache applies to all `fetch` requests, including those with the `cache: 'no-store'` option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.

You can disable the HMR cache by setting `serverComponentsHmrCache` to `false` in your `next.config.js` file:

next.config.ts

TypeScript

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    serverComponentsHmrCache: false, // defaults to true
  },
}
 
export default nextConfig
```

> **Good to know:** For better observability, we recommend using the [`logging.fetches`](/docs/app/api-reference/config/next-config-js/logging) option which logs fetch cache hits and misses in the console during development.

[Previous

serverActions

](/docs/app/api-reference/config/next-config-js/serverActions)

[Next

serverExternalPackages

](/docs/app/api-reference/config/next-config-js/serverExternalPackages)

Was this helpful?

supported.

Send


