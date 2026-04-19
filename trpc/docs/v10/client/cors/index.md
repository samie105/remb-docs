---
title: "Send cookies cross-origin"
source: "https://trpc.io/docs/v10/client/cors"
canonical_url: "https://trpc.io/docs/v10/client/cors"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:04.963Z"
content_hash: "76a959db7fa49d588433411093dbc15c9bd663f304557390577d4b037d3d7560"
menu_path: ["Send cookies cross-origin"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/index.md", "title": "Client Overview"}
nav_next: {"path": "trpc/docs/v10/client/headers/index.md", "title": "Custom header"}
---

If your API resides on a different origin than your front-end and you wish to send cookies to it, you will need to enable [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) on your server and send cookies with your requests by providing the option `{credentials: "include"}` to fetch.

The arguments provided to the fetch function used by tRPC can be modified as follow.

app.ts

ts

`import { createTRPCProxyClient, httpBatchLink } from '@trpc/client';`

`const client = createTRPCProxyClient<AppRouter>({`

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

You also need to enable CORS on your server by modifying your [adapter](trpc/docs/server/adapters/index.md), or the HTTP server which fronts your API. The best way to do this varies adapter-by-adapter and based on your hosting infrastructure, and individual adapters generally document this process where applicable.
