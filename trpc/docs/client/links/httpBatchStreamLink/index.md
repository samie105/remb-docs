---
title: "HTTP Batch Stream Link"
source: "https://trpc.io/docs/client/links/httpBatchStreamLink"
canonical_url: "https://trpc.io/docs/client/links/httpBatchStreamLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:53.448Z"
content_hash: "29d613169e361c7cdd92b7a6a2cb6cf34cfcaa69fa6a46d0762d61f2738a946f"
menu_path: ["HTTP Batch Stream Link"]
section_path: []
nav_prev: {"path": "trpc/docs/client/links/httpLink/index.md", "title": "HTTP Link"}
nav_next: {"path": "trpc/docs/client/links/httpSubscriptionLink/index.md", "title": "HTTP Subscription Link"}
---

`httpBatchStreamLink` is a [**terminating link**](trpc/docs/client/links/index.md#the-terminating-link) that batches an array of individual tRPC operations into a single HTTP request that's sent to a single tRPC procedure (equivalent to [`httpBatchLink`](trpc/docs/client/links/httpBatchLink/index.md)), but doesn't wait for all the responses of the batch to be ready and streams the responses as soon as any data is available.

## Options[​](#options "Direct link to Options")

Options are identical to [`httpBatchLink options`](trpc/docs/client/links/httpBatchLink/index.md#options), with the following addition:

Option

Type

Default

Description

`streamHeader`

`'trpc-accept'` | `'accept'`

`'trpc-accept'`

Which header to use to signal the server that the client wants a streaming response. `'accept'` uses the standard `Accept` header instead of the custom `trpc-accept` header, which can avoid CORS preflight for cross-origin streaming queries since `Accept` is a CORS-safelisted header.

## Usage[​](#usage "Direct link to Usage")

> All usage and options are identical to [`httpBatchLink`](trpc/docs/client/links/httpBatchLink/index.md).

note

If you require the ability to change/set response headers (which includes cookies) from within your procedures, make sure to use `httpBatchLink` instead! This is due to the fact that `httpBatchStreamLink` does not support setting headers once the stream has begun. [Read more](trpc/docs/client/links/httpBatchLink/index.md).

You can import and add the `httpBatchStreamLink` to the `links` array as such:

client/index.ts

ts

`import { createTRPCClient, httpBatchStreamLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchStreamLink({`

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

## Streaming mode[​](#streaming-mode "Direct link to Streaming mode")

When batching requests together, the behavior of a regular `httpBatchLink` is to wait for all requests to finish before sending the response. If you want to send responses as soon as they are ready, you can use `httpBatchStreamLink` instead. This is useful for long-running requests.

client/index.ts

ts

`import { createTRPCClient, httpBatchStreamLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchStreamLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

Compared to a regular `httpBatchLink`, a `httpBatchStreamLink` will:

*   Cause the requests to be sent with a `trpc-accept: application/jsonl` header (or `Accept: application/jsonl` when using `streamHeader: 'accept'`)
*   Cause the response to be sent with a `transfer-encoding: chunked` and `content-type: application/jsonl`
*   Remove the `data` key from the argument object passed to `responseMeta` (because with a streamed response, the headers are sent before the data is available)

## Async generators and deferred promises[​](#generators "Direct link to Async generators and deferred promises")

You can try this out on the homepage of tRPC.io: [https://trpc.io/?try=minimal#try-it-out](https://trpc.io/?try=minimal#try-it-out)

ts

`import { createTRPCClient, httpBatchStreamLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const trpc = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchStreamLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

`const iterable = await trpc.examples.iterable.query();`

`for await (const value of iterable) {`

  `console.log('Iterable:', value);`

`}`

## Compatibility (client-side)[​](#compatibility-client-side "Direct link to Compatibility (client-side)")

### Browsers[​](#browsers "Direct link to Browsers")

Browser support should be identical to [`fetch`](https://caniuse.com/fetch) support.

### Node.js / Deno[​](#nodejs--deno "Direct link to Node.js / Deno")

For runtimes other than the browser ones, the `fetch` implementation should support streaming, meaning that the response obtained by `await fetch(...)` should have a `body` property of type `ReadableStream<Uint8Array> | NodeJS.ReadableStream`, meaning that:

*   either `response.body.getReader` is a function that returns a `ReadableStreamDefaultReader<Uint8Array>` object
*   or `response.body` is a `Uint8Array` `Buffer`

This includes support for `undici`, `node-fetch`, native Node.js fetch implementation, and WebAPI fetch implementation (browsers).

### React Native[​](#react-native "Direct link to React Native")

Receiving the stream relies on the `TextDecoder` and `TextDecoderStream` APIs, which are not available in React Native. It's important to note that if your `TextDecoderStream` polyfill does not automatically polyfill `ReadableStream` and `WritableStream` those will also need to be polyfilled. If you still want to enable streaming, you need to polyfill those.

You will also need to override the default fetch in the `httpBatchStreamLink` configuration options. In the below example we will be using the [Expo fetch](https://docs.expo.dev/versions/latest/sdk/expo/) package for the fetch implementation.

ts

`import { httpBatchStreamLink } from '@trpc/client';`

`httpBatchStreamLink({`

  `fetch: (url, opts) =>`

    `fetch(url, {`

      `...opts,`

      `reactNative: { textStreaming: true },`

    `}),`

  `url: 'http://localhost:3000',`

`});`

## Compatibility (server-side)[​](#compatibility-server-side "Direct link to Compatibility (server-side)")

AWS Lambda

`httpBatchStreamLink` only supported on AWS Lambda when your [infrastructure is set up](trpc/docs/server/adapters/aws-lambda/index.md#aws-lambda-response-streaming-adapter) for streaming responses. If not this Link will simply behave like a regular `httpBatchLink`.

## Reference[​](#reference "Direct link to Reference")

You can check out the source code for this link on [GitHub.](https://github.com/trpc/trpc/blob/main/packages/client/src/links/httpBatchStreamLink.ts)

## Configure a ping option to keep the connection alive[​](#configure-a-ping-option-to-keep-the-connection-alive "Direct link to Configure a ping option to keep the connection alive")

When setting up your root config, you can pass in a `jsonl` option to configure a ping option to keep the connection alive.

ts

`import { initTRPC } from '@trpc/server';`

`const t = initTRPC.create({`

  `jsonl: {`

    `pingMs: 1000,`

  `},`

`});`

