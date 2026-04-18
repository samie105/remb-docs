---
title: "Split Link"
source: "https://trpc.io/docs/client/links/splitLink"
canonical_url: "https://trpc.io/docs/client/links/splitLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:17.892Z"
content_hash: "db70f8604b45fea1775282c21808c4e814aebeab594e5e3f09ec400784a892c3"
menu_path: ["Split Link"]
section_path: []
---
`splitLink` is a link that allows you to branch your link chain's execution depending on a given condition. Both the `true` and `false` branches are required. You can provide just one link, or multiple links per branch via an array.

It's important to note that when you provide links for `splitLink` to execute, `splitLink` will create an entirely new link chain based on the links you passed. Therefore, you need to use a [**terminating link**](https://trpc.io/docs/client/links#the-terminating-link) if you only provide one link or add the terminating link at the end of the array if you provide multiple links to be executed on a branch. Here's a visual representation of how `splitLink` works:

## Usage Example[​](#usage-example "Direct link to Usage Example")

### Disable batching for certain requests[​](#disable-batching-for-certain-requests "Direct link to Disable batching for certain requests")

Let's say you're using `httpBatchLink` as the terminating link in your tRPC client config. This means request batching is enabled in every request. However, if you need to disable batching only for certain requests, you would need to change the terminating link in your tRPC client config dynamically between `httpLink` and `httpBatchLink`. This is a perfect opportunity for `splitLink` to be used:

#### 1\. Configure client / `utils/trpc.ts`[​](#1-configure-client--utilstrpcts "Direct link to 1-configure-client--utilstrpcts")

client/index.ts

ts

`import {`

  `createTRPCClient,`

  `httpBatchLink,`

  `httpLink,`

  `splitLink,`

`} from '@trpc/client';`

`import type { AppRouter } from './server';`

``const url = `http://localhost:3000`;``

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `splitLink({`

      `condition(op) {`

        `` // check for context property `skipBatch` ``

        `return Boolean(op.context.skipBatch);`

      `},`

      `// when condition is true, use normal request`

      `true: httpLink({`

        `url,`

      `}),`

      `// when condition is false, use batching`

      `false: httpBatchLink({`

        `url,`

      `}),`

    `}),`

  `],`

`});`

#### 2\. Perform request without batching[​](#2-perform-request-without-batching "Direct link to 2. Perform request without batching")

client.ts

ts

`const postResult = proxy.posts.query(undefined, {`

  `context: {`

    `skipBatch: true,`

  `},`

`});`

or:

MyComponent.tsx

tsx

`import { trpc } from './trpc';`

`export function MyComponent() {`

  `const postsQuery = trpc.posts.useQuery(undefined, {`

    `trpc: {`

      `context: {`

        `skipBatch: true,`

      `},`

    `}`

  `});`

  `return (`

    `<pre>{JSON.stringify(postsQuery.data ?? null, null, 4)}</pre>`

  `)`

`}`

## `splitLink` Options[​](#splitlink-options "Direct link to splitlink-options")

The `splitLink` function takes an options object that has three fields: `condition`, `true`, and `false`.

ts

`declare function splitLink<TRouter extends AnyRouter = AnyRouter>(opts: {`

  `condition: (op: Operation) => boolean;`

  `/**`

   ``* The link to execute next if the test function returns `true`.``

   `*/`

  `true: TRPCLink<TRouter> | TRPCLink<TRouter>[];`

  `/**`

   ``* The link to execute next if the test function returns `false`.``

   `*/`

  `false: TRPCLink<TRouter> | TRPCLink<TRouter>[];`

`}): TRPCLink<TRouter>;`

## Reference[​](#reference "Direct link to Reference")

You can check out the source code for this link on [GitHub.](https://github.com/trpc/trpc/blob/main/packages/client/src/links/splitLink.ts)
