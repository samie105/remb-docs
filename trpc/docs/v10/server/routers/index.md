---
title: "Define Routers"
source: "https://trpc.io/docs/v10/server/routers"
canonical_url: "https://trpc.io/docs/v10/server/routers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:16.513Z"
content_hash: "5d5c87278574f2046b1856fcb23cfe4b757dca56e9ed31cdf6ed36822b5ba720"
menu_path: ["Define Routers"]
section_path: []
nav_prev: {"path": "../procedures/index.md", "title": "Define Procedures"}
nav_next: {"path": "../server-side-calls/index.md", "title": "Server Side Calls"}
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

In order for these endpoints to be exposed to the frontend, your [Adapter](../../../server/adapters/index.md) should be configured with your `appRouter` instance.

server/\_app.ts

ts

`import { publicProcedure, router } from './trpc';`

`const appRouter = router({`

  `greeting: publicProcedure.query(() => 'hello tRPC v10!'),`

`});`

`// Export only the type of a router!`

`// This prevents us from importing server code on the client.`

`export type AppRouter = typeof appRouter;`

## Advanced usage[​](#advanced-usage "Direct link to Advanced usage")

When initializing your router, tRPC allows you to:

*   Setup [request contexts](../../../server/context/index.md)
*   Assign [metadata](../../../server/metadata/index.md) to procedures
*   [Format](../../../server/error-formatting/index.md) and [handle](../../../server/error-handling/index.md) errors
*   [Transform data](../../../server/data-transformers/index.md) as needed
*   Customize the [runtime configuration](#runtime-configuration)

You can use method chaining to customize your `t`\-object on initialization. For example:

ts

`const t = initTRPC.context<Context>().meta<Meta>().create({`

  `/* [...] */`

`});`

### Runtime Configuration[​](#runtime-configuration "Direct link to Runtime Configuration")

ts

`export interface RuntimeConfig<TTypes extends RootConfigTypes> {`

  `/**`

   `* Use a data transformer`

   `* @see https://trpc.io/docs/data-transformers`

   `*/`

  `transformer: TTypes['transformer'];`

  `/**`

   `* Use custom error formatting`

   `* @see https://trpc.io/docs/error-formatting`

   `*/`

  `errorFormatter: ErrorFormatter<TTypes['ctx'], any>;`

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
