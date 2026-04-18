---
title: "WebSocket Link"
source: "https://trpc.io/docs/v10/client/links/wsLink"
canonical_url: "https://trpc.io/docs/v10/client/links/wsLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:39.420Z"
content_hash: "bbd530c1a0440489811a0434c2c3dc44a346c4dc9cfc416cefd9f882dac0db61"
menu_path: ["WebSocket Link"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/links/loggerLink/index.md", "title": "Logger Link"}
nav_next: {"path": "trpc/docs/v10/client/links/splitLink/index.md", "title": "Split Link"}
---

`wsLink` is a [**terminating link**](trpc/docs/v10/client/links/index.md#the-terminating-link) that's used when using tRPC's WebSockets Client and Subscriptions, which you can learn more about [here](trpc/docs/v10/subscriptions/index.md).

## Usage[​](#usage "Direct link to Usage")

To use `wsLink`, you need to pass it a `TRPCWebSocketClient`, which you can create with `createWSClient`:

client/index.ts

ts

`import { createTRPCProxyClient, createWSClient, wsLink } from '@trpc/client';`

`import type { AppRouter } from '../server';`

`const wsClient = createWSClient({`

  `url: 'ws://localhost:3000',`

`});`

`const trpcClient = createTRPCProxyClient<AppRouter>({`

  `links: [wsLink<AppRouter>({ client: wsClient })],`

`});`

## `wsLink` Options[​](#wslink-options "Direct link to wslink-options")

The `wsLink` function requires a `TRPCWebSocketClient` to be passed, which can be configured with the fields defined in `WebSocketClientOptions`:

ts

`export interface WebSocketLinkOptions {`

  `client: TRPCWebSocketClient;`

`}`

`function createWSClient(opts: WebSocketClientOptions) => TRPCWebSocketClient`

`export interface WebSocketClientOptions {`

  `url: string;`

  `WebSocket?: typeof WebSocket;`

  `retryDelayMs?: typeof retryDelay;`

  `onOpen?: () => void;`

  `onClose?: (cause?: { code?: number }) => void;`

`}`

## Reference[​](#reference "Direct link to Reference")

You can check out the source code for this link on [GitHub.](https://github.com/trpc/trpc/blob/main/packages/client/src/links/wsLink.ts)
