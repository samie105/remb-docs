---
title: "useQuery()"
source: "https://trpc.io/docs/v10/client/react/useQuery"
canonical_url: "https://trpc.io/docs/v10/client/react/useQuery"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:31.055Z"
content_hash: "d90381c5f8cb81ea64a758bf50d432268d26f8595401da7260731c385629bac2"
menu_path: ["useQuery()"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/react/useQueries/index.md", "title": "useQueries()"}
nav_next: {"path": "trpc/docs/v10/client/react/useUtils/index.md", "title": "useUtils"}
---

note

The hooks provided by `@trpc/react-query` are a thin wrapper around @tanstack/react-query. For in-depth information about options and usage patterns, refer to their docs on [queries](https://tanstack.com/query/v4/docs/react/guides/queries).

tsx

`function useQuery(`

  `input: TInput,`

  `opts?: UseTRPCQueryOptions;`

`)`

`interface UseTRPCQueryOptions`

  `extends UseQueryOptions {`

  `trpc: {`

    `ssr?: boolean;`

    `abortOnUnmount?: boolean;`

    `context?: Record<string, unknown>;`

  `}`

`}`

Since `UseTRPCQueryOptions` extends @tanstack/react-query's `UseQueryOptions`, you can use any of their options here such as `enabled`, `refetchOnWindowFocus`, etc. We also have some `trpc` specific options that let you opt in or out of certain behaviors on a per-procedure level:

*   **`trpc.ssr`:** If you have `ssr: true` in your [global config](../../nextjs/setup/index.md#ssr-boolean-default-false), you can set this to false to disable ssr for this particular query. _Note that this does not work the other way around, i.e., you can not enable ssr on a procedure if your global config is set to false._
*   **`trpc.abortOnUnmount`:** Override the [global config](../../nextjs/setup/index.md#config-callback) and opt in or out of aborting queries on unmount.
*   **`trpc.context`:** Add extra meta data that could be used in [Links](../../../../client/links/index.md).

tip

If you need to set any options but don't want to pass any input, you can pass `undefined` instead.

You'll notice that you get autocompletion on the `input` based on what you have set in your `input` schema on your backend.

### Example[​](#example "Direct link to Example")

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
