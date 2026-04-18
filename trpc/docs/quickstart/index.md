---
title: "Quickstart"
source: "https://trpc.io/docs/quickstart"
canonical_url: "https://trpc.io/docs/quickstart"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:31:57.688Z"
content_hash: "8d973d985f0d6dccf1e49e9a15a54e49764c18ef4943f48da9386b23d288f14e"
menu_path: ["Quickstart"]
section_path: []
nav_prev: {"path": "trpc/docs/index.md", "title": "tRPC | tRPC"}
nav_next: {"path": "trpc/docs/skills/index.md", "title": "Agent Skills"}
---

## Installation[​](#installation "Direct link to Installation")

tRPC is split between several packages, so you can install only what you need. Make sure to install the packages you want in the proper sections of your codebase. For this quickstart guide we'll keep it simple and use the vanilla client only. For framework guides, check out [usage with React](trpc/docs/client/tanstack-react-query/setup/index.md) and [usage with Next.js](trpc/docs/client/nextjs/index.md).

Requirements

*   tRPC requires TypeScript >=5.7.2
*   We strongly recommend using `"strict": true` in your `tsconfig.json` as we don't officially support non-strict mode.

Start off by installing the `@trpc/server` and `@trpc/client` packages:

*   npm
*   yarn
*   pnpm
*   bun
*   deno

npm install @trpc/server @trpc/client

AI Agents

If you use an AI coding agent, install tRPC skills for better code generation:

bash

`npx @tanstack/intent@latest install`

## Your first tRPC API[​](#your-first-trpc-api "Direct link to Your first tRPC API")

Let's walk through the steps of building a typesafe API with tRPC. To start, this API will contain three endpoints with these TypeScript signatures:

ts

`type User = { id: string; name: string; };`

`userList: () => User[];`

`userById: (id: string) => User;`

`userCreate: (data: { name: string }) => User;`

Here's the file structure we'll be building. We recommend separating tRPC initialization, router definition, and server setup into distinct files to prevent cyclic dependencies:

`.`

`├── server/`

`│   ├── trpc.ts        # tRPC instantiation & setup`

`│   ├── appRouter.ts   # Your API logic and type export`

`│   └── index.ts       # HTTP server`

`└── client/`

    `└── index.ts       # tRPC client`

### 1\. Create a router instance[​](#1-create-a-router-instance "Direct link to 1. Create a router instance")

First, let's initialize the tRPC backend. It's good convention to do this in a separate file and export reusable helper functions instead of the entire tRPC object.

server/trpc.ts

ts

`import { initTRPC } from '@trpc/server';`

`/**`

 `* Initialization of tRPC backend`

 `* Should be done only once per backend!`

 `*/`

`const t = initTRPC.create();`

`/**`

 `* Export reusable router and procedure helpers`

 `* that can be used throughout the router`

 `*/`

`export const router = t.router;`

`export const publicProcedure = t.procedure;`

Next, we'll initialize our main router instance, commonly referred to as `appRouter`, to which we'll later add procedures. Lastly, we need to export the type of the router which we'll later use on the client side.

server/appRouter.ts

ts

`import { router } from './trpc';`

`export const appRouter = router({`

  `// ...`

`});`

`export type AppRouter = typeof appRouter;`

### 2\. Add a query procedure[​](#2-add-a-query-procedure "Direct link to 2. Add a query procedure")

Use `publicProcedure.query()` to add a query procedure to the router.

The following creates a query procedure called `userList` that returns a list of users:

server/appRouter.ts

ts

`import { publicProcedure, router } from './trpc';`

`export const appRouter = router({`

  `userList: publicProcedure`

    `.query(async () => {`

      `const users: User[] = [{ id: '1', name: 'Katt' }];`

      `return users;`

    `}),`

`});`

`export type AppRouter = typeof appRouter;`

### 3\. Using input parser to validate procedure inputs[​](#3-using-input-parser-to-validate-procedure-inputs "Direct link to 3. Using input parser to validate procedure inputs")

To implement the `userById` procedure, we need to accept input from the client. tRPC lets you define [input parsers](trpc/docs/server/validators/index.md) to validate and parse the input. You can define your own input parser or use a validation library of your choice, like [zod](https://zod.dev/), [yup](https://github.com/jquense/yup), or [superstruct](https://docs.superstructjs.org/).

You define your input parser on `publicProcedure.input()`, which can then be accessed on the resolver function as shown below:

*   Vanilla
*   Zod
*   Yup
*   Valibot

The input parser can be any `ZodType`, e.g. `z.string()` or `z.object()`.

  

server/appRouter.ts

ts

`import { publicProcedure, router } from './trpc';`

`import { z } from 'zod';`

`export const appRouter = router({`

  `// ...`

  `userById: publicProcedure`

    `.input(z.string())`

    `.query(async (opts) => {`

      `const { input } = opts;`

               `const input: string`

      `const user: User = { id: input, name: 'Katt' };`

      `return user;`

    `}),`

`});`

`export type AppRouter = typeof appRouter;`

server/appRouter.ts

ts

`import { publicProcedure, router } from './trpc';`

`import { z } from 'zod';`

`export const appRouter = router({`

  `// ...`

  `userById: publicProcedure`

    `.input(z.string())`

    `.query(async (opts) => {`

      `const { input } = opts;`

               `const input: string`

      `const user: User = { id: input, name: 'Katt' };`

      `return user;`

    `}),`

`});`

`export type AppRouter = typeof appRouter;`

### 4\. Adding a mutation procedure[​](#4-adding-a-mutation-procedure "Direct link to 4. Adding a mutation procedure")

Similar to GraphQL, tRPC makes a distinction between Query and Mutation procedures.

The distinction between a Query and a Mutation is primarily semantic. Queries use HTTP GET and are intended for read operations, while Mutations use HTTP POST and are intended for operations that cause side effects.

Let's add a `userCreate` mutation by adding it as a new property on our router object:

server/appRouter.ts

ts

`import { publicProcedure, router } from './trpc';`

`export const appRouter = router({`

  `// ...`

  `userCreate: publicProcedure`

    `.input(z.object({ name: z.string() }))`

    `.mutation(async (opts) => {`

      `const { input } = opts;`

               `const input: {     name: string; }`

      `// Create the user in your DB`

      `const user: User = { id: '1', ...input };`

      `return user;`

    `}),`

`});`

`export type AppRouter = typeof appRouter;`

## Serving the API[​](#serving-the-api "Direct link to Serving the API")

Now that we have defined our router, we can serve it. tRPC has first-class [adapters](trpc/docs/server/adapters/index.md) for many popular web servers. To keep it simple, we'll use the [`standalone`](trpc/docs/server/adapters/standalone/index.md) Node.js adapter here.

server/index.ts

ts

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`import { appRouter } from './appRouter';`

`const server = createHTTPServer({`

  `router: appRouter,`

`});`

`server.listen(3000);`

See the full backend code

## Using your new backend on the client[​](#using-your-new-backend-on-the-client "Direct link to Using your new backend on the client")

Let's now move to the client-side code and embrace the power of end-to-end typesafety. When we import the `AppRouter` type for the client to use, we have achieved full typesafety for our system without leaking any implementation details to the client.

### 1\. Setup the tRPC Client[​](#1-setup-the-trpc-client "Direct link to 1. Setup the tRPC Client")

client/index.ts

ts

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from './appRouter';`

`//     👆 **type-only** imports are stripped at build time`

``// Pass AppRouter as a type parameter. 👇 This lets `trpc` know``

`// what procedures are available on the server and their input/output types.`

`const trpc = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

Links in tRPC are similar to links in GraphQL, they let us control the data flow to the server. In the example above, we use the [httpBatchLink](trpc/docs/client/links/httpBatchLink/index.md), which automatically batches up multiple calls into a single HTTP request. For more in-depth usage of links, see the [links documentation](trpc/docs/client/links/index.md).

### 2\. Type Inference & Autocomplete[​](#2-type-inference--autocomplete "Direct link to 2. Type Inference & Autocomplete")

You now have access to your API procedures on the `trpc` object. Try it out!

client/index.ts

ts

`// Inferred types`

`const user = await trpc.userById.query('1');`

       `const user: User`

`const createdUser = await trpc.userCreate.mutate({ name: 'Katt' });`

          `const createdUser: User`

You can also use your autocomplete to explore the API on your client

client/index.ts

ts

`trpc.u;`

*   `userById`
*   `userCreate`
*   `userList`

## Next steps[​](#next-steps "Direct link to Next steps")

What's next?

Description

[Example Apps](trpc/docs/example-apps/index.md)

Explore tRPC in your chosen framework

[TanStack React Query](trpc/docs/client/tanstack-react-query/setup/index.md)

Recommended React integration via `@trpc/tanstack-react-query`

[Next.js](trpc/docs/client/nextjs/index.md)

Usage with Next.js

[Server Adapters](trpc/docs/server/adapters/index.md)

Express, Fastify, and more

[Transformers](trpc/docs/server/data-transformers/index.md#using-superjson)

Use superjson to retain complex types like `Date`
