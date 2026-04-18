---
title: "@std/cli"
source: "https://docs.deno.com/runtime/reference/std/cli/"
canonical_url: "https://docs.deno.com/runtime/reference/std/cli/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:39.511Z"
content_hash: "9cc094fa7cf4418d00b48738d5c2acb37f1752b4fa9f3e2474083e04a1ec4654"
menu_path: ["@std/cli"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/cbor/index.md", "title": "@std/cbor"}
nav_next: {"path": "deno/deno/runtime/reference/std/collections/index.md", "title": "@std/collections"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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

