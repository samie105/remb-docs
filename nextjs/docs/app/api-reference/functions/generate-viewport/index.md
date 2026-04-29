---
title: "generateViewport"
source: "https://nextjs.org/docs/app/api-reference/functions/generate-viewport"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/generate-viewport"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:10:26.865Z"
content_hash: "d299e2fbb5e9d2ccf9d588a8b44f2dc2c11de540710e7a74b22bfd0497f2cbdf"
menu_path: ["generateViewport"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/generate-static-params/index.md", "title": "generateStaticParams"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/headers/index.md", "title": "headers"}
---

# generateViewport

Last updated April 23, 2026

You can customize the initial viewport of the page with the static `viewport` object or the dynamic `generateViewport` function.

> **Good to know**:
> 
> -   The `viewport` object and `generateViewport` function exports are **only supported in Server Components**.
> -   You cannot export both the `viewport` object and `generateViewport` function from the same route segment.
> -   If you're coming from migrating `metadata` exports, you can use [metadata-to-viewport-export codemod](../../../guides/upgrading/codemods/index.md#metadata-to-viewport-export) to update your changes.

## The `viewport` object[](#the-viewport-object)

To define the viewport options, export a `viewport` object from a `layout.jsx` or `page.jsx` file.

layout.tsx | page.tsx

JavaScriptTypeScript

```
import type { Viewport } from 'next'
 
export const viewport: Viewport = {
  themeColor: 'black',
}
 
export default function Page() {}
```

## `generateViewport` function[](#generateviewport-function)

`generateViewport` should return a [`Viewport` object](#viewport-fields) containing one or more viewport fields.

layout.tsx | page.tsx

JavaScriptTypeScript

```
export function generateViewport({ params }) {
  return {
    themeColor: '...',
  }
}
```

In TypeScript, the `params` argument can be typed via [`PageProps<'/route'>`](../../file-conventions/page/index.md#page-props-helper) or [`LayoutProps<'/route'>`](../../file-conventions/layout/index.md#layout-props-helper) depending on where `generateViewport` is defined.

> **Good to know**:
> 
> -   If the viewport doesn't depend on request information, it should be defined using the static [`viewport` object](#the-viewport-object) rather than `generateViewport`.

## Viewport Fields[](#viewport-fields)

### `themeColor`[](#themecolor)

Learn more about [`theme-color`](https://developer.mozilla.org/docs/Web/HTML/Element/meta/name/theme-color).

**Simple theme color**

layout.tsx | page.tsx

JavaScriptTypeScript

```
import type { Viewport } from 'next'
 
export const viewport: Viewport = {
  themeColor: 'black',
}
```

<head> output

```
<meta name="theme-color" content="black" />
```

**With media attribute**

layout.tsx | page.tsx

JavaScriptTypeScript

```
import type { Viewport } from 'next'
 
export const viewport: Viewport = {
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: 'cyan' },
    { media: '(prefers-color-scheme: dark)', color: 'black' },
  ],
}
```

<head> output

```
<meta name="theme-color" media="(prefers-color-scheme: light)" content="cyan" />
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="black" />
```

### `width`, `initialScale`, `maximumScale` and `userScalable`[](#width-initialscale-maximumscale-and-userscalable)

> **Good to know**: The `viewport` meta tag is automatically set, and manual configuration is usually unnecessary as the default is sufficient. However, the information is provided for completeness.

layout.tsx | page.tsx

JavaScriptTypeScript

```
import type { Viewport } from 'next'
 
export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  // Also supported but less commonly used
  // interactiveWidget: 'resizes-visual',
}
```

<head> output

```
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
/>
```

### `colorScheme`[](#colorscheme)

Learn more about [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta/name#:~:text=color%2Dscheme%3A%20specifies,of%20the%20following%3A).

layout.tsx | page.tsx

JavaScriptTypeScript

```
import type { Viewport } from 'next'
 
export const viewport: Viewport = {
  colorScheme: 'dark',
}
```

<head> output

```
<meta name="color-scheme" content="dark" />
```

## With Cache Components[](#with-cache-components)

When [Cache Components](../../../getting-started/caching/index.md) is enabled, `generateViewport` follows the same rules as other components. If viewport accesses runtime data (`cookies()`, `headers()`, `params`, `searchParams`) or performs uncached data fetching, it defers to request time.

Unlike metadata, viewport cannot be streamed because it affects initial page load UI. If `generateViewport` defers to request time, the page would need to block until resolved.

If viewport depends on external data but not runtime data, use `use cache`:

app/layout.tsx

```
export async function generateViewport() {
  'use cache'
  const { width, initialScale } = await db.query('viewport-size')
  return { width, initialScale }
}
```

If viewport genuinely requires runtime data, wrap the document `<body>` in a Suspense boundary to signal that the entire route should be dynamic:

app/layout.tsx

```
import { Suspense } from 'react'
import { cookies } from 'next/headers'
 
export async function generateViewport() {
  const cookieJar = await cookies()
  return {
    themeColor: cookieJar.get('theme-color')?.value,
  }
}
 
export default function RootLayout({ children }) {
  return (
    <Suspense>
      <html>
        <body>{children}</body>
      </html>
    </Suspense>
  )
}
```

Caching is preferred because it allows static shell generation. Wrapping the document `body` in Suspense means there is no static shell or content to immediately send when a request arrives, making the entire route block until ready on every request.

> **Good to know**: Use [multiple root layouts](../../file-conventions/layout/index.md#root-layout) to isolate fully dynamic viewport to specific routes, while still letting other routes in your application generate a static shell.

## Types[](#types)

You can add type safety to your viewport object by using the `Viewport` type. If you are using the [built-in TypeScript plugin](../../config/typescript/index.md) in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.

### `viewport` object[](#viewport-object)

```
import type { Viewport } from 'next'
 
export const viewport: Viewport = {
  themeColor: 'black',
}
```

### `generateViewport` function[](#generateviewport-function-1)

#### Regular function[](#regular-function)

```
import type { Viewport } from 'next'
 
export function generateViewport(): Viewport {
  return {
    themeColor: 'black',
  }
}
```

#### With segment props[](#with-segment-props)

```
import type { Viewport } from 'next'
 
type Props = {
  params: Promise<{ id: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}
 
export function generateViewport({ params, searchParams }: Props): Viewport {
  return {
    themeColor: 'black',
  }
}
 
export default function Page({ params, searchParams }: Props) {}
```

#### JavaScript Projects[](#javascript-projects)

For JavaScript projects, you can use JSDoc to add type safety.

```
/** @type {import("next").Viewport} */
export const viewport = {
  themeColor: 'black',
}
```

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v14.0.0` | `viewport` and `generateViewport` introduced. |

## Next Steps

View all the Metadata API options.

[

### Metadata Files

API documentation for the metadata file conventions.

](../../file-conventions/metadata/index.md)[

### Caching

Learn how to cache data and UI in Next.js

](../../../getting-started/caching/index.md)[

### cacheComponents

Learn how to enable the cacheComponents flag in Next.js.

](../../config/next-config-js/cacheComponents/index.md)

Was this helpful?
