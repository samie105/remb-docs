---
title: "Authorization"
source: "https://trpc.io/docs/server/authorization"
canonical_url: "https://trpc.io/docs/server/authorization"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:33.782Z"
content_hash: "3333d47935db88baf55324c941fe5fcb2a1a405e6c3730f3a28f3ce6b94c2a73"
menu_path: ["Authorization"]
section_path: []
nav_prev: {"path": "trpc/docs/server/adapters/standalone/index.md", "title": "Standalone Adapter"}
nav_next: {"path": "trpc/docs/server/caching/index.md", "title": "Response Caching"}
---

The `createContext` function is called for each incoming request, so here you can add contextual information about the calling user from the request object.

server/context.ts

ts

`import type { CreateHTTPContextOptions } from '@trpc/server/adapters/standalone';`

`import { decodeAndVerifyJwtToken } from './utils';`

`export async function createContext({ req, res }: CreateHTTPContextOptions) {`

  `// Create your context based on the request object`

  ``// Will be available as `ctx` in all your resolvers``

  `// This is just an example of something you might want to do in your ctx fn`

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

`export type Context = Awaited<ReturnType<typeof createContext>>;`

server/routers/\_app.ts

ts

`import { initTRPC, TRPCError } from '@trpc/server';`

`import { z } from 'zod';`

`type Context = { user: { name: string } | null };`

`export const t = initTRPC.context<Context>().create();`

`const appRouter = t.router({`

  `// open for anyone`

  `hello: t.procedure`

    `.input(z.string().nullish())`

    ``.query((opts) => `hello ${opts.input ?? opts.ctx.user?.name ?? 'world'}`),``

  `// checked in resolver`

  `secret: t.procedure.query((opts) => {`

    `if (!opts.ctx.user) {`

      `throw new TRPCError({ code: 'UNAUTHORIZED' });`

    `}`

    `return {`

      `secret: 'sauce',`

    `};`

  `}),`

`});`

## Option 2: Authorize using middleware[​](#option-2-authorize-using-middleware "Direct link to Option 2: Authorize using middleware")

server/routers/\_app.ts

ts

`import { initTRPC, TRPCError } from '@trpc/server';`

`import { z } from 'zod';`

`type Context = { user: { name: string } | null };`

`export const t = initTRPC.context<Context>().create();`

`// you can reuse this for any procedure`

`export const protectedProcedure = t.procedure.use(`

  `async function isAuthed(opts) {`

    `const { ctx } = opts;`

    ``// `ctx.user` is nullable``

    `if (!ctx.user) {`

              `(property) user: {     name: string; } | null`

      `throw new TRPCError({ code: 'UNAUTHORIZED' });`

    `}`

    `return opts.next({`

      `ctx: {`

        `// ✅ user value is known to be non-null now`

        `user: ctx.user,`

         `(property) user: {     name: string; }`

      `},`

    `});`

  `},`

`);`

`t.router({`

  `// this is accessible for everyone`

  `hello: t.procedure`

    `.input(z.string().nullish())`

    ``.query((opts) => `hello ${opts.input ?? opts.ctx.user?.name ?? 'world'}`),``

  `admin: t.router({`

    `// this is accessible only to admins`

    `secret: protectedProcedure.query((opts) => {`

      `return {`

        `secret: 'sauce',`

      `};`

    `}),`

  `}),`

`});`

