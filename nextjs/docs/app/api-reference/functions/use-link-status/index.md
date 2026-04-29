---
title: "useLinkStatus"
source: "https://nextjs.org/docs/app/api-reference/functions/use-link-status"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/use-link-status"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:11:09.130Z"
content_hash: "4be84c46572d2a1636102e83e1949f46f1e54bc692b2fddd1610da165012db94"
menu_path: ["useLinkStatus"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/updateTag/index.md", "title": "updateTag"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/use-params/index.md", "title": "useParams"}
---

# useLinkStatus

Last updated April 23, 2026

The `useLinkStatus` hook lets you track the **pending** state of a `<Link>`. Use it for subtle, inline feedback, for example a shimmer effect over the clicked link, while navigation completes. Prefer route-level fallbacks with `loading.js`, and prefetching for instant transitions.

`useLinkStatus` is useful when:

-   [Prefetching](../../../getting-started/linking-and-navigating/index.md#prefetching) is disabled or in progress meaning navigation is blocked.
-   The destination route is dynamic **and** doesn't include a [`loading.js`](../../file-conventions/loading/index.md) file that would allow an instant navigation.

app/hint.tsx

JavaScriptTypeScript

```
'use client'
 
import Link from 'next/link'
import { useLinkStatus } from 'next/link'
 
function Hint() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}
 
export default function Header() {
  return (
    <header>
      <Link href="/dashboard" prefetch={false}>
        <span className="label">Dashboard</span> <Hint />
      </Link>
    </header>
  )
}
```

> **Good to know**:
> 
> -   `useLinkStatus` must be used within a descendant component of a `Link` component
> -   The hook is most useful when `prefetch={false}` is set on the `Link` component
> -   If the linked route has been prefetched, the pending state will be skipped
> -   When clicking multiple links in quick succession, only the last link's pending state is shown
> -   This hook is not supported in the Pages Router and always returns `{ pending: false }`
> -   Inline indicators can easily introduce layout shifts. Prefer a fixed-size, always-rendered hint element and toggle its opacity, or use an animation.

## You might not need `useLinkStatus`[](#you-might-not-need-uselinkstatus)

Before adding inline feedback, consider if:

-   The destination is static and prefetched in production, so the pending phase may be skipped.
-   The route has a `loading.js` file, enabling instant transitions with a route-level fallback.

Navigation is typically fast. Use `useLinkStatus` as a quick patch when you identify a slow transition, then iterate to fix the root cause with prefetching or a `loading.js` fallback.

## Parameters[](#parameters)

```
const { pending } = useLinkStatus()
```

`useLinkStatus` does not take any parameters.

## Returns[](#returns)

`useLinkStatus` returns an object with a single property:

| Property | Type | Description |
| --- | --- | --- |
| pending | boolean | `true` before history updates, `false` after |

## Example[](#example)

### Inline link hint[](#inline-link-hint)

Add a subtle, fixed-size hint that doesn’t affect layout to confirm a click when prefetching hasn’t completed.

app/components/loading-indicator.tsx

JavaScriptTypeScript

```
'use client'
 
import { useLinkStatus } from 'next/link'
 
export default function LoadingIndicator() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}
```

app/shop/layout.tsx

JavaScriptTypeScript

```
import Link from 'next/link'
import LoadingIndicator from './components/loading-indicator'
 
const links = [
  { href: '/shop/electronics', label: 'Electronics' },
  { href: '/shop/clothing', label: 'Clothing' },
  { href: '/shop/books', label: 'Books' },
]
 
function Menubar() {
  return (
    <div>
      {links.map((link) => (
        <Link key={link.label} href={link.href}>
          <span className="label">{link.label}</span> <LoadingIndicator />
        </Link>
      ))}
    </div>
  )
}
 
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <Menubar />
      {children}
    </div>
  )
}
```

If the navigation to a new route is fast, users may see an unnecessary flash of the hint. One way to improve the user experience and only show the hint when the navigation takes time to complete is to add an initial animation delay (e.g. 100ms) and start the animation as invisible (e.g. `opacity: 0`).

app/styles/global.css

```
.link-hint {
  display: inline-block;
  width: 0.6em;
  height: 0.6em;
  margin-left: 0.25rem;
  border-radius: 9999px;
  background: currentColor;
  opacity: 0;
  visibility: hidden; /* reserve space without showing the hint */
}
 
.link-hint.is-pending {
  /* Animation 1: fade in after 100ms and keep final opacity */
  /* Animation 2: subtle pulsing while pending */
  visibility: visible;
  animation-name: fadeIn, pulse;
  animation-duration: 200ms, 1s;
  /* Appear only if navigation actually takes time */
  animation-delay: 100ms, 100ms;
  animation-timing-function: ease, ease-in-out;
  animation-iteration-count: 1, infinite;
  animation-fill-mode: forwards, none;
}
 
@keyframes fadeIn {
  to {
    opacity: 0.35;
  }
}
@keyframes pulse {
  50% {
    opacity: 0.15;
  }
}
```

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v15.3.0` | `useLinkStatus` introduced. |

## Next Steps

Learn more about the features mentioned in this page by reading the API Reference.

[

### Link Component

Enable fast client-side navigation with the built-in \`next/link\` component.

](../../components/link/index.md)[

### loading.js

API reference for the loading.js file.

](../../file-conventions/loading/index.md)

Was this helpful?
