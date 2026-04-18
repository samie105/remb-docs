---
title: "Metadata"
source: "https://trpc.io/docs/server/metadata"
canonical_url: "https://trpc.io/docs/server/metadata"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:59.845Z"
content_hash: "fdf15ed375b45821a3a0c2c0bb0b1edeb1b95a05b79fd66f5049d31433ce240c"
menu_path: ["Metadata"]
section_path: []
nav_prev: {"path": "trpc/docs/server/merging-routers/index.md", "title": "Merging Routers"}
nav_next: {"path": "trpc/docs/server/non-json-content-types/index.md", "title": "Content Types"}
---

Procedure metadata allows you to add an optional procedure specific `meta` property which will be available in all [middleware](trpc/docs/server/middlewares/index.md) function parameters.

tip

Use metadata together with [`trpc-openapi`](https://github.com/jlalmes/trpc-openapi) if you want to expose REST-compatible endpoints for your application.

tsx

`import { initTRPC } from '@trpc/server';`

`type Context = { user: { name: string } | null };`

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

`import { initTRPC, TRPCError } from '@trpc/server';`

`type Context = { user: { name: string } | null };`

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

`type Context = { user: { name: string } | null };`

`interface Meta {`

  `authRequired?: boolean;`

  `role?: 'user' | 'admin'`

`}`

`export const t = initTRPC`

  `.context<Context>()`

  `.meta<Meta>()`

  `.create({`

    `// Set a default value`

    `defaultMeta: { authRequired: false }`

  `});`

`const authMiddleware = t.middleware((opts) => opts.next());`

`const publicProcedure = t.procedure`

`const authProcedure = publicProcedure`

  `.use(authMiddleware)`

  `.meta({`

    `authRequired: true,`

    `role: 'user'`

  `});`

`const adminProcedure = authProcedure`

  `.meta({`

    `role: 'admin'`

  `});`
