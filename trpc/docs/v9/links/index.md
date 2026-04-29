---
title: "Links & Request Batching"
source: "https://trpc.io/docs/v9/links"
canonical_url: "https://trpc.io/docs/v9/links"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:21.353Z"
content_hash: "59fd3ee7e1dcd499f5aa8d50484c3db123808be5558b187e1a9f2812cd78abd4"
menu_path: ["Links & Request Batching"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/invalidateQueries/index.md", "title": "invalidateQueries"}
nav_next: {"path": "trpc/docs/v9/love/index.md", "title": "Testimonials / Love"}
---

Similar to urql's [_exchanges_](https://formidable.com/open-source/urql/docs/architecture/) or Apollo's [links](https://www.apollographql.com/docs/react/api/link/introduction/). Links enables you to customize the flow of data between tRPC Client and the tRPC-server.

## Request Batching[​](#request-batching "Direct link to Request Batching")

Request batching is automatically enabled which batches your requests to the server, this can make the below code produce exactly **one** HTTP request and on the server exactly **one** database query:

ts

`// below will be done in the same request when batching is enabled`

`const somePosts = await Promise.all([`

  `client.query('post.byId', 1),`

  `client.query('post.byId', 2),`

  `client.query('post.byId', 3),`

`]);`

## Customizing data flow[​](#customizing-data-flow "Direct link to Customizing data flow")

> The below examples assuming you use Next.js, but the same as below can be added if you use the vanilla tRPC client

### Setting a maximum batch size[​](#setting-a-maximum-batch-size "Direct link to Setting a maximum batch size")

This limits the number of requests that can be sent together in batch ( useful to prevent the url from getting too large and run into [HTTP error 413](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/413) ).

server.ts

ts

`// 👇 import the httpBatchLink`

`import { httpBatchLink } from '@trpc/client/links/httpBatchLink';`

`import { withTRPC } from '@trpc/next';`

`import { AppType } from 'next/dist/shared/lib/utils';`

`import type { AppRouter } from 'pages/api/trpc/[trpc]';`

`const MyApp: AppType = ({ Component, pageProps }) => {`

  `return <Component {...pageProps} />;`

`};`

`export default withTRPC<AppRouter>({`

  `config() {`

    `return {`

      `links: [`

        `httpBatchLink({`

          `url: '/api/trpc',`

          `maxBatchSize: 10, // a reasonable size`

        `}),`

      `],`

    `};`

  `},`

`})(MyApp);`

### Disabling request batching[​](#disabling-request-batching "Direct link to Disabling request batching")

#### 1\. Disable `batching` on your server:[​](#1-disable-batching-on-your-server "Direct link to 1-disable-batching-on-your-server")

In your `[trpc].ts`:

pages/api/trpc/\[trpc\].ts

ts

`export default trpcNext.createNextApiHandler({`

  `// [...]`

  `// 👇 disable batching`

  `batching: {`

    `enabled: false,`

  `},`

`});`

#### 2\. Use batch-free link in your tRPC Client[​](#2-use-batch-free-link-in-your-trpc-client "Direct link to 2. Use batch-free link in your tRPC Client")

pages/\_app.tsx

tsx

`// 👇 import the httpLink`

`import { httpLink } from '@trpc/client/links/httpLink';`

`import { withTRPC } from '@trpc/next';`

`import { AppType } from 'next/dist/shared/lib/utils';`

`import type { AppRouter } from 'pages/api/trpc/[trpc]';`

`const MyApp: AppType = ({ Component, pageProps }) => {`

  `return <Component {...pageProps} />;`

`};`

`export default withTRPC<AppRouter>({`

  `config() {`

    `return {`

      `links: [`

        `httpLink({`

          `url: '/api/trpc',`

        `}),`

      `],`

    `};`

  `},`

  `// ssr: false,`

`})(MyApp);`

### Using a `splitLink` to control request flow[​](#using-a-splitlink-to-control-request-flow "Direct link to using-a-splitlink-to-control-request-flow")

#### Disable batching for certain requests[​](#disable-batching-for-certain-requests "Direct link to Disable batching for certain requests")

##### 1\. Configure client / `_app.tsx`[​](#1-configure-client--_apptsx "Direct link to 1-configure-client--_apptsx")

pages/\_app.tsx

tsx

`import { httpBatchLink } from '@trpc/client/links/httpBatchLink';`

`import { httpLink } from '@trpc/client/links/httpLink';`

`import { splitLink } from '@trpc/client/links/splitLink';`

`import { withTRPC } from '@trpc/next';`

`// [..]`

`export default withTRPC<AppRouter>({`

  `config() {`

    ``const url = `http://localhost:3000`;``

    `return {`

      `links: [`

        `splitLink({`

          `condition(op) {`

            `` // check for context property `skipBatch` ``

            `return op.context.skipBatch === true;`

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

    `};`

  `},`

`})(MyApp);`

##### 2\. Perform request without batching[​](#2-perform-request-without-batching "Direct link to 2. Perform request without batching")

MyComponent.tsx

tsx

`export function MyComponent() {`

  `const postsQuery = trpc.useQuery(['posts'], {`

    `context: {`

      `skipBatch: true,`

    `},`

  `});`

  `return (`

    `<pre>{JSON.stringify(postsQuery.data ?? null, null, 4)}</pre>`

  `)`

`})`

or:

client.ts

ts

`const postResult = client.query('posts', null, {`

  `context: {`

    `skipBatch: true,`

  `},`

`});`

### Creating a custom link[​](#creating-a-custom-link "Direct link to Creating a custom link")

pages/\_app.tsx

tsx

`import { TRPCLink } from '@trpc/client';`

`import type { AppRouter } from 'pages/api/trpc/[trpc]';`

`const customLink: TRPCLink<AppRouter> = (runtime) => {`

  `// here we just got initialized in the app - this happens once per app`

  `// useful for storing cache for instance`

  `return ({ prev, next, op }) => {`

    `// this is when passing the result to the next link`

    `next(op, (result) => {`

      `// this is when we've gotten result from the server`

      `if (result instanceof Error) {`

        `// maybe send to bugsnag?`

      `}`

      `prev(result);`

    `});`

  `};`

`};`

`export default withTRPC<AppRouter>({`

  `config() {`

    `return {`

      `links: [`

        `customLink,`

        `// [..]`

        `` // ❗ Make sure to end with a `httpBatchLink` or `httpLink` ``

      `],`

    `};`

  `},`

  `// ssr: false`

`})(MyApp);`
