---
title: "@std/html"
source: "https://docs.deno.com/runtime/reference/std/html/"
canonical_url: "https://docs.deno.com/runtime/reference/std/html/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:43:06.262Z"
content_hash: "6d58ec1f58e76500a0942085617d3ed3307d910349a1499c3d1e25a1aaf3649b"
menu_path: ["@std/html"]
section_path: []
content_language: "en"
nav_prev: {"path": "../fs/index.md", "title": "@std/fs"}
nav_next: {"path": "../http/index.md", "title": "@std/http"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

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
