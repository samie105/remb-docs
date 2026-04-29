---
title: "Usage with Next.js"
source: "https://trpc.io/docs/v9/nextjs"
canonical_url: "https://trpc.io/docs/v9/nextjs"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:01.910Z"
content_hash: "db1396623e1eeed135bd6949b35b623e1a346be04ebe7586fb4c10a042c760fa"
menu_path: ["Usage with Next.js"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/middlewares/index.md", "title": "Middlewares"}
nav_next: {"path": "trpc/docs/v9/output-validation/index.md", "title": "Output Validation"}
---

tip

If you're using tRPC in a new project, consider using one of the example projects as a starting point or for reference: [tRPC Example Projects](../example-apps/index.md)

tRPC and Next.js are a match made in heaven! Next.js makes it easy for you to build your client and server together in one codebase. This makes it easy to share types between them.

tRPC includes dedicated tools to make the Next.js developer experience as seamless as possible.

## Recommended file structure[​](#recommended-file-structure "Direct link to Recommended file structure")

Recommended but not enforced file structure. This is what you get when starting from [the examples](../example-apps/index.md).

graphql

`.`

`├── prisma # <-- if prisma is added`

`│   └── [..]`

`├── src`

`│   ├── pages`

``│   │   ├── _app.tsx # <-- add `withTRPC()`-HOC here``

`│   │   ├── api`

`│   │   │   └── trpc`

`│   │   │       └── [trpc].ts # <-- tRPC HTTP handler`

`│   │   └── [..]`

`│   ├── server`

`│   │   ├── routers`

`│   │   │   ├── app.ts   # <-- main app router`

`│   │   │   ├── post.ts  # <-- sub routers`

`│   │   │   └── [..]`

`│   │   ├── context.ts      # <-- create app context`

`│   │   └── createRouter.ts # <-- router helper`

`│   └── utils`

`│       └── trpc.ts  # <-- your typesafe tRPC hooks`

`└── [..]`

## Add tRPC to existing Next.js project[​](#add-trpc-to-existing-nextjs-project "Direct link to Add tRPC to existing Next.js project")

### 1\. Install deps[​](#1-install-deps "Direct link to 1. Install deps")

bash

`yarn add @trpc/client @trpc/server @trpc/react @trpc/next zod react-query@3`

*   React Query: `@trpc/react` provides a thin wrapper over [@tanstack/react-query](https://tanstack.com/query/v3/docs/react/overview). It is required as a peer dependency.
*   Zod: most examples use [Zod](https://github.com/colinhacks/zod) for input validation and we highly recommended it, though it isn't required. You can use a validation library of your choice ([Yup](https://github.com/jquense/yup), [Superstruct](https://github.com/ianstormtaylor/superstruct), [io-ts](https://github.com/gcanti/io-ts), etc). In fact, any object containing a `parse`, `create` or `validateSync` method will work.

### 2\. Enable strict mode[​](#2-enable-strict-mode "Direct link to 2. Enable strict mode")

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

### 3\. Create a tRPC router[​](#3-create-a-trpc-router "Direct link to 3. Create a tRPC router")

Implement your tRPC router in `./pages/api/trpc/[trpc].ts`. If you need to split your router into several subrouters, implement them in a top-level `server` directory in your project root, then import them into `./pages/api/trpc/[trpc].ts` and [merge them](../merging-routers/index.md) into a single root `appRouter`.

View sample router

### 4\. Create tRPC hooks[​](#4-create-trpc-hooks "Direct link to 4. Create tRPC hooks")

Create a set of strongly-typed hooks using your API's type signature.

utils/trpc.ts

tsx

`import { createReactQueryHooks } from '@trpc/react';`

`import type { AppRouter } from '../pages/api/trpc/[trpc]';`

`export const trpc = createReactQueryHooks<AppRouter>();`

`// => { useQuery: ..., useMutation: ...}`

### 5\. Configure `_app.tsx`[​](#5-configure-_apptsx "Direct link to 5-configure-_apptsx")

The `createReactQueryHooks` function expects certain parameters to be passed via the Context API. To set these parameters, create a custom `_app.tsx` using the `withTRPC` higher-order component:

pages/\_app.tsx

tsx

`import { withTRPC } from '@trpc/next';`

`import { AppType } from 'next/dist/shared/lib/utils';`

`import type { AppRouter } from './api/trpc/[trpc]';`

`const MyApp: AppType = ({ Component, pageProps }) => {`

  `return <Component {...pageProps} />;`

`};`

`export default withTRPC<AppRouter>({`

  `config(config) {`

    `/**`

     `* If you want to use SSR, you need to use the server's full URL`

     `* @see https://trpc.io/docs/ssr`

     `*/`

    `const url = process.env.VERCEL_URL`

      `` ? `https://${process.env.VERCEL_URL}/api/trpc` ``

      `: 'http://localhost:3000/api/trpc';`

    `return {`

      `url,`

      `/**`

       `* @see https://tanstack.com/query/v3/docs/react/reference/QueryClient`

       `*/`

      `// queryClientConfig: { defaultOptions: { queries: { staleTime: 60 } } },`

    `};`

  `},`

  `/**`

   `* @see https://trpc.io/docs/ssr`

   `*/`

  `ssr: true,`

`})(MyApp);`

### 6\. Make API requests[​](#6-make-api-requests "Direct link to 6. Make API requests")

pages/index.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export default function IndexPage() {`

  `const hello = trpc.useQuery(['hello', { text: 'client' }]);`

  `if (!hello.data) {`

    `return <div>Loading...</div>;`

  `}`

  `return (`

    `<div>`

      `<p>{hello.data.greeting}</p>`

    `</div>`

  `);`

`}`

## `withTRPC()` options[​](#withtrpc-options "Direct link to withtrpc-options")

### `config`\-callback[​](#config-callback "Direct link to config-callback")

The `config`\-argument is a function that returns an object that configures the tRPC and React Query clients. This function has a `ctx` input that gives you access to the Next.js `req` object, among other things. The returned value can contain the following properties:

*   Exactly **one of** these are **required**:
    
    *   `url` your API URL.
    *   `links` to customize the flow of data between tRPC Client and the tRPC-server. [Read more](../links/index.md).
*   Optional:
    
    *   `queryClientConfig`: a configuration object for the React Query `QueryClient` used internally by the tRPC React hooks: [QueryClient docs](https://tanstack.com/query/v3/docs/react/reference/QueryClient)
    *   `headers`: an object or a function that returns an object of outgoing tRPC requests
    *   `transformer`: a transformer applied to outgoing payloads. Read more about [Data Transformers](../data-transformers/index.md)
    *   `fetch`: customize the implementation of `fetch` used by tRPC internally
    *   `AbortController`: customize the implementation of `AbortController` used by tRPC internally

### `ssr`\-boolean (default: `false`)[​](#ssr-boolean-default-false "Direct link to ssr-boolean-default-false")

Whether tRPC should await queries when server-side rendering a page. Defaults to `false`.

### `responseMeta`\-callback[​](#responsemeta-callback "Direct link to responsemeta-callback")

Ability to set request headers and HTTP status when server-side rendering.

#### Example[​](#example "Direct link to Example")

pages/\_app.tsx

tsx

`export default withTRPC<AppRouter>({`

  `config(config) {`

    `/* [...] */`

  `},`

  `ssr: true,`

  `responseMeta({ clientErrors, ctx }) {`

    `if (clientErrors.length) {`

      `// propagate first http error from API calls`

      `return {`

        `status: clientErrors[0].data?.httpStatus ?? 500,`

      `};`

    `}`

    `// cache full page for 1 day + revalidate once every second`

    `const ONE_DAY_IN_SECONDS = 60 * 60 * 24;`

    `return {`

      ``'Cache-Control': `s-maxage=1, stale-while-revalidate=${ONE_DAY_IN_SECONDS}`,``

    `};`

  `},`

`})(MyApp);`

## Next steps[​](#next-steps "Direct link to Next steps")

Refer to the `@trpc/react` docs for additional information on executing [Queries](../react-queries/index.md) and [Mutations](../react-mutations/index.md) inside your components.
