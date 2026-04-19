---
title: "@std/math"
source: "https://docs.deno.com/runtime/reference/std/math/"
canonical_url: "https://docs.deno.com/runtime/reference/std/math/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:04:17.070Z"
content_hash: "b6647ee722b2fef94eed73a2cb42f6bc2a55b0b947c55e7d67397da652a87084"
menu_path: ["@std/math"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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
