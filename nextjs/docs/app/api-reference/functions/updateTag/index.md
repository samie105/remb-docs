---
title: "updateTag"
source: "https://nextjs.org/docs/app/api-reference/functions/updateTag"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/updateTag"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:11:08.650Z"
content_hash: "c2e5c5bd2b9ecd8e858a0221bd5a850be49a26b4c3de502fef3fa7110db77655"
menu_path: ["updateTag"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../unstable_rethrow/index.md", "title": "unstable_rethrow"}
nav_next: {"path": "../use-link-status/index.md", "title": "useLinkStatus"}
---

# updateTag

Last updated April 23, 2026

`updateTag` allows you to update cached data on-demand for a specific cache tag from within [Server Actions](/docs/app/getting-started/mutating-data).

This function is designed for **read-your-own-writes** scenarios, where a user makes a change (like creating a post), and the UI immediately shows the change, rather than stale data.

## Usage[](#usage)

`updateTag` can **only** be called from within [Server Actions](/docs/app/getting-started/mutating-data). It cannot be used in Route Handlers, Client Components, or any other context.

If you need to invalidate cache tags in Route Handlers or other contexts, use [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag) instead.

> **Good to know**: `updateTag` immediately expires the cached data for the specified tag. The next request will wait to fetch fresh data rather than serving stale content from the cache, ensuring users see their changes immediately.

## Parameters[](#parameters)

```
updateTag(tag: string): void;
```

-   `tag`: A string representing the cache tag associated with the data you want to update. Must not exceed 256 characters. This value is case-sensitive.

Tags must first be assigned to cached data. You can do this in two ways:

-   Using the [`next.tags`](/docs/app/api-reference/functions/fetch) option with `fetch` for caching external API requests:

```
fetch(url, { next: { tags: ['posts'] } })
```

-   Using [`cacheTag`](/docs/app/api-reference/functions/cacheTag) inside cached functions or components with the `'use cache'` directive:

```
import { cacheTag } from 'next/cache'
 
async function getData() {
  'use cache'
  cacheTag('posts')
  // ...
}
```

## Returns[](#returns)

`updateTag` does not return a value.

## Differences from revalidateTag[](#differences-from-revalidatetag)

While both `updateTag` and `revalidateTag` invalidate cached data, they serve different purposes:

-   **`updateTag`**:
    
    -   Can only be used in Server Actions
    -   Next request waits for fresh data (no stale content served)
    -   Designed for read-your-own-writes scenarios
-   **`revalidateTag`**:
    
    -   Can be used in Server Actions and Route Handlers
    -   With `profile="max"` (recommended): Serves cached data while fetching fresh data in the background (stale-while-revalidate)
    -   With custom profile: Can be configured to any cache life profile for advanced usage
    -   Without profile: legacy behavior which is equivalent to `updateTag`

## Examples[](#examples)

### Server Action with Read-Your-Own-Writes[](#server-action-with-read-your-own-writes)

app/actions.ts

JavaScriptTypeScript

```
'use server'
 
import { updateTag } from 'next/cache'
import { redirect } from 'next/navigation'
 
export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')
 
  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })
 
  // Invalidate cache tags so the new post is immediately visible
  // 'posts' tag: affects any page that displays a list of posts
  updateTag('posts')
  // 'post-{id}' tag: affects the individual post detail page
  updateTag(`post-${post.id}`)
 
  // Redirect to the new post - user will see fresh data, not cached
  redirect(`/posts/${post.id}`)
}
```

### Error when used outside Server Actions[](#error-when-used-outside-server-actions)

app/api/posts/route.ts

JavaScriptTypeScript

```
import { updateTag } from 'next/cache'
 
export async function POST() {
  // This will throw an error
  updateTag('posts')
  // Error: updateTag can only be called from within a Server Action
 
  // Use revalidateTag instead in Route Handlers
  revalidateTag('posts', 'max')
}
```

## When to use updateTag[](#when-to-use-updatetag)

Use `updateTag` when:

-   You're in a Server Action
-   You need immediate cache invalidation for read-your-own-writes
-   You want to ensure the next request sees updated data

Use `revalidateTag` instead when:

-   You're in a Route Handler or other non-action context
-   You want stale-while-revalidate semantics
-   You're building a webhook or API endpoint for cache invalidation

## Related[](#related)

-   [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag) - For invalidating tags in Route Handlers
-   [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath) - For invalidating specific paths

Was this helpful?
