---
title: "Function: httpSubscriptionLink()"
source: "https://trpc.io/docs/typedoc/client/index/functions/httpSubscriptionLink"
canonical_url: "https://trpc.io/docs/typedoc/client/index/functions/httpSubscriptionLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:29.785Z"
content_hash: "2e7565b6b398fcbe342a00a6ba0877c8d7dc5997ebe40356062b000580a7de05"
menu_path: ["Function: httpSubscriptionLink()"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/index/functions/httpBatchStreamLink/index.md", "title": "Function: httpBatchStreamLink()"}
nav_next: {"path": "trpc/docs/typedoc/client/index/functions/isFormData/index.md", "title": "Function: isFormData()"}
---

> **httpSubscriptionLink**<`TInferrable`, `TEventSource`\>(`opts`): [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TInferrable`\>

Defined in: [packages/client/src/links/httpSubscriptionLink.ts:65](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/httpSubscriptionLink.ts#L65)

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TInferrable` _extends_ `InferrableClientTypes`

`TEventSource` _extends_ `AnyConstructor`

## Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`opts`

`HTTPSubscriptionLinkOptions`<`inferClientTypes`<`TInferrable`\>, `TEventSource`\>

## Returns[​](#returns "Direct link to Returns")

[`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TInferrable`\>

## See[​](#see "Direct link to See")

[https://trpc.io/docs/client/links/httpSubscriptionLink](trpc/docs/client/links/httpSubscriptionLink/index.md)


