---
title: "Cannot access `cookies()` or `headers()` in `\"use cache\"`"
source: "https://nextjs.org/docs/messages/next-request-in-use-cache"
canonical_url: "https://nextjs.org/docs/messages/next-request-in-use-cache"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:25.106Z"
content_hash: "e8bb7b7539af8c8d6d8fdd3c020483cbdaf18b5d9b393b2c1db777b0fdfa37de"
menu_path: ["Cannot access `cookies()` or `headers()` in `\"use cache\"`"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../next-dynamic-modules/index.md", "title": "`next/dynamic` has deprecated loading multiple modules at once"}
nav_next: {"path": "../next-script-for-ga/index.md", "title": "Using Google Analytics with Next.js (through `@next/third-parties/google`)"}
---

# Cannot access \`cookies()\` or \`headers()\` in \`"use cache"\`

## Why This Error Occurred[](#why-this-error-occurred)

A function is trying to read from the current incoming request inside the scope of a function annotated with `"use cache"`. This is not supported because it would make the cache invalidated by every request which is probably not what you intended.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Instead of calling this inside the `"use cache"` function, move it outside the function and pass the value in as an argument. The specific value will now be part of the cache key through its arguments.

Before:

app/page.js

```
import { cookies } from 'next/headers'
 
async function getExampleData() {
  "use cache"
  const isLoggedIn = (await cookies()).has('token')
  ...
}
 
export default async function Page() {
  const data = await getExampleData()
  return ...
}
```

After:

app/page.js

```
import { cookies } from 'next/headers'
 
async function getExampleData(isLoggedIn) {
  "use cache"
  ...
}
 
export default async function Page() {
  const isLoggedIn = (await cookies()).has('token')
  const data = await getExampleData(isLoggedIn)
  return ...
}
```

## Useful Links[](#useful-links)

-   [`headers()` function](/docs/app/api-reference/functions/headers)
-   [`cookies()` function](/docs/app/api-reference/functions/cookies)
-   [`draftMode()` function](/docs/app/api-reference/functions/draft-mode)

Was this helpful?
