---
title: "Suspense"
source: "https://trpc.io/docs/client/react/suspense"
canonical_url: "https://trpc.io/docs/client/react/suspense"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:52.362Z"
content_hash: "5eff6b92662afa2b4ff70214f062d8905d40d8f7f02360a75698518df5c14224"
menu_path: ["Suspense"]
section_path: []
nav_prev: {"path": "../setup/index.md", "title": "Set up the React Query Integration"}
nav_next: {"path": "../useInfiniteQuery/index.md", "title": "useInfiniteQuery()"}
---

info

*   Ensure you're on the latest version of React
*   If you use suspense with [tRPC's _automatic_ SSR in Next.js](../../nextjs/pages-router/ssr/index.md), the full page will crash on the server if a query fails, even if you have an `<ErrorBoundary />`

## Usage[​](#usage "Direct link to Usage")

tip

`useSuspenseQuery` & `useSuspenseInfiniteQuery` both return a `[data, query]`\-_tuple_, to make it easy to directly use your data and renaming the variable to something descriptive

### `useSuspenseQuery()`[​](#usesuspensequery "Direct link to usesuspensequery")

tsx

`import { trpc } from '../utils/trpc';`

`function PostView() {`

  `const [post, postQuery] = trpc.post.byId.useSuspenseQuery({ id: '1' });`

  `return <>{/* ... */}</>;`

`}`

### `useSuspenseInfiniteQuery()`[​](#usesuspenseinfinitequery "Direct link to usesuspenseinfinitequery")

tsx

`import { trpc } from '../utils/trpc';`

`import type { PostPage } from '../server';`

`function PostView() {`

  `const [{ pages }, allPostsQuery] = trpc.post.all.useSuspenseInfiniteQuery(`

    `{},`

    `{`

      `getNextPageParam(lastPage: PostPage) {`

        `return lastPage.nextCursor;`

      `},`

      `initialCursor: '',`

    `},`

  `);`

  `const { isFetching, isFetchingNextPage, fetchNextPage, hasNextPage } =`

    `allPostsQuery;`

  `return <>{/* ... */}</>;`

`}`

### `useSuspenseQueries()`[​](#usesuspensequeries "Direct link to usesuspensequeries")

Suspense equivalent of [`useQueries()`](../useQueries/index.md).

tsx

`import { trpc } from '../utils/trpc';`

`const Component = (props: { postIds: string[] }) => {`

  `const [posts, postQueries] = trpc.useSuspenseQueries((t) =>`

    `props.postIds.map((id) => t.post.byId({ id })),`

  `);`

  `return <>{/* [...] */}</>;`

`};`

## Prefetching[​](#prefetching "Direct link to Prefetching")

The performance of suspense queries can be improved by prefetching the query data before the Suspense component is rendered (this is sometimes called ["render-as-you-fetch"](https://tanstack.com/query/v5/docs/framework/react/guides/suspense#fetch-on-render-vs-render-as-you-fetch)).

note

*   Prefetching and the render-as-you-fetch model are very dependent on the framework and router you are using. We recommend reading your frameworks router docs along with the [@tanstack/react-query docs](https://tanstack.com/query/v5/docs/react/guides/prefetching) to understand how to implement these patterns.
*   If you are using Next.js please look at the docs on [Server-Side Helpers](../../nextjs/pages-router/server-side-helpers/index.md) to implement server-side prefetching.

### Route-level prefetching[​](#route-level-prefetching "Direct link to Route-level prefetching")

tsx

`import { createTRPCQueryUtils } from '@trpc/react-query';`

`import { createTRPCClient, httpBatchLink } from '@trpc/client';`

`import { QueryClient } from '@tanstack/react-query';`

`import type { AppRouter } from './server';`

`const queryClient = new QueryClient();`

`const trpcClient = createTRPCClient<AppRouter>({ links: [httpBatchLink({ url: 'http://localhost:3000' })] });`

`const utils = createTRPCQueryUtils({ queryClient, client: trpcClient });`

`// tanstack router/ react router loader`

`const loader = async (params: { id: string }) =>`

  `utils.post.byId.ensureData({ id: params.id });`

### Component-level prefetching with `usePrefetchQuery`[​](#component-level-prefetching-with-useprefetchquery "Direct link to component-level-prefetching-with-useprefetchquery")

tsx

`import React, { Suspense } from 'react';`

`import { trpc } from '../utils/trpc';`

`function PostView(props: { postId: string }) {`

  `return <></>;`

`}`

`function PostViewPage(props: { postId: string }) {`

  `trpc.post.byId.usePrefetchQuery({ id: props.postId });`

  `return (`

    `<Suspense>`

      `<PostView postId={props.postId} />`

    `</Suspense>`

  `);`

`}`

### Component-level prefetching with `usePrefetchInfiniteQuery`[​](#component-level-prefetching-with-useprefetchinfinitequery "Direct link to component-level-prefetching-with-useprefetchinfinitequery")

tsx

`import React, { Suspense } from 'react';`

`import { trpc } from '../utils/trpc';`

`import type { PostPage } from '../server';`

`function PostView(props: { postId: string }) {`

  `return <></>;`

`}`

`function PostViewPage(props: { postId: string }) {`

  `trpc.post.all.usePrefetchInfiniteQuery(`

    `{},`

    `{`

      `getNextPageParam(lastPage: PostPage) {`

        `return lastPage.nextCursor;`

      `},`

      `initialCursor: '',`

    `},`

  `);`

  `return (`

    `<Suspense>`

      `<PostView postId={props.postId} />`

    `</Suspense>`

  `);`

`}`
