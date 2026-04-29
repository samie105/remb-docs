---
title: "cacheLife"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:05:59.151Z"
content_hash: "9ef37bddefec1668a174373275e0e4d2c56b63ccc2b89ec16ad52facd5098a6e"
menu_path: ["cacheLife"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/cacheHandlers/index.md", "title": "cacheHandlers"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/compress/index.md", "title": "compress"}
---

# cacheLife

Last updated April 23, 2026

The `cacheLife` option allows you to define **custom cache profiles** when using the [`cacheLife`](../../../functions/cacheLife/index.md) function inside components or functions, and within the scope of the [`use cache` directive](../../../directives/use-cache/index.md).

## Usage[](#usage)

To define a profile, enable the [`cacheComponents` flag](../cacheComponents/index.md) and add the cache profile in the `cacheLife` object in the `next.config.js` file. For example, a `blog` profile:

next.config.ts

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  cacheComponents: true,
  cacheLife: {
    blog: {
      stale: 3600, // 1 hour
      revalidate: 900, // 15 minutes
      expire: 86400, // 1 day
    },
  },
}
 
export default nextConfig
```

You can now use this custom `blog` configuration in your component or function as follows:

app/actions.ts

JavaScriptTypeScript

```
import { cacheLife } from 'next/cache'
 
export async function getCachedData() {
  'use cache'
  cacheLife('blog')
  const data = await fetch('/api/data')
  return data
}
```

## Reference[](#reference)

The configuration object has key values with the following format:

| **Property** | **Value** | **Description** | **Requirement** |
| --- | --- | --- | --- |
| `stale` | `number` | Duration the client should cache a value without checking the server. | Optional |
| `revalidate` | `number` | Frequency at which the cache should refresh on the server; stale values may be served while revalidating. | Optional |
| `expire` | `number` | Maximum duration for which a value can remain stale before switching to dynamic. | Optional - Must be longer than `revalidate` |

## Related

View related API references.

[

### use cache

Learn how to use the "use cache" directive to cache data in your Next.js application.

](../../../directives/use-cache/index.md)[

### cacheHandlers

Configure custom cache handlers for use cache directives in Next.js.

](../cacheHandlers/index.md)[

### cacheLife

Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.

](../../../functions/cacheLife/index.md)

Was this helpful?
