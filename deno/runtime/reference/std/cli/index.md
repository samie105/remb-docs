---
title: "@std/cli"
source: "https://docs.deno.com/runtime/reference/std/cli/"
canonical_url: "https://docs.deno.com/runtime/reference/std/cli/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:39:54.863Z"
content_hash: "d8c833072ced9f2c1af021abf206295527857c81b816d15d3bbb85cd9ecb747f"
menu_path: ["@std/cli"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/cbor/index.md", "title": "@std/cbor"}
nav_next: {"path": "deno/runtime/reference/std/collections/index.md", "title": "@std/collections"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Tools for creating interactive command line tools.

```js
import { parseArgs } from "@std/cli/parse-args";
import { assertEquals } from "@std/assert";

// Same as running `deno run example.ts --foo --bar=baz ./quux.txt`
const args = parseArgs(["--foo", "--bar=baz", "./quux.txt"]);
assertEquals(args, { foo: true, bar: "baz", _: ["./quux.txt"] });
```

### Add to your project

\>\_

```sh
deno add jsr:@std/cli
```

[See all symbols in @std/cli on](https://jsr.io/@std/cli/doc)
