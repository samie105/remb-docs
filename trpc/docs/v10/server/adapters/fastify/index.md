---
title: "Fastify Adapter"
source: "https://trpc.io/docs/v10/server/adapters/fastify"
canonical_url: "https://trpc.io/docs/v10/server/adapters/fastify"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:13.030Z"
content_hash: "7a63561ff92ab323e42f9c124d8378fa083794c71835fe15cab0d89f531e3574"
menu_path: ["Fastify Adapter"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/server/adapters/express/index.md", "title": "Express Adapter"}
nav_next: {"path": "trpc/docs/v10/server/adapters/fetch/index.md", "title": "Fetch / Edge Runtimes Adapter"}
---

## Example app[​](#example-app "Direct link to Example app")

The best way to start with the Fastify adapter is to take a look at the example application.

Description

Links

*   Fastify server with WebSocket
*   Simple tRPC client in node

*   [CodeSandbox](https://codesandbox.io/s/github/trpc/trpc/tree/main/examples/fastify-server)
*   [Source](https://github.com/trpc/trpc/tree/main/examples/fastify-server)

## How to use tRPC with Fastify[​](#how-to-use-trpc-with-fastify "Direct link to How to use tRPC with Fastify")

### Install dependencies[​](#install-dependencies "Direct link to Install dependencies")

bash

`yarn add @trpc/server fastify zod`

> [Zod](https://github.com/colinhacks/zod) isn't a required dependency, but it's used in the sample router below.

### Create the router[​](#create-the-router "Direct link to Create the router")

First of all you need a [router](trpc/docs/server/routers/index.md) to handle your queries, mutations and subscriptions.

A sample router is given below, save it in a file named `router.ts`.

router.ts

If your router file starts getting too big, split your router into several subrouters each implemented in its own file. Then [merge them](trpc/docs/server/merging-routers/index.md) into a single root `appRouter`.

### Create the context[​](#create-the-context "Direct link to Create the context")

Then you need a [context](trpc/docs/server/context/index.md) that will be created for each request.

A sample context is given below, save it in a file named `context.ts`:

context.ts

### Create Fastify server[​](#create-fastify-server "Direct link to Create Fastify server")

tRPC includes an adapter for [Fastify](https://www.fastify.io/) out of the box. This adapter lets you convert your tRPC router into a [Fastify plugin](https://www.fastify.io/docs/latest/Reference/Plugins/). In order to prevent errors during large batch requests, make sure to set the `maxParamLength` Fastify option to a suitable value, as shown.

tip

Due to limitations in Fastify's plugin system and type inference, there might be some issues getting for example `onError` typed correctly. You can add a `satisfies FastifyTRPCPluginOptions<AppRouter>['trpcOptions']` to help TypeScript out and get the correct types.

server.ts

ts

`import {`

  `fastifyTRPCPlugin,`

  `FastifyTRPCPluginOptions,`

`} from '@trpc/server/adapters/fastify';`

`import fastify from 'fastify';`

`import { createContext } from './context';`

`import { appRouter, type AppRouter } from './router';`

`const server = fastify({`

  `maxParamLength: 5000,`

`});`

`server.register(fastifyTRPCPlugin, {`

  `prefix: '/trpc',`

  `trpcOptions: {`

    `router: appRouter,`

    `createContext,`

    `onError({ path, error }) {`

      `// report to error monitoring`

      ``console.error(`Error in tRPC handler on path '${path}':`, error);``

    `},`

  `} satisfies FastifyTRPCPluginOptions<AppRouter>['trpcOptions'],`

`});`

`(async () => {`

  `try {`

    `await server.listen({ port: 3000 });`

  `} catch (err) {`

    `server.log.error(err);`

    `process.exit(1);`

  `}`

`})();`

Your endpoints are now available via HTTP!

Endpoint

HTTP URI

`getUser`

`GET http://localhost:3000/trpc/getUserById?input=INPUT`

where `INPUT` is a URI-encoded JSON string.

`createUser`

`POST http://localhost:3000/trpc/createUser`

with `req.body` of type `User`

## How to enable subscriptions (WebSocket)[​](#how-to-enable-subscriptions-websocket "Direct link to How to enable subscriptions (WebSocket)")

The Fastify adapter supports [subscriptions](trpc/docs/v10/subscriptions/index.md) via the [@fastify/websocket](https://www.npmjs.com/package/@fastify/websocket) plugin. All you have to do in addition to the above steps is install the dependency, add some subscriptions to your router and activate the `useWSS` [option](#fastify-plugin-options) in the plugin. The minimum Fastify version required for `@fastify/websocket` is `3.11.0`.

### Install dependencies[​](#install-dependencies-1 "Direct link to Install dependencies")

bash

`yarn add @fastify/websocket`

### Import and register `@fastify/websocket`[​](#import-and-register-fastifywebsocket "Direct link to import-and-register-fastifywebsocket")

ts

`import ws from '@fastify/websocket';`

`server.register(ws);`

### Add some subscriptions[​](#add-some-subscriptions "Direct link to Add some subscriptions")

Edit the `router.ts` file created in the previous steps and add the following code:

router.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { observable } from '@trpc/server/observable';`

`const t = initTRPC.create();`

`export const appRouter = t.router({`

  `randomNumber: t.procedure.subscription(() => {`

    `return observable<{ randomNumber: number }>((emit) => {`

      `const timer = setInterval(() => {`

        `emit.next({ randomNumber: Math.random() });`

      `}, 1000);`

      `return () => {`

        `clearInterval(timer);`

      `};`

    `});`

  `}),`

`});`

### Activate the `useWSS` option[​](#activate-the-usewss-option "Direct link to activate-the-usewss-option")

server.ts

ts

`server.register(fastifyTRPCPlugin, {`

  `useWSS: true,`

  `// ...`

`});`

It's alright, you can subscribe to the topic `randomNumber` and you should receive a random number every second 🚀.

## Fastify plugin options[​](#fastify-plugin-options "Direct link to Fastify plugin options")

name

type

optional

default

description

prefix

`string`

`true`

`"/trpc"`

useWSS

`boolean`

`true`

`false`

trpcOptions

`NodeHTTPHandlerOptions`

`false`

`n/a`
