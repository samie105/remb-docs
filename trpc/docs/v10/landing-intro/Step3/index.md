---
title: "Step3"
source: "https://trpc.io/docs/v10/landing-intro/Step3"
canonical_url: "https://trpc.io/docs/v10/landing-intro/Step3"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:29.518Z"
content_hash: "dd138d62172dbf6c13057d131ab91f97514bf6666fc49b15b7c97bc599b68454"
menu_path: ["Step3"]
section_path: []
nav_prev: {"path": "../Step2/index.md", "title": "Step2"}
nav_next: {"path": "../../migrate-from-v9-to-v10/index.md", "title": "Migrate from v9 to v10"}
---

ts

`const trpc = createTRPCProxyClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

`const res = await trpc.greeting.query({ name: 'John' });`

      `` const res: `Hello ${string}` ``
