---
title: "@std/text"
source: "https://docs.deno.com/runtime/reference/std/text/"
canonical_url: "https://docs.deno.com/runtime/reference/std/text/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:48:06.304Z"
content_hash: "cd78bedd2dc740989a68323944d9753e01e6a7d6657d1cf633756fc806e39a6a"
menu_path: ["@std/text"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/testing/index.md", "title": "@std/testing"}
nav_next: {"path": "deno/runtime/reference/std/toml/index.md", "title": "@std/toml"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Utility functions for working with text.

```js
import { toCamelCase, compareSimilarity } from "@std/text";
import { assertEquals } from "@std/assert";

assertEquals(toCamelCase("snake_case"), "snakeCase");

const words = ["hi", "help", "hello"];

// Words most similar to "hep" will be at the front
assertEquals(words.sort(compareSimilarity("hep")), ["help", "hi", "hello"]);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/text
```

[See all symbols in @std/text on](https://jsr.io/@std/text/doc)
