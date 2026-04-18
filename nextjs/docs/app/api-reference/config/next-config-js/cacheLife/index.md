---
title: "cacheLife"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:07.840Z"
content_hash: "bcbcb998e524cf9ad5b40c07b64eac2c9fbb520261968c0af73120d2469612c9"
menu_path: ["cacheLife"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/cacheHandlers/index.md", "title": "cacheHandlers"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/compress/index.md", "title": "compress"}
---

# cacheLife

Last updated April 15, 2026

The `cacheLife` option allows you to define **custom cache profiles** when using the [`cacheLife`](/docs/app/api-reference/functions/cacheLife) function inside components or functions, and within the scope of the [`use cache` directive](/docs/app/api-reference/directives/use-cache).

## Usage[](#usage)

To define a profile, enable the [`cacheComponents` flag](/docs/app/api-reference/config/next-config-js/cacheComponents) and add the cache profile in the `cacheLife` object in the `next.config.js` file. For example, a `blog` profile:

next.config.ts

TypeScript

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

TypeScript

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

**Property**

**Value**

**Description**

**Requirement**

`stale`

`number`

Duration the client should cache a value without checking the server.

Optional

`revalidate`

`number`

Frequency at which the cache should refresh on the server; stale values may be served while revalidating.

Optional

`expire`

`number`

Maximum duration for which a value can remain stale before switching to dynamic.

Optional - Must be longer than `revalidate`

## Related

View related API references.

[

### use cache

Learn how to use the "use cache" directive to cache data in your Next.js application.

](/docs/app/api-reference/directives/use-cache)[

### cacheHandlers

Configure custom cache handlers for use cache directives in Next.js.

](/docs/app/api-reference/config/next-config-js/cacheHandlers)[

### cacheLife

Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.

](/docs/app/api-reference/functions/cacheLife)

[Previous

cacheHandlers

](/docs/app/api-reference/config/next-config-js/cacheHandlers)

[Next

compress

](/docs/app/api-reference/config/next-config-js/compress)

Was this helpful?

supported.

Send




