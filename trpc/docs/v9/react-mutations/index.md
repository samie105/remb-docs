---
title: "useMutation()"
source: "https://trpc.io/docs/v9/react-mutations"
canonical_url: "https://trpc.io/docs/v9/react-mutations"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:21.579Z"
content_hash: "f2bd457f4cd33be4313c06829a14d158afddea11348ca570550e40a7eba3fe18"
menu_path: ["useMutation()"]
section_path: []
---
tsx

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `// This can either be a tuple ['login'] or string 'login'`

  `const mutation = trpc.useMutation(['login']);`

  `const handleLogin = async () => {`

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
