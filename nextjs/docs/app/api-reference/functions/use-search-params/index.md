---
title: "useSearchParams"
source: "https://nextjs.org/docs/app/api-reference/functions/use-search-params"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/use-search-params"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:11:23.986Z"
content_hash: "8bb6f0c54acb79eabd0c9f74940f3eba3709f67bad13c7f116934cca1031f9da"
menu_path: ["useSearchParams"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/use-router/index.md", "title": "useRouter"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/use-selected-layout-segment/index.md", "title": "useSelectedLayoutSegment"}
---

# useSearchParams

Last updated April 23, 2026

`useSearchParams` is a **Client Component** hook that lets you read the current URL's **query string**.

`useSearchParams` returns a **read-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface.

app/dashboard/search-bar.tsx

JavaScriptTypeScript

```
'use client'
 
import { useSearchParams } from 'next/navigation'
 
export default function SearchBar() {
  const searchParams = useSearchParams()
 
  const search = searchParams.get('search')
 
  // URL -> `/dashboard?search=my-project`
  // `search` -> 'my-project'
  return <>Search: {search}</>
}
```

## Parameters[](#parameters)

```
const searchParams = useSearchParams()
```

`useSearchParams` does not take any parameters.

## Returns[](#returns)

`useSearchParams` returns a **read-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface, which includes utility methods for reading the URL's query string:

-   [`URLSearchParams.get()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/get): Returns the first value associated with the search parameter. For example:
    
    | URL | `searchParams.get("a")` |
    | --- | --- |
    | `/dashboard?a=1` | `'1'` |
    | `/dashboard?a=` | `''` |
    | `/dashboard?b=3` | `null` |
    | `/dashboard?a=1&a=2` | `'1'` _\- use [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll) to get all values_ |
    
-   [`URLSearchParams.has()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/has): Returns a boolean value indicating if the given parameter exists. For example:
    
    | URL | `searchParams.has("a")` |
    | --- | --- |
    | `/dashboard?a=1` | `true` |
    | `/dashboard?b=3` | `false` |
    
-   Learn more about other **read-only** methods of [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams), including the [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll), [`keys()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/keys), [`values()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/values), [`entries()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/entries), [`forEach()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/forEach), and [`toString()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/toString).
    

> **Good to know**:
> 
> -   `useSearchParams` is a [Client Component](../../../getting-started/server-and-client-components/index.md) hook and is **not supported** in [Server Components](../../../getting-started/server-and-client-components/index.md) to prevent stale values during [partial rendering](../../../getting-started/linking-and-navigating/index.md#client-side-transitions).
> -   If you want to fetch data in a Server Component based on search params, it's often a better option to read the [`searchParams` prop](../../file-conventions/page/index.md#searchparams-optional) of the corresponding Page. You can then pass it down by props to any component (Server or Client) within that Page.
> -   If an application includes the `/pages` directory, `useSearchParams` will return `ReadonlyURLSearchParams | null`. The `null` value is for compatibility during migration since search params cannot be known during prerendering of a page that doesn't use `getServerSideProps`

## Behavior[](#behavior)

### Prerendering[](#prerendering)

If a route is [prerendered](../../../glossary/index.md#prerendering), calling `useSearchParams` will cause the Client Component tree up to the closest [`Suspense` boundary](../../file-conventions/loading/index.md#examples) to be client-side rendered.

This allows a part of the route to be prerendered while the dynamic part that uses `useSearchParams` is client-side rendered.

We recommend wrapping the Client Component that uses `useSearchParams` in a `<Suspense/>` boundary. This will allow any Client Components above it to be prerendered and sent as part of initial HTML. [Example](index.md#prerendering).

For example:

app/dashboard/search-bar.tsx

JavaScriptTypeScript

```
'use client'
 
import { useSearchParams } from 'next/navigation'
 
export default function SearchBar() {
  const searchParams = useSearchParams()
 
  const search = searchParams.get('search')
 
  // This will not be logged on the server during prerendering
  console.log(search)
 
  return <>Search: {search}</>
}
```

app/dashboard/page.tsx

JavaScriptTypeScript

```
import { Suspense } from 'react'
import SearchBar from './search-bar'
 
// This component passed as a fallback to the Suspense boundary
// will be rendered in place of the search bar in the initial HTML.
// When the value is available during React hydration the fallback
// will be replaced with the `<SearchBar>` component.
function SearchBarFallback() {
  return <>placeholder</>
}
 
export default function Page() {
  return (
    <>
      <nav>
        <Suspense fallback={<SearchBarFallback />}>
          <SearchBar />
        </Suspense>
      </nav>
      <h1>Dashboard</h1>
    </>
  )
}
```

> **Good to know**:
> 
> -   In development, routes are rendered on-demand, so `useSearchParams` doesn't suspend and things may appear to work without `Suspense`.
> -   During production builds, a static page that calls `useSearchParams` from a Client Component must be wrapped in a `Suspense` boundary, otherwise the build fails with the [Missing Suspense boundary with useSearchParams](../../../../messages/missing-suspense-with-csr-bailout/index.md) error.
> -   If you intend the route to be dynamically rendered, prefer using the [`connection`](../connection/index.md) function first in a Server Component to wait for an incoming request, this excludes everything below from prerendering. See what makes a route dynamic in the [Dynamic Rendering guide](../../../glossary/index.md#dynamic-rendering).
> -   If you're already in a Server Component Page, consider using the [`searchParams` prop](../../file-conventions/page/index.md#searchparams-optional) and passing the values to Client Components.
> -   You can also pass the Page [`searchParams` prop](../../file-conventions/page/index.md#searchparams-optional) directly to a Client Component and unwrap it with React's `use()`. Although this will suspend, so the Client Component should be wrapped with a `Suspense` boundary.

### Dynamic Rendering[](#dynamic-rendering)

If a route is dynamically rendered, `useSearchParams` will be available on the server during the initial server render of the Client Component.

For example:

app/dashboard/search-bar.tsx

JavaScriptTypeScript

```
'use client'
 
import { useSearchParams } from 'next/navigation'
 
export default function SearchBar() {
  const searchParams = useSearchParams()
 
  const search = searchParams.get('search')
 
  // This will be logged on the server during the initial render
  // and on the client on subsequent navigations.
  console.log(search)
 
  return <>Search: {search}</>
}
```

app/dashboard/page.tsx

JavaScriptTypeScript

```
import { connection } from 'next/server'
import SearchBar from './search-bar'
 
export default async function Page() {
  await connection()
  return (
    <>
      <nav>
        <SearchBar />
      </nav>
      <h1>Dashboard</h1>
    </>
  )
}
```

> **Good to know**:
> 
> -   Previously, setting `export const dynamic = 'force-dynamic'` on the page was used to force dynamic rendering. Prefer using [`connection()`](../connection/index.md) instead, as it semantically ties dynamic rendering to the incoming request.

### Server Components[](#server-components)

#### Pages[](#pages)

To access search params in [Pages](../../file-conventions/page/index.md) (Server Components), use the [`searchParams`](../../file-conventions/page/index.md#searchparams-optional) prop.

#### Layouts[](#layouts)

Unlike Pages, [Layouts](../../file-conventions/layout/index.md) (Server Components) **do not** receive the `searchParams` prop. This is because a shared layout is [not re-rendered during navigation](../../../getting-started/linking-and-navigating/index.md#client-side-transitions) which could lead to stale `searchParams` between navigations. View [detailed explanation](../../file-conventions/layout/index.md#query-params).

Instead, use the Page [`searchParams`](../../file-conventions/page/index.md) prop or the [`useSearchParams`](index.md) hook in a Client Component, which is re-rendered on the client with the latest `searchParams`.

## Examples[](#examples)

### Updating `searchParams`[](#updating-searchparams)

You can use [`useRouter`](../use-router/index.md) or [`Link`](../../components/link/index.md) to set new `searchParams`. After a navigation is performed, the current [`page.js`](../../file-conventions/page/index.md) will receive an updated [`searchParams` prop](../../file-conventions/page/index.md#searchparams-optional).

app/example-client-component.tsx

JavaScriptTypeScript

```
'use client'
 
export default function ExampleClientComponent() {
  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()
 
  // Get a new searchParams string by merging the current
  // searchParams with a provided key/value pair
  const createQueryString = useCallback(
    (name: string, value: string) => {
      const params = new URLSearchParams(searchParams.toString())
      params.set(name, value)
 
      return params.toString()
    },
    [searchParams]
  )
 
  return (
    <>
      <p>Sort By</p>
 
      {/* using useRouter */}
      <button
        onClick={() => {
          // <pathname>?sort=asc
          router.push(pathname + '?' + createQueryString('sort', 'asc'))
        }}
      >
        ASC
      </button>
 
      {/* using <Link> */}
      <Link
        href={
          // <pathname>?sort=desc
          pathname + '?' + createQueryString('sort', 'desc')
        }
      >
        DESC
      </Link>
    </>
  )
}
```

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `useSearchParams` introduced. |

Was this helpful?
