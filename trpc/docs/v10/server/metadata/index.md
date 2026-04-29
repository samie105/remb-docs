---
title: "Metadata"
source: "https://trpc.io/docs/v10/server/metadata"
canonical_url: "https://trpc.io/docs/v10/server/metadata"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:40.500Z"
content_hash: "1c6429a82fa0bc69ef887e841082df807a613e4fbbc7bc7097abfec685a78c4f"
menu_path: ["Metadata"]
section_path: []
nav_prev: {"path": "../merging-routers/index.md", "title": "Merging Routers"}
nav_next: {"path": "../middlewares/index.md", "title": "Middlewares"}
---

Procedure metadata allows you to add an optional procedure specific `meta` property which will be available in all [middleware](../middlewares/index.md) function parameters.

tip

Use metadata together with [`trpc-openapi`](https://github.com/jlalmes/trpc-openapi) if you want to expose REST-compatible endpoints for your application.

tsx

`import { initTRPC } from '@trpc/server';`

`// [...]`

`interface Meta {`

  `authRequired: boolean;`

`}`

`export const t = initTRPC.context<Context>().meta<Meta>().create();`

`export const appRouter = t.router({`

  `// [...]`

`});`

## Example with per route authentication settings[​](#example-with-per-route-authentication-settings "Direct link to Example with per route authentication settings")

server.ts

tsx

`import { initTRPC } from '@trpc/server';`

`// [...]`

`interface Meta {`

  `authRequired: boolean;`

`}`

`export const t = initTRPC.context<Context>().meta<Meta>().create();`

`export const authedProcedure = t.procedure.use(async (opts) => {`

  `const { meta, next, ctx } = opts;`

  `// only check authorization if enabled`

  `if (meta?.authRequired && !ctx.user) {`

    `throw new TRPCError({ code: 'UNAUTHORIZED' });`

  `}`

  `return next();`

`});`

`export const appRouter = t.router({`

  `hello: authedProcedure.meta({ authRequired: false }).query(() => {`

    `return {`

      `greeting: 'hello world',`

    `};`

  `}),`

  `protectedHello: authedProcedure.meta({ authRequired: true }).query(() => {`

    `return {`

      `greeting: 'hello-world',`

    `};`

  `}),`

`});`

You can set default values for your meta type, and if you chain meta on top of a base procedure it will be shallow merged.

tsx

`import { initTRPC } from '@trpc/server';`

`interface Meta {`

  `authRequired: boolean;`

  `role?: 'user' | 'admin'`

`}`

`export const t = initTRPC`

  `.context<Context>()`

  `.meta<Meta>()`

  `.create({`

    `// Set a default value`

    `defaultMeta: { authRequired: false }`

  `});`

`const publicProcedure = t.procedure`

`// ^ Default Meta: { authRequired: false }`

`const authProcedure = publicProcedure`

  `.use(authMiddleware)`

  `.meta({`

    `authRequired: true;`

    `role: 'user'`

  `});`

`// ^ Meta: { authRequired: true, role: 'user' }`

`const adminProcedure = authProcedure`

  `.meta({`

    `role: 'admin'`

  `});`

`// ^ Meta: { authRequired: true, role: 'admin' }`
