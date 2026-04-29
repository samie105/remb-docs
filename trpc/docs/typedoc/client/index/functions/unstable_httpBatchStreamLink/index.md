---
title: "Function: unstable_httpBatchStreamLink()"
source: "https://trpc.io/docs/typedoc/client/index/functions/unstable_httpBatchStreamLink"
canonical_url: "https://trpc.io/docs/typedoc/client/index/functions/unstable_httpBatchStreamLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:45.745Z"
content_hash: "480635f3b9fa1512326990ec94cc78d1530bf5d2760012fca41d75908650357e"
menu_path: ["Function: unstable_httpBatchStreamLink()"]
section_path: []
nav_prev: {"path": "../retryLink/index.md", "title": "Function: retryLink()"}
nav_next: {"path": "../unstable_httpSubscriptionLink/index.md", "title": "Function: unstable_httpSubscriptionLink()"}
---

> **unstable\_httpBatchStreamLink**<`TRouter`\>(`opts`): [`TRPCLink`](../../type-aliases/TRPCLink/index.md)<`TRouter`\>

Defined in: [packages/client/src/links/httpBatchStreamLink.ts:227](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/httpBatchStreamLink.ts#L227)

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TRouter` _extends_ `AnyRouter`

## Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`opts`

[`HTTPBatchStreamLinkOptions`](../../type-aliases/HTTPBatchStreamLinkOptions/index.md)<`TRouter`\[`"_def"`\]\[`"_config"`\]\[`"$types"`\]>

## Returns[​](#returns "Direct link to Returns")

[`TRPCLink`](../../type-aliases/TRPCLink/index.md)<`TRouter`\>

## Deprecated[​](#deprecated "Direct link to Deprecated")

use [httpBatchStreamLink](../httpBatchStreamLink/index.md) instead

## See[​](#see "Direct link to See")

[https://trpc.io/docs/client/links/httpBatchStreamLink](../../../../../client/links/httpBatchStreamLink/index.md)
