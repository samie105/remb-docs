---
title: "Interface: LoggerLinkOptions<TRouter>"
source: "https://trpc.io/docs/typedoc/client/links/loggerLink/interfaces/LoggerLinkOptions"
canonical_url: "https://trpc.io/docs/typedoc/client/links/loggerLink/interfaces/LoggerLinkOptions"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:47.101Z"
content_hash: "84ec29b3ed070aa9e745440f3db8ad71c28aceb1a5130c10ca80d550ae0c02b8"
menu_path: ["Interface: LoggerLinkOptions<TRouter>"]
section_path: []
nav_prev: {"path": "trpc/docs/typedoc/client/links/loggerLink/functions/loggerLink/index.md", "title": "Function: loggerLink()"}
nav_next: {"path": "trpc/docs/typedoc/client/links/splitLink/index.md", "title": "links/splitLink"}
---

Defined in: [packages/client/src/links/loggerLink.ts:61](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/loggerLink.ts#L61)

## Type Parameters[​](#type-parameters "Direct link to Type Parameters")

Type Parameter

`TRouter` _extends_ `AnyRouter`

## Properties[​](#properties "Direct link to Properties")

### colorMode?[​](#colormode "Direct link to colorMode?")

> `optional` **colorMode**: `ColorMode`

Defined in: [packages/client/src/links/loggerLink.ts:72](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/loggerLink.ts#L72)

Color mode

#### Default[​](#default "Direct link to Default")

ts

`typeof window === 'undefined' ? 'ansi' : 'css'`

* * *

### console?[​](#console "Direct link to console?")

> `optional` **console**: `ConsoleEsque`

Defined in: [packages/client/src/links/loggerLink.ts:67](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/loggerLink.ts#L67)

Used in the built-in defaultLogger

* * *

### enabled?[​](#enabled "Direct link to enabled?")

> `optional` **enabled**: `EnabledFn`<`TRouter`\>

Defined in: [packages/client/src/links/loggerLink.ts:63](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/loggerLink.ts#L63)

* * *

### logger?[​](#logger "Direct link to logger?")

> `optional` **logger**: `LoggerLinkFn`<`TRouter`\>

Defined in: [packages/client/src/links/loggerLink.ts:62](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/loggerLink.ts#L62)

* * *

### withContext?[​](#withcontext "Direct link to withContext?")

> `optional` **withContext**: `boolean`

Defined in: [packages/client/src/links/loggerLink.ts:77](https://github.com/trpc/trpc/blob/63407c577124e7a2890a7599484d52a0cf025536/packages/client/src/links/loggerLink.ts#L77)

Include context in the log - defaults to false unless `colorMode` is 'css'


