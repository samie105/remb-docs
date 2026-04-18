---
title: "Standard Assertions (@std/assert)"
source: "https://docs.deno.com/runtime/reference/std/assert/"
canonical_url: "https://docs.deno.com/runtime/reference/std/assert/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:39.073Z"
content_hash: "d8f44ae68d773bacd895884ac6720c1ac65972c5b874a8a91c2258cbcb7aa7c0"
menu_path: ["Standard Assertions (@std/assert)"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/index.md", "title": "Deno Standard Library (@std)"}
nav_next: {"path": "deno/deno/runtime/reference/std/async/index.md", "title": "@std/async"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

A library of assertion functions. If the assertion is false an `AssertionError` will be thrown which will result in pretty-printed diff of the failing assertion.

This module is browser compatible, but do not rely on good formatting of values for AssertionError messages in browsers.

```js
import { assert } from "@std/assert";

assert("I am truthy"); // Doesn't throw
assert(false); // Throws `AssertionError`
```

### Add to your project

\>\_

```sh
deno add jsr:@std/assert
```

[See all symbols in @std/assert on](https://jsr.io/@std/assert/doc)

