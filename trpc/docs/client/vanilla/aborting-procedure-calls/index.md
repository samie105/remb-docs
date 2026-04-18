---
title: "Aborting Procedure Calls"
source: "https://trpc.io/docs/client/vanilla/aborting-procedure-calls"
canonical_url: "https://trpc.io/docs/client/vanilla/aborting-procedure-calls"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:56.036Z"
content_hash: "99f5879d020cd565d4a1eca643fb327ecac7153894b9a7acd6cb4f787bc780c7"
menu_path: ["Aborting Procedure Calls"]
section_path: []
---
tRPC supports the standard `AbortController`/`AbortSignal` API for aborting procedures. All you have to do is pass an `AbortSignal` to the query or mutation options, and call the `AbortController` instance's `abort` method if you need to cancel the request.

utils.ts

ts

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000/trpc',`

    `}),`

  `],`

`});`

`// 1. Create an AbortController instance - this is a standard javascript API`

`const ac = new AbortController();`

`// 2. Pass the signal to a query or mutation`

`const query = client.userById.query('id_bilbo', { signal: ac.signal });`

`// 3. Cancel the request if needed`

`ac.abort();`
