---
title: "Usage with Express.js"
source: "https://trpc.io/docs/v9/express"
canonical_url: "https://trpc.io/docs/v9/express"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:55.555Z"
content_hash: "f11729e1abfe5c7eba7280b0a0d59f87be7bfa7ed38b7b4dce2d21c84a94d9a4"
menu_path: ["Usage with Express.js"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/example-apps/index.md", "title": "Example Apps"}
nav_next: {"path": "trpc/docs/v9/fastify/index.md", "title": "Usage with Fastify"}
---

## Example app[​](#example-app "Direct link to Example app")

Description

URL

Links

Express server & procedure calls with node.js.

_n/a_

*   [CodeSandbox](https://githubbox.com/trpc/trpc/tree/main/examples/express-server)
*   [Source](https://github.com/trpc/trpc/tree/main/examples/express-server)

## How to add tRPC to existing Express.js project[​](#how-to-add-trpc-to-existing-expressjs-project "Direct link to How to add tRPC to existing Express.js project")

### 1\. Install deps[​](#1-install-deps "Direct link to 1. Install deps")

bash

`yarn add @trpc/server zod`

> [Zod](https://github.com/colinhacks/zod) isn't a required dependency, but it's used in the sample router below.

### 2\. Create a tRPC router[​](#2-create-a-trpc-router "Direct link to 2. Create a tRPC router")

Implement your tRPC router. A sample router is given below:

server.ts

ts

`import * as trpc from '@trpc/server';`

`import { z } from 'zod';`

`const appRouter = trpc`

  `.router()`

  `.query('getUser', {`

    `input: z.string(),`

    `async resolve(req) {`

      `req.input; // string`

      `return { id: req.input, name: 'Bilbo' };`

    `},`

  `})`

  `.mutation('createUser', {`

    `// validate input with Zod`

    `input: z.object({ name: z.string().min(5) }),`

    `async resolve(req) {`

      `// use your ORM of choice`

      `return await UserModel.create({`

        `data: req.input,`

      `});`

    `},`

  `});`

`// export type definition of API`

`export type AppRouter = typeof appRouter;`

If your router file starts getting too big, split your router into several subrouters each implemented in its own file. Then [merge them](trpc/docs/v9/merging-routers/index.md) into a single root `appRouter`.

### 3\. Use the Express.js adapter[​](#3-use-the-expressjs-adapter "Direct link to 3. Use the Express.js adapter")

tRPC includes an adapter for Express.js out of the box. This adapter lets you convert your tRPC router into an Express.js middleware.

server.ts

ts

`import * as trpcExpress from '@trpc/server/adapters/express';`

`const appRouter = /* ... */;`

`const app = express();`

`// created for each request`

`const createContext = ({`

  `req,`

  `res,`

`}: trpcExpress.CreateExpressContextOptions) => ({}) // no context`

`type Context = trpc.inferAsyncReturnType<typeof createContext>;`

`app.use(`

  `'/trpc',`

  `trpcExpress.createExpressMiddleware({`

    `router: appRouter,`

    `createContext,`

  `})`

`);`

`app.listen(4000);`

Your endpoints are now available via HTTP!

Endpoint

HTTP URI

`getUser`

`GET http://localhost:4000/trpc/getUser?input=INPUT`

where `INPUT` is a URI-encoded JSON string.

`createUser`

`POST http://localhost:4000/trpc/createUser`

with `req.body` of type `{name: string}`


