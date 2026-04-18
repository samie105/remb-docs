---
title: "Send cookies cross-origin"
source: "https://trpc.io/docs/client/cors"
canonical_url: "https://trpc.io/docs/client/cors"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:35.632Z"
content_hash: "8b671d32d8829b38a97a6764eb62de5d5e2e063233dfe1f25b6ee8aa614a43ee"
menu_path: ["Send cookies cross-origin"]
section_path: []
---
If your API resides on a different origin than your front-end and you wish to send cookies to it, you will need to enable [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) on your server and send cookies with your requests by providing the option `{credentials: "include"}` to fetch.

The arguments provided to the fetch function used by tRPC can be modified as follows.

app.ts

ts

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'YOUR_SERVER_URL',`

      `fetch(url, options) {`

        `return fetch(url, {`

          `...options,`

          `credentials: 'include',`

        `});`

      `},`

    `}),`

  `],`

`});`

info

You also need to enable CORS on your server by modifying your [adapter](https://trpc.io/docs/server/adapters), or the HTTP server which fronts your API. The best way to do this varies adapter-by-adapter and based on your hosting infrastructure, and individual adapters generally document this process where applicable.
