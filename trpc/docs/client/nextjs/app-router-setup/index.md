---
title: "Set up with Next.js App Router"
source: "https://trpc.io/docs/client/nextjs/app-router-setup"
canonical_url: "https://trpc.io/docs/client/nextjs/app-router-setup"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:39.115Z"
content_hash: "b949a55c41b5b9f49cd4d0da9a4e49b9790213bce68f5b5ca1706664d83df076"
menu_path: ["Set up with Next.js App Router"]
section_path: []
---
note

We recommend reading TanStack React Query's [Advanced Server Rendering](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr) docs to understand the different types of server rendering and footguns to avoid.

## Recommended file structure[​](#recommended-file-structure "Direct link to Recommended file structure")

graphql

`.`

`├── src`

`│   ├── app`

`│   │   ├── api`

`│   │   │   └── trpc`

`│   │   │       └── [trpc]`

`│   │   │           └── route.ts  # <-- tRPC HTTP handler`

`│   │   ├── layout.tsx            # <-- mount TRPCReactProvider`

`│   │   └── page.tsx              # <-- server component`

`│   ├── trpc`

`│   │   ├── init.ts               # <-- tRPC server init & context`

`│   │   ├── routers`

`│   │   │   ├── _app.ts           # <-- main app router`

`│   │   │   ├── post.ts           # <-- sub routers`

`│   │   │   └── [..]`

`│   │   ├── client.tsx            # <-- client hooks & provider`

`│   │   ├── query-client.ts       # <-- shared QueryClient factory`

`│   │   └── server.tsx            # <-- server-side caller`

`│   └── [..]`

`└── [..]`

## Add tRPC to an existing Next.js App Router project[​](#add-trpc-to-an-existing-nextjs-app-router-project "Direct link to Add tRPC to an existing Next.js App Router project")

### 1\. Install deps[​](#1-install-deps "Direct link to 1. Install deps")

*   npm
*   yarn
*   pnpm
*   bun
*   deno

npm install @trpc/server @trpc/client @trpc/tanstack-react-query @tanstack/react-query@latest zod client-only server-only

AI Agents

If you use an AI coding agent, install tRPC skills for better code generation:

bash

`npx @tanstack/intent@latest install`

### 2\. Create a tRPC router[​](#2-create-a-trpc-router "Direct link to 2. Create a tRPC router")

Initialize your tRPC backend in `trpc/init.ts` using the `initTRPC` function, and create your first router. We're going to make a simple "hello world" router and procedure here — for deeper information on creating your tRPC API, refer to the [Quickstart guide](https://trpc.io/docs/quickstart) and [Backend usage docs](https://trpc.io/docs/server/overview).

trpc/init.ts

ts

`import { initTRPC } from '@trpc/server';`

`/**`

 ``* This context creator accepts `headers` so it can be reused in both``

 ``* the RSC server caller (where you pass `next/headers`) and the``

 `* API route handler (where you pass the request headers).`

 `*/`

`export const createTRPCContext = async (opts: { headers: Headers }) => {`

  `// const user = await auth(opts.headers);`

  `return { userId: 'user_123' };`

`};`

`// Avoid exporting the entire t-object`

`// since it's not very descriptive.`

`// For instance, the use of a t variable`

`// is common in i18n libraries.`

`const t = initTRPC`

  `.context<Awaited<ReturnType<typeof createTRPCContext>>>()`

  `.create({`

    `/**`

     `* @see https://trpc.io/docs/server/data-transformers`

     `*/`

    `// transformer: superjson,`

  `});`

`// Base router and procedure helpers`

`export const createTRPCRouter = t.router;`

`export const createCallerFactory = t.createCallerFactory;`

`export const baseProcedure = t.procedure;`

  

trpc/routers/\_app.ts

ts

`import { z } from 'zod';`

`import { baseProcedure, createTRPCRouter } from '../init';`

`export const appRouter = createTRPCRouter({`

  `hello: baseProcedure`

    `.input(`

      `z.object({`

        `text: z.string(),`

      `}),`

    `)`

    `.query((opts) => {`

      `return {`

        ``greeting: `hello ${opts.input.text}`,``

      `};`

    `}),`

`});`

`// export type definition of API`

`export type AppRouter = typeof appRouter;`

### 3\. Create the API route handler[​](#3-create-the-api-route-handler "Direct link to 3. Create the API route handler")

With the App Router, use the [fetch adapter](https://trpc.io/docs/server/adapters/fetch) to handle tRPC requests. Create a route handler that exports both `GET` and `POST`:

app/api/trpc/\[trpc\]/route.ts

ts

`import { fetchRequestHandler } from '@trpc/server/adapters/fetch';`

`import { createTRPCContext } from './trpc/init';`

`import { appRouter } from './trpc/routers/_app';`

`const handler = (req: Request) =>`

  `fetchRequestHandler({`

    `endpoint: '/api/trpc',`

    `req,`

    `router: appRouter,`

    `createContext: () => createTRPCContext({ headers: req.headers }),`

  `});`

`export { handler as GET, handler as POST };`

note

App Router uses the [fetch adapter](https://trpc.io/docs/server/adapters/fetch) (via `fetchRequestHandler`) rather than the Next.js-specific adapter used by the Pages Router. This is because App Router route handlers are based on the Web standard `Request` and `Response` objects.

### 4\. Create a Query Client factory[​](#4-create-a-query-client-factory "Direct link to 4. Create a Query Client factory")

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
*   `serializeData` and `deserializeData` (optional): If you set up a [data transformer](https://trpc.io/docs/server/data-transformers) in the previous step, set this option to make sure the data is serialized correctly when hydrating the query client over the server-client boundary.

### 5\. Create a tRPC client for Client Components[​](#5-create-a-trpc-client-for-client-components "Direct link to 5. Create a tRPC client for Client Components")

The `trpc/client.tsx` is the entrypoint when consuming your tRPC API from client components. In here, import the **type definition** of your tRPC router and create typesafe hooks using `createTRPCContext`. We'll also export our context provider from this file.

trpc/client.tsx

tsx

`'use client';`

`// ^-- to make sure we can mount the Provider from a server component`

`import type { QueryClient } from '@tanstack/react-query';`

`import { QueryClientProvider } from '@tanstack/react-query';`

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import { createTRPCContext } from '@trpc/tanstack-react-query';`

`import { useState } from 'react';`

`import { makeQueryClient } from './query-client';`

`import type { AppRouter } from './routers/_app';`

`export const { TRPCProvider, useTRPC } = createTRPCContext<AppRouter>();`

`let browserQueryClient: QueryClient;`

`function getQueryClient() {`

  `if (typeof window === 'undefined') {`

    `// Server: always make a new query client`

    `return makeQueryClient();`

  `}`

  `// Browser: make a new query client if we don't already have one`

  `// This is very important, so we don't re-make a new client if React`

  `// suspends during the initial render. This may not be needed if we`

  `// have a suspense boundary BELOW the creation of the query client`

  `if (!browserQueryClient) browserQueryClient = makeQueryClient();`

  `return browserQueryClient;`

`}`

`function getUrl() {`

  `const base = (() => {`

    `if (typeof window !== 'undefined') return '';`

    ``if (process.env.VERCEL_URL) return `https://${process.env.VERCEL_URL}`;``

    `return 'http://localhost:3000';`

  `})();`

  ``return `${base}/api/trpc`;``

`}`

`export function TRPCReactProvider(`

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

    `createTRPCClient<AppRouter>({`

      `links: [`

        `httpBatchLink({`

          `// transformer: superjson, <-- if you use a data transformer`

          `url: getUrl(),`

        `}),`

      `],`

    `}),`

  `);`

  `return (`

    `<QueryClientProvider client={queryClient}>`

      `<TRPCProvider trpcClient={trpcClient} queryClient={queryClient}>`

        `{props.children}`

      `</TRPCProvider>`

    `</QueryClientProvider>`

  `);`

`}`

Mount the provider in the root layout of your application:

app/layout.tsx

tsx

`import { TRPCReactProvider } from '~/trpc/client';`

`export default function RootLayout({`

  `children,`

`}: Readonly<{`

  `children: React.ReactNode;`

`}>) {`

  `return (`

    `<html lang="en">`

      `<body>`

        `<TRPCReactProvider>{children}</TRPCReactProvider>`

      `</body>`

    `</html>`

  `);`

`}`

### 6\. Create a tRPC caller for Server Components[​](#6-create-a-trpc-caller-for-server-components "Direct link to 6. Create a tRPC caller for Server Components")

To prefetch queries from server components, we create a proxy from our router. You can also pass in a client if your router is on a separate server.

trpc/server.tsx

tsx

`import 'server-only'; // <-- ensure this file cannot be imported from the client`

`import { createTRPCOptionsProxy } from '@trpc/tanstack-react-query';`

`import { headers } from 'next/headers';`

`import { cache } from 'react';`

`import { createTRPCContext } from './init';`

`import { makeQueryClient } from './query-client';`

`import { appRouter } from './routers/_app';`

`// IMPORTANT: Create a stable getter for the query client that`

`//            will return the same client during the same request.`

`export const getQueryClient = cache(makeQueryClient);`

`export const trpc = createTRPCOptionsProxy({`

  `ctx: async () =>`

    `createTRPCContext({`

      `headers: await headers(),`

    `}),`

  `router: appRouter,`

  `queryClient: getQueryClient,`

`});`

`// If your router is on a separate server, pass a client instead:`

`// createTRPCOptionsProxy({`

`//   client: createTRPCClient({ links: [httpLink({ url: '...' })] }),`

`//   queryClient: getQueryClient,`

`// });`

### 7\. Make API requests[​](#7-make-api-requests "Direct link to 7. Make API requests")

You're all set! You can now prefetch queries in server components and consume them in client components.

#### Prefetching in a Server Component[​](#prefetching-in-a-server-component "Direct link to Prefetching in a Server Component")

app/page.tsx

tsx

`import { dehydrate, HydrationBoundary } from '@tanstack/react-query';`

`import { getQueryClient, trpc } from '~/trpc/server';`

`import { ClientGreeting } from './client-greeting';`

`export default async function Home() {`

  `const queryClient = getQueryClient();`

  `void queryClient.prefetchQuery(`

    `trpc.hello.queryOptions({`

      `text: 'world',`

    `}),`

  `);`

  `return (`

    `<HydrationBoundary state={dehydrate(queryClient)}>`

      `<ClientGreeting />`

    `</HydrationBoundary>`

  `);`

`}`

#### Using data in a Client Component[​](#using-data-in-a-client-component "Direct link to Using data in a Client Component")

app/client-greeting.tsx

tsx

`'use client';`

`// <-- hooks can only be used in client components`

`import { useQuery } from '@tanstack/react-query';`

`import { useTRPC } from '~/trpc/client';`

`export function ClientGreeting() {`

  `const trpc = useTRPC();`

  `const greeting = useQuery(trpc.hello.queryOptions({ text: 'world' }));`

  `if (!greeting.data) return <div>Loading...</div>;`

  `return <div>{greeting.data.greeting}</div>;`

`}`

tip

You can create `prefetch` and `HydrateClient` helper functions to make this more concise:

trpc/server.tsx

tsx

`export function HydrateClient(props: { children: React.ReactNode }) {`

  `const queryClient = getQueryClient();`

  `return (`

    `<HydrationBoundary state={dehydrate(queryClient)}>`

      `{props.children}`

    `</HydrationBoundary>`

  `);`

`}`

`export function prefetch<T extends ReturnType<TRPCQueryOptions<any>>>(`

  `queryOptions: T,`

`) {`

  `const queryClient = getQueryClient();`

  `if (queryOptions.queryKey[1]?.type === 'infinite') {`

    `void queryClient.prefetchInfiniteQuery(queryOptions as any);`

  `} else {`

    `void queryClient.prefetchQuery(queryOptions);`

  `}`

`}`

Then you can use it like this:

tsx

`import { HydrateClient, prefetch, trpc } from '~/trpc/server';`

`import { ClientGreeting } from './client-greeting';`

`function Home() {`

  `prefetch(trpc.hello.queryOptions({ text: 'world' }));`

  `return (`

    `<HydrateClient>`

      `<ClientGreeting />`

    `</HydrateClient>`

  `);`

`}`

## Leveraging Suspense[​](#leveraging-suspense "Direct link to Leveraging Suspense")

You may prefer handling loading and error states using Suspense and Error Boundaries. You can do this by using the `useSuspenseQuery` hook.

app/page.tsx

tsx

`import { HydrateClient, prefetch, trpc } from '~/trpc/server';`

`import { Suspense } from 'react';`

`import { ErrorBoundary } from 'react-error-boundary';`

`import { ClientGreeting } from './client-greeting';`

`export default async function Home() {`

  `prefetch(trpc.hello.queryOptions());`

  `return (`

    `<HydrateClient>`

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

`import { useSuspenseQuery } from '@tanstack/react-query';`

`import { useTRPC } from '~/trpc/client';`

`export function ClientGreeting() {`

  `const trpc = useTRPC();`

  `const { data } = useSuspenseQuery(trpc.hello.queryOptions());`

  `return <div>{data.greeting}</div>;`

`}`

## Getting data in a Server Component[​](#getting-data-in-a-server-component "Direct link to Getting data in a Server Component")

If you need access to the data in a server component, we recommend creating a server caller and using it directly. Please note that this method is detached from your query client and does not store the data in the cache. This means that you cannot use the data in a server component and expect it to be available in the client. This is intentional and explained in more detail in the [Advanced Server Rendering](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr#data-ownership-and-revalidation) guide.

trpc/server.tsx

tsx

`import { headers } from 'next/headers';`

`import { createTRPCContext } from './init';`

`import { appRouter } from './routers/_app';`

`// ...`

`export const caller = appRouter.createCaller(async () =>`

  `createTRPCContext({ headers: await headers() }),`

`);`

app/page.tsx

tsx

`import { caller } from '~/trpc/server';`

`export default async function Home() {`

  `const greeting = await caller.hello();`

           `const greeting: {     greeting: string; }`

  `return <div>{greeting.greeting}</div>;`

`}`

If you **really** need to use the data both on the server as well as inside client components and understand the tradeoffs explained in the [Advanced Server Rendering](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr#data-ownership-and-revalidation) guide, you can use `fetchQuery` instead of `prefetch` to have the data both on the server as well as hydrating it down to the client:

app/page.tsx

tsx

`import { getQueryClient, HydrateClient, trpc } from '~/trpc/server';`

`import { ClientGreeting } from './client-greeting';`

`export default async function Home() {`

  `const queryClient = getQueryClient();`

  `const greeting = await queryClient.fetchQuery(trpc.hello.queryOptions());`

  `// Do something with greeting on the server`

  `return (`

    `<HydrateClient>`

      `<ClientGreeting />`

    `</HydrateClient>`

  `);`

`}`

## Next steps[​](#next-steps "Direct link to Next steps")

*   Learn about [Server Actions](https://trpc.io/docs/client/nextjs/server-actions) for defining tRPC-powered server actions
*   Learn about [queries](https://trpc.io/docs/client/react/useQuery) and [mutations](https://trpc.io/docs/client/react/useMutation) in client components
*   Explore [server-side calls](https://trpc.io/docs/server/server-side-calls) for more advanced server-side patterns
*   Check out the [SSE Chat example](https://github.com/trpc/trpc/tree/main/examples/next-sse-chat) for a full App Router example with subscriptions
