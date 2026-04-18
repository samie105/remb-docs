---
title: "useQuery()"
source: "https://trpc.io/docs/client/react/useQuery"
canonical_url: "https://trpc.io/docs/client/react/useQuery"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:12.303Z"
content_hash: "e778d5684925393c938a9c752c3a882915b0d119ef582f4b0c53996f14836887"
menu_path: ["useQuery()"]
section_path: []
nav_prev: {"path": "trpc/docs/client/react/useQueries/index.md", "title": "useQueries()"}
nav_next: {"path": "trpc/docs/client/react/useSubscription/index.md", "title": "useSubscription()"}
---

`useQuery` is the primary hook for data fetching, it works similarly to `@tanstack/react-query`'s `useQuery`, but with some `trpc` specific options and additional features like streaming.

note

For in-depth information about options and usage patterns, refer to the TanStack Query docs on [queries](https://tanstack.com/query/v5/docs/framework/react/guides/queries).

## Signature[​](#signature "Direct link to Signature")

tsx

`declare function useQuery(`

  `input: TInput | SkipToken,`

  `opts?: UseTRPCQueryOptions,`

`): void;`

`interface UseTRPCQueryOptions`

  `extends UseQueryOptions {`

  `trpc: {`

    `ssr?: boolean;`

    `abortOnUnmount?: boolean;`

    `context?: Record<string, unknown>;`

  `}`

`}`

Since `UseTRPCQueryOptions` extends `@tanstack/react-query`'s `UseQueryOptions`, you can use any of their options here such as `enabled`, `refetchOnWindowFocus`, etc. We also have some `trpc` specific options that let you opt in or out of certain behaviors on a per-procedure level:

*   **`trpc.ssr`:** If you have `ssr: true` in your [global config](trpc/docs/client/nextjs/pages-router/setup/index.md#ssr-boolean-default-false), you can set this to false to disable ssr for this particular query. _Note that this does not work the other way around, i.e., you can not enable ssr on a procedure if your global config is set to false._
*   **`trpc.abortOnUnmount`:** Override the [global config](trpc/docs/client/nextjs/pages-router/setup/index.md#config-callback) and opt in or out of aborting queries on unmount.
*   **`trpc.context`:** Add extra meta data that could be used in [Links](trpc/docs/client/links/index.md).

tip

If you need to set any options but don't want to pass any input, you can pass `undefined` instead.

You'll notice that you get autocompletion on the `input` based on what you have set in your `input` schema on your backend.

## Example usage[​](#example-usage "Direct link to Example usage")

Backend code

components/MyComponent.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `// input is optional, so we don't have to pass second argument`

  `const helloNoArgs = trpc.hello.useQuery();`

  `const helloWithArgs = trpc.hello.useQuery({ text: 'client' });`

  `return (`

    `<div>`

      `<h1>Hello World Example</h1>`

      `<ul>`

        `<li>`

          `helloNoArgs ({helloNoArgs.status}):{' '}`

          `<pre>{JSON.stringify(helloNoArgs.data, null, 2)}</pre>`

        `</li>`

        `<li>`

          `helloWithArgs ({helloWithArgs.status}):{' '}`

          `<pre>{JSON.stringify(helloWithArgs.data, null, 2)}</pre>`

        `</li>`

      `</ul>`

    `</div>`

  `);`

`}`

## Streaming responses using async generators[​](#streaming "Direct link to Streaming responses using async generators")

When returning an async generator in a query, you will:

*   Get the results of the iterator in the `data`\-property **as an array** which updates as the response comes in
*   The `status` will be `success` as soon as the first chunk is received.
*   The `fetchStatus` property which will be `fetching` until the last chunk is received.

### Example[​](#example "Direct link to Example")

server/routers/\_app.ts

tsx

`import { initTRPC } from '@trpc/server';`

`const t = initTRPC.create();`

`const appRouter = t.router({`

  `iterable: t.procedure.query(async function* () {`

    `for (let i = 0; i < 3; i++) {`

      `await new Promise((resolve) => setTimeout(resolve, 500));`

      `yield i;`

    `}`

  `}),`

`});`

`export type AppRouter = typeof appRouter;`

components/MyComponent.tsx

tsx

`import React, { Fragment } from 'react';`

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const result = trpc.iterable.useQuery();`

  `return (`

    `<div>`

      `{result.data?.map((chunk, index) => (`

        `<Fragment key={index}>{chunk}</Fragment>`

      `))}`

    `</div>`

  `);`

`}`

`result` properties while streaming:

`status`

`fetchStatus`

`data`

`'pending'`

`'fetching'`

`undefined`

`'success'`

`'fetching'`

`[]`

`'success'`

`'fetching'`

`[0]`

`'success'`

`'fetching'`

`[0, 1]`

`'success'`

`'fetching'`

`[0, 1, 2]`

`'success'`

`'idle'`

`[0, 1, 2]`

