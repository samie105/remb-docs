---
title: "notFound"
source: "https://nextjs.org/docs/app/api-reference/functions/not-found"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/not-found"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:10:42.548Z"
content_hash: "95a2c9c58e2d0597b7c677d132e3c34d124c843057023acbca01afd2a6e61c8c"
menu_path: ["notFound"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/next-response/index.md", "title": "NextResponse"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/permanentRedirect/index.md", "title": "permanentRedirect"}
---

# notFound

Last updated April 23, 2026

The `notFound` function allows you to render the [`not-found file`](../../file-conventions/not-found/index.md) within a route segment as well as inject a [`<meta name="robots" content="noindex" />`](../../file-conventions/loading/index.md#status-codes) tag for search engines.

## `notFound()`[](#notfound)

Invoking the `notFound()` function throws a `NEXT_HTTP_ERROR_FALLBACK;404` error and terminates rendering of the route segment in which it was thrown. Specifying a [**not-found** file](../../file-conventions/not-found/index.md) allows you to gracefully handle such errors by rendering a Not Found UI within the segment.

app/user/\[id\]/page.js

```
import { notFound } from 'next/navigation'
 
async function fetchUser(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}
 
export default async function Profile({ params }) {
  const { id } = await params
  const user = await fetchUser(id)
 
  if (!user) {
    notFound()
  }
 
  // ...
}
```

> **Good to know**: `notFound()` does not require you to use `return notFound()` due to using the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `notFound` introduced. |

Was this helpful?
