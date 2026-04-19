---
title: "useInfiniteQuery"
source: "https://trpc.io/docs/v9/useInfiniteQuery"
canonical_url: "https://trpc.io/docs/v9/useInfiniteQuery"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:20.329Z"
content_hash: "9b2edc9bdce46e9f7de01ff1069ce9929521c00aae57a602c9694aaebb716051"
menu_path: ["useInfiniteQuery"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/subscriptions/index.md", "title": "Subscriptions / WebSockets"}
nav_next: {"path": "trpc/docs/v9/vanilla/index.md", "title": "Vanilla client"}
---

info

*   Your procedure needs to accept a `cursor` input of `any` type
*   For more details on infinite queries read the [react-query docs](https://tanstack.com/query/v3/docs/react/reference/useInfiniteQuery)
*   In this example we're using Prisma - see their docs on [cursor-based pagination](https://www.prisma.io/docs/concepts/components/prisma-client/pagination#cursor-based-pagination)

## Example Procedure[​](#example-procedure "Direct link to Example Procedure")

server/routers/\_app.ts

tsx

`import * as trpc from '@trpc/server';`

`import { Context } from './[trpc]';`

`import { z } from 'zod';`

`export const appRouter = trpc.router<Context>()`

  `.query('infinitePosts', {`

    `input: z.object({`

      `limit: z.number().min(1).max(100).nullish(),`

      `cursor: z.number().nullish(), // <-- "cursor" needs to exist, but can be any type`

    `}),`

    `async resolve({ input }) {`

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

      `})`

      `let nextCursor: typeof cursor | undefined = undefined;`

      `if (items.length > limit) {`

        `const nextItem = items.pop()`

        `nextCursor = nextItem!.myCursor;`

      `}`

      `return {`

        `items,`

        `nextCursor,`

      `};`

    `})`

## Example React Component[​](#example-react-component "Direct link to Example React Component")

components/MyComponent.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const myQuery = trpc.useInfiniteQuery(`

    `[`

      `'infinitePosts',`

      `{`

        `limit: 10,`

      `},`

    `],`

    `{`

      `getNextPageParam: (lastPage) => lastPage.nextCursor,`

    `},`

  `);`

  `// [...]`

`}`

## Helpers[​](#helpers "Direct link to Helpers")

### `getInfiniteQueryData()`[​](#getinfinitequerydata "Direct link to getinfinitequerydata")

This helper gets the currently cached data from an existing infinite query

components/MyComponent.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const utils = trpc.useContext();`

  `const myMutation = trpc.useMutation('infinitePosts.add', {`

    `onMutate({ post }) {`

      `await utils.cancelQuery(['infinitePosts']);`

      `const allPosts = utils.getInfiniteQueryData(['infinitePosts', { limit: 10 }]);`

      `// [...]`

    `}`

  `})`

`}`

### `setInfiniteQueryData()`[​](#setinfinitequerydata "Direct link to setinfinitequerydata")

This helper allows you to update a queries cached data

components/MyComponent.tsx

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const utils = trpc.useContext();`

  `const myMutation = trpc.useMutation('infinitePosts.delete', {`

    `onMutate({ post }) {`

      `await utils.cancelQuery(['infinitePosts']);`

      `utils.setInfiniteQueryData(['infinitePosts', { limit: 10 }], (data) => {`

        `if (!data) {`

          `return {`

            `pages: [],`

            `pageParams: []`

          `}`

        `}`

        `return {`

          `...data,`

          `pages: data.pages.map((page) => {`

            `...page,`

            `items: page.items.filter((item) => item.status === 'published')`

          `})`

        `}`

      `});`

    `}`

  `});`

  `// [...]`

`}`
