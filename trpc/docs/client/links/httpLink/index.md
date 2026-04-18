---
title: "HTTP Link"
source: "https://trpc.io/docs/client/links/httpLink"
canonical_url: "https://trpc.io/docs/client/links/httpLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:50.971Z"
content_hash: "c19c919d1138930b1b84cc363f63813917aaee6b1694fbe6c91ac3779d2efa9d"
menu_path: ["HTTP Link"]
section_path: []
nav_prev: {"path": "trpc/docs/client/links/httpBatchLink/index.md", "title": "HTTP Batch Link"}
nav_next: {"path": "trpc/docs/client/links/httpBatchStreamLink/index.md", "title": "HTTP Batch Stream Link"}
---

Version: 11.x

`httpLink` is a [**terminating link**](trpc/docs/client/links/index.md#the-terminating-link) that sends a tRPC operation to a tRPC procedure over HTTP.

`httpLink` supports both POST and GET requests.

## Usage[​](#usage "Direct link to Usage")

You can import and add the `httpLink` to the `links` array as such:

client/index.ts

ts

`import { createTRPCClient, httpLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpLink({`

      `url: 'http://localhost:3000',`

      `// transformer,`

    `}),`

  `],`

`});`

## `httpLink` Options[​](#httplink-options "Direct link to httplink-options")

The `httpLink` function takes an options object that has the `HTTPLinkOptions` shape.

ts

`export interface HTTPLinkOptions {`

  `url: string | URL;`

  `/**`

   `* Add ponyfill for fetch`

   `*/`

  `fetch?: typeof fetch;`

  `/**`

   `* Data transformer`

   `* @see https://trpc.io/docs/server/data-transformers`

   `**/`

  `transformer?: DataTransformerOptions;`

  `/**`

   `* Headers to be set on outgoing requests or a callback that of said headers`

   `* @see https://trpc.io/docs/client/headers`

   `*/`

  `headers?:`

    `| HTTPHeaders`

    `| ((opts: { op: Operation }) => HTTPHeaders | Promise<HTTPHeaders>);`

  `/**`

   `* Send all requests as POSTS requests regardless of the procedure type`

   `* The server must separately allow overriding the method. See:`

   `* @see https://trpc.io/docs/rpc`

   `*/`

  `methodOverride?: 'POST';`

`}`

## Reference[​](#reference "Direct link to Reference")

You can check out the source code for this link on [GitHub.](https://github.com/trpc/trpc/blob/main/packages/client/src/links/httpLink.ts)
