---
title: "Set up with Next.js"
source: "https://trpc.io/docs/v10/client/nextjs/setup"
canonical_url: "https://trpc.io/docs/v10/client/nextjs/setup"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:06.026Z"
content_hash: "c59e68bfa83bf30c18615ebcd4bcca58c0043a7a63adc5cd8757434fb3a6bbfe"
menu_path: ["Set up with Next.js"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/nextjs/server-side-helpers/index.md", "title": "Server-Side Helpers"}
nav_next: {"path": "trpc/docs/v10/client/nextjs/ssg/index.md", "title": "Static Site Generation"}
---

## Recommended file structure[​](#recommended-file-structure "Direct link to Recommended file structure")

We recommend a file structure like this one, although it is not enforced by tRPC. This is what you'll see in [our examples](trpc/docs/v10/example-apps/index.md). The rest of this page will take you through the process of adding tRPC in to this structure.

graphql

`.`

`├── prisma  # <-- if prisma is added`

`│   └── [..]`

`├── src`

`│   ├── pages`

``│   │   ├── _app.tsx  # <-- add `withTRPC()`-HOC here``

`│   │   ├── api`

`│   │   │   └── trpc`

`│   │   │       └── [trpc].ts  # <-- tRPC HTTP handler`

`│   │   └── [..]`

`│   ├── server`

`│   │   ├── routers`

`│   │   │   ├── _app.ts  # <-- main app router`

`│   │   │   ├── post.ts  # <-- sub routers`

`│   │   │   └── [..]`

`│   │   ├── context.ts   # <-- create app context`

`│   │   └── trpc.ts      # <-- procedure helpers`

`│   └── utils`

`│       └── trpc.ts  # <-- your typesafe tRPC hooks`

`└── [..]`

## Add tRPC to existing Next.js project[​](#add-trpc-to-existing-nextjs-project "Direct link to Add tRPC to existing Next.js project")

### 1\. Install deps[​](#1-install-deps "Direct link to 1. Install deps")

*   npm
*   yarn
*   pnpm
*   bun

sh

`npm install @trpc/server @trpc/client @trpc/react-query @trpc/next @tanstack/react-query@4 zod`

sh

`npm install @trpc/server @trpc/client @trpc/react-query @trpc/next @tanstack/react-query@4 zod`

The Next.js integration is actually a combination of our [React Query Integration](trpc/docs/v10/client/react/index.md) and some Next.js specific integrations.

### 2\. Enable strict mode[​](#2-enable-strict-mode "Direct link to 2. Enable strict mode")

If you want to use Zod for input validation, make sure you have enabled strict mode in your `tsconfig.json`:

tsconfig.json

diff

`"compilerOptions": {`

`+   "strict": true`

`}`

If strict mode is too harsh, you'll at least want to enable `strictNullChecks`:

tsconfig.json

diff

`"compilerOptions": {`

`+   "strictNullChecks": true`

`}`

### 3\. Create a tRPC router[​](#3-create-a-trpc-router "Direct link to 3. Create a tRPC router")

Initialize your tRPC backend in `src/server/trpc.ts` using the `initTRPC` function, and create your first router. We're going to make a simple "hello world" router and procedure here - but for deeper information on creating your tRPC API you should refer to:

*   the [Quickstart guide](trpc/docs/quickstart/index.md) and [Backend usage docs](trpc/docs/server/overview/index.md) for tRPC information
*   the [Next.js Adapter docs](trpc/docs/server/adapters/nextjs/index.md) for mounting tRPC within your Next.js server.

View sample backend

### 4\. Create tRPC hooks[​](#4-create-trpc-hooks "Direct link to 4. Create tRPC hooks")

use the `createTRPCNext` function to create a set of strongly-typed hooks from your API's type signature.

utils/trpc.ts

tsx

`import { httpBatchLink } from '@trpc/client';`

`import { createTRPCNext } from '@trpc/next';`

`import type { AppRouter } from '../server/routers/_app';`

`function getBaseUrl() {`

  `if (typeof window !== 'undefined')`

    `// browser should use relative path`

    `return '';`

  `if (process.env.VERCEL_URL)`

    `// reference for vercel.com`

    ``return `https://${process.env.VERCEL_URL}`;``

  `if (process.env.RENDER_INTERNAL_HOSTNAME)`

    `// reference for render.com`

    ``return `http://${process.env.RENDER_INTERNAL_HOSTNAME}:${process.env.PORT}`;``

  `// assume localhost`

  ``return `http://localhost:${process.env.PORT ?? 3000}`;``

`}`

`export const trpc = createTRPCNext<AppRouter>({`

  `config(config) {`

    `return {`

      `links: [`

        `httpBatchLink({`

          `/**`

           `* If you want to use SSR, you need to use the server's full URL`

           `* @see https://trpc.io/docs/ssr`

           `**/`

          ``url: `${getBaseUrl()}/api/trpc`,``

          `// You can pass any HTTP headers you wish here`

          `async headers() {`

            `return {`

              `// authorization: getAuthCookie(),`

            `};`

          `},`

        `}),`

      `],`

    `};`

  `},`

  `/**`

   `* @see https://trpc.io/docs/ssr`

   `**/`

  `ssr: false,`

`});`

note

`createTRPCNext` does not work with the tRPC-v9 interop mode. If you are migrating from v9 using interop, you should continue using [the old way of initializing tRPC](trpc/docs/v9/nextjs/index.md#4-create-trpc-hooks).

### 5\. Configure `_app.tsx`[​](#5-configure-_apptsx "Direct link to 5-configure-_apptsx")

Wrap your root app page in the `trpc.withTRPC` HOC, similar to this:

pages/\_app.tsx

tsx

`import type { AppType } from 'next/app';`

`import { trpc } from '../utils/trpc';`

`const MyApp: AppType = ({ Component, pageProps }) => {`

  `return <Component {...pageProps} />;`

`};`

`export default trpc.withTRPC(MyApp);`

### 6\. Make an API request[​](#6-make-an-api-request "Direct link to 6. Make an API request")

You're all set!

You can now use the React hooks you have just created to invoke your API. For more detail see the [React Query Integration](trpc/docs/v10/client/react/index.md)

pages/index.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export default function IndexPage() {`

  `const hello = trpc.hello.useQuery({ text: 'client' });`

  `if (!hello.data) {`

    `return <div>Loading...</div>;`

  `}`

  `return (`

    `<div>`

      `<p>{hello.data.greeting}</p>`

    `</div>`

  `);`

`}`

## `createTRPCNext()` options[​](#createtrpcnext-options "Direct link to createtrpcnext-options")

### `config`\-callback[​](#config-callback "Direct link to config-callback")

The `config`\-argument is a function that returns an object that configures the tRPC and React Query clients. This function has a `ctx` input that gives you access to the Next.js `req` object, among other things. The returned value can contain the following properties:

*   **Required**:
*   `links` to customize the flow of data between tRPC Client and the tRPC Server. [Read more](trpc/docs/client/links/index.md).
*   Optional:
*   `queryClientConfig`: a configuration object for the React Query `QueryClient` used internally by the tRPC React hooks: [QueryClient docs](https://tanstack.com/query/v4/docs/reference/QueryClient)
*   `queryClient`: a React Query [QueryClient instance](https://tanstack.com/query/v4/docs/reference/QueryClient)
    *   **Note:** You can only provide either a `queryClient` or a `queryClientConfig`.
*   `transformer`: a transformer applied to outgoing payloads. Read more about [Data Transformers](trpc/docs/server/data-transformers/index.md)
*   `abortOnUnmount`: determines if in-flight requests will be cancelled on component unmount. This defaults to `false`.

### `overrides`: (default: `undefined`)[​](#overrides "Direct link to overrides")

Configure [overrides for React Query's hooks](trpc/docs/client/react/useUtils/index.md#invalidate-full-cache-on-every-mutation).

### `ssr`\-boolean (default: `false`)[​](#ssr-boolean-default-false "Direct link to ssr-boolean-default-false")

Whether tRPC should await queries when server-side rendering a page. Defaults to `false`.

### `responseMeta`\-callback[​](#responsemeta-callback "Direct link to responsemeta-callback")

Ability to set request headers and HTTP status when server-side rendering.

#### Example[​](#example "Direct link to Example")

utils/trpc.ts

tsx

`import { createTRPCNext } from '@trpc/next';`

`import type { AppRouter } from '../pages/api/trpc/[trpc]';`

`export const trpc = createTRPCNext<AppRouter>({`

  `config(config) {`

    `/* [...] */`

  `},`

  `ssr: true,`

  `responseMeta(opts) {`

    `const { clientErrors } = opts;`

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

`});`

## Next steps[​](#next-steps "Direct link to Next steps")

Browse the rest of the docs to learn more about things like [authorization](trpc/docs/server/authorization/index.md), [middlewares](trpc/docs/server/middlewares/index.md), and [error handling](trpc/docs/server/error-handling/index.md).

You can also find information about [queries](trpc/docs/client/react/useQuery/index.md) and [mutations](trpc/docs/client/react/useMutation/index.md) now that you're using `@trpc/react-query`.

