---
title: "Inferring Types"
source: "https://trpc.io/docs/v10/client/vanilla/infer-types"
canonical_url: "https://trpc.io/docs/v10/client/vanilla/infer-types"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:03.753Z"
content_hash: "dfce87e7b4fc1cf325e046f9046ecb7cd10505fcaeb8038bc0fc25555c8dbf58"
menu_path: ["Inferring Types"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/vanilla/setup/index.md", "title": "Set up a tRPC Client"}
nav_next: {"path": "trpc/docs/v10/community/contributing/index.md", "title": "Contributing"}
---

It is often useful to access the types of your API within your clients. For this purpose, you are able to infer the types contained in your `AppRouter`.

`@trpc/server` exports the following helper types to assist with inferring these types from the `AppRouter` exported by your `@trpc/server` router:

*   `inferRouterInputs<TRouter>`
*   `inferRouterOutputs<TRouter>`

## Inferring Input & Output Types[​](#inferring-input--output-types "Direct link to Inferring Input & Output Types")

Let's assume we have this example router:

server.ts

ts

`// @filename: server.ts`

`import { initTRPC } from '@trpc/server';`

`import { z } from "zod";`

`const t = initTRPC.create();`

`const appRouter = t.router({`

  `post: t.router({`

    `list: t.procedure`

      `.query(() => {`

        `// imaginary db call`

        `return [{ id: 1, title: 'tRPC is the best!' }];`

    `}),`

    `byId: t.procedure`

      `.input(z.string())`

      `.query((opts) => {`

        `// imaginary db call`

        `return { id: 1, title: 'tRPC is the best!' };`

    `}),`

    `create: t.procedure`

      `.input(z.object({ title: z.string(), text: z.string(), }))`

      `.mutation((opts) => {`

        `// imaginary db call`

        `return { id: 1, ...opts.input };`

    `}),`

  `}),`

`});`

`export type AppRouter = typeof appRouter;`

Using the helpers, we can infer the types of our router. The following example shows how to infer the types of the `post.create` procedure:

client.ts

ts

`// @filename: client.ts`

`import type { inferRouterInputs, inferRouterOutputs } from '@trpc/server';`

`import type { AppRouter } from './server';`

`type RouterInput = inferRouterInputs<AppRouter>;`

`type RouterOutput = inferRouterOutputs<AppRouter>;`

`type PostCreateInput = RouterInput['post']['create'];`

           `type PostCreateInput = {     title: string;     text: string; }`

`type PostCreateOutput = RouterOutput['post']['create'];`

            `type PostCreateOutput = {     title: string;     text: string;     id: number; }`

## Infer `TRPCClientError` types[​](#infer-trpcclienterror-types "Direct link to infer-trpcclienterror-types")

It's also useful to infer the error type for your `AppRouter`

client.ts

ts

`// @filename: client.ts`

`import { TRPCClientError } from '@trpc/client';`

`import type { AppRouter } from './server';`

`import { trpc } from './trpc';`

`export function isTRPCClientError(`

  `cause: unknown,`

`): cause is TRPCClientError<AppRouter> {`

  `return cause instanceof TRPCClientError;`

`}`

`async function main() {`

  `try {`

    `await trpc.post.byId.query('1');`

  `} catch (cause) {`

    `if (isTRPCClientError(cause)) {`

      `` // `cause` is now typed as your router's `TRPCClientError` ``

      `console.log('data', cause.data);`

                                 `(property) TRPCClientError<BuiltRouter<{ ctx: object; meta: object; errorShape: DefaultErrorShape; transformer: false; }, DecorateCreateRouterOptions<{ post: BuiltRouter<{ ctx: object; meta: object; errorShape: DefaultErrorShape; transformer: false; }, DecorateCreateRouterOptions<...>>; }>>>.data: Maybe<DefaultErrorData>`

    `} else {`

      `// [...]`

    `}`

  `}`

`}`

`main();`
