---
title: "querystring - Node documentation"
source: "https://docs.deno.com/api/node/querystring/"
canonical_url: "https://docs.deno.com/api/node/querystring/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:10:35.461Z"
content_hash: "975d7b31d7e30f813574fa47b14dae7eaf00d778821d7b58fa3129d2dbbe2a58"
menu_path: ["querystring - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/node/punycode/index.md", "title": "punycode - Node documentation"}
nav_next: {"path": "deno/api/node/readline/index.md", "title": "readline - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:querystring";
```

The `node:querystring` module provides utilities for parsing and formatting URL query strings. It can be accessed using:

```js
import querystring from 'node:querystring';
```

`querystring` is more performant than `URLSearchParams` but is not a standardized API. Use `URLSearchParams` when performance is not critical or when compatibility with browser code is desirable.

f

[escape](.././querystring/~/escape "escape")

The `querystring.escape()` method performs URL percent-encoding on the given `str` in a manner that is optimized for the specific requirements of URL query strings.

f

[parse](.././querystring/~/parse "parse")

The `querystring.parse()` method parses a URL query string (`str`) into a collection of key and value pairs.

f

[stringify](.././querystring/~/stringify "stringify")

The `querystring.stringify()` method produces a URL query string from a given `obj` by iterating through the object's "own properties".

f

[unescape](.././querystring/~/unescape "unescape")

The `querystring.unescape()` method performs decoding of URL percent-encoded characters on the given `str`.

I

[ParsedUrlQuery](.././querystring/~/ParsedUrlQuery "ParsedUrlQuery")

No documentation available

I

[ParsedUrlQueryInput](.././querystring/~/ParsedUrlQueryInput "ParsedUrlQueryInput")

No documentation available

I

[ParseOptions](.././querystring/~/ParseOptions "ParseOptions")

No documentation available

-   [decodeURIComponent](.././querystring/~/ParseOptions#property_decodeuricomponent)
-   [maxKeys](.././querystring/~/ParseOptions#property_maxkeys)

I

[StringifyOptions](.././querystring/~/StringifyOptions "StringifyOptions")

The `node:querystring` module provides utilities for parsing and formatting URL query strings. It can be accessed using:

-   [encodeURIComponent](.././querystring/~/StringifyOptions#property_encodeuricomponent)

v

[decode](.././querystring/~/decode "decode")

The querystring.decode() function is an alias for querystring.parse().

v

[encode](.././querystring/~/encode "encode")

The querystring.encode() function is an alias for querystring.stringify().
