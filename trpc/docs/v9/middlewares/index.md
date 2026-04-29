---
title: "Middlewares"
source: "https://trpc.io/docs/v9/middlewares"
canonical_url: "https://trpc.io/docs/v9/middlewares"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:50.782Z"
content_hash: "7d5394bdc8ae7a6a9e3d89aba722f411cf035a8514125530185339a1a1bcdbd5"
menu_path: ["Middlewares"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/metadata/index.md", "title": "Route Metadata"}
nav_next: {"path": "trpc/docs/v9/nextjs/index.md", "title": "Usage with Next.js"}
---

You are able to add middleware(s) to a whole router with the `middleware()` method. The middleware(s) will wrap the invocation of the procedure and must pass through its return value.

In the example below any call to `admin.*` will ensure that the user is an "admin" before executing any query or mutation.

ts

`trpc`

  `.router<Context>()`

  `.query('foo', {`

    `resolve() {`

      `return 'bar';`

    `},`

  `})`

  `.merge(`

    `'admin.',`

    `trpc`

      `.router<Context>()`

      `.middleware(async (opts) => {`

        `if (!opts.ctx.user?.isAdmin) {`

          `throw new TRPCError({ code: 'UNAUTHORIZED' });`

        `}`

        `return opts.next();`

      `})`

      `.query('secretPlace', {`

        `resolve() {`

          `return 'a key';`

        `},`

      `}),`

  `);`

tip

See [Error Handling](../error-handling/index.md) to learn more about the `TRPCError` thrown in the above example.

## Logging[​](#logging "Direct link to Logging")

In the example below timings for queries are logged automatically.

ts

`trpc`

  `.router<Context>()`

  `.middleware(async ({ path, type, next }) => {`

    `const start = Date.now();`

    `const result = await next();`

    `const durationMs = Date.now() - start;`

    `result.ok`

      `? logMock('OK request timing:', { path, type, durationMs })`

      `: logMock('Non-OK request timing', { path, type, durationMs });`

    `return result;`

  `})`

  `.query('foo', {`

    `resolve() {`

      `return 'bar';`

    `},`

  `})`

  `.query('abc', {`

    `resolve() {`

      `return 'def';`

    `},`

  `});`

## Context Swapping[​](#context-swapping "Direct link to Context Swapping")

A middleware can replace the router's context, and downstream procedures will receive the new context value:

ts

`interface Context {`

  `// user is nullable`

  `user?: {`

    `id: string;`

  `};`

`}`

`trpc`

  `.router<Context>()`

  `.middleware((opts) => {`

    `if (!opts.ctx.user) {`

      `throw new TRPCError({ code: 'UNAUTHORIZED' });`

    `}`

    `return opts.next({`

      `ctx: {`

        `...opts.ctx,`

        `user: opts.ctx.user, // user value is known to be non-null now`

      `},`

    `});`

  `})`

  `.query('userId', {`

    `async resolve({ ctx }) {`

      `return ctx.user.id;`

    `},`

  `});`

### `createProtectedRouter()`\-helper[​](#createprotectedrouter-helper "Direct link to createprotectedrouter-helper")

This helper can be used anywhere in your app tree to enforce downstream procedures to be authorized.

server/createRouter.ts

tsx

`import * as trpc from '@trpc/server';`

`import { Context } from './context';`

`export function createProtectedRouter() {`

  `return trpc.router<Context>().middleware((opts) => {`

    `if (!opts.ctx.user) {`

      `throw new trpc.TRPCError({ code: 'UNAUTHORIZED' });`

    `}`

    `return opts.next({`

      `ctx: {`

        `...opts.ctx,`

        ``// infers that `user` is non-nullable to downstream procedures``

        `user: opts.ctx.user,`

      `},`

    `});`

  `});`

`}`

## Raw input[​](#raw-input "Direct link to Raw input")

A middleware can access the raw input that will be passed to a procedure. This can be used for authentication / other preprocessing in the middleware that requires access to the procedure input, and can be especially useful when used in conjunction with Context Swapping.

caution

The `rawInput` passed to a middleware has not yet been validated by a procedure's `input` schema / validator, so be careful when using it! Because of this, `rawInput` has type `unknown`. For more info see [#1059](https://github.com/trpc/trpc/pull/1059#issuecomment-932985023).

ts

`const inputSchema = z.object({ userId: z.string() });`

`trpc`

  `.router<Context>()`

  `.middleware(async ({ next, rawInput, ctx }) => {`

    `const result = inputSchema.safeParse(rawInput);`

    `if (!result.success) throw new TRPCError({ code: 'BAD_REQUEST' });`

    `const { userId } = result.data;`

    `// Check user id auth`

    `return next({ ctx: { ...ctx, userId } });`

  `})`

  `.query('userId', {`

    `input: inputSchema,`

    `resolve({ ctx }) {`

      `return ctx.userId;`

    `},`

  `});`
