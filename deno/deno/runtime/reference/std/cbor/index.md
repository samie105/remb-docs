---
title: "@std/cbor"
source: "https://docs.deno.com/runtime/reference/std/cbor/"
canonical_url: "https://docs.deno.com/runtime/reference/std/cbor/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:30.288Z"
content_hash: "fd7f2cdfaf5014fd3068a2394b05991085fd59cd670b66616072f1af208cbff8"
menu_path: ["@std/cbor"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/cache/index.md", "title": "@std/cache"}
nav_next: {"path": "deno/deno/runtime/reference/std/cli/index.md", "title": "@std/cli"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

Concise Binary Object Representation (CBOR) is a binary data serialization format optimized for compactness and efficiency. It is designed to encode a wide range of data types, including integers, strings, arrays, and maps, in a space-efficient manner. [RFC 8949 - Concise Binary Object Representation (CBOR)](https://datatracker.ietf.org/doc/html/rfc8949) spec.

### Limitations

*   This implementation only supports the encoding and decoding of "Text String" keys.
*   This implementation encodes decimal numbers with 64 bits. It takes no effort to figure out if the decimal can be encoded with 32 or 16 bits.
*   When decoding, integers with a value below 2 \*\* 32 will be of type [number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number), with all larger integers being of type [bigint](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt).

Functions and classes may have more specific limitations listed.

```js
import { assert, assertEquals } from "@std/assert";
import { decodeCbor, encodeCbor } from "@std/cbor";

const rawMessage = "I am a raw Message!";

const encodedMessage = encodeCbor(rawMessage);
const decodedMessage = decodeCbor(encodedMessage);

assert(typeof decodedMessage === "string");
assertEquals(decodedMessage, rawMessage);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/cbor
```

[See all symbols in @std/cbor on](https://jsr.io/@std/cbor/doc)

