---
title: "@std/fs"
source: "https://docs.deno.com/runtime/reference/std/fs/"
canonical_url: "https://docs.deno.com/runtime/reference/std/fs/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:42:46.699Z"
content_hash: "d132e2f135281d3fcfb2b6351dc71eda668d7c919b033cf5a569f431bcf6db4e"
menu_path: ["@std/fs"]
section_path: []
content_language: "en"
nav_prev: {"path": "../front-matter/index.md", "title": "@std/front-matter"}
nav_next: {"path": "../html/index.md", "title": "@std/html"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

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
