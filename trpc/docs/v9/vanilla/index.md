---
title: "Vanilla client"
source: "https://trpc.io/docs/v9/vanilla"
canonical_url: "https://trpc.io/docs/v9/vanilla"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:25.486Z"
content_hash: "212e6726aff244d6b353af6da432605c4dd1b54097e098a4d28026d77083c692"
menu_path: ["Vanilla client"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/useInfiniteQuery/index.md", "title": "useInfiniteQuery"}
nav_next: {"path": "trpc/docs/client/index.md", "title": "tRPC Client"}
---

The magic of tRPC is making _strongly typed_ API calls without relying on code generation. With full-stack TypeScript projects, you can directly _import types from the server into the client_! This is a vital part of how tRPC works.

Import the `AppRouter` type into your client from the file your root tRPC router is defined. This single type represents the type signature of your entire API.

client.ts

ts

`import type { AppRouter } from '../path/to/server/trpc';`

The `import type` keywords let you import from _any TypeScript file_ on your filesystem. Plus `import type` can only import types, **NOT** code. So there's no danger of accidentally importing server-side code into your client. All calls to `import type` are _always fully erased_ from your compiled JavaScript bundle ([source](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export)).

### Initialize a tRPC client[​](#initialize-a-trpc-client "Direct link to Initialize a tRPC client")

Create a typesafe client with the `createTRPCClient` method from `@trpc/client`:

client.ts

ts

`// pages/index.tsx`

`import { createTRPCClient } from '@trpc/client';`

`import type { AppRouter } from '../path/to/server/trpc';`

`const client = createTRPCClient<AppRouter>({`

  `url: 'http://localhost:5000/trpc',`

`});`

As you can see, we passed `AppRouter` as a **type argument** of `createTRPCClient`. This returns a strongly typed `client` instance:

client.ts

ts

`const bilbo = await client.query('getUser', 'id_bilbo');`

`// => { id: 'id_bilbo', name: 'Bilbo' };`

`const frodo = await client.mutation('createUser', { name: 'Frodo' });`

`// => { id: 'id_frodo', name: 'Frodo' };`

