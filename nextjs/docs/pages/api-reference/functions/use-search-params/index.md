---
title: "useSearchParams"
source: "https://nextjs.org/docs/pages/api-reference/functions/use-search-params"
canonical_url: "https://nextjs.org/docs/pages/api-reference/functions/use-search-params"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:22:35.643Z"
content_hash: "e8116648f65ba05a4f896a84648ba646024527263fda869e9b5d1148d25a435c"
menu_path: ["useSearchParams"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/functions/use-router/index.md", "title": "useRouter"}
nav_next: {"path": "nextjs/docs/pages/api-reference/functions/userAgent/index.md", "title": "userAgent"}
---

# useSearchParams

Last updated April 15, 2026

`useSearchParams` is a hook that lets you read the current URL's **query string**.

`useSearchParams` returns a **read-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface.

pages/dashboard.tsx

TypeScript

JavaScriptTypeScript

```
import { useSearchParams } from 'next/navigation'
 
export default function Dashboard() {
  const searchParams = useSearchParams()
 
  if (!searchParams) {
    // Render fallback UI while search params are not yet available
    return null
  }
 
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

`useSearchParams` returns a **read-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface, or `null` during [prerendering](#behavior-during-prerendering).

The interface includes utility methods for reading the URL's query string:

*   [`URLSearchParams.get()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/get): Returns the first value associated with the search parameter. For example:
    
    URL
    
    `searchParams.get("a")`
    
    `/dashboard?a=1`
    
    `'1'`
    
    `/dashboard?a=`
    
    `''`
    
    `/dashboard?b=3`
    
    `null`
    
    `/dashboard?a=1&a=2`
    
    `'1'` _\- use [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll) to get all values_
    
*   [`URLSearchParams.has()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/has): Returns a boolean value indicating if the given parameter exists. For example:
    
    URL
    
    `searchParams.has("a")`
    
    `/dashboard?a=1`
    
    `true`
    
    `/dashboard?b=3`
    
    `false`
    
*   Learn more about other **read-only** methods of [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams), including the [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll), [`keys()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/keys), [`values()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/values), [`entries()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/entries), [`forEach()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/forEach), and [`toString()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/toString).
    

> **Good to know**: `useSearchParams` is a [React Hook](https://react.dev/learn#using-hooks) and cannot be used with classes.

## Behavior[](#behavior)

### Behavior during prerendering[](#behavior-during-prerendering)

For pages that are [statically optimized](/docs/pages/building-your-application/rendering/automatic-static-optimization) (not using `getServerSideProps`), `useSearchParams` will return `null` during prerendering. After hydration, the value will be updated to the actual search params.

This is because search params cannot be known during static generation as they depend on the request.

pages/dashboard.tsx

TypeScript

JavaScriptTypeScript

```
import { useSearchParams } from 'next/navigation'
 
export default function Dashboard() {
  const searchParams = useSearchParams()
 
  if (!searchParams) {
    // Return a fallback UI while search params are loading
    // This prevents hydration mismatches
    return <DashboardSkeleton />
  }
 
  const search = searchParams.get('search')
 
  return <>Search: {search}</>
}
```

### Using with `getServerSideProps`[](#using-with-getserversideprops)

When using [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props), the page is server-rendered on each request and `useSearchParams` will return the actual search params immediately:

pages/dashboard.tsx

TypeScript

JavaScriptTypeScript

```
import { useSearchParams } from 'next/navigation'
 
export default function Dashboard() {
  const searchParams = useSearchParams()
 
  // With getServerSideProps, this fallback is never rendered because
  // searchParams is always available on the server. However, keeping
  // the fallback allows this component to be reused on other pages
  // that may not use getServerSideProps.
  if (!searchParams) {
    return null
  }
 
  const search = searchParams.get('search')
 
  return <>Search: {search}</>
}
 
export async function getServerSideProps() {
  return { props: {} }
}
```

## Examples[](#examples)

### Updating search params[](#updating-search-params)

You can use the [`useRouter`](/docs/pages/api-reference/functions/use-router) hook to update search params:

pages/dashboard.tsx

TypeScript

JavaScriptTypeScript

```
import { useRouter } from 'next/router'
import { useSearchParams } from 'next/navigation'
import { useCallback } from 'react'
 
export default function Dashboard() {
  const router = useRouter()
  const searchParams = useSearchParams()
 
  const createQueryString = useCallback(
    (name: string, value: string) => {
      const params = new URLSearchParams(searchParams?.toString())
      params.set(name, value)
      return params.toString()
    },
    [searchParams]
  )
 
  if (!searchParams) {
    return null
  }
 
  return (
    <>
      <p>Sort By</p>
      <button
        onClick={() => {
          router.push(router.pathname + '?' + createQueryString('sort', 'asc'))
        }}
      >
        ASC
      </button>
      <button
        onClick={() => {
          router.push(router.pathname + '?' + createQueryString('sort', 'desc'))
        }}
      >
        DESC
      </button>
    </>
  )
}
```

### Sharing components with App Router[](#sharing-components-with-app-router)

`useSearchParams` from `next/navigation` works in both the Pages Router and App Router. This allows you to create shared components that work in either context:

components/search-bar.tsx

TypeScript

JavaScriptTypeScript

```
import { useSearchParams } from 'next/navigation'
 
// This component works in both pages/ and app/
export function SearchBar() {
  const searchParams = useSearchParams()
 
  if (!searchParams) {
    // Fallback for Pages Router during prerendering
    return <input defaultValue="" placeholder="Search..." />
  }
 
  const search = searchParams.get('search') ?? ''
 
  return <input defaultValue={search} placeholder="Search..." />
}
```

> **Good to know**: When using this component in the App Router, wrap it in a `<Suspense>` boundary for [prerendering](/docs/app/api-reference/functions/use-search-params#prerendering) support.

## Version History[](#version-history)

Version

Changes

`v13.0.0`

`useSearchParams` introduced.

Was this helpful?

supported.

Send


