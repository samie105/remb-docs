---
title: "Usage with React"
source: "https://trpc.io/docs/v9/react"
canonical_url: "https://trpc.io/docs/v9/react"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:25.273Z"
content_hash: "b23d3b14c977f4b2acdb0f61f91da84d40e20874ae24b39ebf1f088eada20bdc"
menu_path: ["Usage with React"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/quickstart/index.md", "title": "Quickstart"}
nav_next: {"path": "trpc/docs/v9/react-mutations/index.md", "title": "useMutation()"}
---

info

*   If you're using Next.js, read the [Usage with Next.js](trpc/docs/v9/nextjs/index.md) guide instead.
*   In order to infer types from your Node.js backend you should have the frontend & backend in the same monorepo.

## Add tRPC to existing React project[​](#add-trpc-to-existing-react-project "Direct link to Add tRPC to existing React project")

### Server Side[​](#server-side "Direct link to Server Side")

#### 1\. Install dependencies[​](#1-install-dependencies "Direct link to 1. Install dependencies")

bash

`yarn add @trpc/server zod`

*   Zod: most examples use [Zod](https://github.com/colinhacks/zod) for input validation and we highly recommended it, though it isn't required. You can use a validation library of your choice ([Yup](https://github.com/jquense/yup), [Superstruct](https://github.com/ianstormtaylor/superstruct), [io-ts](https://github.com/gcanti/io-ts), etc). In fact, any object containing a `parse`, `create` or `validateSync` method will work.

#### 2\. Enable strict mode[​](#2-enable-strict-mode "Direct link to 2. Enable strict mode")

If you want to use Zod for input validation, make sure you have enabled strict mode in your `tsconfig.json`:

json

`// tsconfig.json`

`{`

  `// ...`

  `"compilerOptions": {`

    `// ...`

    `"strict": true`

  `}`

`}`

If strict mode is too much, at least enable `strictNullChecks`:

json

`// tsconfig.json`

`{`

  `// ...`

  `"compilerOptions": {`

    `// ...`

    `"strictNullChecks": true`

  `}`

`}`

#### 3\. Implement your `appRouter`[​](#3-implement-your-approuter "Direct link to 3-implement-your-approuter")

Follow the [Quickstart](trpc/docs/v9/quickstart/index.md) and read the [`@trpc/server` docs](trpc/docs/v9/router/index.md) for guidance on this. Once you have your API implemented and listening via HTTP, continue to the next step.

### Client Side[​](#client-side "Direct link to Client Side")

> tRPC works fine with Create React App!

#### 1\. Install dependencies[​](#1-install-dependencies-1 "Direct link to 1. Install dependencies")

bash

`yarn add @trpc/client @trpc/server @trpc/react react-query@3`

*   @trpc/server: This is a peer dependency of `@trpc/client` so you have to install it again!
*   Tanstack's React Query: @trpc/react provides a thin wrapper over @tanstack/react-query. It is required as a peer dependency.

#### 2\. Create tRPC hooks[​](#2-create-trpc-hooks "Direct link to 2. Create tRPC hooks")

Create a set of strongly-typed React hooks from your `AppRouter` type signature with `createReactQueryHooks`.

utils/trpc.ts

tsx

`// utils/trpc.ts`

`import { createReactQueryHooks } from '@trpc/react';`

`import type { AppRouter } from '../path/to/router.ts';`

`export const trpc = createReactQueryHooks<AppRouter>();`

`// => { useQuery: ..., useMutation: ...}`

#### 3\. Add tRPC providers[​](#3-add-trpc-providers "Direct link to 3. Add tRPC providers")

In your `App.tsx`

App.tsx

tsx

`import React, { useState } from 'react';`

`import { QueryClient, QueryClientProvider } from 'react-query';`

`import { trpc } from './utils/trpc';`

`export function App() {`

  `const [queryClient] = useState(() => new QueryClient());`

  `const [trpcClient] = useState(() =>`

    `trpc.createClient({`

      `url: 'http://localhost:5000/trpc',`

      `// optional`

      `headers() {`

        `return {`

          `authorization: getAuthCookie(),`

        `};`

      `},`

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

#### 4\. Fetch data[​](#4-fetch-data "Direct link to 4. Fetch data")

pages/IndexPage.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export default function IndexPage() {`

  `const hello = trpc.useQuery(['hello', { text: 'client' }]);`

  `if (!hello.data) return <div>Loading...</div>;`

  `return (`

    `<div>`

      `<p>{hello.data.greeting}</p>`

    `</div>`

  `);`

`}`
