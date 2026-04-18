---
title: "@std/html"
source: "https://docs.deno.com/runtime/reference/std/html/"
canonical_url: "https://docs.deno.com/runtime/reference/std/html/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:49.835Z"
content_hash: "0905c2c3a60bb3270c31817893e402a75e5666e85d084aee25daf42248aa5a39"
menu_path: ["@std/html"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/fs/index.md", "title": "@std/fs"}
nav_next: {"path": "deno/deno/runtime/reference/std/http/index.md", "title": "@std/http"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Functions for HTML tasks such as escaping or unescaping HTML entities.

```js
import { unescape } from "@std/html/entities";
import { assertEquals } from "@std/assert";

assertEquals(unescape("&lt;&gt;'&amp;AA"), "<>'&AA");
assertEquals(unescape("&thorn;&eth;"), "&thorn;&eth;");
```

### Add to your project

\>\_

```sh
deno add jsr:@std/html
```

[See all symbols in @std/html on](https://jsr.io/@std/html/doc)


