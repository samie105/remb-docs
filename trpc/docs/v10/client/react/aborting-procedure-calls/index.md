---
title: "Aborting Procedure Calls"
source: "https://trpc.io/docs/v10/client/react/aborting-procedure-calls"
canonical_url: "https://trpc.io/docs/v10/client/react/aborting-procedure-calls"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:32.877Z"
content_hash: "317546541a6d06a72fd56566f77b8afb56f3f43f962b487f6f1b463d657fef7b"
menu_path: ["Aborting Procedure Calls"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/react/index.md", "title": "React Query Integration"}
nav_next: {"path": "trpc/docs/v10/client/react/getQueryKey/index.md", "title": "getQueryKey"}
---

By default, tRPC does not cancel requests via React Query. If you want to opt into this behaviour, you can provide `abortOnUnmount` in your configuration.

note

@tanstack/react-query only supports aborting queries.

### Globally[​](#globally "Direct link to Globally")

client.ts

ts

`// @filename: utils.ts`

`import { createTRPCReact } from '@trpc/react-query';`

`export const trpc = createTRPCReact<AppRouter>({`

  `abortOnUnmount: true,`

`});`

`trpc.createClient({`

  `// ...`

`});`

### Per-request[​](#per-request "Direct link to Per-request")

You may also override this behaviour at the query level.

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
