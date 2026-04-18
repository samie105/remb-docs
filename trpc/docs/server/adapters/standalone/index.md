---
title: "Standalone Adapter"
source: "https://trpc.io/docs/server/adapters/standalone"
canonical_url: "https://trpc.io/docs/server/adapters/standalone"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:28.544Z"
content_hash: "6c85ff51975bdd5f3b0f803a18cc299baee22a9c6968bd50be82d69556744955"
menu_path: ["Standalone Adapter"]
section_path: []
nav_prev: {"path": "trpc/docs/server/adapters/fetch/index.md", "title": "Fetch / Edge Runtimes Adapter"}
nav_next: {"path": "trpc/docs/server/authorization/index.md", "title": "Authorization"}
---

tRPC's Standalone Adapter is the simplest way to get a new project working. It's ideal for local development, and for server-based production environments. In essence it's just a wrapper around the standard [Node.js HTTP Server](https://nodejs.org/api/http.html) with the normal options related to tRPC.

If you have an existing API deployment like [Express](trpc/docs/server/adapters/express/index.md), [Fastify](trpc/docs/server/adapters/fastify/index.md), or [Next.js](trpc/docs/server/adapters/nextjs/index.md), which you want to integrate tRPC into, you should have a look at their respective adapters. Likewise if you have a preference to host on serverless or edge compute, we have adapters like [AWS Lambda](trpc/docs/server/adapters/aws-lambda/index.md) and [Fetch](trpc/docs/server/adapters/fetch/index.md) which may fit your needs.

It's also not uncommon, where the deployed adapter is hard to run on local machines, to have 2 entry-points in your application. You could use the Standalone Adapter for local development, and a different adapter when deployed.

## Example app[​](#example-app "Direct link to Example app")

Description

Links

Standalone tRPC Server

*   [StackBlitz](https://stackblitz.com/github/trpc/trpc/tree/main/examples/minimal)
*   [Source](https://github.com/trpc/trpc/blob/main/examples/minimal/src/server/index.ts)

Standalone tRPC Server with CORS handling

*   [StackBlitz](https://stackblitz.com/github/trpc/trpc/tree/main/examples/minimal-react)
*   [Source](https://github.com/trpc/trpc/blob/main/examples/minimal-react/server/index.ts)

AI Agents

If you use an AI coding agent, install tRPC skills for better code generation:

bash

`npx @tanstack/intent@latest install`

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

      `return { id: '1', ...opts.input };`

    `}),`

`});`

`// export type definition of API`

`export type AppRouter = typeof appRouter;`

For more information, you can look at the [quickstart guide](trpc/docs/quickstart/index.md)

### 2\. Use the Standalone adapter[​](#2-use-the-standalone-adapter "Direct link to 2. Use the Standalone adapter")

The Standalone adapter runs a simple Node.js HTTP server.

server.ts

ts

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`import { appRouter } from './appRouter';`

`createHTTPServer({`

  `router: appRouter,`

  `createContext() {`

    `return {};`

  `},`

  `// basePath: '/trpc/', // optional, defaults to '/'`

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

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`import cors from 'cors';`

`import { appRouter } from './appRouter';`

`createHTTPServer({`

  `middleware: cors(),`

  `router: appRouter,`

  `createContext() {`

    `return {};`

  `},`

`}).listen(3333);`

The `middleware` option will accept any function which resembles a connect/node.js middleware, so it can be used for more than `cors` handling if you wish. It is, however, intended to be a simple escape hatch and as such won't on its own allow you to compose multiple middlewares together. If you want to do this then you could:

1.  Use an alternate adapter with more comprehensive middleware support, like the [Express adapter](trpc/docs/server/adapters/express/index.md)
2.  Use a solution to compose middlewares such as [connect](https://github.com/senchalabs/connect)
3.  Extend the Standalone `createHTTPHandler` with a custom http server (see below)

## Adding a handler to a Custom HTTP server[​](#adding-a-handler-to-a-custom-http-server "Direct link to Adding a handler to a Custom HTTP server")

`createHTTPServer` is returning an instance of Node's built-in [`http.Server`](https://nodejs.org/api/http.html#class-httpserver), which means that you have an access to all its properties and APIs. However, if `createHTTPServer` isn't enough for your use case, you can also use the standalone adapter's `createHTTPHandler` function to create your own HTTP server. For instance:

server.ts

ts

`import { createServer } from 'http';`

`import { createHTTPHandler } from '@trpc/server/adapters/standalone';`

`import { appRouter } from './appRouter';`

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

`}).listen(3001);`

## Custom base path for handling requests[​](#custom-basePath "Direct link to Custom base path for handling requests")

The Standalone adapter also supports a `basePath` option, which will slice the basePath from the beginning of the request path.

server.ts

ts

`import { createServer } from 'http';`

`import { createHTTPHandler } from '@trpc/server/adapters/standalone';`

`import { appRouter } from './appRouter';`

`const handler = createHTTPHandler({`

  `router: appRouter,`

  `basePath: '/trpc/',`

`});`

`createServer((req, res) => {`

  `if (req.url?.startsWith('/trpc/')) {`

    `return handler(req, res);`

  `}`

  `// [... insert your custom logic here ...]`

  `res.statusCode = 404;`

  `res.end('Not Found');`

`}).listen(3001);`

## HTTP2[​](#http2 "Direct link to HTTP2")

The Standalone adapter also supports HTTP/2.

server.ts

ts

`import http2 from 'http2';`

`import { createHTTP2Handler } from '@trpc/server/adapters/standalone';`

`import { appRouter } from './_app';`

`import { createContext } from './context';`

`const handler = createHTTP2Handler({`

  `router: appRouter,`

  `createContext,`

  `// basePath: '/trpc/', // optional, defaults to '/'`

`});`

`const server = http2.createSecureServer(`

  `{`

    `key: '...',`

    `cert: '...',`

  `},`

  `(req, res) => {`

    `/**`

     `* Handle the request however you like,`

     `* just call the tRPC handler when you're ready`

     `*/`

    `handler(req, res);`

  `},`

`);`

`server.listen(3001);`

context.ts

ts

`import { CreateHTTP2ContextOptions } from '@trpc/server/adapters/standalone';`

`export async function createContext(opts: CreateHTTP2ContextOptions) {`

  `opts.req;`

       `(property) req: http2.Http2ServerRequest`

  `opts.res;`

       `(property) res: http2.Http2ServerResponse`

  `opts.info;`

        `(property) info: TRPCRequestInfo`

  `return {};`

`}`

`export type Context = Awaited<ReturnType<typeof createContext>>;`
