---
title: "useParams"
source: "https://nextjs.org/docs/pages/api-reference/functions/use-params"
canonical_url: "https://nextjs.org/docs/pages/api-reference/functions/use-params"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:21:51.348Z"
content_hash: "3a5954bd4e5ff96075d846ef630a7697df40ee86669050aa2c70c84d26c782d8"
menu_path: ["useParams"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../next-response/index.md", "title": "NextResponse"}
nav_next: {"path": "../use-report-web-vitals/index.md", "title": "useReportWebVitals"}
---

# useParams

Last updated April 23, 2026

`useParams` is a hook that lets you read a route's [dynamic params](/docs/pages/building-your-application/routing/dynamic-routes) filled in by the current URL.

pages/shop/\[slug\].tsx

JavaScriptTypeScript

```
import { useParams } from 'next/navigation'
 
export default function ShopPage() {
  const params = useParams<{ slug: string }>()
 
  if (!params) {
    // Render fallback UI while params are not yet available
    return null
  }
 
  // Route -> /shop/[slug]
  // URL -> /shop/shoes
  // `params` -> { slug: 'shoes' }
  return <>Shop: {params.slug}</>
}
```

## Parameters[](#parameters)

```
const params = useParams()
```

`useParams` does not take any parameters.

## Returns[](#returns)

`useParams` returns an object containing the current route's filled in [dynamic parameters](/docs/pages/building-your-application/routing/dynamic-routes), or `null` during [prerendering](#behavior-during-prerendering).

-   Each property in the object is an active dynamic segment.
-   The property name is the segment's name, and the property value is what the segment is filled in with.
-   The property value will either be a `string` or array of `string`s depending on the [type of dynamic segment](/docs/pages/building-your-application/routing/dynamic-routes).
-   If the route contains no dynamic parameters, `useParams` returns an empty object.

For example:

| Route | URL | `useParams()` |
| --- | --- | --- |
| `pages/shop/page.js` | `/shop` | `{}` |
| `pages/shop/[slug].js` | `/shop/1` | `{ slug: '1' }` |
| `pages/shop/[tag]/[item].js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |
| `pages/shop/[...slug].js` | `/shop/1/2` | `{ slug: ['1', '2'] }` |

> **Good to know**: `useParams` is a [React Hook](https://react.dev/learn#using-hooks) and cannot be used with classes.

## Behavior[](#behavior)

### Behavior during prerendering[](#behavior-during-prerendering)

For pages that are [statically optimized](/docs/pages/building-your-application/rendering/automatic-static-optimization), `useParams` will return `null` on the initial render. After hydration, the value will be updated to the actual params once the router is ready.

This is because params cannot be known during static generation for dynamic routes.

pages/shop/\[slug\].tsx

JavaScriptTypeScript

```
import { useParams } from 'next/navigation'
 
export default function ShopPage() {
  const params = useParams<{ slug: string }>()
 
  if (!params) {
    // Return a fallback UI while params are loading
    // This prevents hydration mismatches
    return <ShopPageSkeleton />
  }
 
  return <>Shop: {params.slug}</>
}
```

### Using with `getServerSideProps`[](#using-with-getserversideprops)

When using [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props), the page is server-rendered on each request and `useParams` will return the actual params immediately:

pages/shop/\[slug\].tsx

JavaScriptTypeScript

```
import { useParams } from 'next/navigation'
 
export default function ShopPage() {
  const params = useParams<{ slug: string }>()
 
  // With getServerSideProps, this fallback is never rendered because
  // params is always available on the server. However, keeping
  // the fallback allows this component to be reused on other pages
  // that may not use getServerSideProps.
  if (!params) {
    return null
  }
 
  return <>Shop: {params.slug}</>
}
 
export async function getServerSideProps() {
  return { props: {} }
}
```

### Comparison with `router.query`[](#comparison-with-routerquery)

`useParams` only returns the dynamic route parameters, whereas [`router.query`](/docs/pages/api-reference/functions/use-router#router-object) from `useRouter` includes both dynamic parameters and query string parameters.

pages/shop/\[slug\].tsx

JavaScriptTypeScript

```
import { useRouter } from 'next/router'
import { useParams } from 'next/navigation'
 
export default function ShopPage() {
  const router = useRouter()
  const params = useParams()
 
  // URL -> /shop/shoes?color=red
 
  // router.query -> { slug: 'shoes', color: 'red' }
  // params -> { slug: 'shoes' }
 
  // ...
}
```

## Examples[](#examples)

### Sharing components with App Router[](#sharing-components-with-app-router)

`useParams` from `next/navigation` works in both the Pages Router and App Router. This allows you to create shared components that work in either context:

components/breadcrumb.tsx

JavaScriptTypeScript

```
import { useParams } from 'next/navigation'
 
// This component works in both pages/ and app/
export function Breadcrumb() {
  const params = useParams<{ slug: string }>()
 
  if (!params) {
    // Fallback for Pages Router during prerendering
    return <nav>Home / ...</nav>
  }
 
  return <nav>Home / {params.slug}</nav>
}
```

> **Good to know**: When using this component in the App Router, `useParams` never returns `null`, so the fallback branch will not be rendered.

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v13.3.0` | `useParams` introduced. |

Was this helpful?
