---
title: "Disabling Queries"
source: "https://trpc.io/docs/client/react/disabling-queries"
canonical_url: "https://trpc.io/docs/client/react/disabling-queries"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:27.814Z"
content_hash: "533e857ac9bea2f31a4507fee7495d4a3288f499791234d853269ac1e5782446"
menu_path: ["Disabling Queries"]
section_path: []
---
To disable queries, you can pass `skipToken` as the first argument to `useQuery`, `useInfiniteQuery`, and `useSubscription`. This will prevent the query from being executed.

### Typesafe conditional queries using `skipToken`[​](#typesafe-conditional-queries-using-skiptoken "Direct link to typesafe-conditional-queries-using-skiptoken")

tsx

`import React, { useState } from 'react';`

`import { skipToken } from '@tanstack/react-query';`

`import { trpc } from './utils/trpc';`

`export function MyComponent() {`

  `const [name, setName] = useState<string | undefined>();`

  `const result = trpc.getUserByName.useQuery(name ? { name: name } : skipToken);`

  `return (`

    `<div>{result.data?.name}</div>`

  `);`

`}`
