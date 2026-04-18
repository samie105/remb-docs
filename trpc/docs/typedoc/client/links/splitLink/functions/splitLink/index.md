---
title: "Function: splitLink()"
source: "https://trpc.io/docs/typedoc/client/links/splitLink/functions/splitLink"
canonical_url: "https://trpc.io/docs/typedoc/client/links/splitLink/functions/splitLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:52.410Z"
content_hash: "d0a339e270df8028de87c9b26e84593063b50f0b566c946a196b222fc7e43a4f"
menu_path: ["Function: splitLink()"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/links/splitLink/index.md", "title": "links/splitLink"}
nav_next: {"path": "trpc/docs/typedoc/client/links/wsLink/wsLink/index.md", "title": "links/wsLink/wsLink"}
---

> **splitLink**<`TRouter`\>(`opts`): [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\>

Defined in: [packages/client/src/links/splitLink.ts:9](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/splitLink.ts#L9)

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

Default type

`TRouter` _extends_ `AnyRouter`

`AnyRouter`

## Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

Description

`opts`

{ `condition`: (`op`) => `boolean`; `false`: [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\> | [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\>\[\]; `true`: [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\> | [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\>\[\]; }

\-

`opts.condition`

(`op`) => `boolean`

\-

`opts.false`

[`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\> | [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\>\[\]

The link to execute next if the test function returns `false`.

`opts.true`

[`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\> | [`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\>\[\]

The link to execute next if the test function returns `true`.

## Returns[​](#returns "Direct link to Returns")

[`TRPCLink`](trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md)<`TRouter`\>


