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
---
> **splitLink**<`TRouter`\>(`opts`): [`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\>

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

{ `condition`: (`op`) => `boolean`; `false`: [`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\> | [`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\>\[\]; `true`: [`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\> | [`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\>\[\]; }

\-

`opts.condition`

(`op`) => `boolean`

\-

`opts.false`

[`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\> | [`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\>\[\]

The link to execute next if the test function returns `false`.

`opts.true`

[`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\> | [`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\>\[\]

The link to execute next if the test function returns `true`.

## Returns[​](#returns "Direct link to Returns")

[`TRPCLink`](https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCLink)<`TRouter`\>
