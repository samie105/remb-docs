---
title: "@std/bytes"
source: "https://docs.deno.com/runtime/reference/std/bytes/"
canonical_url: "https://docs.deno.com/runtime/reference/std/bytes/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:07.115Z"
content_hash: "fddf1addda49619202f9e2846b80c06624f2eb7467baa0608766627e9ba871ea"
menu_path: ["@std/bytes"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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
