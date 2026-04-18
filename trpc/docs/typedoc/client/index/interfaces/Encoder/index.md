---
title: "Interface: Encoder"
source: "https://trpc.io/docs/typedoc/client/index/interfaces/Encoder"
canonical_url: "https://trpc.io/docs/typedoc/client/index/interfaces/Encoder"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:52.448Z"
content_hash: "da98feeb3fc152c815c924445112015e2e4d5820a7e7c310da1b3f9e36db4bb5"
menu_path: ["Interface: Encoder"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/index/functions/unstable_httpSubscriptionLink/index.md", "title": "Function: unstable_httpSubscriptionLink()"}
nav_next: {"path": "trpc/docs/typedoc/client/index/interfaces/TRPCClientRuntime/index.md", "title": "Interface: TRPCClientRuntime"}
---

Defined in: packages/server/dist/adapters/ws.d.mts:22

Encoder for WebSocket wire format. Encodes outgoing messages and decodes incoming messages.

## Example[​](#example "Direct link to Example")

ts

`const customEncoder: Encoder = {`

  `encode: (data) => myFormat.stringify(data),`

  `decode: (data) => myFormat.parse(data),`

`};`

## Methods[​](#methods "Direct link to Methods")

### decode()[​](#decode "Direct link to decode()")

> **decode**(`data`): `unknown`

Defined in: packages/server/dist/adapters/ws.d.mts:26

Decode data received from the wire

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`data`

`string` | `ArrayBuffer` | `Uint8Array`<`ArrayBufferLike`\>

#### Returns[​](#returns "Direct link to Returns")

`unknown`

* * *

### encode()[​](#encode "Direct link to encode()")

> **encode**(`data`): `string` | `Uint8Array`<`ArrayBufferLike`\>

Defined in: packages/server/dist/adapters/ws.d.mts:24

Encode data for transmission over the wire

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`data`

`unknown`

#### Returns[​](#returns-1 "Direct link to Returns")

`string` | `Uint8Array`<`ArrayBufferLike`\>


