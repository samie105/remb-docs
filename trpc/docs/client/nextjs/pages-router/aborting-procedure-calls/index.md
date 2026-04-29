---
title: "Aborting Procedure Calls"
source: "https://trpc.io/docs/client/nextjs/pages-router/aborting-procedure-calls"
canonical_url: "https://trpc.io/docs/client/nextjs/pages-router/aborting-procedure-calls"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:42.099Z"
content_hash: "83abca433d5fa9929f00108b2b45fb65c5faddf4afc97a663c3a80eb04bfe9f3"
menu_path: ["Aborting Procedure Calls"]
section_path: []
nav_prev: {"path": "../../app-router-setup/index.md", "title": "Set up with Next.js App Router"}
nav_next: {"path": "../server-side-helpers/index.md", "title": "Server-Side Helpers"}
---

By default, tRPC does not cancel requests on unmount. If you want to opt into this behavior, you can provide `abortOnUnmount` in your configuration callback.

### Globally[​](#globally "Direct link to Globally")

client.ts

ts

`import { httpBatchLink } from '@trpc/client';`

`import { createTRPCNext } from '@trpc/next';`

`import type { AppRouter } from './server/routers/_app';`

`export const trpc = createTRPCNext<AppRouter>({`

  `config() {`

    `return {`

      `links: [`

        `httpBatchLink({`

          `url: '/api/trpc',`

        `}),`

      `],`

      `abortOnUnmount: true,`

    `};`

  `},`

`});`

### Per-request[​](#per-request "Direct link to Per-request")

You may also override this behavior at the request level.

client.ts

tsx

`import { trpc } from './utils/trpc';`

`import { useRouter } from 'next/router';`

`function PostViewPage() {`

  `const id = useRouter().query.id as string;`

  `const postQuery = trpc.post.byId.useQuery({ id }, { trpc: { abortOnUnmount: true } });`

  `return null;`

`}`
