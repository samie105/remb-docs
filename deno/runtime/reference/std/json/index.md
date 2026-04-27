---
title: "@std/json"
source: "https://docs.deno.com/runtime/reference/std/json/"
canonical_url: "https://docs.deno.com/runtime/reference/std/json/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:44:22.564Z"
content_hash: "6d4f8642e29be32eb60bdb0f20cec8ea5b97cf6ddef8e1c8e8c29bbb56a8275f"
menu_path: ["@std/json"]
section_path: []
content_language: "en"
---
**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

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
