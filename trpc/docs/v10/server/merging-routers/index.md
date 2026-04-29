---
title: "Merging Routers"
source: "https://trpc.io/docs/v10/server/merging-routers"
canonical_url: "https://trpc.io/docs/v10/server/merging-routers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:29.985Z"
content_hash: "de879c98c1841a14375f133774dc0973c1ab925cde2dfb6babaae1ff4a88090b"
menu_path: ["Merging Routers"]
section_path: []
nav_prev: {"path": "../introduction/index.md", "title": "tRPC server documentation"}
nav_next: {"path": "../metadata/index.md", "title": "Metadata"}
---

Writing all API-code in your code in the same file is not a great idea. It's easy to merge routers with other routers.

server.ts

ts

`// @filename: trpc.ts`

`import { initTRPC } from '@trpc/server';`

`const t = initTRPC.create();`

`export const router = t.router;`

`export const publicProcedure = t.procedure;`

`// @filename: routers/_app.ts`

`import { router } from '../trpc';`

`import { z } from 'zod';`

`import { userRouter } from './user';`

`import { postRouter } from './post';`

`const appRouter = router({`

  `user: userRouter, // put procedures under "user" namespace`

  `post: postRouter, // put procedures under "post" namespace`

`});`

`// You can then access the merged route with`

`// http://localhost:3000/trpc/<NAMESPACE>.<PROCEDURE>`

`export type AppRouter = typeof appRouter;`

`// @filename: routers/post.ts`

`import { router, publicProcedure } from '../trpc';`

`import { z } from 'zod';`

`export const postRouter = router({`

  `create: publicProcedure`

    `.input(`

      `z.object({`

        `title: z.string(),`

      `}),`

    `)`

    `.mutation((opts) => {`

      `const { input } = opts;`

               `const input: {     title: string; }`

      `// [...]`

    `}),`

  `list: publicProcedure.query(() => {`

    `// ...`

    `return [];`

  `}),`

`});`

`// @filename: routers/user.ts`

`import { router, publicProcedure } from '../trpc';`

`import { z } from 'zod';`

`export const userRouter = router({`

  `list: publicProcedure.query(() => {`

    `// [..]`

    `return [];`

  `}),`

`});`

If you prefer having all procedures flat in one single namespace, you can instead use `t.mergeRouters`

server.ts

ts

`// @filename: trpc.ts`

`import { initTRPC } from '@trpc/server';`

`const t = initTRPC.create();`

`export const router = t.router;`

`export const publicProcedure = t.procedure;`

`export const mergeRouters = t.mergeRouters;`

`// @filename: routers/_app.ts`

`import { router, publicProcedure, mergeRouters } from '../trpc';`

`import { z } from 'zod';`

`import { userRouter } from './user';`

`import { postRouter } from './post';`

`const appRouter = mergeRouters(userRouter, postRouter)`

`export type AppRouter = typeof appRouter;`

`// @filename: routers/post.ts`

`import { router, publicProcedure } from '../trpc';`

`import { z } from 'zod';`

`export const postRouter = router({`

  `postCreate: publicProcedure`

    `.input(`

      `z.object({`

        `title: z.string(),`

      `}),`

    `)`

    `.mutation((opts) => {`

      `const { input } = opts;`

               `const input: {     title: string; }`

      `// [...]`

    `}),`

  `postList: publicProcedure.query(() => {`

    `// ...`

    `return [];`

  `}),`

`});`

`// @filename: routers/user.ts`

`import { router, publicProcedure } from '../trpc';`

`import { z } from 'zod';`

`export const userRouter = router({`

  `userList: publicProcedure.query(() => {`

    `// [..]`

    `return [];`

  `}),`

`});`
