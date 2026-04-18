---
title: "useMutation()"
source: "https://trpc.io/docs/v10/client/react/useMutation"
canonical_url: "https://trpc.io/docs/v10/client/react/useMutation"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:20.017Z"
content_hash: "18c047483c5b82040ce7bb233dfed1cafb2fc4497b6c8284ac16f7698f183631"
menu_path: ["useMutation()"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/react/useInfiniteQuery/index.md", "title": "useInfiniteQuery"}
nav_next: {"path": "trpc/docs/v10/client/react/useQueries/index.md", "title": "useQueries()"}
---

tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `// This can either be a tuple ['login'] or string 'login'`

  `const mutation = trpc.login.useMutation();`

  `const handleLogin = () => {`

    `const name = 'John Doe';`

    `mutation.mutate({ name });`

  `};`

  `return (`

    `<div>`

      `<h1>Login Form</h1>`

      `<button onClick={handleLogin} disabled={mutation.isLoading}>`

        `Login`

      `</button>`

      `{mutation.error && <p>Something went wrong! {mutation.error.message}</p>}`

    `</div>`

  `);`

`}`

