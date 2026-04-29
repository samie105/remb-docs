---
title: "React Query Integration"
source: "https://trpc.io/docs/v10/client/react"
canonical_url: "https://trpc.io/docs/v10/client/react"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:29.836Z"
content_hash: "195c63f9d42075f801c37b35a12198e8b93f80f0d889b3634b9eba39a56e53a7"
menu_path: ["React Query Integration"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/nextjs/starter-projects/index.md", "title": "Starter Projects"}
nav_next: {"path": "trpc/docs/v10/client/react/aborting-procedure-calls/index.md", "title": "Aborting Procedure Calls"}
---

tRPC offers a first class integration with React. Under the hood this is simply a wrapper around the very popular [@tanstack/react-query](https://tanstack.com/query/latest), so we recommend that you familiarise yourself with React Query, as their docs go in to much greater depth on its usage.

### The tRPC React Query Integration[​](#the-trpc-react-query-integration "Direct link to The tRPC React Query Integration")

This library enables usage directly within React components

pages/IndexPage.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export default function IndexPage() {`

  `const helloQuery = trpc.hello.useQuery({ name: 'Bob' });`

  `const goodbyeMutation = trpc.goodbye.useMutation();`

  `return (`

    `<div>`

      `<p>{helloQuery.data?.greeting}</p>`

      `<button onClick={() => goodbyeMutation.mutate()}>Say Goodbye</button>`

    `</div>`

  `);`

`}`

### Differences to vanilla React Query[​](#differences-to-vanilla-react-query "Direct link to Differences to vanilla React Query")

The wrapper abstracts some aspects of React Query for you:

*   Query Keys - these are generated and managed by tRPC on your behalf, based on the procedure inputs you provide
    *   If you need the query key which tRPC calculates, you can use [getQueryKey](../../../client/react/getQueryKey/index.md)
*   Type safe by default - the types you provide in your tRPC Backend also drive the types of your React Query client, providing safety throughout your React app
