---
title: "useQueries()"
source: "https://trpc.io/docs/v10/client/react/useQueries"
canonical_url: "https://trpc.io/docs/v10/client/react/useQueries"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:22.956Z"
content_hash: "48e55df471dfec124786c235b15d3298eaa8529e7f76b6e4fd3e183ae106c578"
menu_path: ["useQueries()"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/react/useMutation/index.md", "title": "useMutation()"}
nav_next: {"path": "trpc/docs/v10/client/react/useQuery/index.md", "title": "useQuery()"}
---

The `useQueries` hook can be used to fetch a variable number of queries at the same time using only one hook call.

The main use case for such a hook is to be able to fetch a number of queries, usually of the same type. For example if you fetch a list of todo ids, you can then map over them in a useQueries hook calling a byId endpoint that would fetch the details of each todo.

note

While fetching multiple types in a `useQueries` hook is possible, there is not much of an advantage compared to using multiple `useQuery` calls unless you use the `suspense` option as that `useQueries` can trigger suspense in parallel while multiple `useQuery` calls would waterfall.

## Usage[​](#usage "Direct link to Usage")

The useQueries hook is the same as that of [@tanstack/query useQueries](https://tanstack.com/query/v4/docs/react/reference/useQueries). The only difference is that you pass in a function that returns an array of queries instead of an array of queries inside an object parameter.

tip

When you're using the [`httpBatchLink`](trpc/docs/client/links/httpBatchLink/index.md) or [`wsLink`](trpc/docs/client/links/wsLink/index.md), the below will end up being only 1 HTTP call to your server. Additionally, if the underlying procedure is using something like Prisma's `findUnique()` it will [automatically batch](https://www.prisma.io/docs/guides/performance-and-optimization/query-optimization-performance#solving-n1-in-graphql-with-findunique-and-prismas-dataloader) & do exactly 1 database query as a well.

tsx

`const Component = (props: { postIds: string[] }) => {`

  `const postQueries = trpc.useQueries((t) =>`

    `props.postIds.map((id) => t.post.byId({ id })),`

  `);`

  `return <>{/* [...] */}</>;`

`};`

### Providing options to individual queries[​](#providing-options-to-individual-queries "Direct link to Providing options to individual queries")

You can also pass in any normal query options to the second parameter of any of the query calls in the array such as `enabled`, `suspense`, `refetchOnWindowFocus`...etc. For a complete overview of all the available options, see the [tanstack useQuery](https://tanstack.com/query/v4/docs/react/reference/useQuery) documentation.

tsx

`const Component = () => {`

  `const [post, greeting] = trpc.useQueries((t) => [`

    `t.post.byId({ id: '1' }, { enabled: false }),`

    `t.greeting({ text: 'world' }),`

  `]);`

  `const onButtonClick = () => {`

    `post.refetch();`

  `};`

  `return (`

    `<div>`

      `<h1>{post.data && post.data.title}</h1>`

      `<p>{greeting.data.message}</p>`

      `<button onClick={onButtonClick}>Click to fetch</button>`

    `</div>`

  `);`

`};`

### Context[​](#context "Direct link to Context")

You can also pass in an optional React Query context to override the default.

tsx

`const [post, greeting] = trpc.useQueries(`

  `(t) => [t.post.byId({ id: '1' }), t.greeting({ text: 'world' })],`

  `myCustomContext,`

`);`


