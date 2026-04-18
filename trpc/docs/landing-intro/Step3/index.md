---
title: "Step3"
source: "https://trpc.io/docs/landing-intro/Step3"
canonical_url: "https://trpc.io/docs/landing-intro/Step3"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:41.278Z"
content_hash: "686118d05d6a9c420c8f53988a50f064690ba67fbdab6cf08a71618b8d386171"
menu_path: ["Step3"]
section_path: []
---
ts

`const trpc = createTRPCClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

`const res = await trpc.greeting.query({ name: 'John' });`
