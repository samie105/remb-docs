---
title: "Class: TRPCUntypedClient<TInferrable>"
source: "https://trpc.io/docs/typedoc/client/index/classes/TRPCUntypedClient"
canonical_url: "https://trpc.io/docs/typedoc/client/index/classes/TRPCUntypedClient"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:12.574Z"
content_hash: "2aa258bb097743cc9f709f6b609cf6fe042874ccb36f11d4da9aa4f634085dfc"
menu_path: ["Class: TRPCUntypedClient<TInferrable>"]
section_path: []
---
Defined in: [packages/client/src/internals/TRPCUntypedClient.ts:47](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/internals/TRPCUntypedClient.ts#L47)

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TInferrable` _extends_ `InferrableClientTypes`

## Constructors[​](#constructors "Direct link to Constructors")

### new TRPCUntypedClient()[​](#new-trpcuntypedclient "Direct link to new TRPCUntypedClient()")

> **new TRPCUntypedClient**<`TInferrable`\>(`opts`): [`TRPCUntypedClient`](https://trpc.io/docs/typedoc/client/index/classes/TRPCUntypedClient)<`TInferrable`\>

Defined in: [packages/client/src/internals/TRPCUntypedClient.ts:52](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/internals/TRPCUntypedClient.ts#L52)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`opts`

`CreateTRPCClientOptions`<`TInferrable`\>

#### Returns[​](#returns "Direct link to Returns")

[`TRPCUntypedClient`](https://trpc.io/docs/typedoc/client/index/classes/TRPCUntypedClient)<`TInferrable`\>

## Properties[​](#properties "Direct link to Properties")

### runtime[​](#runtime "Direct link to runtime")

> `readonly` **runtime**: [`TRPCClientRuntime`](https://trpc.io/docs/typedoc/client/index/interfaces/TRPCClientRuntime)

Defined in: [packages/client/src/internals/TRPCUntypedClient.ts:49](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/internals/TRPCUntypedClient.ts#L49)

## Methods[​](#methods "Direct link to Methods")

### mutation()[​](#mutation "Direct link to mutation()")

> **mutation**(`path`, `input`?, `opts`?): `Promise`<`unknown`\>

Defined in: [packages/client/src/internals/TRPCUntypedClient.ts:106](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/internals/TRPCUntypedClient.ts#L106)

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`path`

`string`

`input`?

`unknown`

`opts`?

[`TRPCRequestOptions`](https://trpc.io/docs/typedoc/client/index/interfaces/TRPCRequestOptions)

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`unknown`\>

* * *

### query()[​](#query "Direct link to query()")

> **query**(`path`, `input`?, `opts`?): `Promise`<`unknown`\>

Defined in: [packages/client/src/internals/TRPCUntypedClient.ts:97](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/internals/TRPCUntypedClient.ts#L97)

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`path`

`string`

`input`?

`unknown`

`opts`?

[`TRPCRequestOptions`](https://trpc.io/docs/typedoc/client/index/interfaces/TRPCRequestOptions)

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`unknown`\>

* * *

### subscription()[​](#subscription "Direct link to subscription()")

> **subscription**(`path`, `input`, `opts`): `Unsubscribable`

Defined in: [packages/client/src/internals/TRPCUntypedClient.ts:115](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/internals/TRPCUntypedClient.ts#L115)

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`path`

`string`

`input`

`unknown`

`opts`

`Partial`<`TRPCSubscriptionObserver`<`unknown`, [`TRPCClientError`](https://trpc.io/docs/typedoc/client/index/classes/TRPCClientError)<`AnyRouter`\>>> & [`TRPCRequestOptions`](https://trpc.io/docs/typedoc/client/index/interfaces/TRPCRequestOptions)

#### Returns[​](#returns-3 "Direct link to Returns")

`Unsubscribable`
