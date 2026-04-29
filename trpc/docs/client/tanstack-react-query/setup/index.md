---
title: "TanStack React Query"
source: "https://trpc.io/docs/client/tanstack-react-query/setup"
canonical_url: "https://trpc.io/docs/client/tanstack-react-query/setup"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:42.097Z"
content_hash: "74d200d8fdd9ce93ef33387dac73a73029df0538801736e0f40eda47a5c3718e"
menu_path: ["TanStack React Query"]
section_path: []
nav_prev: {"path": "../server-components/index.md", "title": "Set up with React Server Components"}
nav_next: {"path": "../usage/index.md", "title": "TanStack React Query"}
---

Compared to our [classic React Query Integration](../../react/index.md) this client is simpler and more TanStack Query-native, providing factories for common TanStack React Query interfaces like QueryKeys, QueryOptions, and MutationOptions. We think it's the future and recommend using this over the classic client, [read the announcement post](https://trpc.io/blog/introducing-tanstack-react-query-client) for more information about this change.

❓ Do I have to use an integration?

## Setup[​](#setup "Direct link to Setup")

### 1\. Install dependencies[​](#1-install-dependencies "Direct link to 1. Install dependencies")

The following dependencies should be installed

*   npm
*   yarn
*   pnpm
*   bun
*   deno

npm install @trpc/server @trpc/client @trpc/tanstack-react-query @tanstack/react-query

AI Agents

If you use an AI coding agent, install tRPC skills for better code generation:

bash

`npx @tanstack/intent@latest install`

### 2\. Import your `AppRouter`[​](#2-import-your-approuter "Direct link to 2-import-your-approuter")

Import your `AppRouter` type into the client application. This type holds the shape of your entire API.

utils/trpc.ts

ts

`import type { AppRouter } from '../server/router';`

tip

By using `import type` you ensure that the reference will be stripped at compile-time, meaning you don't inadvertently import server-side code into your client. For more information, [see the Typescript docs](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export).

### 3a. Set up the tRPC context provider[​](#3a-set-up-the-trpc-context-provider "Direct link to 3a. Set up the tRPC context provider")

In cases where you rely on React context, such as when using server-side rendering in full-stack frameworks like Next.js, it's important to create a new QueryClient for each request so that your users don't end up sharing the same cache, you can use the `createTRPCContext` to create a set of type-safe context providers and consumers from your `AppRouter` type signature.

utils/trpc.ts

tsx

`import { createTRPCContext } from '@trpc/tanstack-react-query';`

`import type { AppRouter } from '../server/router';`

`export const { TRPCProvider, useTRPC, useTRPCClient } = createTRPCContext<AppRouter>();`

Then, create a tRPC client, and wrap your application in the `TRPCProvider`, as below. You will also need to set up and connect React Query, which [they document in more depth](https://tanstack.com/query/latest/docs/framework/react/quick-start).

tip

If you already use React Query in your application, you **should** re-use the `QueryClient` and `QueryClientProvider` you already have. You can read more about the QueryClient initialization in the [React Query docs](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr#initial-setup).

components/App.tsx

tsx

`import { QueryClient, QueryClientProvider } from '@tanstack/react-query';`

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import { useState } from 'react';`

`import type { AppRouter } from '../server/router';`

`import { TRPCProvider } from '../utils/trpc';`

`function makeQueryClient() {`

  `return new QueryClient({`

    `defaultOptions: {`

      `queries: {`

        `// With SSR, we usually want to set some default staleTime`

        `// above 0 to avoid refetching immediately on the client`

        `staleTime: 60 * 1000,`

      `},`

    `},`

  `});`

`}`

`let browserQueryClient: QueryClient | undefined = undefined;`

`function getQueryClient() {`

  `if (typeof window === 'undefined') {`

    `// Server: always make a new query client`

    `return makeQueryClient();`

  `} else {`

    `// Browser: make a new query client if we don't already have one`

    `// This is very important, so we don't re-make a new client if React`

    `// suspends during the initial render. This may not be needed if we`

    `// have a suspense boundary BELOW the creation of the query client`

    `if (!browserQueryClient) browserQueryClient = makeQueryClient();`

    `return browserQueryClient;`

  `}`

`}`

`export function App() {`

  `const queryClient = getQueryClient();`

  `const [trpcClient] = useState(() =>`

    `createTRPCClient<AppRouter>({`

      `links: [`

        `httpBatchLink({`

          `url: 'http://localhost:2022',`

        `}),`

      `],`

    `}),`

  `);`

  `return (`

    `<QueryClientProvider client={queryClient}>`

      `<TRPCProvider trpcClient={trpcClient} queryClient={queryClient}>`

        `{null /* Your app here */}`

      `</TRPCProvider>`

    `</QueryClientProvider>`

  `);`

`}`

### 3b. Set up with Query/Mutation Key Prefixing enabled[​](#3b-set-up-with-querymutation-key-prefixing-enabled "Direct link to 3b. Set up with Query/Mutation Key Prefixing enabled")

If you want to prefix all queries and mutations with a specific key, see [Query Key Prefixing](../usage/index.md#keyPrefix) for setup and usage examples.

### 3c. Set up without React context[​](#3c-set-up-without-react-context "Direct link to 3c. Set up without React context")

When building an SPA using only client-side rendering with something like Vite, you can create the `QueryClient` and tRPC client outside of React context as singletons.

utils/trpc.ts

ts

`import { QueryClient } from '@tanstack/react-query';`

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import { createTRPCOptionsProxy } from '@trpc/tanstack-react-query';`

`import type { AppRouter } from '../server/router';`

`export const queryClient = new QueryClient();`

`const trpcClient = createTRPCClient<AppRouter>({`

  `links: [httpBatchLink({ url: 'http://localhost:2022' })],`

`});`

`export const trpc = createTRPCOptionsProxy<AppRouter>({`

  `client: trpcClient,`

  `queryClient,`

`});`

components/App.tsx

tsx

`import { QueryClientProvider } from '@tanstack/react-query';`

`import { queryClient } from '../utils/trpc';`

`export function App() {`

  `return (`

    `<QueryClientProvider client={queryClient}>`

      `{/* Your app here */}`

    `</QueryClientProvider>`

  `);`

`}`

### 4\. Fetch data[​](#4-fetch-data "Direct link to 4. Fetch data")

You can now use the tRPC React Query integration to call queries and mutations on your API.

components/user-list.tsx

tsx

`import { useMutation, useQuery } from '@tanstack/react-query';`

`import { useTRPC } from '../utils/trpc';`

`export default function UserList() {`

  ``const trpc = useTRPC(); // use `import { trpc } from './utils/trpc'` if you're using the singleton pattern``

  `const userQuery = useQuery(trpc.getUser.queryOptions({ id: 'id_bilbo' }));`

  `const userCreator = useMutation(trpc.createUser.mutationOptions());`

  `return (`

    `<div>`

      `<p>{userQuery.data?.name}</p>`

      `<button onClick={() => userCreator.mutate({ name: 'Frodo' })}>`

        `Create Frodo`

      `</button>`

    `</div>`

  `);`

`}`
