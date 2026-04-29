---
title: "Merging Routers"
source: "https://trpc.io/docs/v9/merging-routers"
canonical_url: "https://trpc.io/docs/v9/merging-routers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:35.619Z"
content_hash: "2b627bde61d52a9d809cae64cdaa3c90d52cca294899239e875a1b1d09f5e000"
menu_path: ["Merging Routers"]
section_path: []
nav_prev: {"path": "../love/index.md", "title": "Testimonials / Love"}
nav_next: {"path": "../metadata/index.md", "title": "Route Metadata"}
---

Writing all API-code in your code in the same file is not a great idea. It's easy to merge routers with other routers.

Thanks to TypeScript 4.1 template literal types we can also prefix the procedures without breaking typesafety.

server.ts

ts

`const createRouter = () => {`

  `return trpc.router<Context>();`

`};`

`const posts = createRouter()`

  `.mutation('create', {`

    `input: z.object({`

      `title: z.string(),`

    `}),`

    `resolve: ({ input }) => {`

      `// ..`

      `return {`

        `id: 'xxxx',`

        `...input,`

      `};`

    `},`

  `})`

  `.query('list', {`

    `resolve() {`

      `// ..`

      `return [];`

    `},`

  `});`

`const users = createRouter().query('list', {`

  `resolve() {`

    `// ..`

    `return [];`

  `},`

`});`

`const appRouter = createRouter()`

  `.merge('user.', users) // prefix user procedures with "user."`

  `.merge('post.', posts); // prefix post procedures with "post."`

server.ts

ts

`const createRouter = () => {`

  `return trpc.router<Context>();`

`};`

`const posts = createRouter()`

  `.mutation('create', {`

    `input: z.object({`

      `title: z.string(),`

    `}),`

    `resolve: ({ input }) => {`

      `// ..`

      `return {`

        `id: 'xxxx',`

        `...input,`

      `};`

    `},`

  `})`

  `.query('list', {`

    `resolve() {`

      `// ..`

      `return [];`

    `},`

  `});`

`const users = createRouter().query('list', {`

  `resolve() {`

    `// ..`

    `return [];`

  `},`

`});`

`const appRouter = createRouter()`

  `.merge('user.', users) // prefix user procedures with "user."`

  `.merge('post.', posts); // prefix post procedures with "post."`
