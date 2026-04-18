---
title: "Type Alias: HTTPLinkOptions<TRoot>"
source: "https://trpc.io/docs/typedoc/client/links/httpLink/type-aliases/HTTPLinkOptions"
canonical_url: "https://trpc.io/docs/typedoc/client/links/httpLink/type-aliases/HTTPLinkOptions"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:40.797Z"
content_hash: "9d3060a60ad3d1c8830557f022950cb77f6d166a959a4d82f233e046b682e719"
menu_path: ["Type Alias: HTTPLinkOptions<TRoot>"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/links/httpLink/functions/httpLink/index.md", "title": "Function: httpLink()"}
nav_next: {"path": "trpc/docs/typedoc/client/links/loggerLink/index.md", "title": "links/loggerLink"}
---

> **HTTPLinkOptions**<`TRoot`\>: `HTTPLinkBaseOptions`<`TRoot`\> & `object`

Defined in: [packages/client/src/links/httpLink.ts:27](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/httpLink.ts#L27)

## Type declaration[​](#type-declaration "Direct link to Type declaration")

### headers?[​](#headers "Direct link to headers?")

> `optional` **headers**: `HTTPHeaders` | (`opts`) => `HTTPHeaders` | `Promise`<`HTTPHeaders`\>

Headers to be set on outgoing requests or a callback that of said headers

#### See[​](#see "Direct link to See")

[http://trpc.io/docs/client/headers](http://trpc.io/docs/client/headers)

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TRoot` _extends_ `AnyClientTypes`


