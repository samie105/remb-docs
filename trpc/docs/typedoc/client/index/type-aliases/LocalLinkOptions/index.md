---
title: "Type Alias: LocalLinkOptions<TRouter>"
source: "https://trpc.io/docs/typedoc/client/index/type-aliases/LocalLinkOptions"
canonical_url: "https://trpc.io/docs/typedoc/client/index/type-aliases/LocalLinkOptions"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:15.572Z"
content_hash: "24c3654596640f75ebe4b9c5f2076a64f23e58977b588a6d75aff280fa967dd0"
menu_path: ["Type Alias: LocalLinkOptions<TRouter>"]
section_path: []
---
> **LocalLinkOptions**<`TRouter`\>: `object` & `TransformerOptions`<`inferClientTypes`<`TRouter`\>>

Defined in: [packages/client/src/links/localLink.ts:29](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/localLink.ts#L29)

## Type declaration[​](#type-declaration "Direct link to Type declaration")

### createContext()[​](#createcontext "Direct link to createContext()")

> **createContext**: () => `Promise`<`inferRouterContext`<`TRouter`\>>

#### Returns[​](#returns "Direct link to Returns")

`Promise`<`inferRouterContext`<`TRouter`\>>

### onError()?[​](#onerror "Direct link to onError()?")

> `optional` **onError**: (`opts`) => `void`

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`opts`

`ErrorHandlerOptions`<`inferRouterContext`<`TRouter`\>>

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

### router[​](#router "Direct link to router")

> **router**: `TRouter`

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TRouter` _extends_ `AnyRouter`
