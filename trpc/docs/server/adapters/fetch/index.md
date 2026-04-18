---
title: "Fetch / Edge Runtimes Adapter"
source: "https://trpc.io/docs/server/adapters/fetch"
canonical_url: "https://trpc.io/docs/server/adapters/fetch"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:21.067Z"
content_hash: "cc422ffb2db3455d887a6c9ec55e71e91c50a7202247a12a16fa0d10236509ea"
menu_path: ["Fetch / Edge Runtimes Adapter"]
section_path: []
nav_prev: {"path": "trpc/docs/server/adapters/fastify/index.md", "title": "Fastify Adapter"}
nav_next: {"path": "trpc/docs/server/adapters/nextjs/index.md", "title": "Next.js Adapter"}
---

You can create a tRPC server within any edge runtime that follow the [WinterCG](https://wintercg.org/), specifically the [Minimum Common Web Platform API](https://common-min-api.proposal.wintercg.org/) specification.

Some of these runtimes include, but are not limited to:

*   Cloudflare Workers
*   Deno Deploy
*   Vercel Edge Runtime (& Next.js Edge Runtime)

This also makes it easy to integrate into frameworks that use the web platform APIs to represent requests and responses, such as:

*   Astro (SSR mode)
*   Remix
*   SolidStart

## Example apps[​](#example-apps "Direct link to Example apps")

Description

Links

Cloudflare Workers example

[

Source

](https://github.com/trpc/trpc/tree/main/examples/cloudflare-workers)

Deno Deploy example

[

Source

](https://github.com/trpc/trpc/tree/main/examples/deno-deploy)

Next.js Edge Runtime example

[

Source

](https://github.com/trpc/trpc/tree/main/examples/next-edge-runtime)

Vercel Edge Runtime example

[

Source

](https://github.com/trpc/trpc/tree/main/examples/vercel-edge-runtime)

## How to use tRPC server with an edge runtime[​](#how-to-use-trpc-server-with-an-edge-runtime "Direct link to How to use tRPC server with an edge runtime")

tRPC provides a [fetch adapter](trpc/docs/server/adapters/fetch/index.md) that uses the native [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) APIs as input and output. The tRPC-specific code is the same across all runtimes, the only difference being how the response is returned.

tRPC includes an adapter for the native [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) out of the box. This adapter lets you convert your tRPC router into a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) handler that returns [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) objects.

## Required Web APIs[​](#required-web-apis "Direct link to Required Web APIs")

tRPC server uses the following Fetch APIs:

*   `Request`, `Response`
*   `fetch`
*   `Headers`
*   `URL`

If your runtime supports these APIs, you can [use tRPC server](#how-to-use-trpc-server-with-an-edge-runtime).

tip

Fun fact: that also means you can use a tRPC server in your browser!

## Common setup[​](#common-setup "Direct link to Common setup")

### Install dependencies[​](#install-dependencies "Direct link to Install dependencies")

tip

You can skip this step if you use Deno Deploy.

*   npm
*   yarn
*   pnpm
*   bun
*   deno

npm install @trpc/server @trpc/client zod

> [Zod](https://github.com/colinhacks/zod) isn't a required dependency, but it's used in the sample router below.

AI Agents

If you use an AI coding agent, install tRPC skills for better code generation:

bash

`npx @tanstack/intent@latest install`

### Create the router[​](#create-the-router "Direct link to Create the router")

First of all you need a [router](trpc/docs/server/routers/index.md) to handle your queries, mutations and subscriptions.

A sample router is given below, save it in a file named `router.ts`.

router.ts

If your router file starts getting too big, split your router into several subrouters each implemented in its own file. Then [merge them](trpc/docs/server/merging-routers/index.md) into a single root `appRouter`.

### Create the context[​](#create-the-context "Direct link to Create the context")

Then you need a [context](trpc/docs/server/context/index.md) that will be created for each request.

A sample context is given below, save it in a file named `context.ts`:

context.ts

## Runtime-specific setup[​](#runtime-specific-setup "Direct link to Runtime-specific setup")

### Astro[​](#astro "Direct link to Astro")

src/pages/trpc/\[trpc\].ts

ts

`import { fetchRequestHandler } from '@trpc/server/adapters/fetch';`

`import type { APIRoute } from 'astro';`

`import { createContext } from '../../server/context';`

`import { appRouter } from '../../server/router';`

`export const ALL: APIRoute = (opts) => {`

  `return fetchRequestHandler({`

    `endpoint: '/trpc',`

    `req: opts.request,`

    `router: appRouter,`

    `createContext,`

  `});`

`};`

### Cloudflare Worker[​](#cloudflare-worker "Direct link to Cloudflare Worker")

#### Create Cloudflare Worker[​](#create-cloudflare-worker "Direct link to Create Cloudflare Worker")

server.ts

ts

`import { fetchRequestHandler } from '@trpc/server/adapters/fetch';`

`import { createContext } from './context';`

`import { appRouter } from './router';`

`export default {`

  `async fetch(request: Request): Promise<Response> {`

    `return fetchRequestHandler({`

      `endpoint: '/trpc',`

      `req: request,`

      `router: appRouter,`

      `createContext,`

    `});`

  `},`

`};`

Run `wrangler dev server.ts` and your endpoints will be available via HTTP!

Endpoint

HTTP URI

`getUser`

`GET http://localhost:8787/trpc/getUserById?input=INPUT`

where `INPUT` is a URI-encoded JSON string.

`createUser`

`POST http://localhost:8787/trpc/createUser`

with `req.body` of type `User`

### Deno Oak[​](#deno-oak "Direct link to Deno Oak")

note

This assumes you have Deno installed and setup. Refer to their [getting started guide](https://deno.com/manual/getting_started/installation) for more information.

#### Update the imports in `router.ts`[​](#update-the-imports-in-routerts "Direct link to update-the-imports-in-routerts")

router.ts

ts

`import { initTRPC } from 'npm:@trpc/server';`

`import { z } from 'npm:zod';`

`import { Context } from './context.ts';`

#### Update the imports in `context.ts`[​](#update-the-imports-in-contextts "Direct link to update-the-imports-in-contextts")

context.ts

ts

`import { FetchCreateContextFnOptions } from 'npm:@trpc/server/adapters/fetch';`

#### Use `fetchRequestHandler` with Oak in `app.ts`[​](#use-fetchrequesthandler-with-oak-in-appts "Direct link to use-fetchrequesthandler-with-oak-in-appts")

app.ts

ts

`import { Application, Router } from 'https://deno.land/x/oak/mod.ts';`

`import { fetchRequestHandler } from 'npm:@trpc/server/adapters/fetch';`

`import { createContext } from './context.ts';`

`import { appRouter } from './router.ts';`

`const app = new Application();`

`const router = new Router();`

`router.all('/trpc/(.*)', async (ctx) => {`

  `const res = await fetchRequestHandler({`

    `endpoint: '/trpc',`

    `req: new Request(ctx.request.url, {`

      `headers: ctx.request.headers,`

      `body:`

        `ctx.request.method !== 'GET' && ctx.request.method !== 'HEAD'`

          `? ctx.request.body({ type: 'stream' }).value`

          `: void 0,`

      `method: ctx.request.method,`

    `}),`

    `router: appRouter,`

    `createContext,`

  `});`

  `ctx.response.status = res.status;`

  `ctx.response.headers = res.headers;`

  `ctx.response.body = res.body;`

`});`

`app.use(router.routes());`

`app.use(router.allowedMethods());`

`await app.listen({ port: 3000 });`

### Deno Deploy[​](#deno-deploy "Direct link to Deno Deploy")

note

This assumes you have Deno installed and setup. Refer to their [getting started guide](https://deno.com/manual/getting_started/installation) for more information.

#### Update the imports in `router.ts`[​](#update-the-imports-in-routerts-1 "Direct link to update-the-imports-in-routerts-1")

router.ts

ts

`import { initTRPC } from 'npm:@trpc/server';`

`import { z } from 'npm:zod';`

`import { Context } from './context.ts';`

#### Update the imports in `context.ts`[​](#update-the-imports-in-contextts-1 "Direct link to update-the-imports-in-contextts-1")

context.ts

ts

`import { FetchCreateContextFnOptions } from 'npm:@trpc/server/adapters/fetch';`

#### Create Deno Deploy Function[​](#create-deno-deploy-function "Direct link to Create Deno Deploy Function")

server.ts

ts

`import { fetchRequestHandler } from 'npm:@trpc/server/adapters/fetch';`

`import { createContext } from './context.ts';`

`import { appRouter } from './router.ts';`

`function handler(request) {`

  `return fetchRequestHandler({`

    `endpoint: '/trpc',`

    `req: request,`

    `router: appRouter,`

    `createContext,`

  `});`

`}`

`Deno.serve(handler);`

Run `deno run --allow-net=:8000 --allow-env ./server.ts` and your endpoints will be available via HTTP!

Endpoint

HTTP URI

`getUser`

`GET http://localhost:8000/trpc/getUserById?input=INPUT`

where `INPUT` is a URI-encoded JSON string.

`createUser`

`POST http://localhost:8000/trpc/createUser`

with `req.body` of type `User`

### Next.js Edge Runtime[​](#nextjs-edge-runtime "Direct link to Next.js Edge Runtime")

See a full example [here](https://github.com/trpc/trpc/tree/main/examples/next-edge-runtime).

### Remix[​](#remix "Direct link to Remix")

app/routes/trpc.$trpc.ts

ts

`import type { ActionFunctionArgs, LoaderFunctionArgs } from '@remix-run/node';`

`import { fetchRequestHandler } from '@trpc/server/adapters/fetch';`

`import { createContext } from '~/server/context';`

`import { appRouter } from '~/server/router';`

`export const loader = async (args: LoaderFunctionArgs) => {`

  `return handleRequest(args);`

`};`

`export const action = async (args: ActionFunctionArgs) => {`

  `return handleRequest(args);`

`};`

`function handleRequest(args: LoaderFunctionArgs | ActionFunctionArgs) {`

  `return fetchRequestHandler({`

    `endpoint: '/trpc',`

    `req: args.request,`

    `router: appRouter,`

    `createContext,`

  `});`

`}`

### SolidStart[​](#solidstart "Direct link to SolidStart")

src/routes/api/trpc/\[trpc\].ts

ts

`import { fetchRequestHandler } from '@trpc/server/adapters/fetch';`

`import type { APIEvent } from '@solidjs/start/server';`

`import { createContext } from '../../server/context';`

`import { appRouter } from '../../server/router';`

`const handler = (event: APIEvent) =>`

  `fetchRequestHandler({`

    `endpoint: '/api/trpc',`

    `req: event.request,`

    `router: appRouter,`

    `createContext,`

  `});`

`export { handler as GET, handler as POST };`

### Vercel Edge Runtime[​](#vercel-edge-runtime "Direct link to Vercel Edge Runtime")

#### Install dependencies[​](#install-dependencies-1 "Direct link to Install dependencies")

*   npm
*   yarn
*   pnpm
*   bun

sh

`npm install -g edge-runtime`

sh

`npm install -g edge-runtime`

#### Create Edge Runtime Function[​](#create-edge-runtime-function "Direct link to Create Edge Runtime Function")

server.ts

ts

`import { fetchRequestHandler } from '@trpc/server/adapters/fetch';`

`import { createContext } from './context';`

`import { appRouter } from './router';`

`// Vercel Edge Runtime uses Service Worker-style addEventListener`

`addEventListener('fetch', (event: any) => {`

  `return event.respondWith(`

    `fetchRequestHandler({`

      `endpoint: '/trpc',`

      `req: event.request,`

      `router: appRouter,`

      `createContext,`

    `}),`

  `);`

`});`

Run `edge-runtime --listen server.ts --port 3000` and your endpoints will be available via HTTP!

Endpoint

HTTP URI

`getUser`

`GET http://localhost:3000/trpc/getUserById?input=INPUT`

where `INPUT` is a URI-encoded JSON string.

`createUser`

`POST http://localhost:3000/trpc/createUser`

with `req.body` of type `User`
