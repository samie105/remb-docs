---
title: "loading.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/loading"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/loading"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:08:47.611Z"
content_hash: "6c76fe6d4dd42c832a8fecf1b636d88497123224b582e34aebbaf1ded9401546"
menu_path: ["loading.js"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/layout/index.md", "title": "layout.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/mdx-components/index.md", "title": "mdx-components.js"}
---

# loading.js

Last updated April 23, 2026

The special file `loading.js` helps you create meaningful Loading UI with [React Suspense](https://react.dev/reference/react/Suspense). With this convention, you can show an [instant loading state](#instant-loading-states) from the server while the content of a route segment streams in. The new content is automatically swapped in once complete.

![Loading UI](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-ui.png)

app/feed/loading.tsx

JavaScriptTypeScript

```
export default function Loading() {
  // Or a custom loading skeleton component
  return <p>Loading...</p>
}
```

Inside the `loading.js` file, you can add any light-weight loading UI. You may find it helpful to use the [React Developer Tools](https://react.dev/learn/react-developer-tools) to manually toggle Suspense boundaries.

By default, this file is a [Server Component](../../../getting-started/server-and-client-components/index.md) - but can also be used as a Client Component through the `"use client"` directive.

## Reference[](#reference)

### Parameters[](#parameters)

Loading UI components do not accept any parameters.

## Behavior[](#behavior)

-   The Fallback UI is [prefetched](../../../getting-started/linking-and-navigating/index.md#prefetching), making navigation immediate unless prefetching hasn't completed.
-   Navigation is interruptible, meaning changing routes does not need to wait for the content of the route to fully load before navigating to another route.
-   Shared layouts remain interactive while new route segments load.

### Instant Loading States[](#instant-loading-states)

An instant loading state is fallback UI that is shown immediately upon navigation. You can prerender loading indicators such as skeletons and spinners, or a small but meaningful part of future screens such as a cover photo, title, etc. This helps users understand the app is responding and provides a better user experience.

Create a loading state by adding a `loading.js` file inside a folder.

![loading.js special file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-special-file.png)

app/dashboard/loading.tsx

JavaScriptTypeScript

```
export default function Loading() {
  // You can add any UI inside Loading, including a Skeleton.
  return <LoadingSkeleton />
}
```

In the same folder, `loading.js` will be nested inside `layout.js`. It will automatically wrap the `page.js` file and any children below in a `<Suspense>` boundary.

![loading.js overview](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-overview.png)

In the [component hierarchy](../../../getting-started/project-structure/index.md#component-hierarchy), `loading.js` wraps `not-found.js`, `page.js`, and nested `layout.js` files in a `<Suspense>` boundary. It does **not** wrap the `layout.js`, `template.js`, or `error.js` in the same segment.

> **Good to know**: If the layout accesses uncached or runtime data (e.g. `cookies()`, `headers()`, or uncached fetches), `loading.js` will not show a fallback for it.
> 
> -   **Without [Cache Components](../../../getting-started/caching/index.md):** Navigation blocks until the layout finishes rendering.
> -   **With [Cache Components](../../../getting-started/caching/index.md):** Uncached or runtime data access in the layout must be explicitly wrapped in `<Suspense>`, otherwise Next.js guides you with a build-time error. The static shell streams first, and the uncached content fills in.
> 
> To ensure instant navigation, move uncached data fetching from `layout.js` into `page.js`, or wrap the runtime data access in your layout in its own `<Suspense>` boundary. See [layout.js Caveats](../layout/index.md#interaction-with-loadingjs) for details and examples.

### SEO[](#seo)

-   For bots that only scrape static HTML, and cannot execute JavaScript like a full browser, such as Twitterbot, Next.js resolves [`generateMetadata`](../../functions/generate-metadata/index.md) before streaming UI, and metadata is placed in the `<head>` of the initial HTML.
-   Otherwise, [streaming metadata](../../functions/generate-metadata/index.md#streaming-metadata) may be used. Next.js automatically detects user agents to choose between blocking and streaming behavior.
-   Since streaming is server-rendered, it does not impact SEO. You can use the [Rich Results Test](https://search.google.com/test/rich-results) tool from Google to see how your page appears to Google's web crawlers and view the serialized HTML ([source](https://web.dev/rendering-on-the-web/#seo-considerations)).

### Status Codes[](#status-codes)

When streaming, a `200` status code will be returned to signal that the request was successful.

The server can still communicate errors or issues to the client within the streamed content itself, for example, when using [`redirect`](../../functions/redirect/index.md) or [`notFound`](../../functions/not-found/index.md). Because the response headers have already been sent to the client, the status code of the response cannot be updated.

For example, when a 404 page is streamed to the client, Next.js includes a `<meta name="robots" content="noindex">` tag in the streamed HTML. This prevents search engines from indexing that URL even if the HTTP status is 200. See Google’s guidance on the [`robots` meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag).

Some crawlers may label these responses as “soft 404s”. In the streaming case, this does not lead to indexation because the page is explicitly marked `noindex` in the HTML.

If you need a 404 status, for compliance or analytics, ensure the resource exists before the response body is streamed, so that the server can set the HTTP status code.

You can run this check in [`proxy`](../proxy/index.md) to rewrite missing slugs to a not-found route, or [produce a 404 response](../proxy/index.md#producing-a-response). Keep proxy checks fast, and avoid fetching full content there.

**When is the response body streamed?**

The response body starts streaming when a Suspense fallback renders (for example, a `loading.tsx`) or when a Server Component suspends under a `Suspense` boundary. Place `notFound()` before those boundaries and before any `await` that may suspend.

To start streaming, the response headers must be set. This is why it is not possible to change the status code after streaming started.

### Browser limits[](#browser-limits)

[Some browsers](https://bugs.webkit.org/show_bug.cgi?id=252413) buffer a streaming response. You may not see the streamed response until the response exceeds 1024 bytes. This typically only affects “hello world” applications, but not real applications.

## Platform Support[](#platform-support)

| Deployment Option | Supported |
| --- | --- |
| [Node.js server](../../../getting-started/deploying/index.md#nodejs-server) | Yes |
| [Docker container](../../../getting-started/deploying/index.md#docker) | Yes |
| [Static export](../../../getting-started/deploying/index.md#static-export) | No |
| [Adapters](../../../getting-started/deploying/index.md#adapters) | Platform-specific |

Learn how to [configure streaming](../../../guides/self-hosting/index.md#streaming-and-suspense) when self-hosting Next.js.

## Examples[](#examples)

### Streaming with Suspense[](#streaming-with-suspense)

In addition to `loading.js`, you can also manually create Suspense Boundaries for your own UI components. The App Router supports streaming with [Suspense](https://react.dev/reference/react/Suspense). See the [Streaming guide](../../../guides/streaming/index.md) for more on how streaming works, including granular Suspense patterns, Route Handler streaming, and infrastructure considerations.

`<Suspense>` works by wrapping a component that performs an asynchronous action (e.g. fetch data), showing fallback UI (e.g. skeleton, spinner) while it's happening, and then swapping in your component once the action completes.

app/dashboard/page.tsx

JavaScriptTypeScript

```
import { Suspense } from 'react'
import { PostFeed, Weather } from './Components'
 
export default function Posts() {
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        <PostFeed />
      </Suspense>
      <Suspense fallback={<p>Loading weather...</p>}>
        <Weather />
      </Suspense>
    </section>
  )
}
```

By using Suspense, you get the benefits of:

1.  **Streaming Server Rendering** - Progressively rendering HTML from the server to the client.
2.  **Selective Hydration** - React prioritizes what components to make interactive first based on user interaction.

For more Suspense examples and use cases, please see the [React Documentation](https://react.dev/reference/react/Suspense).

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `loading` introduced. |

Was this helpful?
