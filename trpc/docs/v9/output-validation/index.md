---
title: "Output Validation"
source: "https://trpc.io/docs/v9/output-validation"
canonical_url: "https://trpc.io/docs/v9/output-validation"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:05.746Z"
content_hash: "cd4f473065d2b66d1818db724110aaa81dc17ce4f01103d7a3e473aa100e6612"
menu_path: ["Output Validation"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/nextjs/index.md", "title": "Usage with Next.js"}
nav_next: {"path": "trpc/docs/v9/quickstart/index.md", "title": "Quickstart"}
---

tRPC gives you automatic type-safety of outputs without the need of adding a validator; however, it can be useful at times to strictly define the output type in order to prevent sensitive data of being leaked.

Similar to `input:`, an `output:` validation to the `query()` and `mutation()` router methods. The output validator is invoked with the payload returned by the `resolve()` function.

When an `output` validator is defined, its inferred type is expected as the return type of the `resolve()` function.

info

*   This is entirely optional and only if you want to ensure you don't accidentally leak anything e
*   If output validation fails, the server will respond with a `INTERNAL_SERVER_ERROR`.

## Examples[​](#examples "Direct link to Examples")

tRPC works out-of-the-box with yup/superstruct/zod/myzod/custom validators/\[..\] - [see test suite](https://github.com/trpc/trpc/blob/feature/output-parser-oas/packages/server/test/outputParser.test.ts)

### With [Zod](https://github.com/colinhacks/zod)[​](#with-zod "Direct link to with-zod")

tsx

`import * as trpc from '@trpc/server';`

`import { z } from 'zod';`

`// [...]`

`export const appRouter = trpc.router<Context>().query('hello', {`

  `output: z.object({`

    `greeting: z.string(),`

  `}),`

  `// expects return type of { greeting: string }`

  `resolve() {`

    `return {`

      `greeting: 'hello!',`

    `};`

  `},`

`});`

`export type AppRouter = typeof appRouter;`

### With [Yup](https://github.com/jquense/yup)[​](#with-yup "Direct link to with-yup")

tsx

`import * as trpc from '@trpc/server';`

`import * as yup from 'yup';`

`// [...]`

`export const appRouter = trpc.router<Context>().query('hello', {`

  `output: yup.object({`

    `greeting: yup.string().required(),`

  `}),`

  `resolve() {`

    `return { greeting: 'hello!' };`

  `},`

`});`

`export type AppRouter = typeof appRouter;`

### With [Superstruct](https://github.com/ianstormtaylor/superstruct)[​](#with-superstruct "Direct link to with-superstruct")

tsx

`import * as trpc from '@trpc/server';`

`import * as t from 'superstruct';`

`// [...]`

`export const appRouter = trpc.router<Context>().query('hello', {`

  `input: t.string(),`

  `output: t.object({`

    `greeting: t.string(),`

  `}),`

  `resolve({ input }) {`

    `return { greeting: input };`

  `},`

`});`

`export type AppRouter = typeof appRouter;`

### With custom validator[​](#with-custom-validator "Direct link to With custom validator")

tsx

`import * as trpc from '@trpc/server';`

`import * as t from 'superstruct';`

`// [...]`

`export const appRouter = trpc.router<Context>().query('hello', {`

  `output: (value: any) => {`

    `if (value && typeof value.greeting === 'string') {`

      `return { greeting: value.greeting };`

    `}`

    `throw new Error('Greeting not found');`

  `},`

  `// expects return type of { greeting: string }`

  `resolve() {`

    `return { greeting: 'hello!' };`

  `},`

`});`

`export type AppRouter = typeof appRouter;`


