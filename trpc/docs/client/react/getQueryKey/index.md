---
title: "getQueryKey"
source: "https://trpc.io/docs/client/react/getQueryKey"
canonical_url: "https://trpc.io/docs/client/react/getQueryKey"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:31.873Z"
content_hash: "9f234ca858691e45cacb100f409af313820aae43b2e255d21ff35f4a82b79450"
menu_path: ["getQueryKey"]
section_path: []
nav_prev: {"path": "trpc/docs/client/react/disabling-queries/index.md", "title": "Disabling Queries"}
nav_next: {"path": "trpc/docs/client/react/infer-types/index.md", "title": "Inferring Types"}
---

We provide a getQueryKey helper that accepts a `router` or `procedure` so that you can easily provide the native function the correct query key.

tsx

`// Queries`

`declare function getQueryKey(`

  `procedure: AnyQueryProcedure,`

  `input?: DeepPartial<TInput>,`

  `type?: QueryType, /** @default 'any' */`

`): TRPCQueryKey;`

`// Routers`

`declare function getQueryKey(`

  `router: AnyRouter,`

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

`import { trpc } from './utils/trpc';`

`function MyComponent() {`

  `const queryClient = useQueryClient();`

  `const posts = trpc.post.list.useQuery();`

  `// See if a query is fetching`

  `const postListKey = getQueryKey(trpc.post.list, undefined, 'query');`

  `const isFetching = useIsFetching({ queryKey: postListKey });`

  `// Set some query defaults for an entire router`

  `const postKey = getQueryKey(trpc.post);`

  `queryClient.setQueryDefaults(postKey, { staleTime: 30 * 60 * 1000 });`

  `// ...`

`}`

## Mutations[​](#mutations "Direct link to Mutations")

Similarly to queries, we provide a getMutationKey for mutations. The underlying function is the same as getQueryKey (in fact, you could technically use getQueryKey for mutations as well), the only difference is in semantics.

tsx

`import { getMutationKey } from '@trpc/react-query';`

`const mutationKey = getMutationKey(trpc.user.create);`

