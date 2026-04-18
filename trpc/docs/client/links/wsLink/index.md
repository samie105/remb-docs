---
title: "WebSocket Link"
source: "https://trpc.io/docs/client/links/wsLink"
canonical_url: "https://trpc.io/docs/client/links/wsLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:24.215Z"
content_hash: "b505c1a23a3143c38619988a2aa800a888f326800669a45e32bf29e412526233"
menu_path: ["WebSocket Link"]
section_path: []
nav_prev: {"path": "trpc/docs/client/links/splitLink/index.md", "title": "Split Link"}
nav_next: {"path": "trpc/docs/client/nextjs/index.md", "title": "Next.js Integration"}
---

`export interface WebSocketLinkOptions {`

`client: TRPCWebSocketClient;`

`/**`

`* Data transformer`

`* @see https://trpc.io/docs/v11/data-transformers`

`**/`

`transformer?: DataTransformerOptions;`

`}`

`declare function createWSClient(opts: WebSocketClientOptions): TRPCWebSocketClient;`

`export interface WebSocketClientOptions {`

`/**`

`* The URL to connect to (can be a function that returns a URL)`

`*/`

`url: string | (() => MaybePromise<string>);`

`/**`

`` * Connection params that are available in `createContext()` ``

`* These are sent as the first message`

`*/`

`connectionParams?: Record<string, string> | null | (() => MaybePromise<Record<string, string> | null>);`

`/**`

`* Ponyfill which WebSocket implementation to use`

`*/`

`WebSocket?: typeof WebSocket;`

`/**`

`* The number of milliseconds before a reconnect is attempted.`

`* @default {@link exponentialBackoff}`

`*/`

`retryDelayMs?: typeof exponentialBackoff;`

`/**`

`* Triggered when a WebSocket connection is established`

`*/`

`onOpen?: () => void;`

`/**`

`* Triggered when a WebSocket connection encounters an error`

`*/`

`onError?: (evt?: Event) => void;`

`/**`

`* Triggered when a WebSocket connection is closed`

`*/`

`onClose?: (cause?: { code?: number }) => void;`

`/**`

`* Lazy mode will close the WebSocket automatically after a period of inactivity (no messages sent or received and no pending requests)`

`*/`

`lazy?: {`

`/**`

`* Enable lazy mode`

`* @default false`

`*/`

`enabled: boolean;`

`/**`

`* Close the WebSocket after this many milliseconds`

`* @default 0`

`*/`

`closeMs: number;`

`};`

`/**`

`* Send ping messages to the server and kill the connection if no pong message is returned`

`*/`

`keepAlive?: {`

`/**`

`* @default false`

`*/`

`enabled: boolean;`

`/**`

`* Send a ping message every this many milliseconds`

`* @default 5_000`

`*/`

`intervalMs?: number;`

`/**`

`* Close the WebSocket after this many milliseconds if the server does not respond`

`* @default 1_000`

`*/`

`pongTimeoutMs?: number;`

`};`

`/**`

`* Custom encoder for wire encoding (e.g. custom binary formats)`

`* @default jsonEncoder`

`*/`

`experimental_encoder?: Encoder;`

`}`
