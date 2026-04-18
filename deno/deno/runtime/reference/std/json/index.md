---
title: "@std/json"
source: "https://docs.deno.com/runtime/reference/std/json/"
canonical_url: "https://docs.deno.com/runtime/reference/std/json/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:45.067Z"
content_hash: "3213c9b9c136902b4b323a62572c59441c1d36b923707462e31dda35c0922bf5"
menu_path: ["@std/json"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/io/index.md", "title": "@std/io"}
nav_next: {"path": "deno/deno/runtime/reference/std/jsonc/index.md", "title": "@std/jsonc"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Utilities for parsing streaming JSON data.

```js
import { JsonStringifyStream } from "@std/json";
import { assertEquals } from "@std/assert";

const stream = ReadableStream.from([{ foo: "bar" }, { baz: 100 }])
  .pipeThrough(new JsonStringifyStream());

assertEquals(await Array.fromAsync(stream), [
  `{"foo":"bar"}\n`,
  `{"baz":100}\n`
]);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/json
```

[See all symbols in @std/json on](https://jsr.io/@std/json/doc)
