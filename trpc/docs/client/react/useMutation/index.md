---
title: "useMutation()"
source: "https://trpc.io/docs/client/react/useMutation"
canonical_url: "https://trpc.io/docs/client/react/useMutation"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:57.549Z"
content_hash: "81de89088c50bbf4940823005976bde0a6aaf1d7be659ada175fafc464ddf030"
menu_path: ["useMutation()"]
section_path: []
nav_prev: {"path": "trpc/docs/client/react/suspense/index.md", "title": "Suspense"}
nav_next: {"path": "trpc/docs/client/react/useInfiniteQuery/index.md", "title": "useInfiniteQuery()"}
---

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const mutation = trpc.login.useMutation();`

  `const handleLogin = () => {`

    `const name = 'John Doe';`

    `mutation.mutate({ name });`

  `};`

  `return (`

    `<div>`

      `<h1>Login Form</h1>`

      `<button onClick={handleLogin} disabled={mutation.isPending}>`

        `Login`

      `</button>`

      `{mutation.error && <p>Something went wrong! {mutation.error.message}</p>}`

    `</div>`

  `);`

`}`

