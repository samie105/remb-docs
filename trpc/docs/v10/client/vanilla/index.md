---
title: "tRPC Client"
source: "https://trpc.io/docs/v10/client/vanilla"
canonical_url: "https://trpc.io/docs/v10/client/vanilla"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:36.305Z"
content_hash: "7ba58f5329be295a41b2b4875a6503afa29532121729f339a313c42c6004ff6c"
menu_path: ["tRPC Client"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/react/useQuery/index.md", "title": "useQuery()"}
nav_next: {"path": "trpc/docs/v10/client/react/useUtils/index.md", "title": "useUtils"}
---

Version: 10.x

The "Vanilla" tRPC client can be used to call your API procedures as if they are local functions, enabling a seamless development experience.

ts

`import type { AppRouter } from '../path/to/server/trpc';`

`const bilbo = await client.getUser.query('id_bilbo');`

`// => { id: 'id_bilbo', name: 'Bilbo' };`

### When to use the Vanilla Client?[​](#when-to-use-the-vanilla-client "Direct link to When to use the Vanilla Client?")

You are likely to use this client in two scenarios:

*   With a frontend framework for which we don't have an official integration
*   With a separate backend service written in TypeScript.

### When **NOT** to use the Vanilla Client?[​](#when-not-to-use-the-vanilla-client "Direct link to when-not-to-use-the-vanilla-client")

*   While you _can_ use the client to call procedures from a React component, you should usually use our [React Query Integration](trpc/docs/v10/client/react/index.md). It offers many additional features such as the ability to manage loading and error state, caching, and invalidation.
*   We recommend you do not use this client when calling procedures of the same API instance, this is because the invocation has to pass through the network layer. For complete recommendations on invoking a procedure in the current API, you can [read more here](trpc/docs/server/server-side-calls/index.md).

