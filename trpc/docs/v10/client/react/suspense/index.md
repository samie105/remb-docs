---
title: "Suspense"
source: "https://trpc.io/docs/v10/client/react/suspense"
canonical_url: "https://trpc.io/docs/v10/client/react/suspense"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:00.217Z"
content_hash: "9b1cb5448785793b047549d812090342df558cc2ff622c3318611248019f750d"
menu_path: ["Suspense"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/react/setup/index.md", "title": "Set up the React Query Integration"}
nav_next: {"path": "trpc/docs/v10/client/react/useInfiniteQuery/index.md", "title": "useInfiniteQuery"}
---

tip

`useSuspenseQuery` & `useSuspenseInfiniteQuery` both return a `[data, query]`\-_tuple_, to make it easy to directly use your data and renaming the variable to something descriptive

tsx

`// @filename: pages/index.tsx`

`import React from 'react';`

`import { trpc } from '../utils/trpc';`

`function PostView() {`

  `const [post, postQuery] = trpc.post.byId.useSuspenseQuery({ id: '1' });`

          `const post: {     id: string;     title: string; }`

  `return <>{/* ... */}</>;`

`}`

tsx

`// @filename: pages/index.tsx`

`import React from 'react';`

`import { trpc } from '../utils/trpc';`

`function PostView() {`

  `const [pages, allPostsQuery] = trpc.post.all.useSuspenseInfiniteQuery(`

    `{},`

    `{`

      `getNextPageParam(lastPage) {`

        `return lastPage.nextCursor;`

      `},`

    `},`

  `);`

  `const { isFetching, isFetchingNextPage, fetchNextPage, hasNextPage } =`

    `allPostsQuery;`

  `return <>{/* ... */}</>;`

`}`

