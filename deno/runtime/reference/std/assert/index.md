---
title: "Standard Assertions (@std/assert)"
source: "https://docs.deno.com/runtime/reference/std/assert/"
canonical_url: "https://docs.deno.com/runtime/reference/std/assert/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:38:31.246Z"
content_hash: "043438b063c6ae2731d89352be39e874b2e9c41e231aa1fa995b4de95ba90e84"
menu_path: ["Standard Assertions (@std/assert)"]
section_path: []
content_language: "en"
nav_prev: {"path": "../index.md", "title": "Deno Standard Library (@std)"}
nav_next: {"path": "../async/index.md", "title": "@std/async"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

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
