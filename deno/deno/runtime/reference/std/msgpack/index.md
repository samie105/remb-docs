---
title: "@std/msgpack"
source: "https://docs.deno.com/runtime/reference/std/msgpack/"
canonical_url: "https://docs.deno.com/runtime/reference/std/msgpack/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:04:33.283Z"
content_hash: "7ec4fde1f0b448f01cf25e3e154381be0fb7e49b164a1c01418b6bdaf383fc4a"
menu_path: ["@std/msgpack"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/media-types/index.md", "title": "@std/media-types"}
nav_next: {"path": "deno/deno/runtime/reference/std/net/index.md", "title": "@std/net"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

This module provides functions to encode and decode MessagePack.

MessagePack is an efficient binary serialization format that is language agnostic. It is like JSON, but generally produces much smaller payloads. [Learn more about MessagePack](https://msgpack.org/).

```js
import { decode, encode } from "@std/msgpack";
import { assertEquals } from "@std/assert";

const obj = {
  str: "deno",
  arr: [1, 2, 3],
  bool: true,
  nil: null,
  map: {
    foo: "bar"
  }
};

const encoded = encode(obj);
assertEquals(encoded.length, 42);

const decoded = decode(encoded);
assertEquals(decoded, obj);
```

MessagePack supports encoding and decoding the following types:

*   `number`
*   `bigint`
*   `string`
*   `boolean`
*   `null`
*   `Uint8Array`
*   arrays of values of these types
*   objects with string or number keys, and values of these types

### Add to your project

\>\_

```sh
deno add jsr:@std/msgpack
```

[See all symbols in @std/msgpack on](https://jsr.io/@std/msgpack/doc)


