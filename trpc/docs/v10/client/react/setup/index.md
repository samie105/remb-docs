---
title: "Set up the React Query Integration"
source: "https://trpc.io/docs/v10/client/react/setup"
canonical_url: "https://trpc.io/docs/v10/client/react/setup"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:57.626Z"
content_hash: "d1e96a48ee7684ef984a3d1061b9685e218a5117a42962d715c6727ebd137f75"
menu_path: ["Set up the React Query Integration"]
section_path: []
nav_prev: {"path": "../infer-types/index.md", "title": "Inferring Types"}
nav_next: {"path": "../suspense/index.md", "title": "Suspense"}
---

### 1\. Install dependencies[​](#1-install-dependencies "Direct link to 1. Install dependencies")

The following dependencies should be installed

*   npm
*   yarn
*   pnpm
*   bun

bash

`npm install @trpc/client @trpc/server @trpc/react-query @tanstack/react-query@4`

bash

`npm install @trpc/client @trpc/server @trpc/react-query @tanstack/react-query@4`

### 2\. Import your `AppRouter`[​](#2-import-your-approuter "Direct link to 2-import-your-approuter")

Import your `AppRouter` type into the client application. This type holds the shape of your entire API.

ts

`import type { AppRouter } from '../server/router';`

tip

By using `import type` you ensure that the reference will be stripped at compile-time, meaning you don't inadvertently import server-side code into your client. For more information, [see the Typescript docs](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export).

### 3\. Create tRPC hooks[​](#3-create-trpc-hooks "Direct link to 3. Create tRPC hooks")

Create a set of strongly-typed React hooks from your `AppRouter` type signature with `createTRPCReact`.

utils/trpc.ts

ts

`import { createTRPCReact } from '@trpc/react-query';`

`import type { AppRouter } from '../server/router';`

`export const trpc = createTRPCReact<AppRouter>();`

### 4\. Add tRPC providers[​](#4-add-trpc-providers "Direct link to 4. Add tRPC providers")

Create a tRPC client, and wrap your application in the tRPC Provider, as below. You will also need to set up and connect React Query, which [they document in more depth](https://tanstack.com/query/latest/docs/react/quick-start).

tip

If you already use React Query in your application, you **should** re-use the `QueryClient` and `QueryClientProvider` you already have.

App.tsx

tsx

`import { QueryClient, QueryClientProvider } from '@tanstack/react-query';`

`import { httpBatchLink } from '@trpc/client';`

`import React, { useState } from 'react';`

`import { trpc } from './utils/trpc';`

`export function App() {`

  `const [queryClient] = useState(() => new QueryClient());`

  `const [trpcClient] = useState(() =>`

    `trpc.createClient({`

      `links: [`

        `httpBatchLink({`

          `url: 'http://localhost:3000/trpc',`

          `// You can pass any HTTP headers you wish here`

          `async headers() {`

            `return {`

              `authorization: getAuthCookie(),`

            `};`

          `},`

        `}),`

      `],`

    `}),`

  `);`

  `return (`

    `<trpc.Provider client={trpcClient} queryClient={queryClient}>`

      `<QueryClientProvider client={queryClient}>`

        `{/* Your app here */}`

      `</QueryClientProvider>`

    `</trpc.Provider>`

  `);`

`}`

note

The reason for using `useState` in the creation of the `queryClient` and the `TRPCClient`, as opposed to declaring them outside of the component, is to ensure that each request gets a unique client when using SSR. If you use client side rendering then you can move them if you wish.

#### 5\. Fetch data[​](#5-fetch-data "Direct link to 5. Fetch data")

You can now use the tRPC React Query integration to call queries and mutations on your API.

pages/IndexPage.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export default function IndexPage() {`

  `const userQuery = trpc.getUser.useQuery({ id: 'id_bilbo' });`

  `const userCreator = trpc.createUser.useMutation();`

  `return (`

    `<div>`

      `<p>{userQuery.data?.name}</p>`

      `<button onClick={() => userCreator.mutate({ name: 'Frodo' })}>`

        `Create Frodo`

      `</button>`

    `</div>`

  `);`

`}`
