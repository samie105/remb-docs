---
title: "Type Alias: TRPCFetch()"
source: "https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCFetch"
canonical_url: "https://trpc.io/docs/typedoc/client/index/type-aliases/TRPCFetch"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:23.462Z"
content_hash: "a51de5eafa08a139cf5686c4d5f1145fee9326dec277f6551d0327c861759239"
menu_path: ["Type Alias: TRPCFetch()"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/index/type-aliases/TRPCClient/index.md", "title": "Type Alias: TRPCClient<TRouter>"}
nav_next: {"path": "trpc/docs/typedoc/client/index/type-aliases/TRPCClientErrorLike/index.md", "title": "Type Alias: TRPCClientErrorLike<TInferrable>"}
---

> **TRPCFetch**: (`url`, `options`?) => `Promise`<`ResponseEsque`\>

Defined in: [packages/client/src/links/types.ts:50](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/types.ts#L50)

The default `fetch` implementation has an overloaded signature. By convention this library only uses the overload taking a string and options object.

## Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`url`

`string`

`options`?

`RequestInit`

## Returns[​](#returns "Direct link to Returns")

`Promise`<`ResponseEsque`\>
