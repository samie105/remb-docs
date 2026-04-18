---
title: "Next.js Integration"
source: "https://trpc.io/docs/client/nextjs"
canonical_url: "https://trpc.io/docs/client/nextjs"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:29.737Z"
content_hash: "c485c6f9d7fd8072b9e2ae315dece5233bcf35a77ecb790ffe4d610dad564771"
menu_path: ["Next.js Integration"]
section_path: []
---
## tRPC + Next.js[​](#trpc--nextjs "Direct link to tRPC + Next.js")

Next.js makes it easy to build a client and server together in one codebase. tRPC makes it easy to share types between them, ensuring typesafety for your application's data fetching.

tRPC provides first-class support for both the **App Router** and the **Pages Router**. Choose the guide that matches your project:

## App Router[​](#app-router "Direct link to App Router")

The recommended approach for new Next.js projects. Uses React Server Components, the [fetch adapter](https://trpc.io/docs/server/adapters/fetch), and [`@trpc/tanstack-react-query`](https://trpc.io/docs/client/tanstack-react-query).

Key features:

*   **Server Components** - Prefetch data on the server and stream it to the client
*   **Streaming** - Leverage Next.js streaming for optimal loading performance
*   **Suspense** - Use `useSuspenseQuery` with Suspense boundaries for loading states

**[Get started with App Router →](https://trpc.io/docs/client/nextjs/app-router-setup)**

## Pages Router[​](#pages-router "Direct link to Pages Router")

Uses `@trpc/next` which provides a higher-order component (HOC) and integrated hooks for the Pages Router data-fetching patterns.

Key features:

*   **Server-side rendering** - Render pages on the server and hydrate them on the client. Read more about [SSR](https://trpc.io/docs/client/nextjs/pages-router/ssr).
*   **Static site generation** - Prefetch queries on the server and generate static HTML files. Read more about [SSG](https://trpc.io/docs/client/nextjs/pages-router/ssg).
*   **Automatic Provider Wrapping** - `@trpc/next` provides a HOC that wraps your app with the necessary providers automatically.

**[Get started with Pages Router →](https://trpc.io/docs/client/nextjs/pages-router/setup)**

## Choosing between App Router and Pages Router[​](#choosing-between-app-router-and-pages-router "Direct link to Choosing between App Router and Pages Router")

App Router

Pages Router

**Recommended for**

New projects

Existing Pages Router projects

**Data fetching**

Server Components, `prefetchQuery`

`getServerSideProps`, `getStaticProps`, SSR via HOC

**Server adapter**

[Fetch adapter](https://trpc.io/docs/server/adapters/fetch)

[Next.js adapter](https://trpc.io/docs/server/adapters/nextjs)

**Client package**

`@trpc/tanstack-react-query`

`@trpc/next` + `@trpc/react-query`

**Provider setup**

Manual `QueryClientProvider` + `TRPCProvider`

Automatic via `withTRPC()` HOC

tip

If you're starting a new project, we recommend the App Router. If you have an existing Pages Router project, the Pages Router integration works well and is fully supported.
