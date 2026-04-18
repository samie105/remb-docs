---
title: "useQuery()"
source: "https://trpc.io/docs/v9/react-queries"
canonical_url: "https://trpc.io/docs/v9/react-queries"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:32.460Z"
content_hash: "a435dece9ac289093d3f2384f70bfc292e1dd0e8ba5826680a47b3d5459974b3"
menu_path: ["useQuery()"]
section_path: []
---
> The hooks provided by `@trpc/react` are a thin wrapper around React Query. For in-depth information about options and usage patterns, refer to their docs on [Queries](https://tanstack.com/query/v3/docs/react/guides/queries).

tsx

`function useQuery(`

  `pathAndInput: [string, TInput?],`

  `opts?: UseTRPCQueryOptions;`

`)`

The first argument is a `[path, input]`\-tuple - if the `input` is optional, you can omit the `, input`\-part.

You'll notice that you get autocompletion on the `path` and automatic typesafety on the `input`.

### Example[​](#example "Direct link to Example")

Backend code

components/MyComponent.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `// input is optional, so we don't have to pass second argument`

  `const helloNoArgs = trpc.useQuery(['hello']);`

  `const helloWithArgs = trpc.useQuery(['hello', { text: 'client' }]);`

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
