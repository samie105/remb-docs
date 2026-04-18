---
title: "Subscriptions / WebSockets"
source: "https://trpc.io/docs/v9/subscriptions"
canonical_url: "https://trpc.io/docs/v9/subscriptions"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:16.621Z"
content_hash: "5b1dba11492aeaa7e54bad2a21e821bc22f5a9cde1ce457faadb17269e457aea"
menu_path: ["Subscriptions / WebSockets"]
section_path: []
---
## Using Subscriptions[​](#using-subscriptions "Direct link to Using Subscriptions")

tip

*   For a full-stack example have a look at [/examples/next-prisma-starter-websockets](https://github.com/trpc/examples-next-prisma-starter-websockets).
*   For a bare-minimum Node.js example see [/examples/standalone-server](https://github.com/trpc/trpc/tree/main/examples/standalone-server).

### Adding a subscription procedure[​](#adding-a-subscription-procedure "Direct link to Adding a subscription procedure")

server/router.ts

tsx

`import { EventEmitter } from 'events';`

`import * as trpc from '@trpc/server';`

`// create a global event emitter (could be replaced by redis, etc)`

`const ee = new EventEmitter();`

`export const appRouter = trpc`

  `.router()`

  `.subscription('onAdd', {`

    `resolve({ ctx }) {`

      `` // `resolve()` is triggered for each client when they start subscribing `onAdd` ``

      ``// return a `Subscription` with a callback which is triggered immediately``

      `return new trpc.Subscription<Post>((emit) => {`

        `const onAdd = (data: Post) => {`

          `// emit data to client`

          `emit.data(data);`

        `};`

        ``// trigger `onAdd()` when `add` is triggered in our event emitter``

        `ee.on('add', onAdd);`

        `// unsubscribe function when client disconnects or stops subscribing`

        `return () => {`

          `ee.off('add', onAdd);`

        `};`

      `});`

    `},`

  `})`

  `.mutation('add', {`

    `input: z.object({`

      `id: z.string().uuid().optional(),`

      `text: z.string().min(1),`

    `}),`

    `async resolve({ ctx, input }) {`

      `const post = { ...input }; /* [..] add to db */`

      `ee.emit('add', post);`

      `return post;`

    `},`

  `});`

### Creating a WebSocket-server[​](#creating-a-websocket-server "Direct link to Creating a WebSocket-server")

bash

`yarn add ws`

server/wsServer.ts

ts

`import { applyWSSHandler } from '@trpc/server/adapters/ws';`

`import ws from 'ws';`

`import { appRouter } from './routers/app';`

`import { createContext } from './trpc';`

`const wss = new ws.Server({`

  `port: 3001,`

`});`

`const handler = applyWSSHandler({ wss, router: appRouter, createContext });`

`wss.on('connection', (ws) => {`

  ``console.log(`➕➕ Connection (${wss.clients.size})`);``

  `ws.once('close', () => {`

    ``console.log(`➖➖ Connection (${wss.clients.size})`);``

  `});`

`});`

`console.log('✅ WebSocket Server listening on ws://localhost:3001');`

`process.on('SIGTERM', () => {`

  `console.log('SIGTERM');`

  `handler.broadcastReconnectNotification();`

  `wss.close();`

`});`

### Setting `TRPCClient` to use WebSockets[​](#setting-trpcclient-to-use-websockets "Direct link to setting-trpcclient-to-use-websockets")

tip

You can [use Links](https://trpc.io/docs/v9/links) to route queries and/or mutations to HTTP transport and subscriptions over WebSockets.

client.ts

tsx

`import { httpBatchLink } from '@trpc/client/links/httpBatchLink';`

`import { createWSClient, wsLink } from '@trpc/client/links/wsLink';`

`// create persistent WebSocket connection`

`const wsClient = createWSClient({`

  ``url: `ws://localhost:3001`,``

`});`

`// configure TRPCClient to use WebSockets transport`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `wsLink({`

      `client: wsClient,`

    `}),`

  `],`

`});`

### Using React[​](#using-react "Direct link to Using React")

See [/examples/next-prisma-starter-websockets](https://github.com/trpc/examples-next-prisma-starter-websockets).

## WebSockets RPC Specification[​](#websockets-rpc-specification "Direct link to WebSockets RPC Specification")

> You can read more details by drilling into the TypeScript definitions:
> 
> *   [/packages/server/src/unstable-core-do-not-import/rpc/envelopes.ts](https://github.com/trpc/trpc/tree/main/packages/server/src/unstable-core-do-not-import/rpc/envelopes.ts)
> *   [/packages/server/src/unstable-core-do-not-import/rpc/codes.ts](https://github.com/trpc/trpc/tree/main/packages/server/src/unstable-core-do-not-import/rpc/codes.ts).

### `query` / `mutation`[​](#query--mutation "Direct link to query--mutation")

#### Request[​](#request "Direct link to Request")

ts

`{`

  `id: number | string;`

  `jsonrpc?: '2.0';`

  `method: 'query' | 'mutation';`

  `params: {`

    `path: string;`

    `input?: unknown; // <-- pass input of procedure, serialized by transformer`

  `};`

`}`

#### Response[​](#response "Direct link to Response")

_... below, or an error._

ts

`{`

  `id: number | string;`

  `jsonrpc: '2.0';`

  `result: {`

    `type: 'data'; // always 'data' for mutation / queries`

    `data: TOutput; // output from procedure`

  `}`

`}`

### `subscription` / `subscription.stop`[​](#subscription--subscriptionstop "Direct link to subscription--subscriptionstop")

#### Start a subscription[​](#start-a-subscription "Direct link to Start a subscription")

ts

`{`

  `id: number | string;`

  `jsonrpc?: '2.0';`

  `method: 'subscription';`

  `params: {`

    `path: string;`

    `input?: unknown; // <-- pass input of procedure, serialized by transformer`

  `};`

`}`

#### To cancel a subscription, call `subscription.stop`[​](#to-cancel-a-subscription-call-subscriptionstop "Direct link to to-cancel-a-subscription-call-subscriptionstop")

ts

`{`

  `id: number | string; // <-- id of your created subscription`

  `jsonrpc?: '2.0';`

  `method: 'subscription.stop';`

`}`

#### Subscription response shape[​](#subscription-response-shape "Direct link to Subscription response shape")

_... below, or an error._

ts

`{`

  `id: number | string;`

  `jsonrpc: '2.0';`

  `result: (`

    `| {`

      `type: 'data';`

        `data: TData; // subscription emitted data`

      `}`

    `| {`

        `type: 'started'; // sub started`

      `}`

    `| {`

        `type: 'stopped'; // sub stopped`

      `}`

  `)`

`}`

## Errors[​](#errors "Direct link to Errors")

See [https://www.jsonrpc.org/specification#error\_object](https://www.jsonrpc.org/specification#error_object) or [Error Formatting](https://trpc.io/docs/v9/error-formatting).

## Notifications from Server to Client[​](#notifications-from-server-to-client "Direct link to Notifications from Server to Client")

### `{id: null, type: 'reconnect' }`[​](#id-null-type-reconnect- "Direct link to id-null-type-reconnect-")

Tells clients to reconnect before shutting down server. Invoked by `wssHandler.broadcastReconnectNotification()`.
