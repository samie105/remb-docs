---
title: "@std/bytes"
source: "https://docs.deno.com/runtime/reference/std/bytes/"
canonical_url: "https://docs.deno.com/runtime/reference/std/bytes/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:39:02.977Z"
content_hash: "cf667625a223ff181adf53528c627cd6787508693abc156ac18b8d141598aa0f"
menu_path: ["@std/bytes"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/async/index.md", "title": "@std/async"}
nav_next: {"path": "deno/runtime/reference/std/cache/index.md", "title": "@std/cache"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Helper functions for working with [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) byte slices.

```js
import { concat, indexOfNeedle, endsWith } from "@std/bytes";
import { assertEquals } from "@std/assert";

const a = new Uint8Array([0, 1, 2]);
const b = new Uint8Array([3, 4, 5]);

const c = concat([a, b]);

assertEquals(c, new Uint8Array([0, 1, 2, 3, 4, 5]));

assertEquals(indexOfNeedle(c, new Uint8Array([2, 3])), 2);

assertEquals(endsWith(c, b), true);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/bytes
```

[See all symbols in @std/bytes on](https://jsr.io/@std/bytes/doc)
