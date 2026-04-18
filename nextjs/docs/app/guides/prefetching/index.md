---
title: "Prefetching"
source: "https://nextjs.org/docs/app/guides/prefetching"
canonical_url: "https://nextjs.org/docs/app/guides/prefetching"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:15:45.653Z"
content_hash: "d89591ad473965358b373e5efa0913e97421913e64f476b0b1fdbdeee6b17b57"
menu_path: ["Prefetching"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/ppr-platform-guide/index.md", "title": "Implementing Partial Prerendering on your platform"}
nav_next: {"path": "nextjs/docs/app/guides/preserving-ui-state/index.md", "title": "Preserving UI state across navigations"}
---

# Prefetching

Last updated April 15, 2026

Prefetching makes navigating between different routes in your application feel instant. Next.js tries to intelligently prefetch by default, based on the links used in your application code.

This guide will explain how prefetching works and show common implementation patterns:

*   [Automatic prefetch](#automatic-prefetch)
*   [Manual prefetch](#manual-prefetch)
*   [Hover-triggered prefetch](#hover-triggered-prefetch)
*   [Extending or ejecting link](#extending-or-ejecting-link)
*   [Disabled prefetch](#disabled-prefetch)

## How does prefetching work?[](#how-does-prefetching-work)

When navigating between routes, the browser requests assets for the page like HTML and JavaScript files. Prefetching is the process of fetching these resources _ahead_ of time, before you navigate to a new route.

Next.js automatically splits your application into smaller JavaScript chunks based on routes. Instead of loading all the code upfront like traditional SPAs, only the code needed for the current route is loaded. This reduces the initial load time while other parts of the app are loaded in the background. By the time you click the link, the resources for the new route have already been loaded into the browser cache.

When navigating to the new page, there's no full page reload or browser loading spinner. Instead, Next.js performs a [client-side transition](/docs/app/getting-started/linking-and-navigating#client-side-transitions), making the page navigation feel instant.

## Prefetching static vs. dynamic routes[](#prefetching-static-vs-dynamic-routes)

**Static page**

**Dynamic page**

**Prefetched**

Yes, full route

No, unless [`loading.js`](/docs/app/api-reference/file-conventions/loading)

[**Client Cache TTL**](/docs/app/glossary#client-cache)

5 min (default)

Off, unless [enabled](/docs/app/api-reference/config/next-config-js/staleTimes)

**Server roundtrip on click**

No

Yes, streamed after [shell](/docs/app/getting-started/caching)

> **Good to know:** During the initial navigation, the browser fetches the HTML, JavaScript, and React Server Components (RSC) Payload. For subsequent navigations, the browser will fetch the RSC Payload for Server Components and JS bundle for Client Components.

## Automatic prefetch[](#automatic-prefetch)

app/ui/nav-link.tsx

TypeScript

JavaScriptTypeScript

```
import Link from 'next/link'
 
export default function NavLink() {
  return <Link href="/about">About</Link>
}
```

**Context**

**Prefetched payload**

**Client Cache TTL**

No `loading.js`

Entire page

Until app reload

With `loading.js`

Layout to first loading boundary

30s ([configurable](/docs/app/api-reference/config/next-config-js/staleTimes))

Automatic prefetching runs only in production. Disable with `prefetch={false}` or use the wrapper in [Disabled Prefetch](#disabled-prefetch).

## Manual prefetch[](#manual-prefetch)

To do manual prefetching, import the `useRouter` hook from `next/navigation`, and call `router.prefetch()` to warm routes outside the viewport or in response to analytics, hover, scroll, etc.

```
'use client'
 
import { useRouter } from 'next/navigation'
import { CustomLink } from '@components/link'
 
export function PricingCard() {
  const router = useRouter()
 
  return (
    <div onMouseEnter={() => router.prefetch('/pricing')}>
      {/* other UI elements */}
      <CustomLink href="/pricing">View Pricing</CustomLink>
    </div>
  )
}
```

If the intent is to prefetch a URL when a component loads, see the extending or rejecting a link \[example\].

## Hover-triggered prefetch[](#hover-triggered-prefetch)

> **Proceed with caution:** Extending `Link` opts you into maintaining prefetching, cache invalidation, and accessibility concerns. Proceed only if defaults are insufficient.

Next.js tries to do the right prefetching by default, but power users can eject and modify based on their needs. You have the control between performance and resource consumption.

For example, you might have to only trigger prefetches on hover, instead of when entering the viewport (the default behavior):

```
'use client'
 
import Link from 'next/link'
import { useState } from 'react'
 
export function HoverPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const [active, setActive] = useState(false)
 
  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```

`prefetch={null}` restores default (static) prefetching once the user shows intent.

## Extending or ejecting link[](#extending-or-ejecting-link)

You can extend the `<Link>` component to create your own custom prefetching strategy. For example, using the [ForesightJS](https://foresightjs.com/docs/integrations/nextjs) library which prefetches links by predicting the direction of the user's cursor.

Alternatively, you can use [`useRouter`](/docs/app/api-reference/functions/use-router) to recreate some of the native `<Link>` behavior. However, be aware this opts you into maintaining prefetching and cache invalidation.

```
'use client'
 
import { useRouter } from 'next/navigation'
import { useEffect } from 'react'
 
function ManualPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const router = useRouter()
 
  useEffect(() => {
    let cancelled = false
    const poll = () => {
      if (!cancelled) router.prefetch(href, { onInvalidate: poll })
    }
    poll()
    return () => {
      cancelled = true
    }
  }, [href, router])
 
  return (
    <a
      href={href}
      onClick={(event) => {
        event.preventDefault()
        router.push(href)
      }}
    >
      {children}
    </a>
  )
}
```

[`onInvalidate`](/docs/app/api-reference/functions/use-router#userouter) is invoked when Next.js suspects cached data is stale, allowing you to refresh the prefetch.

> **Good to know:** Using an `a` tag will cause a full page navigation to the destination route, you can use `onClick` to prevent the full page navigation, and then invoke `router.push` to navigate to the destination.

## Disabled prefetch[](#disabled-prefetch)

You can fully disable prefetching for certain routes for more fine-grained control over resource consumption.

```
'use client'
 
import Link, { LinkProps } from 'next/link'
 
function NoPrefetchLink({
  prefetch,
  ...rest
}: LinkProps & { children: React.ReactNode }) {
  return <Link {...rest} prefetch={false} />
}
```

For example, you may still want to have consistent usage of `<Link>` in your application, but links in your footer might not need to be prefetched when entering the viewport.

## Prefetching optimizations[](#prefetching-optimizations)

### Client cache[](#client-cache)

Next.js stores prefetched React Server Component payloads in memory, keyed by route segments. When navigating between sibling routes (e.g. `/dashboard/settings` → `/dashboard/analytics`), it reuses the parent layout and only fetches the updated leaf page. This reduces network traffic and improves navigation speed.

### Prefetch scheduling[](#prefetch-scheduling)

Next.js maintains a small task queue, which prefetches in the following order:

1.  Links in the viewport
2.  Links showing user intent (hover or touch)
3.  Newer links replace older ones
4.  Links scrolled off-screen are discarded

The scheduler prioritizes likely navigations while minimizing unused downloads.

### Partial Prerendering (PPR)[](#partial-prerendering-ppr)

When PPR is enabled, a page is divided into a [static shell](/docs/app/guides/streaming#the-static-shell) and a streamed dynamic section:

*   The shell, which can be prefetched, streams immediately
*   Uncached data streams when ready
*   Data invalidations (`revalidateTag`, `revalidatePath`) silently refresh associated prefetches

## Troubleshooting[](#troubleshooting)

### Triggering unwanted side-effects during prefetching[](#triggering-unwanted-side-effects-during-prefetching)

If your layouts or pages are not [pure](https://react.dev/learn/keeping-components-pure#purity-components-as-formulas) and have side-effects (e.g. tracking analytics), these might be triggered when the route is prefetched, not when the user visits the page.

To avoid this, you should move side-effects to a `useEffect` hook or a Server Action triggered from a Client Component.

**Before**:

app/dashboard/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { trackPageView } from '@/lib/analytics'
 
export default function Layout({ children }: { children: React.ReactNode }) {
  // This runs during prefetch
  trackPageView()
 
  return <div>{children}</div>
}
```

**After**:

app/ui/analytics-tracker.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { useEffect } from 'react'
import { trackPageView } from '@/lib/analytics'
 
export function AnalyticsTracker() {
  useEffect(() => {
    trackPageView()
  }, [])
 
  return null
}
```

app/dashboard/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { AnalyticsTracker } from '@/app/ui/analytics-tracker'
 
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <AnalyticsTracker />
      {children}
    </div>
  )
}
```

### Preventing too many prefetches[](#preventing-too-many-prefetches)

Next.js automatically prefetches links in the viewport when using the `<Link>` component.

There may be cases where you want to prevent this to avoid unnecessary usage of resources, such as when rendering a large list of links (e.g. an infinite scroll table).

You can disable prefetching by setting the `prefetch` prop of the `<Link>` component to `false`.

app/ui/no-prefetch-link.tsx

TypeScript

JavaScriptTypeScript

```
<Link prefetch={false} href={`/blog/${post.id}`}>
  {post.title}
</Link>
```

However, this means static routes will only be fetched on click, and dynamic routes will wait for the server to render before navigating.

To reduce resource usage without disabling prefetch entirely, you can defer prefetching until the user hovers over a link. This targets only links the user is likely to visit.

app/ui/hover-prefetch-link.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import Link from 'next/link'
import { useState } from 'react'
 
export function HoverPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const [active, setActive] = useState(false)
 
  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```

[Previous

PPR Platform Guide

](/docs/app/guides/ppr-platform-guide)

[Next

Preserving UI state

](/docs/app/guides/preserving-ui-state)

Was this helpful?

supported.

Send


