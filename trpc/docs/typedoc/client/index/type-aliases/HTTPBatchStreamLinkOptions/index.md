---
title: "Type Alias: HTTPBatchStreamLinkOptions<TRoot>"
source: "https://trpc.io/docs/typedoc/client/index/type-aliases/HTTPBatchStreamLinkOptions"
canonical_url: "https://trpc.io/docs/typedoc/client/index/type-aliases/HTTPBatchStreamLinkOptions"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:11.639Z"
content_hash: "1a5a9455a00f6aef427bdad85b65ba5a47542a2b73a11ae800626f42ec0c2645"
menu_path: ["Type Alias: HTTPBatchStreamLinkOptions<TRoot>"]
section_path: []
---
> **HTTPBatchStreamLinkOptions**<`TRoot`\>: [`HTTPBatchLinkOptions`](https://trpc.io/docs/typedoc/client/index/type-aliases/HTTPBatchLinkOptions)<`TRoot`\> & `object`

Defined in: [packages/client/src/links/httpBatchStreamLink.ts:21](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/httpBatchStreamLink.ts#L21)

## Type declaration[​](#type-declaration "Direct link to Type declaration")

> `optional` **streamHeader**: `"trpc-accept"` | `"accept"`

Which header to use to signal the server that the client wants a streaming response.

*   `'trpc-accept'` (default): sends `trpc-accept: application/jsonl` header
*   `'accept'`: sends `Accept: application/jsonl` header, which can avoid CORS preflight for cross-origin streaming queries. Be aware that `application/jsonl` is not an official MIME type and so this is not completely spec-compliant - you should test that your infrastructure supports this value.

#### Default[​](#default "Direct link to Default")

ts

`'trpc-accept'`

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TRoot` _extends_ `AnyClientTypes`
