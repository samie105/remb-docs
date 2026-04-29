---
title: "Route Metadata"
source: "https://trpc.io/docs/v9/metadata"
canonical_url: "https://trpc.io/docs/v9/metadata"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:40.221Z"
content_hash: "c3d0e04a96080e288096b5508e2239467b959e080900b1c48abc40d455132dfc"
menu_path: ["Route Metadata"]
section_path: []
nav_prev: {"path": "../merging-routers/index.md", "title": "Merging Routers"}
nav_next: {"path": "../middlewares/index.md", "title": "Middlewares"}
---

Route metadata allows you to add an optional route specific `meta` property which will be available in all `middleware` function parameters.

jsx

`import * as trpc from '@trpc/server';`

`// [...]`

`interface Meta {`

  `hasAuth: boolean`

`}`

`export const appRouter = trpc.router<Context, Meta>();`

server.ts

tsx

`import * as trpc from '@trpc/server';`

`// [...]`

`interface Meta {`

  `hasAuth: boolean;`

`}`

`export const appRouter = trpc`

  `.router<Context, Meta>()`

  `.middleware(async ({ meta, next, ctx }) => {`

    `// only check authorization if enabled`

    `if (meta?.hasAuth && !ctx.user) {`

      `throw new TRPCError({ code: 'UNAUTHORIZED' });`

    `}`

    `return next();`

  `})`

  `.query('hello', {`

    `meta: {`

      `hasAuth: false,`

    `},`

    `resolve({ ctx }) {`

      `return {`

        ``greeting: `hello world`,``

      `};`

    `},`

  `})`

  `.query('protected-hello', {`

    `meta: {`

      `hasAuth: true,`

    `},`

    `resolve({ ctx }) {`

      `return {`

        ``greeting: `hello world`,``

      `};`

    `},`

  `});`
