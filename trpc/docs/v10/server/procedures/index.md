---
title: "Define Procedures"
source: "https://trpc.io/docs/v10/server/procedures"
canonical_url: "https://trpc.io/docs/v10/server/procedures"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:51.392Z"
content_hash: "641b06eb8b0c0dd6a2f0d39d67f99311090524f18e1845ab389608a977a8b361"
menu_path: ["Define Procedures"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/server/metadata/index.md", "title": "Metadata"}
nav_next: {"path": "trpc/docs/v10/server/middlewares/index.md", "title": "Middlewares"}
---

A procedure is a function which is exposed to the client, it can be one of:

*   a `Query` - used to fetch data, generally does not change any data
*   a `Mutation` - used to send data, often for create/update/delete purposes
*   a `Subscription` - you might not need this, and we have [dedicated documentation](trpc/docs/v10/subscriptions/index.md)

Procedures in tRPC are very flexible primitives to create backend functions. They use an immutable builder pattern, which means you can [create reusable base procedures](#reusable-base-procedures) that share functionality among multiple procedures.

## Writing procedures[​](#writing-procedures "Direct link to Writing procedures")

The `t` object you create during tRPC setup returns an initial `t.procedure` which all other procedures are built on:

ts

`import { initTRPC } from '@trpc/server';`

`import { z } from 'zod';`

`const t = initTRPC.context<{ signGuestBook: () => Promise<void> }>().create();`

`export const router = t.router;`

`export const publicProcedure = t.procedure;`

`const appRouter = router({`

  `// Queries are the best place to fetch data`

  `hello: publicProcedure.query(() => {`

    `return {`

      `message: 'hello world',`

    `};`

  `}),`

  `// Mutations are the best place to do things like updating a database`

  `goodbye: publicProcedure.mutation(async (opts) => {`

    `await opts.ctx.signGuestBook();`

    `return {`

      `message: 'goodbye!',`

    `};`

  `}),`

`});`

## Reusable "Base Procedures"[​](#reusable-base-procedures "Direct link to Reusable \"Base Procedures\"")

As a general pattern we recommend you rename and export `t.procedure` as `publicProcedure`, which then makes room for you to create other named procedures for specific use cases and export those too. This pattern is called "base procedures" and is a key pattern for code and behaviour re-use in tRPC; every application is likely to need it.

The below example takes a user input and [authorizes](https://en.wikipedia.org/wiki/Authorization) them like protective towns-people. This is obviously a contrived example for simplicity, and not an appropriate way to securely authorize an application user, so in practice you may want to use some combination of [Headers](trpc/docs/client/headers/index.md), [Context](trpc/docs/v10/server/context/index.md), [Middleware](trpc/docs/v10/server/middlewares/index.md), and [Metadata](trpc/docs/v10/server/metadata/index.md), to [authenticate](https://en.wikipedia.org/wiki/Authentication) and authorize your users.

ts

`export const authorizedProcedure = publicProcedure`

  `.input(z.object({ townName: z.string() }))`

  `.use((opts) => {`

    `if (opts.input.townName !== 'Pucklechurch') {`

      `throw new TRPCError({`

        `code: 'FORBIDDEN',`

        `message: "We don't take kindly to out-of-town folk",`

      `});`

    `}`

    `return opts.next();`

  `});`

`export const appRouter = t.router({`

  `hello: authorizedProcedure.query(() => {`

    `return {`

      `message: 'hello world',`

    `};`

  `}),`

  `goodbye: authorizedProcedure.mutation(async (opts) => {`

    `await opts.ctx.signGuestBook();`

    `return {`

      `message: 'goodbye!',`

    `};`

  `}),`

`});`

