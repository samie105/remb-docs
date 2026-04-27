---
title: "connection"
source: "https://nextjs.org/docs/app/api-reference/functions/connection"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/connection"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:59.535Z"
content_hash: "c45c9519757a735a9f1b2dd456a116a73eaa218c05e714827db0d707d5bd12ea"
menu_path: ["connection"]
section_path: []
version: "latest"
content_language: "en"
---
[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)connection

# connection

Last updated April 23, 2026

The `connection()` function allows you to indicate rendering should wait for an incoming user request before continuing.

It's useful when a component doesn't use [Request-time APIs](/docs/app/glossary#request-time-apis), but you want it to be rendered at runtime and not prerendered at build time. This usually occurs when you access external information that you intentionally want to change the result of a render, such as `Math.random()` or `new Date()`.

app/page.tsx

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

-   The function does not accept any parameters.

### Returns[](#returns)

-   The function returns a `void` Promise. It is not meant to be consumed.

## Good to know[](#good-to-know)

-   `connection` replaces [`unstable_noStore`](/docs/app/api-reference/functions/unstable_noStore) to better align with the future of Next.js.
-   The function is only necessary when dynamic rendering is required and common Request-time APIs are not used.

### Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | `connection` stabilized. |
| `v15.0.0-RC` | `connection` introduced. |

Was this helpful?
