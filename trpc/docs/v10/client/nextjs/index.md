---
title: "Next.js Integration"
source: "https://trpc.io/docs/v10/client/nextjs"
canonical_url: "https://trpc.io/docs/v10/client/nextjs"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:44.434Z"
content_hash: "5366637a7991adcddb6ac6b962800e99209a5e2d513b4fb2576ec330cc020497"
menu_path: ["Next.js Integration"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/links/splitLink/index.md", "title": "Split Link"}
nav_next: {"path": "trpc/docs/v10/client/nextjs/aborting-procedure-calls/index.md", "title": "Aborting Procedure Calls"}
---

Version: 10.x

### tRPC ❤️ Next.js[​](#trpc-️-nextjs "Direct link to tRPC ❤️ Next.js")

Next.js makes it easy to build a client and server together in one codebase. tRPC makes it easy to share types between them, ensuring typesafety for your application's data fetching.

Our Next.js integration is built on top of our [React Query Integration](trpc/docs/v10/index.md) with some Next.js specific APIs, to handle both client and server side rendering.

When using the Next.js integration, you'll get the following features:

*   **Server-side rendering** - You can tell tRPC to render your pages on the server, and then hydrate them on the client. This way, you'll avoid an initial loading state, although time to first byte will be blocked by the server. Read more about [Server-side rendering](trpc/docs/v10/client/nextjs/ssr/index.md).
*   **Static site generation** - Prefetch queries on the server and generate static HTML files that are ready to be served. Read more about [Static site generation](trpc/docs/v10/client/nextjs/ssg/index.md).
*   **Automatic Provider Wrapping** - `@trpc/next` provides a higher-order component (HOC) that wraps your app with the necessary providers so you don't have to do it yourself.

tip

If you're using tRPC in a new project, consider using one of the example projects for reference: [tRPC Example Projects](trpc/docs/example-apps/index.md)


