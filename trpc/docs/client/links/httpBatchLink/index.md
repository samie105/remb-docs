---
title: "HTTP Batch Link"
source: "https://trpc.io/docs/client/links/httpBatchLink"
canonical_url: "https://trpc.io/docs/client/links/httpBatchLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:46.897Z"
content_hash: "83406f954e8f3bf2915cf0a90f22f8f645562c3f3efdaa2c0c42972c27d6838c"
menu_path: ["HTTP Batch Link"]
section_path: []
nav_prev: {"path": "trpc/docs/client/links/index.md", "title": "Links Overview"}
nav_next: {"path": "trpc/docs/client/links/httpLink/index.md", "title": "HTTP Link"}
---

`httpBatchLink` is a [**terminating link**](trpc/docs/client/links/index.md#the-terminating-link) that batches an array of individual tRPC operations into a single HTTP request that's sent to a single tRPC procedure.

## Usage[​](#usage "Direct link to Usage")

You can import and add the `httpBatchLink` to the `links` array as such:

client/index.ts

ts

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

      `// transformer,`

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

## `httpBatchLink` Options[​](#options "Direct link to options")

The `httpBatchLink` function takes an options object that has the `HTTPBatchLinkOptions` shape.

ts

`export interface HTTPBatchLinkOptions extends HTTPLinkOptions {`

  `/**`

   `* Maximum length of HTTP URL allowed before operations are split into multiple requests`

   `* @default Infinity`

   `*/`

  `maxURLLength?: number;`

  `/**`

   `* Maximum number of operations allowed in a single batch request`

   `* @default Infinity`

   `*/`

  `maxItems?: number;`

`}`

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

    `| ((opts: { opList: NonEmptyArray<Operation> }) => HTTPHeaders | Promise<HTTPHeaders>);`

`}`

## Setting a maximum URL length[​](#setting-a-maximum-url-length "Direct link to Setting a maximum URL length")

When sending batch requests, sometimes the URL can become too large causing HTTP errors like [`413 Payload Too Large`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/413), [`414 URI Too Long`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/414), and [`404 Not Found`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404). The `maxURLLength` option will limit the number of requests that can be sent together in a batch.

client/index.ts

ts

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

      `maxURLLength: 2083, // a suitable size`

      `// alternatively, you can make all RPC-calls to be called with POST`

      `// methodOverride: 'POST',`

    `}),`

  `],`

`});`

## Limiting batch size[​](#limiting-batch-size "Direct link to Limiting batch size")

### 1\. Set a maximum batch size on your server:[​](#1-set-a-maximum-batch-size-on-your-server "Direct link to 1. Set a maximum batch size on your server:")

`maxBatchSize` limits how many operations may be sent in a single batch request. Requests exceeding this limit will be rejected with a `400 Bad Request` error. This can be passed to any tRPC adapter.

server.ts

ts

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`createHTTPServer({`

  `maxBatchSize: 10,`

`});`

or for example if using Next.js:

pages/api/trpc/\[trpc\].ts

ts

`export default trpcNext.createNextApiHandler({`

  `maxBatchSize: 10,`

`});`

### 2\. Set a matching limit on the client:[​](#2-set-a-matching-limit-on-the-client "Direct link to 2. Set a matching limit on the client:")

Use the `maxItems` option on your batch link to ensure the client doesn't exceed the server's limit. This splits large batches into multiple HTTP requests automatically

client/index.ts

ts

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from '../server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

      `// 👇 should be the same or lower than the server's maxBatchSize`

      `maxItems: 10,`

    `}),`

  `],`

`});`

## Disabling request batching[​](#disabling-request-batching "Direct link to Disabling request batching")

### 1\. Disable `batching` on your server:[​](#1-disable-batching-on-your-server "Direct link to 1-disable-batching-on-your-server")

server.ts

ts

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`import { appRouter } from './router';`

`createHTTPServer({`

  `router: appRouter,`

  `// 👇 disable batching`

  `allowBatching: false,`

`});`

or, if you're using Next.js:

pages/api/trpc/\[trpc\].ts

ts

`import { createNextApiHandler } from '@trpc/server/adapters/next';`

`import { appRouter } from '../../../router';`

`export default createNextApiHandler({`

  `router: appRouter,`

  `// 👇 disable batching`

  `allowBatching: false,`

`});`

### 2\. Replace `httpBatchLink` with [`httpLink`](trpc/docs/client/links/httpLink/index.md) in your tRPC Client[​](#2-replace-httpbatchlink-with-httplink-in-your-trpc-client "Direct link to 2-replace-httpbatchlink-with-httplink-in-your-trpc-client")

client/index.ts

ts

`import { createTRPCClient, httpLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

or, if you're using Next.js:

utils/trpc.ts

tsx

`import type { AppRouter } from '../server';`

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


