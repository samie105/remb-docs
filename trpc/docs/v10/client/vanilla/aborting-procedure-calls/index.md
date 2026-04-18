---
title: "Aborting Procedure Calls"
source: "https://trpc.io/docs/v10/client/vanilla/aborting-procedure-calls"
canonical_url: "https://trpc.io/docs/v10/client/vanilla/aborting-procedure-calls"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:49.855Z"
content_hash: "1690d665f2f21f2dacabac72491fbca49354081e67ab0ff9f125b3ac3fe1925c"
menu_path: ["Aborting Procedure Calls"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/react/useUtils/index.md", "title": "useUtils"}
nav_next: {"path": "trpc/docs/v10/client/vanilla/setup/index.md", "title": "Set up a tRPC Client"}
---

tRPC adheres to the industry standard when it comes to aborting procedures. All you have to do is pass an `AbortSignal` to the query or mutation options, and call the `AbortController` instance's `abort` method if you need to cancel the request.

utils.ts

ts

`// @filename: server.ts`

`import { createTRPCProxyClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from 'server.ts';`

`const proxy = createTRPCProxyClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000/trpc',`

    `}),`

  `],`

`});`

`// 1. Create an AbortController instance - this is a standard javascript API`

`const ac = new AbortController();`

`// 2. Pass the signal to a query or mutation`

`const query = proxy.userById.query('id_bilbo', { signal: ac.signal });`

`// 3. Cancel the request if needed`

`ac.abort();`


