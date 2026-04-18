---
title: "Inferring Types"
source: "https://trpc.io/docs/client/vanilla/infer-types"
canonical_url: "https://trpc.io/docs/client/vanilla/infer-types"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:04.533Z"
content_hash: "3c31fa191b91f2d1faf4b9bb66f6e26f0f12d24ed98dddbff9463b815a0587c1"
menu_path: ["Inferring Types"]
section_path: []
nav_prev: {"path": "trpc/docs/client/vanilla/setup/index.md", "title": "Set up a tRPC Client"}
nav_next: {"path": "trpc/docs/community/awesome-trpc/index.md", "title": "Awesome tRPC Collection"}
---

It is often useful to access the types of your API within your clients. For this purpose, you are able to infer the types contained in your `AppRouter`.

`@trpc/server` exports the following helper types to assist with inferring these types from the `AppRouter` exported by your `@trpc/server` router:

*   `inferRouterInputs<TRouter>`
*   `inferRouterOutputs<TRouter>`
*   `inferProcedureInput<TProcedure>`
*   `inferProcedureOutput<TProcedure>`
*   `inferSubscriptionInput<TProcedure>`
*   `inferSubscriptionOutput<TProcedure>`

## Inferring Input & Output Types[​](#inferring-input--output-types "Direct link to Inferring Input & Output Types")

Let's assume we have this example router:

server.ts

ts

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

    `onPostAdd: t.procedure`

      `.input(z.object({ authorId: z.string() }))`

      `.subscription(async function* ({ input }) {`

        `// imaginary event source`

        `yield {`

          `id: 1,`

          `title: 'tRPC is the best!',`

          `authorId: input.authorId,`

        `};`

    `}),`

  `}),`

`});`

`export type AppRouter = typeof appRouter;`

Using the helpers, we can infer the types of our router. The following example shows how to infer the types of the `post.create` procedure:

client.ts

ts

`import type { inferRouterInputs, inferRouterOutputs } from '@trpc/server';`

`import type { AppRouter } from './server';`

`type RouterInput = inferRouterInputs<AppRouter>;`

`type RouterOutput = inferRouterOutputs<AppRouter>;`

`type PostCreateInput = RouterInput['post']['create'];`

`type PostCreateOutput = RouterOutput['post']['create'];`

## Inferring Individual Procedure Types[​](#inferring-individual-procedure-types "Direct link to Inferring Individual Procedure Types")

If you already have access to a specific procedure on your router, you can infer its input or output directly:

client.ts

ts

`import type {`

  `inferProcedureInput,`

  `inferProcedureOutput,`

`} from '@trpc/server';`

`import type { AppRouter } from './server';`

`type PostByIdInput = inferProcedureInput<AppRouter['post']['byId']>;`

`type PostByIdOutput = inferProcedureOutput<AppRouter['post']['byId']>;`

For subscriptions, you can infer the subscription input and the emitted data type:

client.ts

ts

`import type {`

  `inferSubscriptionInput,`

  `inferSubscriptionOutput,`

`} from '@trpc/server';`

`import type { AppRouter } from './server';`

`type OnPostAddInput = inferSubscriptionInput<AppRouter['post']['onPostAdd']>;`

`type OnPostAddOutput = inferSubscriptionOutput<AppRouter['post']['onPostAdd']>;`

## Infer `TRPCClientError` types[​](#infer-trpcclienterror-types "Direct link to infer-trpcclienterror-types")

It's also useful to infer the error type for your `AppRouter`

client.ts

ts

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

    `} else {`

      `// [...]`

    `}`

  `}`

`}`

`main();`

