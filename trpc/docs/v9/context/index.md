---
title: "Request Context"
source: "https://trpc.io/docs/v9/context"
canonical_url: "https://trpc.io/docs/v9/context"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:26.964Z"
content_hash: "32509d282008cfba53be2429ea14f4ce7d1f44f287923152bb58004512ef1b5a"
menu_path: ["Request Context"]
section_path: []
---
The `createContext()` function is called for each request and the result is propagated to all resolvers. You can use this to pass contextual data down to the resolvers.

server/context.ts

ts

`import * as trpc from '@trpc/server';`

`import * as trpcNext from '@trpc/server/adapters/next';`

`// The app's context - is generated for each incoming request`

`export async function createContext(opts?: trpcNext.CreateNextContextOptions) {`

  `// Create your context based on the request object`

  ``// Will be available as `ctx` in all your resolvers``

  `// This is just an example of something you'd might want to do in your ctx fn`

  `async function getUserFromHeader() {`

    `if (opts?.req.headers.authorization) {`

      `// const user = await decodeJwtToken(req.headers.authorization.split(' ')[1])`

      `// return user;`

    `}`

    `return null;`

  `}`

  `const user = await getUserFromHeader();`

  `return {`

    `user,`

  `};`

`}`

`type Context = trpc.inferAsyncReturnType<typeof createContext>;`

`// Helper function to create a router with your app's context`

`export function createRouter() {`

  `return trpc.router<Context>();`

`}`
