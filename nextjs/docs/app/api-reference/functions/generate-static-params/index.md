---
title: "generateStaticParams"
source: "https://nextjs.org/docs/app/api-reference/functions/generate-static-params"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/generate-static-params"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:11:44.429Z"
content_hash: "8a4333bda750eeb080f53dfcfff8a7bb7801ef99304f206d90962321f143f318"
menu_path: ["generateStaticParams"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/generate-sitemaps/index.md", "title": "generateSitemaps"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/generate-viewport/index.md", "title": "generateViewport"}
---

# generateStaticParams

Last updated April 15, 2026

The `generateStaticParams` function can be used in combination with [dynamic route segments](/docs/app/api-reference/file-conventions/dynamic-routes) to [**statically generate**](/docs/app/glossary#prerendering) routes at build time instead of on-demand at request time.

`generateStaticParams` can be used with:

*   [Pages](/docs/app/api-reference/file-conventions/page) (`page.tsx`/`page.js`)
*   [Layouts](/docs/app/api-reference/file-conventions/layout) (`layout.tsx`/`layout.js`)
*   [Route Handlers](/docs/app/api-reference/file-conventions/route) (`route.ts`/`route.js`)

app/blog/\[slug\]/page.tsx

TypeScript

JavaScriptTypeScript

```
// Return a list of `params` to populate the [slug] dynamic segment
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())
 
  return posts.map((post) => ({
    slug: post.slug,
  }))
}
 
// Multiple versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // ...
}
```

> **Good to know**:
> 
> *   You can use the [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams) segment config option to control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.
> *   You must return [an empty array from `generateStaticParams`](#all-paths-at-build-time) or utilize [`export const dynamic = 'force-static'`](/docs/app/guides/caching-without-cache-components#dynamic) in order to revalidate (ISR) [paths at runtime](#all-paths-at-runtime).
> *   During `next dev`, `generateStaticParams` will be called when you navigate to a route.
> *   During `next build`, `generateStaticParams` runs before the corresponding Layouts or Pages are generated.
> *   During revalidation (ISR), `generateStaticParams` will not be called again.
> *   `generateStaticParams` replaces the [`getStaticPaths`](/docs/pages/api-reference/functions/get-static-paths) function in the Pages Router.

## Parameters[](#parameters)

`options.params` (optional)

If multiple dynamic segments in a route use `generateStaticParams`, the child `generateStaticParams` function is executed once for each set of `params` the parent generates.

The `params` object contains the populated `params` from the parent `generateStaticParams`, which can be used to [generate the `params` in a child segment](#multiple-dynamic-segments-in-a-route).

## Returns[](#returns)

`generateStaticParams` should return an array of objects where each object represents the populated dynamic segments of a single route.

*   Each property in the object is a dynamic segment to be filled in for the route.
*   The properties name is the segment's name, and the properties value is what that segment should be filled in with.

Example Route

`generateStaticParams` Return Type

`/product/[id]`

`{ id: string }[]`

`/products/[category]/[product]`

`{ category: string, product: string }[]`

`/products/[...slug]`

`{ slug: string[] }[]`

## Single Dynamic Segment[](#single-dynamic-segment)

app/product/\[id\]/page.tsx

TypeScript

JavaScriptTypeScript

```
export function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }, { id: '3' }]
}
 
// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/1
// - /product/2
// - /product/3
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  // ...
}
```

## Multiple Dynamic Segments[](#multiple-dynamic-segments)

app/products/\[category\]/\[product\]/page.tsx

TypeScript

JavaScriptTypeScript

```
export function generateStaticParams() {
  return [
    { category: 'a', product: '1' },
    { category: 'b', product: '2' },
    { category: 'c', product: '3' },
  ]
}
 
// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /products/a/1
// - /products/b/2
// - /products/c/3
export default async function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  const { category, product } = await params
  // ...
}
```

## Catch-all Dynamic Segment[](#catch-all-dynamic-segment)

app/product/\[...slug\]/page.tsx

TypeScript

JavaScriptTypeScript

```
export function generateStaticParams() {
  return [{ slug: ['a', '1'] }, { slug: ['b', '2'] }, { slug: ['c', '3'] }]
}
 
// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/a/1
// - /product/b/2
// - /product/c/3
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string[] }>
}) {
  const { slug } = await params
  // ...
}
```

## Examples[](#examples)

### Prerendering[](#prerendering)

#### All paths at build time[](#all-paths-at-build-time)

To statically render all paths at build time, supply the full list of paths to `generateStaticParams`:

app/blog/\[slug\]/page.tsx

TypeScript

JavaScriptTypeScript

```
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())
 
  return posts.map((post) => ({
    slug: post.slug,
  }))
}
```

#### Subset of paths at build time[](#subset-of-paths-at-build-time)

To statically render a subset of paths at build time, and the rest the first time they're visited at runtime, return a partial list of paths:

app/blog/\[slug\]/page.tsx

TypeScript

JavaScriptTypeScript

```
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())
 
  // Render the first 10 posts at build time
  return posts.slice(0, 10).map((post) => ({
    slug: post.slug,
  }))
}
```

Then, by using the [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams) segment config option, you can control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.

app/blog/\[slug\]/page.tsx

TypeScript

JavaScriptTypeScript

```
// All posts besides the top 10 will be a 404
export const dynamicParams = false
 
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())
  const topPosts = posts.slice(0, 10)
 
  return topPosts.map((post) => ({
    slug: post.slug,
  }))
}
```

#### All paths at runtime[](#all-paths-at-runtime)

To statically render all paths the first time they're visited, return an empty array (no paths will be rendered at build time) or utilize [`export const dynamic = 'force-static'`](/docs/app/guides/caching-without-cache-components#dynamic):

app/blog/\[slug\]/page.js

```
export async function generateStaticParams() {
  return []
}
```

> **Good to know:**
> 
> *   You must always return an array from `generateStaticParams`, even if it's empty. Otherwise, the route will be dynamically rendered.

app/changelog/\[slug\]/page.js

```
export const dynamic = 'force-static'
```

#### With Cache Components[](#with-cache-components)

When using [Cache Components](/docs/app/getting-started/caching) with dynamic routes, `generateStaticParams` must return **at least one param**. Empty arrays cause a [build error](/docs/messages/empty-generate-static-params). This allows Cache Components to validate your route doesn't incorrectly access `cookies()`, `headers()`, or `searchParams` at runtime.

> **Good to know**: If you don't know the actual param values at build time, you can return a placeholder param (e.g., `[{ slug: '__placeholder__' }]`) for validation, then handle it in your page with `notFound()`. However, this prevents build time validation from working effectively and may cause runtime errors.

See the [dynamic routes section](/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components) for detailed walkthroughs.

### With Route Handlers[](#with-route-handlers)

You can use `generateStaticParams` with [Route Handlers](/docs/app/api-reference/file-conventions/route) to statically generate API responses at build time:

app/api/posts/\[id\]/route.ts

TypeScript

JavaScriptTypeScript

```
export async function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }, { id: '3' }]
}
 
export async function GET(
  request: Request,
  { params }: RouteContext<'/api/posts/[id]'>
) {
  const { id } = await params
  // This will be statically generated for IDs 1, 2, and 3
  return Response.json({ id, title: `Post ${id}` })
}
```

### Route Handlers with Cache Components[](#route-handlers-with-cache-components)

When using [Cache Components](/docs/app/getting-started/caching), combine with `use cache` for optimal caching:

app/api/posts/\[id\]/route.ts

```
export async function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }, { id: '3' }]
}
 
async function getPost(id: Promise<string>) {
  'use cache'
  const resolvedId = await id
  const response = await fetch(`https://api.example.com/posts/${resolvedId}`)
  return response.json()
}
 
export async function GET(
  request: Request,
  { params }: RouteContext<'/api/posts/[id]'>
) {
  const post = await getPost(params.then((p) => p.id))
  return Response.json(post)
}
```

See the [Route Handlers documentation](/docs/app/api-reference/file-conventions/route#static-generation-with-generatestaticparams) for more details.

### Disable rendering for unspecified paths[](#disable-rendering-for-unspecified-paths)

To prevent unspecified paths from being prerendered at runtime, add the `export const dynamicParams = false` option in a route segment. When this config option is used, only paths provided by `generateStaticParams` will be served, and unspecified routes will 404 or match (in the case of [catch-all routes](/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)).

### Multiple Dynamic Segments in a Route[](#multiple-dynamic-segments-in-a-route)

You can generate params for dynamic segments above the current layout or page, but **not below**. For example, given the `app/products/[category]/[product]` route:

*   `app/products/[category]/[product]/page.js` can generate params for **both** `[category]` and `[product]`.
*   `app/products/[category]/layout.js` can **only** generate params for `[category]`.

There are two approaches to generating params for a route with multiple dynamic segments:

#### Generate params from the bottom up[](#generate-params-from-the-bottom-up)

Generate multiple dynamic segments from the child route segment.

app/products/\[category\]/\[product\]/page.tsx

TypeScript

JavaScriptTypeScript

```
// Generate segments for both [category] and [product]
export async function generateStaticParams() {
  const products = await fetch('https://.../products').then((res) => res.json())
 
  return products.map((product) => ({
    category: product.category.slug,
    product: product.id,
  }))
}
 
export default function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  // ...
}
```

#### Generate params from the top down[](#generate-params-from-the-top-down)

Generate the parent segments first and use the result to generate the child segments.

app/products/\[category\]/layout.tsx

TypeScript

JavaScriptTypeScript

```
// Generate segments for [category]
export async function generateStaticParams() {
  const products = await fetch('https://.../products').then((res) => res.json())
 
  return products.map((product) => ({
    category: product.category.slug,
  }))
}
 
export default function Layout({
  params,
}: {
  params: Promise<{ category: string }>
}) {
  // ...
}
```

A child route segment's `generateStaticParams` function is executed once for each segment a parent `generateStaticParams` generates.

The child `generateStaticParams` function can use the `params` returned from the parent `generateStaticParams` function to dynamically generate its own segments.

app/products/\[category\]/\[product\]/page.tsx

TypeScript

JavaScriptTypeScript

```
// Generate segments for [product] using the `params` passed from
// the parent segment's `generateStaticParams` function
export async function generateStaticParams({
  params: { category },
}: {
  params: { category: string }
}) {
  const products = await fetch(
    `https://.../products?category=${category}`
  ).then((res) => res.json())
 
  return products.map((product) => ({
    product: product.id,
  }))
}
 
export default function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  // ...
}
```

Notice that the params argument can be accessed synchronously and includes only parent segment params.

For type completion, you can make use of the TypeScript `Awaited` helper in combination with either [`Page Props helper`](/docs/app/api-reference/file-conventions/page#page-props-helper) or [`Layout Props helper`](/docs/app/api-reference/file-conventions/layout#layout-props-helper):

app/products/\[category\]/\[product\]/page.tsx

TypeScript

JavaScriptTypeScript

```
export async function generateStaticParams({
  params: { category },
}: {
  params: Awaited<LayoutProps<'/products/[category]'>['params']>
}) {
  const products = await fetch(
    `https://.../products?category=${category}`
  ).then((res) => res.json())
 
  return products.map((product) => ({
    product: product.id,
  }))
}
```

> **Good to know**: `fetch` requests are automatically [memoized](/docs/app/glossary#memoization) for the same data across all `generate`\-prefixed functions, Layouts, Pages, and Server Components. React [`cache` can be used](https://react.dev/reference/react/cache) if `fetch` is unavailable.

## Version History[](#version-history)

Version

Changes

`v13.0.0`

`generateStaticParams` introduced.

[Previous

generateSitemaps

](/docs/app/api-reference/functions/generate-sitemaps)

[Next

generateViewport

](/docs/app/api-reference/functions/generate-viewport)

Was this helpful?

supported.

Send
