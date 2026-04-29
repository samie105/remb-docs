---
title: "createTRPCQueryUtils"
source: "https://trpc.io/docs/client/react/createTRPCQueryUtils"
canonical_url: "https://trpc.io/docs/client/react/createTRPCQueryUtils"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:26.510Z"
content_hash: "ed7534cbd827f4bcbda5f1fd75932c99019a0ddfb857179b915c47b1004b279a"
menu_path: ["createTRPCQueryUtils"]
section_path: []
nav_prev: {"path": "trpc/docs/client/react/aborting-procedure-calls/index.md", "title": "Aborting Procedure Calls"}
nav_next: {"path": "trpc/docs/client/react/disabling-queries/index.md", "title": "Disabling Queries"}
---

The use case for `createTRPCQueryUtils` is when you need to use the helpers outside of a React Component, for example in `react-router`'s loaders.

Similar to `useUtils`, `createTRPCQueryUtils` is a function that gives you access to helpers that let you manage the cached data of the queries you execute via `@trpc/react-query`. These helpers are actually thin wrappers around `@tanstack/react-query`'s [`queryClient`](https://tanstack.com/query/v5/docs/reference/QueryClient) methods. If you want more in-depth information about options and usage patterns for `useUtils` helpers than what we provide here, we will link to their respective `@tanstack/react-query` docs so you can refer to them accordingly.

The difference between `useUtils` and `createTRPCQueryUtils` is that `useUtils` is a react hook that uses `useQueryClient` under the hood. This means that it is able to work better within React Components.

If you need access to the client directly, you can use the `client` object that you passed to `createTRPCQueryUtils` during creation.

caution

You should avoid using `createTRPCQueryUtils` in React Components. Instead, use `useUtils` which is a React hook that implements `useCallback` and `useQueryClient` under the hood.

## Usage[​](#usage "Direct link to Usage")

`createTRPCQueryUtils` returns an object with all the available queries you have in your routers. You use it the same way as your `trpc` client object. Once you reach a query, you'll have access to the query helpers. For example, let's say you have a `post` router with an `all` query:

Now in our route loader, when we navigate the object `createTRPCQueryUtils` gives us and reach the `post.all` query, we'll get access to our query helpers!

MyPage.tsx

tsx

`import { QueryClient } from '@tanstack/react-query';`

`import { createTRPCQueryUtils, createTRPCReact } from '@trpc/react-query';`

`import type { AppRouter } from './server';`

`const trpc = createTRPCReact<AppRouter>();`

`const trpcClient = trpc.createClient({ links: [] });`

`const queryClient = new QueryClient();`

`const clientUtils = createTRPCQueryUtils({ queryClient, client: trpcClient });`

`// This is a react-router loader`

`export async function loader() {`

  `const allPostsData = await clientUtils.post.all.ensureData(); // Fetches data if it doesn't exist in the cache`

  `return {`

    `allPostsData,`

  `};`

`}`

`// This is a react component`

`export function Component() {`

  `const loaderData = useLoaderData() as Awaited<ReturnType<typeof loader>>;`

  `const allPostQuery = trpc.post.all.useQuery(undefined, {`

    `initialData: loaderData.allPostsData, // Uses the data from the loader`

  `});`

  `return (`

    `<div>`

      `{allPostQuery.data.posts.map((post) => (`

        `<div key={post.id}>{post.title}</div>`

      `))}`

    `</div>`

  `);`

`}`

note

If you were using Remix Run or SSR you wouldn't re-use the same `queryClient` for every request. Instead, you would create a new `queryClient` for every request so that there's no cross-request data leakage.

## Helpers[​](#helpers "Direct link to Helpers")

Much like `useUtils`, `createTRPCQueryUtils` gives you access to same set of helpers, including `queryOptions` and `infiniteQueryOptions`. The only difference is that you need to pass in the `queryClient` and `client` objects.

You can see them on the [useUtils](../useUtils/index.md#helpers)\-page.
