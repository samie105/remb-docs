---
title: "Interface: WebSocketClientOptions"
source: "https://trpc.io/docs/typedoc/client/index/interfaces/WebSocketClientOptions"
canonical_url: "https://trpc.io/docs/typedoc/client/index/interfaces/WebSocketClientOptions"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:07.546Z"
content_hash: "1b51eb657cdc410c8d07d300f161d905780643b8784f15c66d01da0877b7bb98"
menu_path: ["Interface: WebSocketClientOptions"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/index/type-aliases/CreateTRPCClient/index.md", "title": "Type Alias: CreateTRPCClient<TRouter>"}
nav_next: {"path": "trpc/docs/typedoc/client/index/type-aliases/HTTPBatchLinkOptions/index.md", "title": "Type Alias: HTTPBatchLinkOptions<TRoot>"}
---

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:4](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L4)

## Extends[​](#extends "Direct link to Extends")

*   `UrlOptionsWithConnectionParams`

## Properties[​](#properties "Direct link to Properties")

### connectionParams?[​](#connectionparams "Direct link to connectionParams?")

> `optional` **connectionParams**: `CallbackOrValue`<`null` | `Dict`<`string`\>>

Defined in: [packages/client/src/links/internals/urlWithConnectionParams.ts:32](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/internals/urlWithConnectionParams.ts#L32)

Connection params that are available in `createContext()`

*   For `wsLink`/`wsClient`, these are sent as the first message
*   For `httpSubscriptionLink`, these are serialized as part of the URL under the `connectionParams` query

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

`UrlOptionsWithConnectionParams.connectionParams`

* * *

### experimental\_encoder?[​](#experimental_encoder "Direct link to experimental_encoder?")

> `optional` **experimental\_encoder**: [`Encoder`](trpc/docs/typedoc/client/index/interfaces/Encoder/index.md)

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:64](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L64)

Custom encoder for wire encoding (e.g. custom binary formats)

#### Default[​](#default "Direct link to Default")

ts

`jsonEncoder`

* * *

### keepAlive?[​](#keepalive "Direct link to keepAlive?")

> `optional` **keepAlive**: `object`

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:44](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L44)

Send ping messages to the server and kill the connection if no pong message is returned

#### enabled[​](#enabled "Direct link to enabled")

> **enabled**: `boolean`

##### Default[​](#default-1 "Direct link to Default")

ts

`false`

#### intervalMs?[​](#intervalms "Direct link to intervalMs?")

> `optional` **intervalMs**: `number`

Send a ping message every this many milliseconds

##### Default[​](#default-2 "Direct link to Default")

ts

`5_000`

#### pongTimeoutMs?[​](#pongtimeoutms "Direct link to pongTimeoutMs?")

> `optional` **pongTimeoutMs**: `number`

Close the WebSocket after this many milliseconds if the server does not respond

##### Default[​](#default-3 "Direct link to Default")

ts

`1_000`

* * *

### lazy?[​](#lazy "Direct link to lazy?")

> `optional` **lazy**: `object`

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:29](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L29)

Lazy mode will close the WebSocket automatically after a period of inactivity (no messages sent or received and no pending requests)

#### closeMs[​](#closems "Direct link to closeMs")

> **closeMs**: `number`

Close the WebSocket after this many milliseconds

##### Default[​](#default-4 "Direct link to Default")

ts

`0`

#### enabled[​](#enabled-1 "Direct link to enabled")

> **enabled**: `boolean`

Enable lazy mode

##### Default[​](#default-5 "Direct link to Default")

ts

`false`

* * *

### onClose()?[​](#onclose "Direct link to onClose()?")

> `optional` **onClose**: (`cause`?) => `void`

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:25](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L25)

Triggered when a WebSocket connection is closed

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`cause`?

{ `code`: `number`; }

`cause.code`?

`number`

#### Returns[​](#returns "Direct link to Returns")

`void`

* * *

### onError()?[​](#onerror "Direct link to onError()?")

> `optional` **onError**: (`evt`?) => `void`

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:21](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L21)

Triggered when a WebSocket connection encounters an error

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`evt`?

`Event`

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

* * *

### onOpen()?[​](#onopen "Direct link to onOpen()?")

> `optional` **onOpen**: () => `void`

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:17](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L17)

Triggered when a WebSocket connection is established

#### Returns[​](#returns-2 "Direct link to Returns")

`void`

* * *

### retryDelayMs()?[​](#retrydelayms "Direct link to retryDelayMs()?")

> `optional` **retryDelayMs**: (`attemptIndex`) => `number`

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:13](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L13)

The number of milliseconds before a reconnect is attempted.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`attemptIndex`

`number`

#### Returns[​](#returns-3 "Direct link to Returns")

`number`

#### Default[​](#default-6 "Direct link to Default")

exponentialBackoff

* * *

### url[​](#url "Direct link to url")

> **url**: `CallbackOrValue`<`string`\>

Defined in: [packages/client/src/links/internals/urlWithConnectionParams.ts:25](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/internals/urlWithConnectionParams.ts#L25)

The URL to connect to (can be a function that returns a URL)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

`UrlOptionsWithConnectionParams.url`

* * *

### WebSocket()?[​](#websocket "Direct link to WebSocket()?")

> `optional` **WebSocket**: (`url`, `protocols`?) => `WebSocket`

Defined in: [packages/client/src/links/wsLink/wsClient/options.ts:8](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/wsLink/wsClient/options.ts#L8)

Ponyfill which WebSocket implementation to use

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`url`

`string` | `URL`

`protocols`?

`string` | `string`\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`WebSocket`


