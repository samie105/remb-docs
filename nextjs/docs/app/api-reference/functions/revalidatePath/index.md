---
title: "revalidatePath"
source: "https://nextjs.org/docs/app/api-reference/functions/revalidatePath"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/revalidatePath"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:12:09.566Z"
content_hash: "b4f87ba1af9b19f8d3b7824868182e45f21edc6a2e9ce158cb71a46cb751d71e"
menu_path: ["revalidatePath"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/refresh/index.md", "title": "refresh"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/revalidateTag/index.md", "title": "revalidateTag"}
---

# revalidatePath

Last updated April 15, 2026

`revalidatePath` allows you to invalidate [cached data](/docs/app/getting-started/caching) on-demand for a specific path.

## Usage[](#usage)

`revalidatePath` can be called in Server Functions and Route Handlers.

`revalidatePath` cannot be called in Client Components or Proxy, as it only works in server environments.

> **Good to know**:
> 
> *   **Server Functions**: Updates the UI immediately (if viewing the affected path). Currently, it also causes all previously visited pages to refresh when navigated to again. This behavior is temporary and will be updated in the future to apply only to the specific path.
> *   **Route Handlers**: Marks the path for revalidation. The revalidation is done on the next visit to the specified path. This means calling `revalidatePath` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.

## Parameters[](#parameters)

```
revalidatePath(path: string, type?: 'page' | 'layout'): void;
```

*   `path`: Either a string that represents your route file structure. This can be a literal path like `/product/123`, or a route pattern with dynamic segments like `/product/[slug]`. Do not append `/page` or `/layout`, use the `type` parameter instead. Must not exceed 1024 characters. This value is case-sensitive. You do not need to include a trailing slash, regardless of your [`trailingSlash`](/docs/app/api-reference/config/next-config-js/trailingSlash) config.
*   `type`: (optional) `'page'` or `'layout'` string to change the type of path to revalidate. If `path` contains a dynamic segment, for example `/product/[slug]`, this parameter is required. If `path` is a literal path like `/product/1`, omit `type`.

Use a literal path when you want to refresh a [single page](#revalidating-a-specific-path). Use a route pattern plus `type` to refresh [all matching pages](#revalidating-a-page-path).

## Returns[](#returns)

`revalidatePath` does not return a value.

## What can be invalidated[](#what-can-be-invalidated)

The path parameter can point to pages, layouts, or route handlers:

*   **Pages**: Invalidates the specific page
*   **Layouts**: Invalidates the layout (the `layout.tsx` at that segment), all nested layouts beneath it, and all pages beneath them
*   **Route Handlers**: Invalidates cached data accessed within route handlers. For example `revalidatePath("/api/data")` invalidates this GET handler:

app/api/data/route.ts

```
export async function GET() {
  const data = await fetch('https://api.vercel.app/blog', {
    cache: 'force-cache',
  })
 
  return Response.json(await data.json())
}
```

## Using `revalidatePath` with rewrites[](#using-revalidatepath-with-rewrites)

When using [rewrites](/docs/app/api-reference/config/next-config-js/rewrites), you must pass the **destination** path (the actual route file location), not the source path that appears in the browser's address bar.

For example, if you have a rewrite from `/blog` to `/news`:

next.config.js

```
module.exports = {
  async rewrites() {
    return [
      {
        source: '/blog',
        destination: '/news',
      },
    ]
  },
}
```

To revalidate this page, use the destination path:

```
// Correct: use the destination path
revalidatePath('/news')
 
// Incorrect: the source path won't match the cache entry
revalidatePath('/blog')
```

This is because `revalidatePath` operates on the route file structure, not the URL visible to users. Cache entries are tagged based on which route file renders them.

## Relationship with `revalidateTag` and `updateTag`[](#relationship-with-revalidatetag-and-updatetag)

`revalidatePath`, [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag) and [`updateTag`](/docs/app/api-reference/functions/updateTag) serve different purposes:

*   **`revalidatePath`**: Invalidates a specific page or layout path
*   **`revalidateTag`**: Marks data with specific tags as **stale**. Applies across all pages that use those tags
*   **`updateTag`**: Expires data with specific tags. Applies across all pages that use those tags

When you call `revalidatePath`, only the specified path gets fresh data on the next visit. Other pages that use the same data tags will continue to serve cached data until those specific tags are also revalidated:

```
// Page A: /blog
const posts = await fetch('https://api.vercel.app/blog', {
  next: { tags: ['posts'] },
})
 
// Page B: /dashboard
const recentPosts = await fetch('https://api.vercel.app/blog?limit=5', {
  next: { tags: ['posts'] },
})
```

After calling `revalidatePath('/blog')`:

*   **Page A (/blog)**: Shows fresh data (page re-rendered)
*   **Page B (/dashboard)**: Still shows stale data (cache tag 'posts' not invalidated)

Learn about the difference between [`revalidateTag` and `updateTag`](/docs/app/api-reference/functions/updateTag#differences-from-revalidatetag).

### Building revalidation utilities[](#building-revalidation-utilities)

`revalidatePath` and `updateTag` are complementary primitives that are often used together in utility functions to ensure comprehensive data consistency across your application:

```
'use server'
 
import { revalidatePath, updateTag } from 'next/cache'
 
export async function updatePost() {
  await updatePostInDatabase()
 
  revalidatePath('/blog') // Refresh the blog page
  updateTag('posts') // Refresh all pages using 'posts' tag
}
```

This pattern ensures that both the specific page and any other pages using the same data remain consistent.

## Examples[](#examples)

### Revalidating a specific path[](#revalidating-a-specific-path)

```
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/post-1')
```

This will invalidate one specific path for revalidation on the next page visit.

### Revalidating a Page path[](#revalidating-a-page-path)

```
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/[slug]', 'page')
// or with route groups
revalidatePath('/(main)/blog/[slug]', 'page')
```

This will invalidate any path that matches the provided `page` file for revalidation on the next page visit. This will _not_ invalidate pages beneath the specific page. For example, `/blog/[slug]` won't invalidate `/blog/[slug]/[author]`.

### Revalidating a Layout path[](#revalidating-a-layout-path)

```
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/[slug]', 'layout')
// or with route groups
revalidatePath('/(main)/post/[slug]', 'layout')
```

This will invalidate any path that matches the provided `layout` file for revalidation on the next page visit. This will cause pages beneath with the same layout to be invalidated and revalidated on the next visit. For example, in the above case, `/blog/[slug]/[another]` would also be invalidated and revalidated on the next visit.

### Revalidating all data[](#revalidating-all-data)

```
import { revalidatePath } from 'next/cache'
 
revalidatePath('/', 'layout')
```

This will purge the [Client Cache](/docs/app/glossary#client-cache), and invalidate all cached data for revalidation on the next page visit.

### Server Function[](#server-function)

app/actions.ts

TypeScript

JavaScriptTypeScript

```
'use server'
 
import { revalidatePath } from 'next/cache'
 
export default async function submit() {
  await submitForm()
  revalidatePath('/')
}
```

### Route Handler[](#route-handler)

app/api/revalidate/route.ts

TypeScript

JavaScriptTypeScript

```
import { revalidatePath } from 'next/cache'
import type { NextRequest } from 'next/server'
 
export async function GET(request: NextRequest) {
  const path = request.nextUrl.searchParams.get('path')
 
  if (path) {
    revalidatePath(path)
    return Response.json({ revalidated: true, now: Date.now() })
  }
 
  return Response.json({
    revalidated: false,
    now: Date.now(),
    message: 'Missing path to revalidate',
  })
}
```

[Previous

refresh

](/docs/app/api-reference/functions/refresh)

[Next

revalidateTag

](/docs/app/api-reference/functions/revalidateTag)

Was this helpful?

supported.

Send


