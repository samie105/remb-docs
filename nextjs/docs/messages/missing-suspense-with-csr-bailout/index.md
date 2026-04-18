---
title: "Missing Suspense boundary with useSearchParams"
source: "https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout"
canonical_url: "https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:17:54.815Z"
content_hash: "7fd00ad2712a1d4953b5a0b86d85795520971ca3d47573c042f6ff173973b45f"
menu_path: ["Missing Suspense boundary with useSearchParams"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/middleware-upgrade-guide/index.md", "title": "Middleware Upgrade Guide"}
nav_next: {"path": "nextjs/docs/messages/next-dynamic-modules/index.md", "title": "`next/dynamic` has deprecated loading multiple modules at once"}
---

# Missing Suspense boundary with useSearchParams

## Why This Error Occurred[](#why-this-error-occurred)

Reading search parameters through `useSearchParams()` without a Suspense boundary will opt the entire page into client-side rendering. This could cause your page to be blank until the client-side JavaScript has loaded.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

You have a few options depending on your intent:

*   To keep the route statically generated, wrap the smallest subtree that calls `useSearchParams()` in `Suspense`, for example you may move its usage into a child Client Component and render that component wrapped with `Suspense`. This preserves the static shell and avoids a full CSR bailout.
*   To make the route dynamically rendered, use the [`connection`](/docs/app/api-reference/functions/connection) function in a Server Component (e.g. the Page or a wrapping Layout). This waits for an incoming request and excludes everything below from prerendering.

app/page.tsx

TypeScript

JavaScriptTypeScript

```
import { connection } from 'next/server'
 
export default async function Page() {
  await connection()
  return <div>...</div>
}
```

*   Before the `connection` API was available setting `export const dynamic = 'force-dynamic'` in a Server Component `page.tsx`, or `layout.tsx`, opted the route into on-demand rendering. Note that setting `dynamic` in a Client Component (`'use client'`) `page.tsx` has no effect.

app/layout.tsx

TypeScript

JavaScriptTypeScript

```
export const dynamic = 'force-dynamic'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return children
}
```

*   Alternatively, a Server Component Page can pass the `searchParams` value down to Client Components. In a Client Component, you can unwrap it with React's `use()` (ensure a surrounding `Suspense` boundary). See [What to use and when](/docs/app/getting-started/layouts-and-pages#what-to-use-and-when).

app/page.tsx

TypeScript

JavaScriptTypeScript

```
import { Suspense } from 'react'
import ClientSearch from './client-search'
 
export default function Page({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>
}) {
  return (
    <Suspense fallback={<>...</>}>
      <ClientSearch searchParams={searchParams} />
    </Suspense>
  )
}
```

app/client-search.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { use } from 'react'
 
export default function ClientSearch({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>
}) {
  const params = use(searchParams)
  return <div>Query: {params.q}</div>
}
```

*   Consider making the Page a Server Component again and isolating Client-only code (that uses `useSearchParams`) into child Client Components.

app/search.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { useSearchParams } from 'next/navigation'
import { Suspense } from 'react'
 
function Search() {
  const searchParams = useSearchParams()
 
  return <input placeholder="Search..." />
}
 
export function Searchbar() {
  return (
    // You could have a loading skeleton as the `fallback` too
    <Suspense>
      <Search />
    </Suspense>
  )
}
```

## Disabling[](#disabling)

> **Note**: This is only available with Next.js version 14.x. If you're in versions above 14 please fix it with the approach above.

We don't recommend disabling this rule. However, if you need to, you can disable it by setting the `missingSuspenseWithCSRBailout` option to `false` in your `next.config.js`:

next.config.js

```
module.exports = {
  experimental: {
    missingSuspenseWithCSRBailout: false,
  },
}
```

This configuration option will be removed in a future major version.

## Debugging[](#debugging)

If you're having trouble locating where `useSearchParams()` is being used without a Suspense boundary, you can get more detailed stack traces by running:

```
next build --debug-prerender
```

This provides unminified stack traces with source maps, making it easier to pinpoint the exact component and route causing the issue.

## Useful Links[](#useful-links)

*   [`useSearchParams`](/docs/app/api-reference/functions/use-search-params)
*   [`connection`](/docs/app/api-reference/functions/connection)
*   [Debugging prerender errors](/docs/app/api-reference/cli/next#debugging-prerender-errors)

Was this helpful?

supported.

Send


