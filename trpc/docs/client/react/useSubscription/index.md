---
title: "useSubscription()"
source: "https://trpc.io/docs/client/react/useSubscription"
canonical_url: "https://trpc.io/docs/client/react/useSubscription"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:17.546Z"
content_hash: "35807a4ec34bc661d8d7f3f106c09ca333229869a0c244819b9e3d7924434162"
menu_path: ["useSubscription()"]
section_path: []
nav_prev: {"path": "../useQuery/index.md", "title": "useQuery()"}
nav_next: {"path": "../useUtils/index.md", "title": "useUtils"}
---

The `useSubscription` hook can be used to subscribe to a [subscription](../../../server/subscriptions/index.md) procedure on the server.

## Signature[​](#signature "Direct link to Signature")

### Options[​](#options "Direct link to Options")

tip

*   If you need to set any options but don't want to pass any input, you can pass `undefined` instead.
*   If you pass `skipToken` from `@tanstack/react-query`, the subscription will be paused.
*   Have a look at our [SSE example](https://github.com/trpc/examples-next-sse-chat) for a complete example of how to use subscriptions

tsx

`interface UseTRPCSubscriptionOptions<TOutput, TError> {`

  `/**`

   `* Called when the subscription is started.`

   `*/`

  `onStarted?: () => void;`

  `/**`

   `* Called when new data is received from the subscription.`

   `*/`

  `onData?: (data: TOutput) => void;`

  `/**`

   `* Called when an **unrecoverable error** occurs and the subscription is stopped.`

   `*/`

  `onError?: (error: TError) => void;`

  `/**`

   `* Called when the subscription is completed on the server.`

   ``* The state will transition to `'idle'` with `data: undefined`.``

   `*/`

  `onComplete?: () => void;`

  `/**`

   ``* @deprecated Use a `skipToken` from `@tanstack/react-query` instead.``

   `* This will be removed in v12.`

   `*/`

  `enabled?: boolean;`

`}`

### Return type[​](#return-type "Direct link to Return type")

The return type is a discriminated union on `status`:

ts

`type TRPCSubscriptionResult<TOutput, TError> =`

  `| TRPCSubscriptionIdleResult<TOutput>`

  `| TRPCSubscriptionConnectingResult<TOutput, TError>`

  `| TRPCSubscriptionPendingResult<TOutput>`

  `| TRPCSubscriptionErrorResult<TOutput, TError>;`

`interface TRPCSubscriptionIdleResult<TOutput> {`

  `/** Subscription is disabled or has ended */`

  `status: 'idle';`

  `data: undefined;`

  `error: null;`

  `reset: () => void;`

`}`

`interface TRPCSubscriptionConnectingResult<TOutput, TError> {`

  `/** Trying to establish a connection (may have a previous error from a reconnection attempt) */`

  `status: 'connecting';`

  `data: TOutput | undefined;`

  `error: TError | null;`

  `reset: () => void;`

`}`

`interface TRPCSubscriptionPendingResult<TOutput> {`

  `/** Connected to the server, receiving data */`

  `status: 'pending';`

  `data: TOutput | undefined;`

  `error: null;`

  `reset: () => void;`

`}`

`interface TRPCSubscriptionErrorResult<TOutput, TError> {`

  `/** An unrecoverable error occurred and the subscription is stopped */`

  `status: 'error';`

  `data: TOutput | undefined;`

  `error: TError;`

  `reset: () => void;`

`}`

## Example Procedure[​](#example-procedure "Direct link to Example Procedure")

server/routers/\_app.ts

tsx

`import EventEmitter, { on } from 'events';`

`import { initTRPC } from '@trpc/server';`

`export const t = initTRPC.create();`

`type Post = { id: string; title: string };`

`const ee = new EventEmitter();`

`export const appRouter = t.router({`

  `onPostAdd: t.procedure.subscription(async function* (opts) {`

    `for await (const [data] of on(ee, 'add', {`

      `signal: opts.signal,`

    `})) {`

      `const post = data as Post;`

      `yield post;`

    `}`

  `}),`

`});`

`export type AppRouter = typeof appRouter;`

## Example React Component[​](#example-react-component "Direct link to Example React Component")

components/PostFeed.tsx

tsx

`import { trpc } from '../utils/trpc';`

`type Post = { id: string; title: string };`

`export function PostFeed() {`

  `const [posts, setPosts] = React.useState<Post[]>([]);`

  `const subscription = trpc.onPostAdd.useSubscription(undefined, {`

    `onData: (post) => {`

      `setPosts((prev) => [...prev, post]);`

    `},`

  `});`

  `return (`

    `<div>`

      `<h1>Live Feed</h1>`

      `{subscription.status === 'connecting' && <p>Connecting...</p>}`

      `{subscription.status === 'error' && (`

        `<div>`

          `<p>Error: {subscription.error.message}</p>`

          `<button onClick={() => subscription.reset()}>Reconnect</button>`

        `</div>`

      `)}`

      `<ul>`

        `{posts.map((post) => (`

          `<li key={post.id}>{post.title}</li>`

        `))}`

      `</ul>`

    `</div>`

  `);`

`}`
