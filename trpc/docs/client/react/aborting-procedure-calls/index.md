---
title: "Aborting Procedure Calls"
source: "https://trpc.io/docs/client/react/aborting-procedure-calls"
canonical_url: "https://trpc.io/docs/client/react/aborting-procedure-calls"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:23.808Z"
content_hash: "861c6b9422d39934cd4e60b1ced8b78bda5d734ba932b00a3ad21c92b0bbb948"
menu_path: ["Aborting Procedure Calls"]
section_path: []
nav_prev: {"path": "trpc/docs/client/react/index.md", "title": "React Query Integration (Classic)"}
nav_next: {"path": "trpc/docs/client/react/createTRPCQueryUtils/index.md", "title": "createTRPCQueryUtils"}
---

By default, tRPC does not cancel requests via React Query. If you want to opt into this behavior, you can provide `abortOnUnmount` in your configuration.

note

@tanstack/react-query only supports aborting queries.

### Globally[​](#globally "Direct link to Globally")

client.ts

ts

`import { createTRPCReact } from '@trpc/react-query';`

`import type { AppRouter } from './server';`

`export const trpc = createTRPCReact<AppRouter>({`

  `abortOnUnmount: true,`

`});`

### Per-request[​](#per-request "Direct link to Per-request")

You may also override this behavior at the query level.

pages/post/\[id\].tsx

tsx

`import { trpc } from '../utils/trpc';`

`function PostViewPage() {`

  `const { query } = useRouter();`

  `const postQuery = trpc.post.byId.useQuery(`

    `{ id: query.id },`

    `{ trpc: { abortOnUnmount: true } }`

  `);`

  `// ...`

`}`
