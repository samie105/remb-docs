---
title: "HTTP RPC Specification"
source: "https://trpc.io/docs/v9/rpc"
canonical_url: "https://trpc.io/docs/v9/rpc"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:48.266Z"
content_hash: "066443fc2ddd4399b29b02cfb4c5b77bdf692eff54ab8e7e07b361547f0a9593"
menu_path: ["HTTP RPC Specification"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/router/index.md", "title": "Define Router"}
nav_next: {"path": "trpc/docs/v9/sponsors/index.md", "title": "Sponsors"}
---

## Methods <-> Type mapping[​](#methods---type-mapping "Direct link to Methods <-> Type mapping")

HTTP Method

Mapping

Notes

`GET`

`.query()`

Input JSON-stringified in query param.  
_e.g._ `myQuery?input=${encodeURIComponent(JSON.stringify(input))`

`POST`

`.mutation()`

Input as POST body.

_n/a_

`.subscription()`

_Subscriptions are not supported in HTTP transport_

## Batching[​](#batching "Direct link to Batching")

When batching, we combine all parallel procedure calls of the same type in one request using a data loader.

*   The called procedures' names are combined by a comma (`,`) in the `pathname`
*   Input parameters are sent as a query parameter called `input` which has the shape `Record<number, unknown>`.
*   We also need to pass `batch=1` as a query parameter.
*   If the response has different statuses we send back `207 Multi-Status` \_(e.g. if one call errored and one succeeded) \_

### Batching Example Request[​](#batching-example-request "Direct link to Batching Example Request")

#### Given a router like this exposed at `/api/trpc`:[​](#given-a-router-like-this-exposed-at-apitrpc "Direct link to given-a-router-like-this-exposed-at-apitrpc")

server/router.ts

tsx

`export const appRouter = trpc`

  `.router<Context>()`

  `.query('postById', {`

    `input: String,`

    `async resolve({ input, ctx }) {`

      `const post = await ctx.post.findUnique({`

        `where: { id: input },`

      `});`

      `return post;`

    `},`

  `})`

  `.query('relatedPosts', {`

    `input: String,`

    `async resolve({ ctx, input }) {`

      `const posts = await ctx.findRelatedPostsById(input);`

      `return posts;`

    `},`

  `});`

#### .. And two queries defined like this in a React component:[​](#-and-two-queries-defined-like-this-in-a-react-component "Direct link to .. And two queries defined like this in a React component:")

MyComponent.tsx

tsx

`export function MyComponent() {`

  `const post1 = trpc.useQuery(['postById', '1']);`

  `const relatedPosts = trpc.useQuery(['relatedPosts', '1']);`

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

`{`

  `id: null;`

  `result: {`

    `type: 'data';`

    `data: TOutput; // output from procedure`

  `}`

`}`

### Error Response[​](#error-response "Direct link to Error Response")

Example JSON Response  

*   When possible, we propagate HTTP status codes from the error thrown.
*   If the response has different statuses we send back `207 Multi-Status` \_(e.g. if one call errored and one succeeded) \_
*   For more on errors and how customize them see [Error Formatting](trpc/docs/v9/error-formatting/index.md).

## Error Codes <-> HTTP Status[​](#error-codes---http-status "Direct link to Error Codes <-> HTTP Status")

ts

`PARSE_ERROR: 400,`

`BAD_REQUEST: 400,`

`NOT_FOUND: 404,`

`INTERNAL_SERVER_ERROR: 500,`

`UNAUTHORIZED: 401,`

`FORBIDDEN: 403,`

`TIMEOUT: 408,`

`CONFLICT: 409,`

`CLIENT_CLOSED_REQUEST: 499,`

`PRECONDITION_FAILED: 412,`

`PAYLOAD_TOO_LARGE: 413,`

`METHOD_NOT_SUPPORTED: 405,`

## Error Codes <-> JSON-RPC 2.0 Error Codes[​](#error-codes---json-rpc-20-error-codes "Direct link to Error Codes <-> JSON-RPC 2.0 Error Codes")

Available codes & JSON-RPC code

## Dig deeper[​](#dig-deeper "Direct link to Dig deeper")

You can read more details by drilling into the TypeScript definitions in

*   [/packages/server/src/unstable-core-do-not-import/rpc/envelopes.ts](https://github.com/trpc/trpc/tree/main/packages/server/src/unstable-core-do-not-import/rpc/envelopes.ts)
*   [/packages/server/src/unstable-core-do-not-import/rpc/codes.ts](https://github.com/trpc/trpc/tree/main/packages/server/src/unstable-core-do-not-import/rpc/codes.ts).
