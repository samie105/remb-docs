---
title: "Type Alias: HTTPBatchLinkOptions<TRoot>"
source: "https://trpc.io/docs/typedoc/client/index/type-aliases/HTTPBatchLinkOptions"
canonical_url: "https://trpc.io/docs/typedoc/client/index/type-aliases/HTTPBatchLinkOptions"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:08.539Z"
content_hash: "ff23121c28a1c090bc40bd6bf08fa06e109d0aff0c954c5c2054e49de17135b4"
menu_path: ["Type Alias: HTTPBatchLinkOptions<TRoot>"]
section_path: []
---
> **HTTPBatchLinkOptions**<`TRoot`\>: `HTTPLinkBaseOptions`<`TRoot`\> & `object`

Defined in: [packages/client/src/links/HTTPBatchLinkOptions.ts:6](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/HTTPBatchLinkOptions.ts#L6)

## Type declaration[​](#type-declaration "Direct link to Type declaration")

> `optional` **headers**: `HTTPHeaders` | (`opts`) => `HTTPHeaders` | `Promise`<`HTTPHeaders`\>

Headers to be set on outgoing requests or a callback that of said headers

#### See[​](#see "Direct link to See")

[http://trpc.io/docs/client/headers](http://trpc.io/docs/client/headers)

### maxItems?[​](#maxitems "Direct link to maxItems?")

> `optional` **maxItems**: `number`

Maximum number of calls in a single batch request

#### Default[​](#default "Direct link to Default")

ts

`Infinity`

### maxURLLength?[​](#maxurllength "Direct link to maxURLLength?")

> `optional` **maxURLLength**: `number`

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TRoot` _extends_ `AnyClientTypes`
