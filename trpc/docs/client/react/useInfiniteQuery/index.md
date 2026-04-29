---
title: "useInfiniteQuery()"
source: "https://trpc.io/docs/client/react/useInfiniteQuery"
canonical_url: "https://trpc.io/docs/client/react/useInfiniteQuery"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:59.510Z"
content_hash: "859e9627693c7d76673f8fdc5d608838b704df92c2f8d5d57b87382b418dac6d"
menu_path: ["useInfiniteQuery()"]
section_path: []
nav_prev: {"path": "../suspense/index.md", "title": "Suspense"}
nav_next: {"path": "../useMutation/index.md", "title": "useMutation()"}
---

info

*   Your procedure needs to accept a `cursor` input of any type (`string`, `number`, etc) to expose this hook.
*   For more details on infinite queries read the [react-query docs](https://tanstack.com/query/v5/docs/framework/react/reference/useInfiniteQuery)
*   In this example we're using Prisma - see their docs on [cursor-based pagination](https://www.prisma.io/docs/concepts/components/prisma-client/pagination#cursor-based-pagination)

## Example Procedure[​](#example-procedure "Direct link to Example Procedure")

server/routers/\_app.ts

tsx

`import { initTRPC } from '@trpc/server';`

`import { z } from 'zod';`

`export const t = initTRPC.create();`

`export const appRouter = t.router({`

  `infinitePosts: t.procedure`

    `.input(`

      `z.object({`

        `limit: z.number().min(1).max(100).nullish(),`

        `cursor: z.number().nullish(), // <-- "cursor" needs to exist, but can be any type`

        `direction: z.enum(['forward', 'backward']), // optional, useful for bi-directional query`

      `}),`

    `)`

    `.query(async (opts) => {`

      `const { input } = opts;`

      `const limit = input.limit ?? 50;`

      `const { cursor } = input;`

      `const items = await prisma.post.findMany({`

        `take: limit + 1, // get an extra item at the end which we'll use as next cursor`

        `where: {`

          `title: {`

            `contains: 'Prisma' /* Optional filter */,`

          `},`

        `},`

        `cursor: cursor ? { myCursor: cursor } : undefined,`

        `orderBy: {`

          `myCursor: 'asc',`

        `},`

      `});`

      `let nextCursor: typeof cursor | undefined = undefined;`

      `if (items.length > limit) {`

        `const nextItem = items.pop();`

        `nextCursor = nextItem!.myCursor;`

      `}`

      `return {`

        `items,`

        `nextCursor,`

      `};`

    `}),`

`});`

## Example React Component[​](#example-react-component "Direct link to Example React Component")

components/MyComponent.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const myQuery = trpc.infinitePosts.useInfiniteQuery(`

    `{`

      `limit: 10,`

    `},`

    `{`

      `getNextPageParam: (lastPage) => lastPage.nextCursor,`

      `// initialCursor: 1, // <-- optional you can pass an initialCursor`

    `},`

  `);`

  `// [...]`

`}`

## Helpers[​](#helpers "Direct link to Helpers")

### `getInfiniteData()`[​](#getinfinitedata "Direct link to getinfinitedata")

This helper gets the currently cached data from an existing infinite query

components/MyComponent.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const utils = trpc.useUtils();`

  `const myMutation = trpc.infinitePosts.add.useMutation({`

    `async onMutate(opts) {`

      `await utils.infinitePosts.list.cancel();`

      `const allPosts = utils.infinitePosts.list.getInfiniteData({ limit: 10 });`

      `// [...]`

    `},`

  `});`

`}`

### `setInfiniteData()`[​](#setinfinitedata "Direct link to setinfinitedata")

This helper allows you to update a query's cached data

components/MyComponent.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const utils = trpc.useUtils();`

  `const myMutation = trpc.infinitePosts.delete.useMutation({`

    `async onMutate(opts) {`

      `await utils.infinitePosts.list.cancel();`

      `utils.infinitePosts.list.setInfiniteData({ limit: 10 }, (data) => {`

        `if (!data) {`

          `return {`

            `pages: [],`

            `pageParams: [],`

          `};`

        `}`

        `return {`

          `...data,`

          `pages: data.pages.map((page) => ({`

            `...page,`

            `items: page.items.filter((item) => item.status === 'published'),`

          `})),`

        `};`

      `});`

    `},`

  `});`

  `// [...]`

`}`
