---
title: "Define Router"
source: "https://trpc.io/docs/v9/router"
canonical_url: "https://trpc.io/docs/v9/router"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:42.899Z"
content_hash: "e29f1ee17d475e6ea94131f7010e17b2469b900897eebe39a23f1386f231d5fe"
menu_path: ["Define Router"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/react-queries/index.md", "title": "useQuery()"}
nav_next: {"path": "trpc/docs/v9/rpc/index.md", "title": "HTTP RPC Specification"}
---

info

*   A procedure can be viewed as the equivalent of a REST-endpoint.
*   There's no internal difference between queries and mutations apart from semantics.
*   Defining router is the same for queries, mutations, and subscription with the exception that subscriptions need to return a `Subscription`\-instance.

## Input validation[​](#input-validation "Direct link to Input validation")

tRPC works out-of-the-box with yup/superstruct/zod/myzod/custom validators/\[..\] - [see test suite](https://github.com/trpc/trpc/blob/main/packages/server/test/validators.test.ts)

### Example without input[​](#example-without-input "Direct link to Example without input")

tsx

`import * as trpc from '@trpc/server';`

`// [...]`

`export const appRouter = trpc`

  `.router<Context>()`

  `// Create procedure at path 'hello'`

  `.query('hello', {`

    `resolve({ ctx }) {`

      `return {`

        ``greeting: `hello world`,``

      `};`

    `},`

  `});`

### With [Zod](https://github.com/colinhacks/zod)[​](#with-zod "Direct link to with-zod")

tsx

`import * as trpc from '@trpc/server';`

`import { z } from 'zod';`

`// [...]`

`export const appRouter = trpc.router<Context>().query('hello', {`

  `input: z`

    `.object({`

      `text: z.string().nullish(),`

    `})`

    `.nullish(),`

  `resolve({ input }) {`

    `return {`

      ``greeting: `hello ${input?.text ?? 'world'}`,``

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

  `input: yup.object({`

    `text: yup.string().required(),`

  `}),`

  `resolve({ input }) {`

    `return {`

      ``greeting: `hello ${input?.text ?? 'world'}`,``

    `};`

  `},`

`});`

`export type AppRouter = typeof appRouter;`

### With [Superstruct](https://github.com/ianstormtaylor/superstruct)[​](#with-superstruct "Direct link to with-superstruct")

tsx

`import * as trpc from '@trpc/server';`

`import * as t from 'superstruct';`

`// [...]`

`export const appRouter = trpc.router<Context>().query('hello', {`

  `input: t.object({`

    `/**`

     `* Also supports inline doc strings when referencing the type.`

     `*/`

    `text: t.defaulted(t.string(), 'world'),`

  `}),`

  `resolve({ input }) {`

    `return {`

      ``greeting: `hello ${input.text}`,``

    `};`

  `},`

`});`

`export type AppRouter = typeof appRouter;`

## Method chaining[​](#method-chaining "Direct link to Method chaining")

To add multiple endpoints, you must chain the calls

tsx

`import * as trpc from '@trpc/server';`

`// [...]`

`export const appRouter = trpc`

  `.router<Context>()`

  `.query('hello', {`

    `resolve() {`

      `return {`

        ``text: `hello world`,``

      `};`

    `},`

  `})`

  `.query('bye', {`

    `resolve() {`

      `return {`

        ``text: `goodbye`,``

      `};`

    `},`

  `});`

`export type AppRouter = typeof appRouter;`


