---
title: "Authorization"
source: "https://trpc.io/docs/v9/authorization"
canonical_url: "https://trpc.io/docs/v9/authorization"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:04.067Z"
content_hash: "9a0bdf784b36823a68cfd3f8dfaf6f576a132743f5c0ff07adac6ef14feebe23"
menu_path: ["Authorization"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/index.md", "title": "tRPC | tRPC"}
nav_next: {"path": "trpc/docs/v9/awesome-trpc/index.md", "title": "Awesome tRPC Collection"}
---

The `createContext`\-function is called for each incoming request so here you can add contextual information about the calling user from the request object.

server/context.ts

ts

`import * as trpc from '@trpc/server';`

`import { inferAsyncReturnType } from '@trpc/server';`

`import * as trpcNext from '@trpc/server/adapters/next';`

`import { decodeAndVerifyJwtToken } from './somewhere/in/your/app/utils';`

`export async function createContext({`

  `req,`

  `res,`

`}: trpcNext.CreateNextContextOptions) {`

  `// Create your context based on the request object`

  ``// Will be available as `ctx` in all your resolvers``

  `// This is just an example of something you'd might want to do in your ctx fn`

  `async function getUserFromHeader() {`

    `if (req.headers.authorization) {`

      `const user = await decodeAndVerifyJwtToken(`

        `req.headers.authorization.split(' ')[1],`

      `);`

      `return user;`

    `}`

    `return null;`

  `}`

  `const user = await getUserFromHeader();`

  `return {`

    `user,`

  `};`

`}`

`type Context = inferAsyncReturnType<typeof createContext>;`

`// [..] Define API handler and app router`

server/routers/\_app.ts

ts

`import * as trpc from '@trpc/server';`

`import { TRPCError } from '@trpc/server';`

`import { createRouter } from '../createRouter';`

`export const appRouter = createRouter()`

  `// open for anyone`

  `.query('hello', {`

    `input: z.string().nullish(),`

    `resolve: (opts) => {`

      ``return `hello ${opts.input ?? opts.ctx.user?.name ?? 'world'}`;``

    `},`

  `})`

  `// checked in resolver`

  `.query('secret', {`

    `resolve: (opts) => {`

      `if (!opts.ctx.user) {`

        `throw new TRPCError({ code: 'UNAUTHORIZED' });`

      `}`

      `return {`

        `secret: 'sauce',`

      `};`

    `},`

  `});`

## Option 2: Authorize using middleware[​](#option-2-authorize-using-middleware "Direct link to Option 2: Authorize using middleware")

server/routers/\_app.ts

ts

`import * as trpc from '@trpc/server';`

`import { TRPCError } from '@trpc/server';`

`import { createRouter } from '../createRouter';`

`export const appRouter = createRouter()`

  `// this is accessible for everyone`

  `.query('hello', {`

    `input: z.string().nullish(),`

    `resolve: (opts) => {`

      ``return `hello ${opts.input ?? opts.ctx.user?.name ?? 'world'}`;``

    `},`

  `})`

  `.merge(`

    `'admin.',`

    `createRouter()`

      `// this protects all procedures defined next in this router`

      `.middleware(async ({ ctx, next }) => {`

        `if (!ctx.user?.isAdmin) {`

          `throw new TRPCError({ code: 'UNAUTHORIZED' });`

        `}`

        `return next();`

      `})`

      `.query('secret', {`

        `resolve: (opts) => {`

          `return {`

            `secret: 'sauce',`

          `};`

        `},`

      `}),`

  `);`

This middleware can be re-used for multiple sub-routers by creating a [protected router](trpc/docs/v9/middlewares/index.md#createprotectedrouter-helper) helper.
