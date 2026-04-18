---
title: "HTTP Batch Stream Link"
source: "https://trpc.io/docs/v10/client/links/httpBatchStreamLink"
canonical_url: "https://trpc.io/docs/v10/client/links/httpBatchStreamLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:26.708Z"
content_hash: "82cf1adcef39087c508f35d081339e2a5490b06f447cfe8a07906c73cd3c7b4b"
menu_path: ["HTTP Batch Stream Link"]
section_path: []
---
`unstable_httpBatchStreamLink` is a [**terminating link**](https://trpc.io/docs/v10/client/links#the-terminating-link) that batches an array of individual tRPC operations into a single HTTP request that's sent to a single tRPC procedure (equivalent to [`httpBatchLink`](https://trpc.io/docs/v10/client/links/httpBatchLink)), but doesn't wait for all the responses of the batch to be ready and streams the responses as soon as any data is available.

info

We have prefixed this as `unstable_` as it's a new API, but you're safe to use it! [Read more](https://trpc.io/docs/faq#unstable).

## Usage[​](#usage "Direct link to Usage")

> All usage and options are identical to [`httpBatchLink`](https://trpc.io/docs/v10/client/links/httpBatchLink).

note

If you require the ability to change/set response headers (which includes cookies) from within your procedures, make sure to use `httpBatchLink` instead! This is due to the fact that `unstable_httpBatchStreamLink` does not support setting headers once the stream has begun. [Read more](https://trpc.io/docs/client/links/httpBatchLink).

You can import and add the `httpBatchStreamLink` to the `links` array as such:

client/index.ts

ts

`import { createTRPCProxyClient, httpBatchStreamLink } from '@trpc/client';`

`import type { AppRouter } from '../server';`

`const client = createTRPCProxyClient<AppRouter>({`

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

> ⚠️ This link is unstable and may change in the future.

When batching requests together, the behavior of a regular `httpBatchLink` is to wait for all requests to finish before sending the response. If you want to send responses as soon as they are ready, you can use `httpBatchStreamLink` instead. This is useful for long-running requests.

client/index.ts

ts

`import {`

  `createTRPCProxyClient,`

  `unstable_httpBatchStreamLink,`

`} from '@trpc/client';`

`import type { AppRouter } from '../server';`

`const client = createTRPCProxyClient<AppRouter>({`

  `links: [`

    `unstable_httpBatchStreamLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

Compared to a regular `httpBatchLink`, a `unstable_httpBatchStreamLink` will:

*   Cause the requests to be sent with a `Trpc-Batch-Mode: stream` header
*   Cause the response to be sent with a `Transfer-Encoding: chunked` and `Vary: trpc-batch-mode` headers
*   Remove the `data` key from the argument object passed to `responseMeta` (because with a streamed response, the headers are sent before the data is available)

## Compatibility (client-side)[​](#compatibility-client-side "Direct link to Compatibility (client-side)")

### Browsers[​](#browsers "Direct link to Browsers")

Browser support should be identical to [`fetch`](https://caniuse.com/fetch) support.

### Node.js / Deno[​](#nodejs--deno "Direct link to Node.js / Deno")

For runtimes other than the browser ones, the `fetch` implementation should support streaming, meaning that the response obtained by `await fetch(...)` should have a `body` property of type `ReadableStream<Uint8Array> | NodeJS.ReadableStream`, meaning that:

*   either `response.body.getReader` is a function that returns a `ReadableStreamDefaultReader<Uint8Array>` object
*   or `response.body` is a `Uint8Array` `Buffer`

This includes support for `undici`, `node-fetch`, native Node.js fetch implementation, and WebAPI fetch implementation (browsers).

### React Native[​](#react-native "Direct link to React Native")

Receiving the stream relies on the `TextDecoder` API, which is not available in React Native. If you still want to enable streaming, you can use a polyfill and pass it to the `httpBatchStreamLink` options:

ts

`unstable_httpBatchStreamLink({`

  `url: 'http://localhost:3000',`

  `textDecoder: new TextDecoder(),`

  `// ^? textDecoder: { decode: (input: Uint8Array) => string }`

`});`

## Compatibility (server-side)[​](#compatibility-server-side "Direct link to Compatibility (server-side)")

> ⚠️ for **aws lambda**, `unstable_httpBatchStreamLink` is not supported (will simply behave like a regular `httpBatchLink`). It should not break anything if enabled, but will not have any effect.

> ⚠️ for **cloudflare workers**, you need to enable the `ReadableStream` API through a feature flag: [`streams_enable_constructors`](https://developers.cloudflare.com/workers/platform/compatibility-dates#streams-constructors)

## Reference[​](#reference "Direct link to Reference")

You can check out the source code for this link on [GitHub.](https://github.com/trpc/trpc/blob/main/packages/client/src/links/httpBatchStreamLink.ts)
