---
title: "@std/io"
source: "https://docs.deno.com/runtime/reference/std/io/"
canonical_url: "https://docs.deno.com/runtime/reference/std/io/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:44:10.341Z"
content_hash: "5b6c2caa07a3f827cc84d16395c0ef2c7fbebad64f9f72bb1af87b24ac1681d6"
menu_path: ["@std/io"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/internal/index.md", "title": "@std/internal"}
nav_next: {"path": "deno/runtime/reference/std/json/index.md", "title": "@std/json"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

Utilities for working with Deno's readers, writers, and web streams.

`Reader` and `Writer` interfaces are deprecated in Deno, and so many of these utilities are also deprecated. Consider using web streams instead.

```js
import { toReadableStream, toWritableStream } from "@std/io";

await toReadableStream(Deno.stdin)
  .pipeTo(toWritableStream(Deno.stdout));
```

### Add to your project

\>\_

```sh
deno add jsr:@std/io
```

[See all symbols in @std/io on](https://jsr.io/@std/io/doc)
