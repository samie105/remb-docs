---
title: "Standalone Adapter"
source: "https://trpc.io/docs/v10/server/adapters/standalone"
canonical_url: "https://trpc.io/docs/v10/server/adapters/standalone"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:30.493Z"
content_hash: "d681637585595cbcbf011ab1a873b32316e8834a687b270ca80ca9ab45d5e844"
menu_path: ["Standalone Adapter"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/server/adapters/nextjs/index.md", "title": "Next.js Adapter"}
nav_next: {"path": "trpc/docs/v10/server/authorization/index.md", "title": "Authorization"}
---

tRPC's Standalone Adapter is the simplest way to get a new project working. It's ideal for local development, and for server-based production environments. In essence it's just a wrapper around the standard [Node.js HTTP Server](https://nodejs.org/api/http.html) with the normal options related to tRPC.

If you have an existing API deployment like [Express](trpc/docs/v10/server/adapters/express/index.md), [Fastify](trpc/docs/v10/server/adapters/fastify/index.md), or [Next.js](trpc/docs/v10/server/adapters/nextjs/index.md), which you want to integrate tRPC into, you should have a look at their respective adapters. Likewise if you have a preference to host on serverless or edge compute, we have adapters like [AWS Lambda](trpc/docs/v10/server/adapters/aws-lambda/index.md) and [Fetch](trpc/docs/v10/server/adapters/fetch/index.md) which may fit your needs.

It's also not uncommon, where the deployed adapter is hard to run on local machines, to have 2 entry-points in your application. You could use the Standalone Adapter for local development, and a different adapter when deployed.

## Example app[​](#example-app "Direct link to Example app")

Description

Links

Standalone tRPC Server

*   [StackBlitz](https://stackblitz.com/github/trpc/trpc/tree/main/examples/minimal)
*   [Source](https://github.com/trpc/trpc/blob/main/examples/minimal/server/index.ts)

Standalone tRPC Server with CORS handling

*   [StackBlitz](https://stackblitz.com/github/trpc/trpc/tree/main/examples/minimal-react)
*   [Source](https://github.com/trpc/trpc/blob/main/examples/minimal-react/server/index.ts)

## Setting up a Standalone tRPC Server[​](#setting-up-a-standalone-trpc-server "Direct link to Setting up a Standalone tRPC Server")

### 1\. Implement your App Router[​](#1-implement-your-app-router "Direct link to 1. Implement your App Router")

Implement your tRPC router. For example:

appRouter.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { z } from 'zod';`

`export const t = initTRPC.create();`

`export const appRouter = t.router({`

  `getUser: t.procedure.input(z.string()).query((opts) => {`

    `return { id: opts.input, name: 'Bilbo' };`

  `}),`

  `createUser: t.procedure`

    `.input(z.object({ name: z.string().min(5) }))`

    `.mutation(async (opts) => {`

      `// use your ORM of choice`

      `return await UserModel.create({`

        `data: opts.input,`

      `});`

    `}),`

`});`

`// export type definition of API`

`export type AppRouter = typeof appRouter;`

For more information you can look at the [quickstart guide](trpc/docs/quickstart/index.md)

### 2\. Use the Standalone adapter[​](#2-use-the-standalone-adapter "Direct link to 2. Use the Standalone adapter")

The Standalone adapter runs a simple Node.js HTTP server.

server.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`import { appRouter } from './appRouter.ts';`

`createHTTPServer({`

  `router: appRouter,`

  `createContext() {`

    `console.log('context 3');`

    `return {};`

  `},`

`}).listen(2022);`

## Handling CORS & OPTIONS[​](#handling-cors--options "Direct link to Handling CORS & OPTIONS")

By default the standalone server will not respond to HTTP OPTIONS requests, or set any CORS headers.

If you're not hosting in an environment which can handle this for you, like during local development, you may need to handle it.

### 1\. Install cors[​](#1-install-cors "Direct link to 1. Install cors")

You can add support yourself with the popular `cors` package

bash

`yarn add cors`

`yarn add -D @types/cors`

For full information on how to configure this package, [check the docs](https://github.com/expressjs/cors#readme)

### 2\. Configure the Standalone server[​](#2-configure-the-standalone-server "Direct link to 2. Configure the Standalone server")

This example just throws open CORS to any request, which is useful for development, but you can and should configure it more strictly in a production environment.

server.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`import cors from 'cors';`

`createHTTPServer({`

  `middleware: cors(),`

  `router: appRouter,`

  `createContext() {`

    `console.log('context 3');`

    `return {};`

  `},`

`}).listen(3333);`

The `middleware` option will accept any function which resembles a connect/node.js middleware, so it can be used for more than `cors` handling if you wish. It is, however, intended to be a simple escape hatch and as such won't on its own allow you to compose multiple middlewares together. If you want to do this then you could:

1.  Use an alternate adapter with more comprehensive middleware support, like the [Express adapter](trpc/docs/server/adapters/express/index.md)
2.  Use a solution to compose middlewares such as [connect](https://github.com/senchalabs/connect)
3.  Extend the Standalone `createHTTPHandler` with a custom http server (see below)

## Going further[​](#going-further "Direct link to Going further")

If `createHTTPServer` isn't enough you can also use the standalone adapter's `createHTTPHandler` function to create your own HTTP Server. For instance:

server.ts

ts

`import { createServer } from 'http';`

`import { initTRPC } from '@trpc/server';`

`import { createHTTPHandler } from '@trpc/server/adapters/standalone';`

`const handler = createHTTPHandler({`

  `router: appRouter,`

  `createContext() {`

    `return {};`

  `},`

`});`

`createServer((req, res) => {`

  `/**`

   `* Handle the request however you like,`

   `* just call the tRPC handler when you're ready`

   `*/`

  `handler(req, res);`

`}).listen(3333);`

