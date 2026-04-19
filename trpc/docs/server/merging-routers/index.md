---
title: "Merging Routers"
source: "https://trpc.io/docs/server/merging-routers"
canonical_url: "https://trpc.io/docs/server/merging-routers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:55.012Z"
content_hash: "8a8daaca720a179ccb8d7327f824ff7715f2b0227a261da42d10fc6b0ce349f1"
menu_path: ["Merging Routers"]
section_path: []
nav_prev: {"path": "trpc/docs/server/error-handling/index.md", "title": "Error Handling"}
nav_next: {"path": "trpc/docs/server/metadata/index.md", "title": "Metadata"}
---

Writing all API-code in the same file can become unwieldy. It's easy to merge routers together in order to break them up.

## Merging with child routers[​](#merging-with-child-routers "Direct link to Merging with child routers")

routers/user.ts

ts

`import { router, publicProcedure } from '../trpc';`

`import { z } from 'zod';`

`export const userRouter = router({`

  `list: publicProcedure.query(() => {`

    `// [..]`

    `return [];`

  `}),`

`});`

routers/post.ts

ts

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

      `// [...]`

    `}),`

  `list: publicProcedure.query(() => {`

    `// ...`

    `return [];`

  `}),`

`});`

routers/\_app.ts

ts

`import { router } from '../trpc';`

`import { userRouter } from './user';`

`import { postRouter } from './post';`

`const appRouter = router({`

  `user: userRouter,`

  `post: postRouter,`

`});`

`appRouter.user`

           `(property) user: DecorateCreateRouterOptions<{     list: QueryProcedure<{         input: void;         output: never[];         meta: object;     }>; }>`

`appRouter.post`

           `(property) post: DecorateCreateRouterOptions<{     create: MutationProcedure<{         input: {             title: string;         };         output: void;         meta: object;     }>;     list: QueryProcedure<{         input: void;         output: never[];         meta: object;     }>; }>`

`export type AppRouter = typeof appRouter;`

## Merging with `t.mergeRouters`[​](#merging-with-tmergerouters "Direct link to merging-with-tmergerouters")

If you prefer having all procedures flat in one single namespace, you can instead use `t.mergeRouters`

routers/user.ts

ts

`import { router, publicProcedure } from '../trpc';`

`import { z } from 'zod';`

`export const userRouter = router({`

  `userList: publicProcedure.query(() => {`

    `// [..]`

    `return [];`

  `}),`

`});`

routers/post.ts

ts

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

      `// [...]`

    `}),`

  `postList: publicProcedure.query(() => {`

    `// ...`

    `return [];`

  `}),`

`});`

routers/\_app.ts

ts

`import { mergeRouters } from '../trpc';`

`import { userRouter } from './user';`

`import { postRouter } from './post';`

`const appRouter = mergeRouters(userRouter, postRouter);`

         `const appRouter: BuiltRouter<{     ctx: object;     meta: object;     errorShape: DefaultErrorShape;     transformer: false; }, DecorateCreateRouterOptions<{     postCreate: MutationProcedure<{         input: {             title: string;         };         output: void;         meta: object;     }>;     postList: QueryProcedure<{         input: void;         output: never[];         meta: object;     }>; }> & DecorateCreateRouterOptions<{     userList: QueryProcedure<{         input: void;         output: never[];         meta: object;     }>; }>>`

`export type AppRouter = typeof appRouter;`

## Dynamically load routers[​](#lazy-load "Direct link to Dynamically load routers")

You can use the `lazy` function to dynamically load your routers. This can be useful to reduce cold starts of your application. There's no difference in how you use the router after it's been lazy loaded vs. how you use a normal router.

routers/greeting.ts

ts

`import { router, publicProcedure } from '../trpc';`

`export const greetingRouter = router({`

  `hello: publicProcedure.query(() => 'world'),`

`});`

routers/user.ts

ts

`import { router, publicProcedure } from '../trpc';`

`export const userRouter = router({`

  `list: publicProcedure.query(() => ['John', 'Jane', 'Jim']),`

`});`

routers/\_app.ts

ts

`import { lazy } from '@trpc/server';`

`import { router } from '../trpc';`

`export const appRouter = router({`

  `// Option 1: Short-hand when the module has exactly 1 router exported`

  `greeting: lazy(() => import('./greeting.js')),`

  `// Option 2: if exporting more than 1 router`

  `user: lazy(() => import('./user.js').then((m) => m.userRouter)),`

`});`

`export type AppRouter = typeof appRouter;`
