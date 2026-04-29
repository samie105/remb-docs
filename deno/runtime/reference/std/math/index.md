---
title: "@std/math"
source: "https://docs.deno.com/runtime/reference/std/math/"
canonical_url: "https://docs.deno.com/runtime/reference/std/math/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:45:13.814Z"
content_hash: "dfb70dc9cc5eee76fa5d45a67eaebd8de1d93f93308139720820993828dd832e"
menu_path: ["@std/math"]
section_path: []
content_language: "en"
nav_prev: {"path": "../../node_apis/index.md", "title": "Node APIs"}
nav_next: {"path": "../xml/index.md", "title": "@std/xml"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Math functions such as modulo and clamp.

```js
import { clamp, modulo } from "@std/math";
import { assertEquals } from "@std/assert";

for (let n = -3; n <= 3; ++n) {
 const val = n * 12 + 5;
 // 5 o'clock is always 5 o'clock, no matter how many twelve-hour cycles you add or remove
 assertEquals(modulo(val, 12), 5);
 assertEquals(clamp(val, 0, 11), n === 0 ? 5 : n > 0 ? 11 : 0);
}
```

### Add to your project

\>\_

```sh
deno add jsr:@std/math
```

[See all symbols in @std/math on](https://jsr.io/@std/math/doc)
