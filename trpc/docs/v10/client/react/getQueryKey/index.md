---
title: "getQueryKey"
source: "https://trpc.io/docs/v10/client/react/getQueryKey"
canonical_url: "https://trpc.io/docs/v10/client/react/getQueryKey"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:40.500Z"
content_hash: "ae361ce9f8398d0e8e57057a2cc80d077feecad8a8c15fa5822389eed444a529"
menu_path: ["getQueryKey"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/react/aborting-procedure-calls/index.md", "title": "Aborting Procedure Calls"}
nav_next: {"path": "trpc/docs/v10/client/react/infer-types/index.md", "title": "Inferring Types"}
---

Version: 10.x

We provide a getQueryKey helper that accepts a `router` or `procedure` so that you can easily provide the native function the correct query key.

tsx

`// Queries`

`function getQueryKey(`

  `procedure: AnyQueryProcedure,`

  `input?: DeepPartial<TInput>,`

  `type?: QueryType; /** @default 'any' */`

`): TRPCQueryKey;`

`// Routers`

`function getQueryKey(`

  `router: AnyRouter,`

`): TRPCQueryKey;`

`// Mutations`

`function getQueryKey(`

  `procedure: AnyMutationProcedure,`

`): TRPCQueryKey;`

`type QueryType = "query" | "infinite" | "any";`

`// for useQuery ──┘         │            │`

`// for useInfiniteQuery ────┘            │`

`// will match all ───────────────────────┘`

note

The query type `any` will match all queries in the cache only if the `react query` method where it's used uses fuzzy matching. See [TanStack/query#5111 (comment)](https://github.com/TanStack/query/issues/5111#issuecomment-1464864361) for more context.

tsx

`import { useIsFetching, useQueryClient } from '@tanstack/react-query';`

`import { getQueryKey } from '@trpc/react-query';`

`import { trpc } from '~/utils/trpc';`

`function MyComponent() {`

  `const queryClient = useQueryClient();`

  `const posts = trpc.post.list.useQuery();`

  `// See if a query is fetching`

  `const postListKey = getQueryKey(trpc.post.list, undefined, 'query');`

  `const isFetching = useIsFetching(postListKey);`

  `// Set some query defaults for an entire router`

  `const postKey = getQueryKey(trpc.post);`

  `queryClient.setQueryDefaults(postKey, { staleTime: 30 * 60 * 1000 });`

  `// ...`

`}`

