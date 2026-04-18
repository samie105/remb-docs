---
title: "connection"
source: "https://nextjs.org/docs/app/api-reference/functions/connection"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/connection"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:11:19.903Z"
content_hash: "a119d4ae58faefbd16f36dd00f804130dda31e4a99205879cd4e133cd6a6c5d1"
menu_path: ["connection"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/catchError/index.md", "title": "unstable_catchError"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/cookies/index.md", "title": "cookies"}
---

# connection

Last updated April 15, 2026

The `connection()` function allows you to indicate rendering should wait for an incoming user request before continuing.

It's useful when a component doesn't use [Request-time APIs](/docs/app/glossary#request-time-apis), but you want it to be rendered at runtime and not prerendered at build time. This usually occurs when you access external information that you intentionally want to change the result of a render, such as `Math.random()` or `new Date()`.

app/page.tsx

TypeScript

JavaScriptTypeScript

```
import { connection } from 'next/server'
 
export default async function Page() {
  await connection()
  // Everything below will be excluded from prerendering
  const rand = Math.random()
  return <span>{rand}</span>
}
```

## Reference[](#reference)

### Type[](#type)

```
function connection(): Promise<void>
```

### Parameters[](#parameters)

*   The function does not accept any parameters.

### Returns[](#returns)

*   The function returns a `void` Promise. It is not meant to be consumed.

## Good to know[](#good-to-know)

*   `connection` replaces [`unstable_noStore`](/docs/app/api-reference/functions/unstable_noStore) to better align with the future of Next.js.
*   The function is only necessary when dynamic rendering is required and common Request-time APIs are not used.

### Version History[](#version-history)

Version

Changes

`v15.0.0`

`connection` stabilized.

`v15.0.0-RC`

`connection` introduced.

[Previous

unstable\_catchError

](/docs/app/api-reference/functions/catchError)

[Next

cookies

](/docs/app/api-reference/functions/cookies)

Was this helpful?

supported.

Send


