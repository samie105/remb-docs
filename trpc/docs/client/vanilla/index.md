---
title: "tRPC Client"
source: "https://trpc.io/docs/client/vanilla"
canonical_url: "https://trpc.io/docs/client/vanilla"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:53.471Z"
content_hash: "876b6723937b2287c92decf47ed9796e88f63d1493b6b0e9d4300a366a1ddc71"
menu_path: ["tRPC Client"]
section_path: []
nav_prev: {"path": "../tanstack-react-query/usage/index.md", "title": "TanStack React Query"}
nav_next: {"path": "aborting-procedure-calls/index.md", "title": "Aborting Procedure Calls"}
---

Version: 11.x

The "Vanilla" tRPC client can be used to call your API procedures as if they are local functions, enabling a seamless development experience.

ts

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [httpBatchLink({ url: 'http://localhost:3000' })],`

`});`

`const bilbo = await client.getUser.query('id_bilbo');`

`// => { id: 'id_bilbo', name: 'Bilbo' };`

### When to use the Vanilla Client?[​](#when-to-use-the-vanilla-client "Direct link to When to use the Vanilla Client?")

You are likely to use this client in two scenarios:

*   With a frontend framework for which we don't have an official integration
*   With a separate backend service written in TypeScript.

### When **NOT** to use the Vanilla Client?[​](#when-not-to-use-the-vanilla-client "Direct link to when-not-to-use-the-vanilla-client")

*   While you _can_ use the client to call procedures from a React component, you should usually use our [TanStack React Query Integration](../tanstack-react-query/setup/index.md). It offers many additional features such as the ability to manage loading and error state, caching, and invalidation.
*   We recommend you do not use this client when calling procedures of the same API instance, this is because the invocation has to pass through the network layer. For complete recommendations on invoking a procedure in the current API, you can [read more here](../../server/server-side-calls/index.md).
