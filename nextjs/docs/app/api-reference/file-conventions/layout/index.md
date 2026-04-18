---
title: "layout.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/layout"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/layout"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:04.751Z"
content_hash: "1fd20e1621a8c1889f456a8dbcaa6edba178a1e5412b8d1afc49d443babdc2e7"
menu_path: ["layout.js"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/intercepting-routes/index.md", "title": "Intercepting Routes"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/loading/index.md", "title": "loading.js"}
---

# layout.js

Last updated April 15, 2026

The `layout` file is used to define a layout in your Next.js application.

app/dashboard/layout.tsx

TypeScript

JavaScriptTypeScript

```
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}
```

In the [component hierarchy](/docs/app/getting-started/project-structure#component-hierarchy), `layout.js` is the outermost component in a route segment. It wraps `template.js`, `error.js`, `loading.js`, `not-found.js`, and `page.js`.

A **root layout** is the top-most layout in the root `app` directory. It is used to define the `<html>` and `<body>` tags and other globally shared UI.

app/layout.tsx

TypeScript

JavaScriptTypeScript

```
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

## Reference[](#reference)

### Props[](#props)

#### `children` (required)[](#children-required)

Layout components should accept and use a `children` prop. During rendering, `children` will be populated with the route segments the layout is wrapping. These will primarily be the component of a child [Layout](/docs/app/api-reference/file-conventions/page) (if it exists) or [Page](/docs/app/api-reference/file-conventions/page), but could also be other special files like [Loading](/docs/app/api-reference/file-conventions/loading) or [Error](/docs/app/getting-started/error-handling) when applicable.

#### `params` (optional)[](#params-optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes) object from the root segment down to that layout.

app/dashboard/\[team\]/layout.tsx

TypeScript

JavaScriptTypeScript

```
export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ team: string }>
}) {
  const { team } = await params
}
```

Example Route

URL

`params`

`app/dashboard/[team]/layout.js`

`/dashboard/1`

`Promise<{ team: '1' }>`

`app/shop/[tag]/[item]/layout.js`

`/shop/1/2`

`Promise<{ tag: '1', item: '2' }>`

`app/blog/[...slug]/layout.js`

`/blog/1/2`

`Promise<{ slug: ['1', '2'] }>`

*   Since the `params` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
    *   In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.

### Layout Props Helper[](#layout-props-helper)

You can type layouts with `LayoutProps` to get a strongly typed `params` and named slots inferred from your directory structure. `LayoutProps` is a globally available helper.

app/dashboard/layout.tsx

```
export default function Layout(props: LayoutProps<'/dashboard'>) {
  return (
    <section>
      {props.children}
      {/* If you have app/dashboard/@analytics, it appears as a typed slot: */}
      {/* {props.analytics} */}
    </section>
  )
}
```

> **Good to know**:
> 
> *   Types are generated during `next dev`, `next build` or `next typegen`.
> *   After type generation, the `LayoutProps` helper is globally available. It doesn't need to be imported.

### Root Layout[](#root-layout)

The `app` directory **must** include a **root layout**, which is the top-most layout in the root `app` directory. Typically, the root layout is `app/layout.js`.

app/layout.tsx

TypeScript

JavaScriptTypeScript

```
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>{children}</body>
    </html>
  )
}
```

*   The root layout **must** define `<html>` and `<body>` tags.
    *   You should **not** manually add `<head>` tags such as `<title>` and `<meta>` to root layouts. Instead, you should use the [Metadata API](/docs/app/getting-started/metadata-and-og-images) which automatically handles advanced requirements such as streaming and de-duplicating `<head>` elements.
*   You can create **multiple root layouts**. Any layout without a `layout.js` above it is a root layout. Two common approaches:
    *   Using [route groups](/docs/app/api-reference/file-conventions/route-groups) like `app/(shop)/layout.js` and `app/(marketing)/layout.js`
    *   Omitting `app/layout.js` so layouts in subdirectories like `app/dashboard/layout.js` and `app/blog/layout.js` each become root layouts for their respective directories.
    *   Navigating **across multiple root layouts** will cause a **full page load** (as opposed to a client-side navigation).
*   The root layout can be under a **dynamic segment**, for example when implementing [internationalization](/docs/app/guides/internationalization) with `app/[lang]/layout.js`.

## Caveats[](#caveats)

### Request Object[](#request-object)

Layouts are cached in the client during navigation to avoid unnecessary server requests.

[Layouts](/docs/app/api-reference/file-conventions/layout) do not rerender. They can be cached and reused to avoid unnecessary computation when navigating between pages. By restricting layouts from accessing the raw request, Next.js can prevent the execution of potentially slow or expensive user code within the layout, which could negatively impact performance.

To access the request object, you can use [`headers`](/docs/app/api-reference/functions/headers) and [`cookies`](/docs/app/api-reference/functions/cookies) APIs in [Server Components](/docs/app/getting-started/server-and-client-components) and Functions.

app/shop/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { cookies } from 'next/headers'
 
export default async function Layout({ children }) {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

### Query params[](#query-params)

Layouts do not rerender on navigation, so they cannot access search params which would otherwise become stale.

To access updated query parameters, you can use the Page [`searchParams`](/docs/app/api-reference/file-conventions/page#searchparams-optional) prop, or read them inside a Client Component using the [`useSearchParams`](/docs/app/api-reference/functions/use-search-params) hook. Since Client Components re-render on navigation, they have access to the latest query parameters.

app/ui/search.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { useSearchParams } from 'next/navigation'
 
export default function Search() {
  const searchParams = useSearchParams()
 
  const search = searchParams.get('search')
 
  return '...'
}
```

app/shop/layout.tsx

TypeScript

JavaScriptTypeScript

```
import Search from '@/app/ui/search'
 
export default function Layout({ children }) {
  return (
    <>
      <Search />
      {children}
    </>
  )
}
```

### Pathname[](#pathname)

Layouts do not re-render on navigation, so they do not access pathname which would otherwise become stale.

To access the current pathname, you can read it inside a Client Component using the [`usePathname`](/docs/app/api-reference/functions/use-pathname) hook. Since Client Components re-render during navigation, they have access to the latest pathname.

app/ui/breadcrumbs.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { usePathname } from 'next/navigation'
 
// Simplified breadcrumbs logic
export default function Breadcrumbs() {
  const pathname = usePathname()
  const segments = pathname.split('/')
 
  return (
    <nav>
      {segments.map((segment, index) => (
        <span key={index}>
          {' > '}
          {segment}
        </span>
      ))}
    </nav>
  )
}
```

app/docs/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { Breadcrumbs } from '@/app/ui/Breadcrumbs'
 
export default function Layout({ children }) {
  return (
    <>
      <Breadcrumbs />
      <main>{children}</main>
    </>
  )
}
```

### Interaction with `loading.js`[](#interaction-with-loadingjs)

Because `loading.js` sits below `layout.js` in the [component hierarchy](/docs/app/getting-started/project-structure#component-hierarchy), it cannot show a fallback for uncached or runtime data access in the layout itself, such as calling [`cookies()`](/docs/app/api-reference/functions/cookies), [`headers()`](/docs/app/api-reference/functions/headers), or making uncached fetches.

The behavior depends on whether [Cache Components](/docs/app/getting-started/caching) is enabled:

*   **Without Cache Components:** The navigation will block until the layout finishes rendering, and the `loading.js` fallback will not be shown.
*   **With Cache Components:** `loading.js` is treated as a regular `<Suspense>` boundary rather than a special prefetch marker. Uncached or runtime data access in the layout must be explicitly wrapped in its own `<Suspense>` boundary, otherwise Next.js guides you with a build-time error. The static shell streams immediately, and the uncached content swaps in as it resolves.

In both cases, to ensure instant navigation, either:

*   Wrap runtime data access in your layout in its own `<Suspense>` boundary with a fallback.
*   Move uncached data fetching from `layout.js` into `page.js` where `loading.js` can show a fallback.

app/dashboard/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { Suspense } from 'react'
import { NavSkeleton } from './nav-skeleton'
import { DashboardNav } from './dashboard-nav'
 
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <Suspense fallback={<NavSkeleton />}>
        <DashboardNav />
      </Suspense>
      <main>{children}</main>
    </>
  )
}
```

### Fetching Data[](#fetching-data)

Layouts cannot pass data to their `children`. However, you can fetch the same data in a route more than once, and use React [`cache`](https://react.dev/reference/react/cache) to dedupe the requests without affecting performance.

Alternatively, when using [`fetch`](/docs/app/api-reference/functions/fetch)in Next.js, requests are automatically deduped.

app/lib/data.ts

TypeScript

JavaScriptTypeScript

```
export async function getUser(id: string) {
  const res = await fetch(`https://.../users/${id}`)
  return res.json()
}
```

app/dashboard/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { getUser } from '@/app/lib/data'
import { UserName } from '@/app/ui/user-name'
 
export default async function Layout({ children }) {
  const user = await getUser('1')
 
  return (
    <>
      <nav>
        {/* ... */}
        <UserName user={user.name} />
      </nav>
      {children}
    </>
  )
}
```

app/dashboard/page.tsx

TypeScript

JavaScriptTypeScript

```
import { getUser } from '@/app/lib/data'
import { UserName } from '@/app/ui/user-name'
 
export default async function Page() {
  const user = await getUser('1')
 
  return (
    <div>
      <h1>Welcome {user.name}</h1>
    </div>
  )
}
```

### Accessing child segments[](#accessing-child-segments)

Layouts do not have access to the route segments below itself. To access all route segments, you can use [`useSelectedLayoutSegment`](/docs/app/api-reference/functions/use-selected-layout-segment) or [`useSelectedLayoutSegments`](/docs/app/api-reference/functions/use-selected-layout-segments) in a Client Component.

app/ui/nav-link.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'
 
export default function NavLink({
  slug,
  children,
}: {
  slug: string
  children: React.ReactNode
}) {
  const segment = useSelectedLayoutSegment()
  const isActive = slug === segment
 
  return (
    <Link
      href={`/blog/${slug}`}
      // Change style depending on whether the link is active
      style={{ fontWeight: isActive ? 'bold' : 'normal' }}
    >
      {children}
    </Link>
  )
}
```

app/blog/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { NavLink } from './nav-link'
import getPosts from './get-posts'
 
export default async function Layout({
  children,
}: {
  children: React.ReactNode
}) {
  const featuredPosts = await getPosts()
  return (
    <div>
      {featuredPosts.map((post) => (
        <div key={post.id}>
          <NavLink slug={post.slug}>{post.title}</NavLink>
        </div>
      ))}
      <div>{children}</div>
    </div>
  )
}
```

## Examples[](#examples)

### Metadata[](#metadata)

You can modify the `<head>` HTML elements such as `title` and `meta` using the [`metadata` object](/docs/app/api-reference/functions/generate-metadata#the-metadata-object) or [`generateMetadata` function](/docs/app/api-reference/functions/generate-metadata#generatemetadata-function).

app/layout.tsx

TypeScript

JavaScriptTypeScript

```
import type { Metadata } from 'next'
 
export const metadata: Metadata = {
  title: 'Next.js',
}
 
export default function Layout({ children }: { children: React.ReactNode }) {
  return '...'
}
```

> **Good to know**: You should **not** manually add `<head>` tags such as `<title>` and `<meta>` to root layouts. Instead, use the [Metadata APIs](/docs/app/api-reference/functions/generate-metadata) which automatically handles advanced requirements such as streaming and de-duplicating `<head>` elements.

### Active Nav Links[](#active-nav-links)

You can use the [`usePathname`](/docs/app/api-reference/functions/use-pathname) hook to determine if a nav link is active.

Since `usePathname` is a client hook, you need to extract the nav links into a Client Component, which can be imported into your layout:

app/ui/nav-links.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { usePathname } from 'next/navigation'
import Link from 'next/link'
 
export function NavLinks() {
  const pathname = usePathname()
 
  return (
    <nav>
      <Link className={`link ${pathname === '/' ? 'active' : ''}`} href="/">
        Home
      </Link>
 
      <Link
        className={`link ${pathname === '/about' ? 'active' : ''}`}
        href="/about"
      >
        About
      </Link>
    </nav>
  )
}
```

app/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { NavLinks } from '@/app/ui/nav-links'
 
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <NavLinks />
        <main>{children}</main>
      </body>
    </html>
  )
}
```

### Displaying content based on `params`[](#displaying-content-based-on-params)

Using [dynamic route segments](/docs/app/api-reference/file-conventions/dynamic-routes), you can display or fetch specific content based on the `params` prop.

app/dashboard/layout.tsx

TypeScript

JavaScriptTypeScript

```
export default async function DashboardLayout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ team: string }>
}) {
  const { team } = await params
 
  return (
    <section>
      <header>
        <h1>Welcome to {team}'s Dashboard</h1>
      </header>
      <main>{children}</main>
    </section>
  )
}
```

### Reading `params` in Client Components[](#reading-params-in-client-components)

To use `params` in a Client Component (which cannot be `async`), you can use React's [`use`](https://react.dev/reference/react/use) function to read the promise:

app/page.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { use } from 'react'
 
export default function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = use(params)
}
```

## Version History[](#version-history)

Version

Changes

`v15.0.0-RC`

`params` is now a promise. A [codemod](/docs/app/guides/upgrading/codemods#150) is available.

`v13.0.0`

`layout` introduced.

[Previous

Intercepting Routes

](/docs/app/api-reference/file-conventions/intercepting-routes)

[Next

loading.js

](/docs/app/api-reference/file-conventions/loading)

Was this helpful?

supported.

Send
