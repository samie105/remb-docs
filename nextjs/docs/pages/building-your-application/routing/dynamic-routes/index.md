---
title: "Dynamic Routes"
source: "https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes"
canonical_url: "https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:22:46.594Z"
content_hash: "84ae2285514ad889cfdea52ed5ddc4329069c956f1c11f6bae98d74daf6f1b65"
menu_path: ["Dynamic Routes"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/building-your-application/routing/pages-and-layouts/index.md", "title": "Pages and Layouts"}
nav_next: {"path": "nextjs/docs/pages/building-your-application/routing/linking-and-navigating/index.md", "title": "Linking and Navigating"}
---

# Dynamic Routes

Last updated April 23, 2026

When you don't know the exact segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or [prerendered](../../data-fetching/get-static-paths/index.md) at build time.

## Convention[](#convention)

A Dynamic Segment can be created by wrapping a file or folder name in square brackets: `[segmentName]`. For example, `[id]` or `[slug]`.

Dynamic Segments can be accessed from [`useRouter`](../../../api-reference/functions/use-router/index.md).

## Example[](#example)

For example, a blog could include the following route `pages/blog/[slug].js` where `[slug]` is the Dynamic Segment for blog posts.

```
import { useRouter } from 'next/router'
 
export default function Page() {
  const router = useRouter()
  return <p>Post: {router.query.slug}</p>
}
```

| Route | Example URL | `params` |
| --- | --- | --- |
| `pages/blog/[slug].js` | `/blog/a` | `{ slug: 'a' }` |
| `pages/blog/[slug].js` | `/blog/b` | `{ slug: 'b' }` |
| `pages/blog/[slug].js` | `/blog/c` | `{ slug: 'c' }` |

## Catch-all Segments[](#catch-all-segments)

Dynamic Segments can be extended to **catch-all** subsequent segments by adding an ellipsis inside the brackets `[...segmentName]`.

For example, `pages/shop/[...slug].js` will match `/shop/clothes`, but also `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`, and so on.

| Route | Example URL | `params` |
| --- | --- | --- |
| `pages/shop/[...slug].js` | `/shop/a` | `{ slug: ['a'] }` |
| `pages/shop/[...slug].js` | `/shop/a/b` | `{ slug: ['a', 'b'] }` |
| `pages/shop/[...slug].js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }` |

## Optional Catch-all Segments[](#optional-catch-all-segments)

Catch-all Segments can be made **optional** by including the parameter in double square brackets: `[[...segmentName]]`.

For example, `pages/shop/[[...slug]].js` will **also** match `/shop`, in addition to `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`.

The difference between **catch-all** and **optional catch-all** segments is that with optional, the route without the parameter is also matched (`/shop` in the example above).

| Route | Example URL | `params` |
| --- | --- | --- |
| `pages/shop/[[...slug]].js` | `/shop` | `{ slug: undefined }` |
| `pages/shop/[[...slug]].js` | `/shop/a` | `{ slug: ['a'] }` |
| `pages/shop/[[...slug]].js` | `/shop/a/b` | `{ slug: ['a', 'b'] }` |
| `pages/shop/[[...slug]].js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }` |

## Next Steps

For more information on what to do next, we recommend the following sections

[

### Linking and Navigating

Learn how navigation works in Next.js, and how to use the Link Component and \`useRouter\` hook.

](../linking-and-navigating/index.md)[

### useRouter

Learn more about the API of the Next.js Router, and access the router instance in your page with the useRouter hook.

](../../../api-reference/functions/use-router/index.md)

Was this helpful?
