---
title: "HTTP Link"
source: "https://trpc.io/docs/v10/client/links/httpLink"
canonical_url: "https://trpc.io/docs/v10/client/links/httpLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:29.656Z"
content_hash: "ea49a9ad8ae0c584338214608a96dbca50b581907e74b2127aff5cb8cd7748fc"
menu_path: ["HTTP Link"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/links/httpBatchStreamLink/index.md", "title": "HTTP Batch Stream Link"}
nav_next: {"path": "trpc/docs/v10/client/links/loggerLink/index.md", "title": "Logger Link"}
---

Version: 10.x

`httpLink` is a [**terminating link**](trpc/docs/v10/client/links/index.md#the-terminating-link) that sends a tRPC operation to a tRPC procedure over HTTP.

`httpLink` supports both POST and GET requests.

## Usage[​](#usage "Direct link to Usage")

You can import and add the `httpLink` to the `links` array as such:

client/index.ts

ts

`import { createTRPCProxyClient, httpLink } from '@trpc/client';`

`import type { AppRouter } from '../server';`

`const client = createTRPCProxyClient<AppRouter>({`

  `links: [`

    `httpLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

## `httpLink` Options[​](#httplink-options "Direct link to httplink-options")

The `httpLink` function takes an options object that has the `HTTPLinkOptions` shape.

ts

`export interface HTTPLinkOptions {`

  `url: string;`

  `/**`

   `* Add ponyfill for fetch`

   `*/`

  `fetch?: typeof fetch;`

  `/**`

   `* Add ponyfill for AbortController`

   `*/`

  `AbortController?: typeof AbortController | null;`

  `/**`

   `* Headers to be set on outgoing requests or a callback that of said headers`

   `* @see http://trpc.io/docs/v10/header`

   `*/`

  `headers?:`

    `| HTTPHeaders`

    `| ((opts: { op: Operation }) => HTTPHeaders | Promise<HTTPHeaders>);`

`}`

## Reference[​](#reference "Direct link to Reference")

You can check out the source code for this link on [GitHub.](https://github.com/trpc/trpc/blob/main/packages/client/src/links/httpLink.ts)
