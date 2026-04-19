---
title: "Function: unstable_localLink()"
source: "https://trpc.io/docs/typedoc/client/index/functions/unstable_localLink"
canonical_url: "https://trpc.io/docs/typedoc/client/index/functions/unstable_localLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:49.730Z"
content_hash: "f4c59b2e83836bc673cc71448877164cf62449d9c534976536c1522bc3694419"
menu_path: ["Function: unstable_localLink()"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/index/functions/unstable_httpSubscriptionLink/index.md", "title": "Function: unstable_httpSubscriptionLink()"}
nav_next: {"path": "trpc/docs/typedoc/client/index/interfaces/Encoder/index.md", "title": "Interface: Encoder"}
---

> **unstable\_localLink**<`TRouter`\>(`opts`): [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\>

Defined in: [packages/client/src/links/localLink.ts:40](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/localLink.ts#L40)

localLink is a terminating link that allows you to make tRPC procedure calls directly in your application without going through HTTP.

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TRouter` _extends_ `AnyRouter`

## Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`opts`

[`LocalLinkOptions`](trpc/docs/typedoc/client/index/type-aliases/LocalLinkOptions/index.md)<`TRouter`\>

## Returns[​](#returns "Direct link to Returns")

[`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\>

## See[​](#see "Direct link to See")

[https://trpc.io/docs/links/localLink](https://trpc.io/docs/links/localLink)
