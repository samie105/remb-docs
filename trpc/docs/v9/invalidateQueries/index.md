---
title: "invalidateQueries"
source: "https://trpc.io/docs/v9/invalidateQueries"
canonical_url: "https://trpc.io/docs/v9/invalidateQueries"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:29.464Z"
content_hash: "c61b5f57a222c9c7909cb2ddd70312e6ac6f108f2f214792ab05c3813869149d"
menu_path: ["invalidateQueries"]
section_path: []
nav_prev: {"path": "../infer-types/index.md", "title": "Inferring Types"}
nav_next: {"path": "../links/index.md", "title": "Links & Request Batching"}
---

A typesafe wrapper around calling `queryClient.invalidateQueries()`, all it does is to call `queryClient.invalidateQueries()` with the passed args. [See react-query docs](https://tanstack.com/query/v3/docs/react/guides/query-invalidation) if you want more fine-grained control.

tsx

`import { trpc } from '../utils/trpc';`

`// In component:`

`const utils = trpc.useUtils();`

`const mutation = trpc.useMutation('post.edit', {`

  `onSuccess(input) {`

    `utils.invalidateQueries(['post.all']);`

    `utils.invalidateQueries(['post.byId', input.id]);`

  `},`

`});`
