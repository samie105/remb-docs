---
title: "Migrating to Cache Components"
source: "https://nextjs.org/docs/app/guides/migrating-to-cache-components"
canonical_url: "https://nextjs.org/docs/app/guides/migrating-to-cache-components"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:14:14.256Z"
content_hash: "a81afa2e0f98460572fc1b50b0aa8872450807e253cc4f790a14e1d08082d51a"
menu_path: ["Migrating to Cache Components"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/guides/migrating/from-vite/index.md", "title": "How to migrate from Vite to Next.js"}
nav_next: {"path": "nextjs/docs/app/guides/multi-tenant/index.md", "title": "How to build multi-tenant apps in Next.js"}
---

# Migrating to Cache Components

Last updated April 23, 2026

When [Cache Components](/docs/app/api-reference/config/next-config-js/cacheComponents) is enabled, route segment configs like `dynamic`, `revalidate`, and `fetchCache` are replaced by [`use cache`](/docs/app/api-reference/directives/use-cache) and [`cacheLife`](/docs/app/api-reference/functions/cacheLife).

## `dynamic = "force-dynamic"`[](#dynamic--force-dynamic)

**Not needed.** All pages are dynamic by default.

app/page.tsx

JavaScriptTypeScript

```
// Before - No longer needed
export const dynamic = 'force-dynamic'
 
export default function Page() {
  return <div>...</div>
}
```

app/page.tsx

JavaScriptTypeScript

```
// After - Just remove it
export default function Page() {
  return <div>...</div>
}
```

## `dynamic = "force-static"`[](#dynamic--force-static)

Start by removing it. When unhandled uncached or runtime data access is detected during development and build time, Next.js raises an error. Otherwise, the prerendering step automatically extracts the static HTML shell.

For uncached data access, add [`use cache`](/docs/app/api-reference/directives/use-cache) as close to the data access as possible with a long [`cacheLife`](/docs/app/api-reference/functions/cacheLife) like `'max'` to maintain cached behavior. If needed, add it at the top of the page or layout.

For runtime data access (`cookies()`, `headers()`, etc.), errors will direct you to wrap it with `<Suspense>`. Since you started by using `force-static`, you must remove the runtime data access to prevent any request time work.

app/page.tsx

JavaScriptTypeScript

```
// Before
export const dynamic = 'force-static'
 
export default async function Page() {
  const data = await fetch('https://api.example.com/data')
  return <div>...</div>
}
```

app/page.tsx

JavaScriptTypeScript

```
import { cacheLife } from 'next/cache'
 
// After - Use 'use cache' instead
export default async function Page() {
  'use cache'
  cacheLife('max')
  const data = await fetch('https://api.example.com/data')
  return <div>...</div>
}
```

## `revalidate`[](#revalidate)

**Replace with `cacheLife`.** Use the `cacheLife` function to define cache duration instead of the route segment config.

app/page.tsx

JavaScriptTypeScript

```
// Before
export const revalidate = 3600 // 1 hour
 
export default async function Page() {
  return <div>...</div>
}
```

app/page.tsx

JavaScriptTypeScript

```
// After - Use cacheLife
import { cacheLife } from 'next/cache'
 
export default async function Page() {
  'use cache'
  cacheLife('hours')
  return <div>...</div>
}
```

## `fetchCache`[](#fetchcache)

**Not needed.** With `use cache`, all data fetching within a cached scope is automatically cached, making `fetchCache` unnecessary.

app/page.tsx

JavaScriptTypeScript

```
// Before
export const fetchCache = 'force-cache'
```

app/page.tsx

JavaScriptTypeScript

```
// After - Use 'use cache' to control caching behavior
export default async function Page() {
  'use cache'
  // All fetches here are cached
  return <div>...</div>
}
```

## `runtime = 'edge'`[](#runtime--edge)

**Not supported.** Cache Components requires the Node.js runtime. Switch to the Node.js runtime (the default) by removing the `runtime = 'edge'` export. If you need edge behavior for specific routes, use [Proxy](/docs/app/api-reference/file-conventions/proxy) instead.

Was this helpful?
