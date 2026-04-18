---
title: "@std/jsonc"
source: "https://docs.deno.com/runtime/reference/std/jsonc/"
canonical_url: "https://docs.deno.com/runtime/reference/std/jsonc/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:54.308Z"
content_hash: "ab833add00b8c3b159d8304bc3e7abd2144387ec0207b26094871e9a1efacc98"
menu_path: ["@std/jsonc"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/json/index.md", "title": "@std/json"}
nav_next: {"path": "deno/deno/runtime/reference/std/log/index.md", "title": "@std/log"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Provides tools for working with [JSONC](https://code.visualstudio.com/docs/languages/json#_json-with-comments) (JSON with comments).

Currently, this module only provides a means of parsing JSONC. JSONC serialization is not yet supported.

```js
import { parse } from "@std/jsonc";
import { assertEquals } from "@std/assert";

assertEquals(parse('{"foo": "bar", } // comment'), { foo: "bar" });
assertEquals(parse('{"foo": "bar", } /* comment *\/'), { foo: "bar" });
```

### Add to your project

\>\_

```sh
deno add jsr:@std/jsonc
```

[See all symbols in @std/jsonc on](https://jsr.io/@std/jsonc/doc)

