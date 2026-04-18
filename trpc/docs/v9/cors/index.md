---
title: "Send cookies cross-origin"
source: "https://trpc.io/docs/v9/cors"
canonical_url: "https://trpc.io/docs/v9/cors"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:34.297Z"
content_hash: "f25b9e7de1d18f6c17fff67245d2845372403899b2892ed538e9282ed5c2cb50"
menu_path: ["Send cookies cross-origin"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/context/index.md", "title": "Request Context"}
nav_next: {"path": "trpc/docs/v9/data-transformers/index.md", "title": "Data Transformers"}
---

If your API reside on a different origin than your front-end and wish to send cookies to it, you will need to enable [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) on your server and send cookies with your requests by providing the option `{credentials: "include"}` to fetch.

The arguments provided to the fetch function used by tRPC can be modified as follow.

app.ts

ts

`import { createTRPCClient } from '@trpc/client';`

`const client = createTRPCClient<AppRouter>({`

  `url: 'YOUR_SERVER_URL',`

  `fetch(url, options) {`

    `return fetch(url, {`

      `...options,`

      `credentials: 'include',`

    `});`

  `},`

`});`


