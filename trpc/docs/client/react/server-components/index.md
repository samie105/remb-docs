---
title: "Set up with React Server Components"
source: "https://trpc.io/docs/client/react/server-components"
canonical_url: "https://trpc.io/docs/client/react/server-components"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:46.190Z"
content_hash: "9f171a1dbfd2c88bce92e48e6e36caeecbbf2ad14245e00b1579f46bcc2082d2"
menu_path: ["Set up with React Server Components"]
section_path: []
nav_prev: {"path": "trpc/docs/client/react/infer-types/index.md", "title": "Inferring Types"}
nav_next: {"path": "trpc/docs/client/react/setup/index.md", "title": "Set up the React Query Integration"}
---

tip

These are the docs for our 'Classic' React Query integration, which (while still supported) is not the recommended way to start new tRPC projects with TanStack React Query. We recommend using the new [TanStack React Query Integration](trpc/docs/client/tanstack-react-query/server-components/index.md) instead.

This guide is an overview of how one may use tRPC with a React Server Components (RSC) framework such as Next.js App Router. Be aware that RSC on its own solves a lot of the same problems tRPC was designed to solve, so you may not need tRPC at all.

There is also not a one-size-fits-all way to integrate tRPC with RSCs, so see this guide as a starting point and adjust it to your needs and preferences.

caution

Please read React Query's [Advanced Server Rendering](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr) docs before proceeding to understand the different types of server rendering and what footguns to avoid.

## Add tRPC to existing projects[​](#add-trpc-to-existing-projects "Direct link to Add tRPC to existing projects")

### 1\. Install deps[​](#1-install-deps "Direct link to 1. Install deps")

*   npm
*   yarn
*   pnpm
*   bun
*   deno

npm install @trpc/server @trpc/client @trpc/react-query @tanstack/react-query@latest zod client-only server-only

### 2\. Create a tRPC router[​](#2-create-a-trpc-router "Direct link to 2. Create a tRPC router")

Initialize your tRPC backend in `trpc/init.ts` using the `initTRPC` function, and create your first router. We're going to make a simple "hello world" router and procedure here - but for deeper information on creating your tRPC API you should refer to the [Quickstart guide](trpc/docs/quickstart/index.md) and [Backend usage docs](trpc/docs/server/overview/index.md) for tRPC information.

info

The file names used here are not enforced by tRPC. You may use any file structure you wish.

View sample backend

### 3\. Create a Query Client factory[​](#3-create-a-query-client-factory "Direct link to 3. Create a Query Client factory")

Create a shared file `trpc/query-client.ts` that exports a function that creates a `QueryClient` instance.

trpc/query-client.ts

ts

`import {`

  `defaultShouldDehydrateQuery,`

  `QueryClient,`

`} from '@tanstack/react-query';`

`import superjson from 'superjson';`

`export function makeQueryClient() {`

  `return new QueryClient({`

    `defaultOptions: {`

      `queries: {`

        `staleTime: 30 * 1000,`

      `},`

      `dehydrate: {`

        `// serializeData: superjson.serialize,`

        `shouldDehydrateQuery: (query) =>`

          `defaultShouldDehydrateQuery(query) ||`

          `query.state.status === 'pending',`

      `},`

      `hydrate: {`

        `// deserializeData: superjson.deserialize,`

      `},`

    `},`

  `});`

`}`

We're setting a few default options here:

*   `staleTime`: With SSR, we usually want to set some default staleTime above 0 to avoid refetching immediately on the client.
*   `shouldDehydrateQuery`: This is a function that determines whether a query should be dehydrated or not. Since the RSC transport protocol supports hydrating promises over the network, we extend the `defaultShouldDehydrateQuery` function to also include queries that are still pending. This will allow us to start prefetching in a server component high up the tree, then consuming that promise in a client component further down.
*   `serializeData` and `deserializeData` (optional): If you set up a [data transformer](trpc/docs/server/data-transformers/index.md) in the previous step, set this option to make sure the data is serialized correctly when hydrating the query client over the server-client boundary.

### 4\. Create a tRPC client for Client Components[​](#4-create-a-trpc-client-for-client-components "Direct link to 4. Create a tRPC client for Client Components")

The `trpc/client.tsx` is the entrypoint when consuming your tRPC API from client components. In here, import the **type definition** of your tRPC router and create typesafe hooks using `createTRPCReact`. We'll also export our context provider from this file.

trpc/client.tsx

tsx

`'use client';`

`// ^-- to make sure we can mount the Provider from a server component`

`import type { QueryClient } from '@tanstack/react-query';`

`import { QueryClientProvider } from '@tanstack/react-query';`

`import { httpBatchLink } from '@trpc/client';`

`import { createTRPCReact } from '@trpc/react-query';`

`import React, { useState } from 'react';`

`import { makeQueryClient } from './query-client';`

`import type { AppRouter } from './routers/_app';`

`export const trpc = createTRPCReact<AppRouter>();`

`let clientQueryClientSingleton: QueryClient;`

`function getQueryClient() {`

  `if (typeof window === 'undefined') {`

    `// Server: always make a new query client`

    `return makeQueryClient();`

  `}`

  `// Browser: use singleton pattern to keep the same query client`

  `return (clientQueryClientSingleton ??= makeQueryClient());`

`}`

`function getUrl() {`

  `const base = (() => {`

    `if (typeof window !== 'undefined') return '';`

    ``if (process.env.VERCEL_URL) return `https://${process.env.VERCEL_URL}`;``

    `return 'http://localhost:3000';`

  `})();`

  ``return `${base}/api/trpc`;``

`}`

`export function TRPCProvider(`

  `props: Readonly<{`

    `children: React.ReactNode;`

  `}>,`

`) {`

  `// NOTE: Avoid useState when initializing the query client if you don't`

  `//       have a suspense boundary between this and the code that may`

  `//       suspend because React will throw away the client on the initial`

  `//       render if it suspends and there is no boundary`

  `const queryClient = getQueryClient();`

  `const [trpcClient] = useState(() =>`

    `trpc.createClient({`

      `links: [`

        `httpBatchLink({`

          `// transformer: superjson, <-- if you use a data transformer`

          `url: getUrl(),`

        `}),`

      `],`

    `}),`

  `);`

  `return (`

    `<trpc.Provider client={trpcClient} queryClient={queryClient}>`

      `<QueryClientProvider client={queryClient}>`

        `{props.children}`

      `</QueryClientProvider>`

    `</trpc.Provider>`

  `);`

`}`

Mount the provider in the root of your application (e.g. `app/layout.tsx` when using Next.js).

### 5\. Create a tRPC caller for Server Components[​](#5-create-a-trpc-caller-for-server-components "Direct link to 5. Create a tRPC caller for Server Components")

To prefetch queries from server components, we use a tRPC caller. The `@trpc/react-query/rsc` module exports a thin wrapper around [`createCaller`](trpc/docs/server/server-side-calls/index.md) that integrates with your React Query client.

trpc/server.tsx

tsx

`import 'server-only'; // <-- ensure this file cannot be imported from the client`

`import { createHydrationHelpers } from '@trpc/react-query/rsc';`

`import { cache } from 'react';`

`import { createCallerFactory, createTRPCContext } from './init';`

`import { makeQueryClient } from './query-client';`

`import { appRouter } from './routers/_app';`

`// IMPORTANT: Create a stable getter for the query client that`

`//            will return the same client during the same request.`

`export const getQueryClient = cache(makeQueryClient);`

`const caller = createCallerFactory(appRouter)(createTRPCContext);`

`export const { trpc, HydrateClient } = createHydrationHelpers<typeof appRouter>(`

  `caller,`

  `getQueryClient,`

`);`

## Using your API[​](#using-your-api "Direct link to Using your API")

Now you can use your tRPC API in your app. While you can use the React Query hooks in client components just like you would in any other React app, we can take advantage of the RSC capabilities by prefetching queries in a server component high up the tree. You may be familiar with this concept as "render as you fetch" commonly implemented as loaders. This means the request fires as soon as possible but without suspending until the data is needed by using the `useQuery` or `useSuspenseQuery` hooks.

app/page.tsx

tsx

`import { trpc, HydrateClient } from '../trpc/server';`

`import { ClientGreeting } from './client-greeting';`

`export default async function Home() {`

  `void trpc.hello.prefetch();`

  `return (`

    `<HydrateClient>`

      `<div>...</div>`

      `{/** ... */}`

      `<ClientGreeting />`

    `</HydrateClient>`

  `);`

`}`

app/client-greeting.tsx

tsx

`'use client';`

`// <-- hooks can only be used in client components`

`import { trpc } from '../trpc/client';`

`export function ClientGreeting() {`

  `const greeting = trpc.hello.useQuery();`

  `if (!greeting.data) return <div>Loading...</div>;`

  `return <div>{greeting.data.greeting}</div>;`

`}`

### Leveraging Suspense[​](#leveraging-suspense "Direct link to Leveraging Suspense")

You may prefer handling loading and error states using Suspense and Error Boundaries. You can do this by using the `useSuspenseQuery` hook.

app/page.tsx

tsx

`import { trpc, HydrateClient } from '../trpc/server';`

`import { Suspense } from 'react';`

`import { ErrorBoundary } from 'react-error-boundary';`

`import { ClientGreeting } from './client-greeting';`

`export default async function Home() {`

  `void trpc.hello.prefetch();`

  `return (`

    `<HydrateClient>`

      `<div>...</div>`

      `{/** ... */}`

      `<ErrorBoundary fallback={<div>Something went wrong</div>}>`

        `<Suspense fallback={<div>Loading...</div>}>`

          `<ClientGreeting />`

        `</Suspense>`

      `</ErrorBoundary>`

    `</HydrateClient>`

  `);`

`}`

app/client-greeting.tsx

tsx

`'use client';`

`import { trpc } from '../trpc/client';`

`export function ClientGreeting() {`

  `const [data] = trpc.hello.useSuspenseQuery();`

  `return <div>{data.greeting}</div>;`

`}`

### Getting data in a server component[​](#getting-data-in-a-server-component "Direct link to Getting data in a server component")

If you need access to the data in a server component, you can invoke the procedure directly instead of using `.prefetch()`, just like you use [the normal server caller](trpc/docs/server/server-side-calls/index.md). Please note that this method is detached from your query client and does not store the data in the cache. This means that you cannot use the data in a server component and expect it to be available in the client. This is intentional and explained in more detail in the [Advanced Server Rendering](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr#data-ownership-and-revalidation) guide.

app/page.tsx

tsx

`import { trpc } from '../trpc/server';`

`export default async function Home() {`

  `` // Use the caller directly without using `.prefetch()` ``

  `const greeting = await trpc.hello();`

  `//    ^? { greeting: string }`

  `return <div>{greeting.greeting}</div>;`

`}`


