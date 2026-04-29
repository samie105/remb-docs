---
title: "React Query Integration (Classic)"
source: "https://trpc.io/docs/client/react"
canonical_url: "https://trpc.io/docs/client/react"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:19.770Z"
content_hash: "d0446929003dda361539fc37f243cf70553777417750c71caf51c31e6bbce555"
menu_path: ["React Query Integration (Classic)"]
section_path: []
nav_prev: {"path": "trpc/docs/client/nextjs/starter-projects/index.md", "title": "Starter Projects"}
nav_next: {"path": "trpc/docs/client/react/aborting-procedure-calls/index.md", "title": "Aborting Procedure Calls"}
---

tip

These are the docs for our 'Classic' React Query integration, which (while still supported) is not the recommended way to start new tRPC projects with TanStack React Query. We recommend using the new [TanStack React Query Integration](../tanstack-react-query/setup/index.md) instead.

tRPC offers a first class integration with React. Under the hood this is simply a wrapper around the very popular [@tanstack/react-query](https://tanstack.com/query/latest), so we recommend that you familiarize yourself with React Query, as their docs go into much greater depth on its usage.

If you are using Next.js we recommend using [our integration with that](../nextjs/index.md) instead.

❓ Do I have to use an integration?

### The tRPC React Query Integration[​](#the-trpc-react-query-integration "Direct link to The tRPC React Query Integration")

This library enables usage directly within React components.

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
    *   If you need the query key which tRPC calculates, you can use [getQueryKey](getQueryKey/index.md)
*   Type safe by default - the types you provide in your tRPC Backend also drive the types of your React Query client, providing safety throughout your React app
