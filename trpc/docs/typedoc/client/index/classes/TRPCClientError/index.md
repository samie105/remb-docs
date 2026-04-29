---
title: "Class: TRPCClientError<TRouterOrProcedure>"
source: "https://trpc.io/docs/typedoc/client/index/classes/TRPCClientError"
canonical_url: "https://trpc.io/docs/typedoc/client/index/classes/TRPCClientError"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:11.232Z"
content_hash: "15db2ec3428c1cd88a0bb298d946e4bbf20010f0ee4acfb4bf1b30ec89436020"
menu_path: ["Class: TRPCClientError<TRouterOrProcedure>"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/index/index.md", "title": "index"}
nav_next: {"path": "trpc/docs/typedoc/client/index/classes/TRPCUntypedClient/index.md", "title": "Class: TRPCUntypedClient<TInferrable>"}
---

Defined in: [packages/client/src/TRPCClientError.ts:47](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L47)

## Extends[​](#extends "Direct link to Extends")

*   `Error`

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TRouterOrProcedure` _extends_ `InferrableClientTypes`

## Implements[​](#implements "Direct link to Implements")

*   [`TRPCClientErrorBase`](../../interfaces/TRPCClientErrorBase/index.md)<`inferErrorShape`<`TRouterOrProcedure`\>>

## Constructors[​](#constructors "Direct link to Constructors")

### new TRPCClientError()[​](#new-trpcclienterror "Direct link to new TRPCClientError()")

> **new TRPCClientError**<`TRouterOrProcedure`\>(`message`, `opts`?): [`TRPCClientError`](index.md)<`TRouterOrProcedure`\>

Defined in: [packages/client/src/TRPCClientError.ts:63](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L63)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`message`

`string`

`opts`?

{ `cause`: `Error`; `meta`: `Record`<`string`, `unknown`\>; `result`: `Maybe`<`TRPCErrorResponse`<`inferErrorShape`<`TRouterOrProcedure`\>>>; }

`opts.cause`?

`Error`

`opts.meta`?

`Record`<`string`, `unknown`\>

`opts.result`?

`Maybe`<`TRPCErrorResponse`<`inferErrorShape`<`TRouterOrProcedure`\>>>

#### Returns[​](#returns "Direct link to Returns")

[`TRPCClientError`](index.md)<`TRouterOrProcedure`\>

#### Overrides[​](#overrides "Direct link to Overrides")

`Error.constructor`

## Properties[​](#properties "Direct link to Properties")

### cause[​](#cause "Direct link to cause")

> `readonly` **cause**: `undefined` | `Error`

Defined in: [packages/client/src/TRPCClientError.ts:53](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L53)

#### Overrides[​](#overrides-1 "Direct link to Overrides")

`Error.cause`

* * *

### data[​](#data "Direct link to data")

> `readonly` **data**: `Maybe`<`inferErrorShape`<`TRouterOrProcedure`\>\[`"data"`\]>

Defined in: [packages/client/src/TRPCClientError.ts:55](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L55)

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[`TRPCClientErrorBase`](../../interfaces/TRPCClientErrorBase/index.md).[`data`](../../interfaces/TRPCClientErrorBase/index.md#data)

* * *

### meta[​](#meta "Direct link to meta")

> **meta**: `undefined` | `Record`<`string`, `unknown`\>

Defined in: [packages/client/src/TRPCClientError.ts:61](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L61)

Additional meta data about the error In the case of HTTP-errors, we'll have `response` and potentially `responseJSON` here

* * *

### shape[​](#shape "Direct link to shape")

> `readonly` **shape**: `Maybe`<`inferErrorShape`<`TRouterOrProcedure`\>>

Defined in: [packages/client/src/TRPCClientError.ts:54](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L54)

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[`TRPCClientErrorBase`](../../interfaces/TRPCClientErrorBase/index.md).[`shape`](../../interfaces/TRPCClientErrorBase/index.md#shape)

## Methods[​](#methods "Direct link to Methods")

### from()[​](#from "Direct link to from()")

> `static` **from**<`TRouterOrProcedure`\>(`_cause`, `opts`): [`TRPCClientError`](index.md)<`TRouterOrProcedure`\>

Defined in: [packages/client/src/TRPCClientError.ts:87](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L87)

#### Type Parameters[​](#type-parameters-1 "Direct link to Type Parameters")

Type Parameter

`TRouterOrProcedure` _extends_ `InferrableClientTypes`

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`_cause`

`object` | `Error` | `TRPCErrorResponse`<`any`\>

`opts`

{ `cause`: `Error`; `meta`: `Record`<`string`, `unknown`\>; }

`opts.cause`?

`Error`

`opts.meta`?

`Record`<`string`, `unknown`\>

#### Returns[​](#returns-1 "Direct link to Returns")

[`TRPCClientError`](index.md)<`TRouterOrProcedure`\>
