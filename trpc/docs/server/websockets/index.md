---
title: "WebSockets"
source: "https://trpc.io/docs/server/websockets"
canonical_url: "https://trpc.io/docs/server/websockets"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:57.199Z"
content_hash: "68ee47958ee527ff832a7b113c8106cbd571c41ac0e50771713e6ec919f6590c"
menu_path: ["WebSockets"]
section_path: []
---
You can use WebSockets for all or some of the communication with your server, see [wsLink](https://trpc.io/docs/client/links/wsLink) for how to set it up on the client.

tip

The document here outlines the specific details of using WebSockets. For general usage of subscriptions, see [our subscriptions guide](https://trpc.io/docs/server/subscriptions).

### Creating a WebSocket-server[​](#creating-a-websocket-server "Direct link to Creating a WebSocket-server")

bash

`yarn add ws`

server/wsServer.ts

ts

`import { applyWSSHandler } from '@trpc/server/adapters/ws';`

`import { WebSocketServer } from 'ws';`

`import { appRouter } from './routers/app';`

`import { createContext } from './trpc';`

`const wss = new WebSocketServer({`

  `port: 3001,`

`});`

`const handler = applyWSSHandler({`

  `wss,`

  `router: appRouter,`

  `createContext,`

  `// Enable heartbeat messages to keep connection open (disabled by default)`

  `keepAlive: {`

    `enabled: true,`

    `// server ping message interval in milliseconds`

    `pingMs: 30000,`

    `// connection is terminated if pong message is not received in this many milliseconds`

    `pongWaitMs: 5000,`

  `},`

`});`

`wss.on('connection', (ws) => {`

  ``console.log(`++ Connection (${wss.clients.size})`);``

  `ws.once('close', () => {`

    ``console.log(`-- Connection (${wss.clients.size})`);``

  `});`

`});`

`console.log('WebSocket Server listening on ws://localhost:3001');`

`process.on('SIGTERM', () => {`

  `console.log('SIGTERM');`

  `handler.broadcastReconnectNotification();`

  `wss.close();`

`});`

### Setting `TRPCClient` to use WebSockets[​](#setting-trpcclient-to-use-websockets "Direct link to setting-trpcclient-to-use-websockets")

tip

You can use [Links](https://trpc.io/docs/client/links) to route queries and/or mutations to HTTP transport and subscriptions over WebSockets.

client.ts

tsx

`import { createTRPCClient, createWSClient, wsLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

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

## Authentication / connection params[​](#connectionParams "Direct link to Authentication / connection params")

tip

If you're doing a web application, you can ignore this section as the cookies are sent as part of the request.

In order to authenticate with WebSockets, you can define `connectionParams` to `createWSClient`. This will be sent as the first message when the client establishes a WebSocket connection.

server/context.ts

ts

`import type { CreateWSSContextFnOptions } from '@trpc/server/adapters/ws';`

`export const createContext = async (opts: CreateWSSContextFnOptions) => {`

  `const token = opts.info.connectionParams?.token;`

         `const token: string | undefined`

  `// [... authenticate]`

  `return {};`

`};`

`export type Context = Awaited<ReturnType<typeof createContext>>;`

client/trpc.ts

ts

`import { createTRPCClient, createWSClient, wsLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`import superjson from 'superjson';`

`const wsClient = createWSClient({`

  ``url: `ws://localhost:3000`,``

  `connectionParams: async () => {`

    `return {`

      `token: 'supersecret',`

    `};`

  `},`

`});`

`export const trpc = createTRPCClient<AppRouter>({`

  `links: [wsLink({ client: wsClient, transformer: superjson })],`

`});`

### Automatic tracking of id using `tracked()` (recommended)[​](#automatic-tracking-of-id-using-tracked-recommended "Direct link to automatic-tracking-of-id-using-tracked-recommended")

If you `yield` an event using our `tracked()`\-helper and include an `id`, the client will automatically reconnect when it gets disconnected and send the last known ID when reconnecting as part of the `lastEventId`\-input.

You can send an initial `lastEventId` when initializing the subscription and it will be automatically updated as the browser receives data.

info

If you're fetching data based on the `lastEventId`, and capturing all events is critical, you may want to use `ReadableStream`'s or a similar pattern as an intermediary as is done in [our full-stack SSE example](https://github.com/trpc/examples-next-sse-chat) to prevent newly emitted events being ignored while yield'ing the original batch based on `lastEventId`.

ts

`import EventEmitter, { on } from 'events';`

`import { initTRPC, tracked } from '@trpc/server';`

`import { z } from 'zod';`

`type Post = { id: string; title: string };`

`const t = initTRPC.create();`

`const publicProcedure = t.procedure;`

`const router = t.router;`

`const ee = new EventEmitter();`

`export const subRouter = router({`

  `onPostAdd: publicProcedure`

    `.input(`

      `z`

        `.object({`

          `// lastEventId is the last event id that the client has received`

          `// On the first call, it will be whatever was passed in the initial setup`

          `// If the client reconnects, it will be the last event id that the client received`

          `lastEventId: z.string().nullish(),`

        `})`

        `.optional(),`

    `)`

    `.subscription(async function* (opts) {`

      `if (opts.input?.lastEventId) {`

        `// [...] get the posts since the last event id and yield them`

      `}`

      `// listen for new events`

      `for await (const [data] of on(ee, 'add', {`

        `// Passing the AbortSignal from the request automatically cancels the event emitter when the subscription is aborted`

        `signal: opts.signal,`

      `})) {`

        `const post = data as Post;`

        `// tracking the post id ensures the client can reconnect at any time and get the latest events since this id`

        `yield tracked(post.id, post);`

      `}`

    `}),`

`});`

## WebSockets RPC Specification[​](#websockets-rpc-specification "Direct link to WebSockets RPC Specification")

> You can read more details by drilling into the TypeScript definitions:
> 
> *   [/packages/server/src/unstable-core-do-not-import/rpc/envelopes.ts](https://github.com/trpc/trpc/tree/main/packages/server/src/unstable-core-do-not-import/rpc/envelopes.ts)
> *   [/packages/server/src/unstable-core-do-not-import/rpc/codes.ts](https://github.com/trpc/trpc/tree/main/packages/server/src/unstable-core-do-not-import/rpc/codes.ts).

### `query` / `mutation`[​](#query--mutation "Direct link to query--mutation")

#### Request[​](#request "Direct link to Request")

ts

`interface RequestMessage {`

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

`interface ResponseMessage {`

  `id: number | string;`

  `jsonrpc?: '2.0';`

  `result: {`

    `type: 'data'; // always 'data' for mutation / queries`

    `data: TOutput; // output from procedure`

  `};`

`}`

### `subscription` / `subscription.stop`[​](#subscription--subscriptionstop "Direct link to subscription--subscriptionstop")

#### Start a subscription[​](#start-a-subscription "Direct link to Start a subscription")

ts

`interface SubscriptionRequest {`

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

`interface SubscriptionStopRequest {`

  `id: number | string; // <-- id of your created subscription`

  `jsonrpc?: '2.0';`

  `method: 'subscription.stop';`

`}`

#### Subscription response shape[​](#subscription-response-shape "Direct link to Subscription response shape")

_... below, or an error._

ts

`interface SubscriptionResponse {`

  `id: number | string;`

  `jsonrpc?: '2.0';`

  `result:`

    `| {`

        `type: 'data';`

        `data: TData; // subscription emitted data`

      `}`

    `| {`

        `type: 'started'; // subscription started`

      `}`

    `| {`

        `type: 'stopped'; // subscription stopped`

      `};`

`}`

#### Connection params[​](#connection-params "Direct link to Connection params")

If the connection is initialized with `?connectionParams=1`, the first message has to be connection params.

ts

`interface ConnectionParamsMessage {`

  `data: Record<string, string> | null;`

  `method: 'connectionParams';`

`}`

## Errors[​](#errors "Direct link to Errors")

See [https://www.jsonrpc.org/specification#error\_object](https://www.jsonrpc.org/specification#error_object) or [Error Formatting](https://trpc.io/docs/server/error-formatting).

## Notifications from Server to Client[​](#notifications-from-server-to-client "Direct link to Notifications from Server to Client")

### `{ id: null, type: 'reconnect' }`[​](#-id-null-type-reconnect- "Direct link to -id-null-type-reconnect-")

Tells clients to reconnect before shutting down the server. Invoked by `wssHandler.broadcastReconnectNotification()`.
