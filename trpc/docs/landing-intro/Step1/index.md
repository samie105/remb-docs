---
title: "Step1"
source: "https://trpc.io/docs/landing-intro/Step1"
canonical_url: "https://trpc.io/docs/landing-intro/Step1"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:35.991Z"
content_hash: "b724c9efce5c63e7737908768617f6ac0d3cdba390abe8e2cf6fe147a7564206"
menu_path: ["Step1"]
section_path: []
nav_prev: {"path": "../../further-reading/index.md", "title": "Further Reading"}
nav_next: {"path": "../Step2/index.md", "title": "Step2"}
---

ts

`const t = initTRPC.create();`

`const router = t.router;`

`const publicProcedure = t.procedure;`

`const appRouter = router({`

  `greeting: publicProcedure`

    `.input(z.object({ name: z.string() }))`

    `.query((opts) => {`

      `const { input } = opts;`

               `const input: {     name: string; }`

      ``return `Hello ${input.name}` as const;``

  `}),`

`});`

`export type AppRouter = typeof appRouter;`
