---
title: "Usage with Fastify"
source: "https://trpc.io/docs/v9/fastify"
canonical_url: "https://trpc.io/docs/v9/fastify"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:01.669Z"
content_hash: "eabd386bfb2ef3817a3f76d48bf682f0c341cfdd800ee8bf254d884ab78f1927"
menu_path: ["Usage with Fastify"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/express/index.md", "title": "Usage with Express.js"}
nav_next: {"path": "trpc/docs/v9/header/index.md", "title": "Custom header"}
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

First of all you need a [router](trpc/docs/v9/router/index.md) to handle your queries, mutations and subscriptions.

A sample router is given below, save it in a file named `router.ts`.

router.ts

If your router file starts getting too big, split your router into several subrouters each implemented in its own file. Then [merge them](trpc/docs/v9/merging-routers/index.md) into a single root `appRouter`.

### Create the context[​](#create-the-context "Direct link to Create the context")

Then you need a [context](trpc/docs/v9/context/index.md) that will be created for each request.

A sample context is given below, save it in a file named `context.ts`:

context.ts

### Create Fastify server[​](#create-fastify-server "Direct link to Create Fastify server")

tRPC includes an adapter for [Fastify](https://www.fastify.io/) out of the box. This adapter lets you convert your tRPC router into an [Fastify plugin](https://www.fastify.io/docs/latest/Reference/Plugins/). In order to prevent errors during large batch requests, make sure to set the `maxParamLength` Fastify option to a suitable value, as shown.

server.ts

ts

`import { fastifyTRPCPlugin } from '@trpc/server/adapters/fastify';`

`import fastify from 'fastify';`

`import { createContext } from './context';`

`import { appRouter } from './router';`

`const server = fastify({`

  `maxParamLength: 5000,`

`});`

`server.register(fastifyTRPCPlugin, {`

  `prefix: '/trpc',`

  `trpcOptions: { router: appRouter, createContext },`

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

The Fastify adapter supports [subscriptions](trpc/docs/v9/subscriptions/index.md) via the [@fastify/websocket](https://www.npmjs.com/package/@fastify/websocket) plugin. All you have to do in addition to the above steps is install the dependency, add some subscriptions to your router and activate the `useWSS` [option](#fastify-plugin-options) in the plugin. The minimum Fastify version required for `@fastify/websocket` is `3.11.0`.

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

`export const appRouter = trpc`

  `.router()`

  `// .query(...)`

  `// .mutation(...)`

  `.subscription('randomNumber', {`

    `resolve() {`

      `return new Subscription<{ randomNumber: number }>((emit) => {`

        `const timer = setInterval(() => {`

          `emit.data({ randomNumber: Math.random() });`

        `}, 1000);`

        `return () => {`

          `clearInterval(timer);`

        `};`

      `});`

    `},`

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


