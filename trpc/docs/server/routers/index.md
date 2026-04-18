---
title: "Define Routers"
source: "https://trpc.io/docs/server/routers"
canonical_url: "https://trpc.io/docs/server/routers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:26.512Z"
content_hash: "71dfdfbb3be7993b4792674f0c5b0dea4d14a84aba4381b2134f68931fcc08cc"
menu_path: ["Define Routers"]
section_path: []
nav_prev: {"path": "trpc/docs/server/procedures/index.md", "title": "Define Procedures"}
nav_next: {"path": "trpc/docs/server/server-side-calls/index.md", "title": "Server Side Calls"}
---

To begin building your tRPC-based API, you'll first need to define your router. Once you've mastered the fundamentals, you can [customize your routers](#advanced-usage) for more advanced use cases.

## Initialize tRPC[​](#initialize-trpc "Direct link to Initialize tRPC")

You should initialize tRPC **exactly once** per application. Multiple instances of tRPC will cause issues.

server/trpc.ts

ts

`import { initTRPC } from '@trpc/server';`

`// You can use any variable name you like.`

`// We use t to keep things simple.`

`const t = initTRPC.create();`

`export const router = t.router;`

`export const publicProcedure = t.procedure;`

You'll notice we are exporting certain methods of the `t` variable here rather than `t` itself. This is to establish a certain set of procedures that we will use idiomatically in our codebase.

## Defining a router[​](#defining-a-router "Direct link to Defining a router")

Next, let's define a router with a procedure to use in our application. We have now created an API "endpoint".

In order for these endpoints to be exposed to the frontend, your [Adapter](trpc/docs/server/adapters/index.md) should be configured with your `appRouter` instance.

server/\_app.ts

ts

`import { publicProcedure, router } from './trpc';`

`const appRouter = router({`

  `greeting: publicProcedure.query(() => 'hello tRPC v11!'),`

`});`

`// Export only the type of a router!`

`// This prevents us from importing server code on the client.`

`export type AppRouter = typeof appRouter;`

## Defining an inline sub-router[​](#inline-sub-router "Direct link to Defining an inline sub-router")

When you define an inline sub-router, you can represent your router as a plain object.

In the below example, `nested1` and `nested2` are equal:

server/\_app.ts

ts

`import * as trpc from '@trpc/server';`

`import { publicProcedure, router } from './trpc';`

`const appRouter = router({`

  `// Using the router() method`

  `nested1: router({`

    `proc: publicProcedure.query(() => '...'),`

  `}),`

  `// Using an inline sub-router`

  `nested2: {`

    `proc: publicProcedure.query(() => '...'),`

  `},`

`});`

## Advanced usage[​](#advanced-usage "Direct link to Advanced usage")

When initializing your router, tRPC allows you to:

*   Setup [request contexts](trpc/docs/server/context/index.md)
*   Assign [metadata](trpc/docs/server/metadata/index.md) to procedures
*   [Format](trpc/docs/server/error-formatting/index.md) and [handle](trpc/docs/server/error-handling/index.md) errors
*   [Transform data](trpc/docs/server/data-transformers/index.md) as needed
*   Customize the [runtime configuration](#runtime-configuration)

You can use method chaining to customize your `t`\-object on initialization. For example:

ts

`const t = initTRPC.context<Context>().meta<Meta>().create({`

  `/* [...] */`

`});`

### Runtime Configuration[​](#runtime-configuration "Direct link to Runtime Configuration")

ts

`interface RootConfig {`

  `/**`

   `* Use a data transformer`

   `* @see https://trpc.io/docs/v11/data-transformers`

   `*/`

  `transformer: DataTransformerOptions;`

  `/**`

   `* Use custom error formatting`

   `* @see https://trpc.io/docs/v11/error-formatting`

   `*/`

  `errorFormatter: ErrorFormatter;`

  `/**`

   ``* Allow `@trpc/server` to run in non-server environments``

   `* @warning **Use with caution**, this should likely mainly be used within testing.`

   `* @default false`

   `*/`

  `allowOutsideOfServer: boolean;`

  `/**`

   `* Is this a server environment?`

   `* @warning **Use with caution**, this should likely mainly be used within testing.`

   `* @default typeof window === 'undefined' || 'Deno' in window || process.env.NODE_ENV === 'test'`

   `*/`

  `isServer: boolean;`

  `/**`

   `* Is this development?`

   `* Will be used to decide if the API should return stack traces`

   `* @default process.env.NODE_ENV !== 'production'`

   `*/`

  `isDev: boolean;`

`}`


