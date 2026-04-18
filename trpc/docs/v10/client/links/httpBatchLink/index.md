---
title: "HTTP Batch Link"
source: "https://trpc.io/docs/v10/client/links/httpBatchLink"
canonical_url: "https://trpc.io/docs/v10/client/links/httpBatchLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:20.927Z"
content_hash: "43b22b54ed9f6499e8b2da178b88084a63403b1f9e9669a345cb39bf3ae72ebf"
menu_path: ["HTTP Batch Link"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/links/index.md", "title": "Links Overview"}
nav_next: {"path": "trpc/docs/v10/client/links/httpBatchStreamLink/index.md", "title": "HTTP Batch Stream Link"}
---

`httpBatchLink` is a [**terminating link**](trpc/docs/v10/client/links/index.md#the-terminating-link) that batches an array of individual tRPC operations into a single HTTP request that's sent to a single tRPC procedure.

## Usage[​](#usage "Direct link to Usage")

You can import and add the `httpBatchLink` to the `links` array as such:

client/index.ts

ts

`import { createTRPCProxyClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from '../server';`

`const client = createTRPCProxyClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

After that, you can make use of batching by setting all your procedures in a `Promise.all`. The code below will produce exactly **one** HTTP request and on the server exactly **one** database query:

ts

`const somePosts = await Promise.all([`

  `trpc.post.byId.query(1),`

  `trpc.post.byId.query(2),`

  `trpc.post.byId.query(3),`

`]);`

## `httpBatchLink` Options[​](#httpbatchlink-options "Direct link to httpbatchlink-options")

The `httpBatchLink` function takes an options object that has the `HTTPBatchLinkOptions` shape.

ts

`export interface HTTPBatchLinkOptions extends HTTPLinkOptions {`

  `maxURLLength?: number;`

`}`

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

    `| ((opts: { opList: Operation[] }) => HTTPHeaders | Promise<HTTPHeaders>);`

`}`

## Setting a maximum URL length[​](#setting-a-maximum-url-length "Direct link to Setting a maximum URL length")

When sending batch requests, sometimes the URL can become too large causing HTTP errors like [`413 Payload Too Large`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/413), [`414 URI Too Long`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/414), and [`404 Not Found`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404). The `maxURLLength` option will limit the number of requests that can be sent together in a batch.

client/index.ts

ts

`import { createTRPCProxyClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from '../server';`

`const client = createTRPCProxyClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

      `maxURLLength: 2083, // a suitable size`

    `}),`

  `],`

`});`

## Disabling request batching[​](#disabling-request-batching "Direct link to Disabling request batching")

### 1\. Disable `batching` on your server:[​](#1-disable-batching-on-your-server "Direct link to 1-disable-batching-on-your-server")

server.ts

ts

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`createHTTPServer({`

  `// [...]`

  `// 👇 disable batching`

  `batching: {`

    `enabled: false,`

  `},`

`});`

or, if you're using Next.js:

pages/api/trpc/\[trpc\].ts

ts

`export default trpcNext.createNextApiHandler({`

  `// [...]`

  `// 👇 disable batching`

  `batching: {`

    `enabled: false,`

  `},`

`});`

### 2\. Replace `httpBatchLink` with [`httpLink`](trpc/docs/v10/client/links/httpLink/index.md) in your tRPC Client[​](#2-replace-httpbatchlink-with-httplink-in-your-trpc-client "Direct link to 2-replace-httpbatchlink-with-httplink-in-your-trpc-client")

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

or, if you're using Next.js:

utils/trpc.ts

tsx

`import type { AppRouter } from '@/server/routers/app';`

`import { httpLink } from '@trpc/client';`

`import { createTRPCNext } from '@trpc/next';`

`export const trpc = createTRPCNext<AppRouter>({`

  `config() {`

    `return {`

      `links: [`

        `httpLink({`

          `url: '/api/trpc',`

        `}),`

      `],`

    `};`

  `},`

`});`

## Reference[​](#reference "Direct link to Reference")

You can check out the source code for this link on [GitHub.](https://github.com/trpc/trpc/blob/main/packages/client/src/links/httpBatchLink/index.ts)
