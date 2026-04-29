---
title: "HTTP RPC Specification"
source: "https://trpc.io/docs/rpc"
canonical_url: "https://trpc.io/docs/rpc"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:53.945Z"
content_hash: "4a62eb857e39f92ef6de146b97a8ef577a0fd574f65025c9ad987f27e9823c39"
menu_path: ["HTTP RPC Specification"]
section_path: []
nav_prev: {"path": "trpc/docs/openapi/index.md", "title": "OpenAPI (alpha)"}
nav_next: {"path": "trpc/docs/server/adapters/index.md", "title": "Overview"}
---

## Methods <-> Type mapping[​](#methods---type-mapping "Direct link to Methods <-> Type mapping")

HTTP Method

Mapping

Notes

`GET`

`.query()`

Input JSON-stringified in query param.  
_e.g._ `myQuery?input=${encodeURIComponent(JSON.stringify(input))}`

`POST`

`.mutation()`

Input as POST body.

`GET`

`.subscription()`

Subscriptions are supported via [Server-sent Events](../client/links/httpSubscriptionLink/index.md) using `httpSubscriptionLink`, or via [WebSockets](../server/websockets/index.md) using `wsLink`.

## Accessing nested procedures[​](#accessing-nested-procedures "Direct link to Accessing nested procedures")

Nested procedures are separated by dots, so a request to `byId` below would end up being a request to `/api/trpc/post.byId`.

ts

`export const appRouter = router({`

  `post: router({`

    `byId: publicProcedure.input(String).query(async (opts) => {`

      `// [...]`

    `}),`

  `}),`

`});`

## Batching[​](#batching "Direct link to Batching")

When batching, we combine all parallel procedure calls of the same HTTP method in one request using a data loader.

*   The called procedures' names are combined by a comma (`,`) in the `pathname`
*   Input parameters are sent as a query parameter called `input` which has the shape `Record<number, unknown>`.
*   We also need to pass `batch=1` as a query parameter.
*   If the response has different statuses, we send back `207 Multi-Status` _(e.g., if one call errored and one succeeded)_

### Batching Example Request[​](#batching-example-request "Direct link to Batching Example Request")

#### Given a router like this exposed at `/api/trpc`:[​](#given-a-router-like-this-exposed-at-apitrpc "Direct link to given-a-router-like-this-exposed-at-apitrpc")

server/router.ts

tsx

`export const appRouter = t.router({`

  `postById: t.procedure.input(String).query(async (opts) => {`

    `const post = await opts.ctx.post.findUnique({`

      `where: { id: opts.input },`

    `});`

    `return post;`

  `}),`

  `relatedPosts: t.procedure.input(String).query(async (opts) => {`

    `const posts = await opts.ctx.findRelatedPostsById(opts.input);`

    `return posts;`

  `}),`

`});`

#### ... And two queries defined like this in a React component:[​](#-and-two-queries-defined-like-this-in-a-react-component "Direct link to ... And two queries defined like this in a React component:")

MyComponent.tsx

tsx

`export function MyComponent() {`

  `const post1 = trpc.postById.useQuery('1');`

  `const relatedPosts = trpc.relatedPosts.useQuery('1');`

  `return (`

    `<pre>`

      `{JSON.stringify(`

        `{`

          `post1: post1.data ?? null,`

          `relatedPosts: relatedPosts.data ?? null,`

        `},`

        `null,`

        `4,`

      `)}`

    `</pre>`

  `);`

`}`

#### The above would result in exactly 1 HTTP call with this data:[​](#the-above-would-result-in-exactly-1-http-call-with-this-data "Direct link to The above would result in exactly 1 HTTP call with this data:")

Location property

Value

`pathname`

`/api/trpc/postById,relatedPosts`

`search`

`?batch=1&input=%7B%220%22%3A%221%22%2C%221%22%3A%221%22%7D` \*

**\*) `input` in the above is the result of:**

ts

`encodeURIComponent(`

  `JSON.stringify({`

    `` 0: '1', // <-- input for `postById` ``

    `` 1: '1', // <-- input for `relatedPosts` ``

  `}),`

`);`

### Batching Example Response[​](#batching-example-response "Direct link to Batching Example Response")

Example output from server

## HTTP Response Specification[​](#http-response-specification "Direct link to HTTP Response Specification")

In order to have a specification that works regardless of the transport layer we try to conform to [JSON-RPC 2.0](https://www.jsonrpc.org/specification) where possible.

### Successful Response[​](#successful-response "Direct link to Successful Response")

Example JSON Response

ts

`interface SuccessResponse {`

  `result: {`

    `data: TOutput; // output from procedure`

  `}`

`}`

### Error Response[​](#error-response "Direct link to Error Response")

Example JSON Response  

*   When possible, we propagate HTTP status codes from the error thrown.
*   If the response has different statuses, we send back `207 Multi-Status` _(e.g., if one call errored and one succeeded)_
*   For more on errors and how to customize them see [Error Formatting](../server/error-formatting/index.md).

## Error Codes <-> HTTP Status[​](#error-codes---http-status "Direct link to Error Codes <-> HTTP Status")

ts

`const HTTP_STATUS_CODES = {`

  `PARSE_ERROR: 400,`

  `BAD_REQUEST: 400,`

  `UNAUTHORIZED: 401,`

  `PAYMENT_REQUIRED: 402,`

  `FORBIDDEN: 403,`

  `NOT_FOUND: 404,`

  `METHOD_NOT_SUPPORTED: 405,`

  `TIMEOUT: 408,`

  `CONFLICT: 409,`

  `PRECONDITION_FAILED: 412,`

  `PAYLOAD_TOO_LARGE: 413,`

  `UNSUPPORTED_MEDIA_TYPE: 415,`

  `UNPROCESSABLE_CONTENT: 422,`

  `PRECONDITION_REQUIRED: 428,`

  `TOO_MANY_REQUESTS: 429,`

  `CLIENT_CLOSED_REQUEST: 499,`

  `INTERNAL_SERVER_ERROR: 500,`

  `NOT_IMPLEMENTED: 501,`

  `BAD_GATEWAY: 502,`

  `SERVICE_UNAVAILABLE: 503,`

  `GATEWAY_TIMEOUT: 504,`

`} as const;`

## Error Codes <-> JSON-RPC 2.0 Error Codes[​](#error-codes---json-rpc-20-error-codes "Direct link to Error Codes <-> JSON-RPC 2.0 Error Codes")

Available codes & JSON-RPC code

### Overriding the default HTTP method[​](#overriding-the-default-http-method "Direct link to Overriding the default HTTP method")

To override the HTTP method used for queries/mutations, you can use the `methodOverride` option:

server/httpHandler.ts

tsx

`// Your server must separately allow the client to override the HTTP method`

`const handler = createHTTPHandler({`

  `router: router,`

  `allowMethodOverride: true,`

`});`

client/trpc.ts

tsx

`import { createTRPCClient, httpLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`// The client can then specify which HTTP method to use for all queries/mutations`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpLink({`

      ``url: `http://localhost:3000`,``

      `methodOverride: 'POST', // all queries and mutations will be sent to the tRPC Server as POST requests.`

    `}),`

  `],`

`});`

## Dig deeper[​](#dig-deeper "Direct link to Dig deeper")

You can read more details by drilling into the TypeScript definitions in

*   [/packages/server/src/unstable-core-do-not-import/rpc/envelopes.ts](https://github.com/trpc/trpc/tree/main/packages/server/src/unstable-core-do-not-import/rpc/envelopes.ts)
*   [/packages/server/src/unstable-core-do-not-import/rpc/codes.ts](https://github.com/trpc/trpc/tree/main/packages/server/src/unstable-core-do-not-import/rpc/codes.ts)
