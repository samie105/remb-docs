---
title: "Quickstart"
source: "https://trpc.io/docs/v10/quickstart"
canonical_url: "https://trpc.io/docs/v10/quickstart"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:23.890Z"
content_hash: "1186bf94b9e6dc2fd1194ff9ee474de08fdd6113901263042946a0440f2d9bd1"
menu_path: ["Quickstart"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/server/adapters/index.md", "title": "Adapters"}
nav_next: {"path": "trpc/docs/v10/server/adapters/aws-lambda/index.md", "title": "AWS Lambda + API Gateway Adapter"}
---

tRPC combines concepts from [REST](https://www.sitepoint.com/rest-api/) and [GraphQL](https://graphql.org/). If you are unfamiliar with either, take a look at the key [Concepts](trpc/docs/v10/concepts/index.md).

## Installation[​](#installation "Direct link to Installation")

tRPC is split between several packages, so you can install only what you need. Make sure to install the packages you want in the proper sections of your codebase. For this quickstart guide we'll keep it simple and use the vanilla client only. For framework guides, checkout [usage with React](trpc/docs/client/react/setup/index.md) and [usage with Next.js](trpc/docs/v10/client/nextjs/setup/index.md).

Requirements

*   tRPC requires TypeScript >= 4.7.0
*   We strongly recommend you using `"strict": true` in your `tsconfig.json` as we don't officially support non-strict mode.

Start off by installing the `@trpc/server` and `@trpc/client` packages:

*   npm
*   yarn
*   pnpm
*   bun

sh

`npm install @trpc/server @trpc/client`

sh

`npm install @trpc/server @trpc/client`

## Defining a backend router[​](#defining-a-backend-router "Direct link to Defining a backend router")

Let's walk through the steps of building a typesafe API with tRPC. To start, this API will contain three endpoints with these TypeScript signatures:

ts

`type User = { id: string; name: string; };`

`userList: () => User[];`

`userById: (id: string) => User;`

`userCreate: (data: { name: string }) => User;`

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

Next, we'll initialize our main router instance, commonly referred to as `appRouter`, in which we'll later add procedures to. Lastly, we need to export the type of the router which we'll later use on the client side.

server/index.ts

ts

`import { router } from './trpc';`

`const appRouter = router({`

  `// ...`

`});`

`// Export type router type signature,`

`// NOT the router itself.`

`export type AppRouter = typeof appRouter;`

### 2\. Add a query procedure[​](#2-add-a-query-procedure "Direct link to 2. Add a query procedure")

Use `publicProcedure.query()` to add a query procedure to the router.

The following creates a query procedure called `userList` that returns a list of users from our database:

server/index.ts

ts

`import { db } from './db';`

`import { publicProcedure, router } from './trpc';`

`const appRouter = router({`

  `userList: publicProcedure.query(async () => {`

    `// Retrieve users from a datasource, this is an imaginary database`

    `const users = await db.user.findMany();`

           `const users: User[]`

    `return users;`

  `}),`

`});`

### 3\. Using input parser to validate procedure inputs[​](#3-using-input-parser-to-validate-procedure-inputs "Direct link to 3. Using input parser to validate procedure inputs")

To implement the `userById` procedure, we need to accept input from the client. tRPC lets you define [input parsers](trpc/docs/v10/server/validators/index.md) to validate and parse the input. You can define your own input parser or use a validation library of your choice, like [zod](https://zod.dev/), [yup](https://github.com/jquense/yup), or [superstruct](https://docs.superstructjs.org/).

You define your input parser on `publicProcedure.input()`, which can then be accessed on the resolver function as shown below:

*   Vanilla
*   Zod
*   Yup
*   Valibot

The input parser can be any `ZodType`, e.g. `z.string()` or `z.object()`.

server.ts

ts

`import { z } from 'zod';`

`import { db } from './db';`

`import { publicProcedure, router } from './trpc';`

`const appRouter = router({`

  `// ...`

  `userById: publicProcedure.input(z.string()).query(async (opts) => {`

    `const { input } = opts;`

             `const input: string`

    `// Retrieve the user with the given ID`

    `const user = await db.user.findById(input);`

           `const user: User | undefined`

    `return user;`

  `}),`

`});`

server.ts

ts

`import { z } from 'zod';`

`import { db } from './db';`

`import { publicProcedure, router } from './trpc';`

`const appRouter = router({`

  `// ...`

  `userById: publicProcedure.input(z.string()).query(async (opts) => {`

    `const { input } = opts;`

             `const input: string`

    `// Retrieve the user with the given ID`

    `const user = await db.user.findById(input);`

           `const user: User | undefined`

    `return user;`

  `}),`

`});`

info

Throughout the remaining of this documentation, we will use `zod` as our validation library.

### 4\. Adding a mutation procedure[​](#4-adding-a-mutation-procedure "Direct link to 4. Adding a mutation procedure")

Similar to GraphQL, tRPC makes a distinction between query and mutation procedures.

The way a procedure works on the server doesn't change much between a query and a mutation. The method name is different, and the way that the client will use this procedure changes - but everything else is the same!

Let's add a `userCreate` mutation by adding it as a new property on our router object:

server.ts

ts

`const appRouter = router({`

  `// ...`

  `userCreate: publicProcedure`

    `.input(z.object({ name: z.string() }))`

    `.mutation(async (opts) => {`

      `const { input } = opts;`

               `const input: {     name: string; }`

      `// Create a new user in the database`

      `const user = await db.user.create(input);`

             `const user: {     name: string;     id: string; }`

      `return user;`

    `}),`

`});`

## Serving the API[​](#serving-the-api "Direct link to Serving the API")

Now that we have defined our router, we can serve it. tRPC has many [adapters](trpc/docs/server/adapters/index.md) so you can use any backend framework of your choice. To keep it simple, we'll use the [`standalone`](trpc/docs/server/adapters/standalone/index.md) adapter.

server/index.ts

ts

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`import { router } from './trpc';`

`const appRouter = router({`

  `// ...`

`});`

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

`import { createTRPCProxyClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`//     👆 **type-only** import`

``// Pass AppRouter as generic here. 👇 This lets the `trpc` object know``

`// what procedures are available on the server and their input/output types.`

`const trpc = createTRPCProxyClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

Links in tRPC are similar to links in GraphQL, they let us control the data flow **before** being sent to the server. In the example above, we use the [httpBatchLink](trpc/docs/client/links/httpBatchLink/index.md), which automatically batches up multiple calls into a single HTTP request. For more in-depth usage of links, see the [links documentation](trpc/docs/client/links/index.md).

### 2\. Querying & mutating[​](#2-querying--mutating "Direct link to 2. Querying & mutating")

You now have access to your API procedures on the `trpc` object. Try it out!

client/index.ts

ts

`// Inferred types`

`const user = await trpc.userById.query('1');`

       `const user: {     name: string;     id: string; } | undefined`

`const createdUser = await trpc.userCreate.mutate({ name: 'sachinraja' });`

          `const createdUser: {     name: string;     id: string; }`

### Full autocompletion[​](#full-autocompletion "Direct link to Full autocompletion")

You can open up your Intellisense to explore your API on your frontend. You'll find all of your procedure routes waiting for you along with the methods for calling them.

client/index.ts

ts

`// Full autocompletion on your routes`

`trpc.u;`

*   `userById`
*   `userCreate`
*   `userList`

## Try it out for yourself![​](#try-it-out-for-yourself "Direct link to Try it out for yourself!")

## Next steps[​](#next-steps "Direct link to Next steps")

tip

We highly encourage you to check out [the example apps](trpc/docs/v10/example-apps/index.md) to learn about how tRPC is installed in your favorite framework.

tip

By default, tRPC will map complex types like `Date` to their JSON-equivalent _(`string` in the case of `Date`)_. If you want to add to retain the integrity of those types, the easiest way to add support for these is to [use superjson](trpc/docs/server/data-transformers/index.md#using-superjson) as a Data Transformer.

tRPC includes more sophisticated client-side tooling designed for React projects and Next.js.

*   [Usage with Next.js](trpc/docs/v10/client/nextjs/index.md)
*   [Usage with Express (server-side)](trpc/docs/server/adapters/express/index.md)
*   [Usage with React (client-side)](trpc/docs/v10/client/react/index.md)
