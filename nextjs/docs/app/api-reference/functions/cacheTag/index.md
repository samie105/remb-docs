---
title: "cacheTag"
source: "https://nextjs.org/docs/app/api-reference/functions/cacheTag"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/cacheTag"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:54.829Z"
content_hash: "37672ddb2c66f148d886180042f556da35fb1b84b47fb4aee2955aa91b2b3008"
menu_path: ["cacheTag"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../cacheLife/index.md", "title": "cacheLife"}
nav_next: {"path": "../catchError/index.md", "title": "unstable_catchError"}
---

# cacheTag

Last updated April 23, 2026

The `cacheTag` function allows you to tag cached data for on-demand invalidation. By associating tags with cache entries, you can selectively purge or revalidate specific cache entries without affecting other cached data.

## Usage[](#usage)

To use `cacheTag`, enable the [`cacheComponents` flag](/docs/app/api-reference/config/next-config-js/cacheComponents) in your `next.config.js` file:

next.config.ts

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  cacheComponents: true,
}
 
export default nextConfig
```

The `cacheTag` function takes one or more string values.

app/data.ts

JavaScriptTypeScript

```
import { cacheTag } from 'next/cache'
 
export async function getData() {
  'use cache'
  cacheTag('my-data')
  const data = await fetch('/api/data')
  return data
}
```

You can then purge the cache on-demand using [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag) API in another function, for example, a [route handler](/docs/app/api-reference/file-conventions/route) or [Server Action](/docs/app/getting-started/mutating-data):

app/action.ts

JavaScriptTypeScript

```
'use server'
 
import { revalidateTag } from 'next/cache'
 
export default async function submit() {
  await addPost()
  revalidateTag('my-data')
}
```

## Good to know[](#good-to-know)

-   **Idempotent Tags**: Applying the same tag multiple times has no additional effect.
-   **Multiple Tags**: You can assign multiple tags to a single cache entry by passing multiple string values to `cacheTag`.

```
cacheTag('tag-one', 'tag-two')
```

-   **Limits**: The max length for a custom tag is 256 characters and the max tag items is 128.

## Examples[](#examples)

### Tagging components or functions[](#tagging-components-or-functions)

Tag your cached data by calling `cacheTag` within a cached function or component:

app/components/bookings.tsx

JavaScriptTypeScript

```
import { cacheTag } from 'next/cache'
 
interface BookingsProps {
  type: string
}
 
export async function Bookings({ type = 'haircut' }: BookingsProps) {
  'use cache'
  cacheTag('bookings-data')
 
  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }
 
  return //...
}
```

### Creating tags from external data[](#creating-tags-from-external-data)

You can use the data returned from an async function to tag the cache entry.

app/components/bookings.tsx

JavaScriptTypeScript

```
import { cacheTag } from 'next/cache'
 
interface BookingsProps {
  type: string
}
 
export async function Bookings({ type = 'haircut' }: BookingsProps) {
  async function getBookingsData() {
    'use cache'
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    cacheTag('bookings-data', data.id)
    return data
  }
  return //...
}
```

### Invalidating tagged cache[](#invalidating-tagged-cache)

Using [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag), you can invalidate the cache for a specific tag when needed:

app/actions.ts

JavaScriptTypeScript

```
'use server'
 
import { revalidateTag } from 'next/cache'
 
export async function updateBookings() {
  await updateBookingData()
  revalidateTag('bookings-data')
}
```

## Related

View related API references.

[

### cacheComponents

Learn how to enable the cacheComponents flag in Next.js.

](/docs/app/api-reference/config/next-config-js/cacheComponents)[

### use cache

Learn how to use the "use cache" directive to cache data in your Next.js application.

](/docs/app/api-reference/directives/use-cache)[

### revalidateTag

API Reference for the revalidateTag function.

](/docs/app/api-reference/functions/revalidateTag)[

### cacheLife

Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.

](/docs/app/api-reference/functions/cacheLife)

Was this helpful?
