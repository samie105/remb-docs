---
title: "Interface: TRPCClientErrorBase<TShape>"
source: "https://trpc.io/docs/typedoc/client/index/interfaces/TRPCClientErrorBase"
canonical_url: "https://trpc.io/docs/typedoc/client/index/interfaces/TRPCClientErrorBase"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:57.579Z"
content_hash: "4ec6a958b491ae97ba99a0a59810aae8dd8c8701447a2fda69b7d177b9f28bdf"
menu_path: ["Interface: TRPCClientErrorBase<TShape>"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/index/interfaces/TRPCClientRuntime/index.md", "title": "Interface: TRPCClientRuntime"}
nav_next: {"path": "trpc/docs/typedoc/client/index/interfaces/TRPCProcedureOptions/index.md", "title": "Interface: TRPCProcedureOptions"}
---

Version: 11.x

Defined in: [packages/client/src/TRPCClientError.ts:14](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L14)

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TShape` _extends_ `DefaultErrorShape`

## Properties[​](#properties "Direct link to Properties")

### data[​](#data "Direct link to data")

> `readonly` **data**: `Maybe`<`TShape`\[`"data"`\]>

Defined in: [packages/client/src/TRPCClientError.ts:17](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L17)

* * *

### message[​](#message "Direct link to message")

> `readonly` **message**: `string`

Defined in: [packages/client/src/TRPCClientError.ts:15](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L15)

* * *

### shape[​](#shape "Direct link to shape")

> `readonly` **shape**: `Maybe`<`TShape`\>

Defined in: [packages/client/src/TRPCClientError.ts:16](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/TRPCClientError.ts#L16)

