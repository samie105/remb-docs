---
title: "@std/fs"
source: "https://docs.deno.com/runtime/reference/std/fs/"
canonical_url: "https://docs.deno.com/runtime/reference/std/fs/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:40.330Z"
content_hash: "94893e7a1dbff5db2a224b1df266078fd553c6a3f07bcd9c42764ff0c64bd266"
menu_path: ["@std/fs"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/front-matter/index.md", "title": "@std/front-matter"}
nav_next: {"path": "deno/deno/runtime/reference/std/html/index.md", "title": "@std/html"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Helpers for working with the filesystem.

```js
import { ensureFile, copy, ensureDir, move } from "@std/fs";

await ensureFile("example.txt");

await copy("example.txt", "example_copy.txt");

await ensureDir("subdir");

await move("example_copy.txt", "subdir/example_copy.txt");
```

### Add to your project

\>\_

```sh
deno add jsr:@std/fs
```

[See all symbols in @std/fs on](https://jsr.io/@std/fs/doc)

