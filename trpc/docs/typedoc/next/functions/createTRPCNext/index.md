---
title: "Function: createTRPCNext()"
source: "https://trpc.io/docs/typedoc/next/functions/createTRPCNext"
canonical_url: "https://trpc.io/docs/typedoc/next/functions/createTRPCNext"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:02.104Z"
content_hash: "40cdc69a9fb872421afd0299507f03dc8c3a5a4384b7119fe093c84986ae62ed"
menu_path: ["Function: createTRPCNext()"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/links/wsLink/wsLink/type-aliases/WebSocketLinkOptions/index.md", "title": "Type Alias: WebSocketLinkOptions<TRouter>"}
nav_next: {"path": "trpc/docs/typedoc/next/index.md", "title": "@trpc/next"}
---

> **createTRPCNext**<`TRouter`, `TSSRContext`\>(`opts`): `ProtectedIntersection`<`CreateTRPCNextBase`<`TRouter`, `TSSRContext`\>, `DecorateRouterRecord`<`TRouter`\[`"_def"`\]\[`"_config"`\]\[`"$types"`\], `TRouter`\[`"_def"`\]\[`"record"`\]>>

Defined in: [createTRPCNext.tsx:60](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/next/src/createTRPCNext.tsx#L60)

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

Default type

`TRouter` _extends_ `AnyRouter`

\-

`TSSRContext` _extends_ `NextPageContext`

`NextPageContext`

## Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`opts`

[`WithTRPCNoSSROptions`](https://trpc.io/docs/typedoc/next/type-aliases/WithTRPCNoSSROptions)<`TRouter`\> | [`WithTRPCSSROptions`](https://trpc.io/docs/typedoc/next/type-aliases/WithTRPCSSROptions)<`TRouter`\>

## Returns[​](#returns "Direct link to Returns")

`ProtectedIntersection`<`CreateTRPCNextBase`<`TRouter`, `TSSRContext`\>, `DecorateRouterRecord`<`TRouter`\[`"_def"`\]\[`"_config"`\]\[`"$types"`\], `TRouter`\[`"_def"`\]\[`"record"`\]>>

