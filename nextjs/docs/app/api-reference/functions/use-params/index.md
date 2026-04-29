---
title: "useParams"
source: "https://nextjs.org/docs/app/api-reference/functions/use-params"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/use-params"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:11:13.441Z"
content_hash: "bd8233888319f5d55ba35bfe2185cabe8cdd1d4d93960023fbe3d570f598598c"
menu_path: ["useParams"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../use-link-status/index.md", "title": "useLinkStatus"}
nav_next: {"path": "../use-pathname/index.md", "title": "usePathname"}
---

# useParams

Last updated April 23, 2026

`useParams` is a **Client Component** hook that lets you read a route's [dynamic params](/docs/app/api-reference/file-conventions/dynamic-routes) filled in by the current URL.

app/example-client-component.tsx

JavaScriptTypeScript

```
'use client'
 
import { useParams } from 'next/navigation'
 
export default function ExampleClientComponent() {
  const params = useParams<{ tag: string; item: string }>()
 
  // Route -> /shop/[tag]/[item]
  // URL -> /shop/shoes/nike-air-max-97
  // `params` -> { tag: 'shoes', item: 'nike-air-max-97' }
  console.log(params)
 
  return '...'
}
```

## Parameters[](#parameters)

```
const params = useParams()
```

`useParams` does not take any parameters.

## Returns[](#returns)

`useParams` returns an object containing the current route's filled in [dynamic parameters](/docs/app/api-reference/file-conventions/dynamic-routes).

-   Each property in the object is an active dynamic segment.
-   The properties name is the segment's name, and the properties value is what the segment is filled in with.
-   The properties value will either be a `string` or array of `string`'s depending on the [type of dynamic segment](/docs/app/api-reference/file-conventions/dynamic-routes).
-   If the route contains no dynamic parameters, `useParams` returns an empty object.
-   If used in Pages Router, `useParams` will return `null` on the initial render and updates with properties following the rules above once the router is ready.

For example:

| Route | URL | `useParams()` |
| --- | --- | --- |
| `app/shop/page.js` | `/shop` | `{}` |
| `app/shop/[slug]/page.js` | `/shop/1` | `{ slug: '1' }` |
| `app/shop/[tag]/[item]/page.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |
| `app/shop/[...slug]/page.js` | `/shop/1/2` | `{ slug: ['1', '2'] }` |

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v13.3.0` | `useParams` introduced. |

Was this helpful?
