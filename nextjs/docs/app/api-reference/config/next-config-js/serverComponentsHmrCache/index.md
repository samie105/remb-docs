---
title: "serverComponentsHmrCache"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:20.074Z"
content_hash: "aaca2488c7b486ed3e2a8ad8b25adb33850bb70efd7909e82dc7436aa130172a"
menu_path: ["serverComponentsHmrCache"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)serverComponentsHmrCache

# serverComponentsHmrCache

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.

By default, the HMR cache applies to all `fetch` requests, including those with the `cache: 'no-store'` option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.

You can disable the HMR cache by setting `serverComponentsHmrCache` to `false` in your `next.config.js` file:

next.config.ts

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

Was this helpful?
