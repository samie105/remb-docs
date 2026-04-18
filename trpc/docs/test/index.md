---
title: "Test"
source: "https://trpc.io/docs/test"
canonical_url: "https://trpc.io/docs/test"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:02.910Z"
content_hash: "7399f1b46ff6246f540437141e9e369e545902f07207e43c0eca534c65f10fd0"
menu_path: ["Test"]
section_path: []
nav_prev: {"path": "trpc/docs/server/websockets/index.md", "title": "WebSockets"}
nav_next: {"path": "trpc/docs/typedoc/client/index.md", "title": "@trpc/client"}
---

tsx

`import { trpc } from '../utils/trpc';`

`function PostView() {`

  `const [{ pages }, allPostsQuery] = trpc.post.all.useSuspenseInfiniteQuery(`

    `{},`

    `{`

      `getNextPageParam(lastPage) {`

        `return lastPage.nextCursor;`

      `},`

      `initialCursor: '',`

    `},`

  `);`

  `return <>{/* ... */}</>;`

`}`
