---
title: "@std/net"
source: "https://docs.deno.com/runtime/reference/std/net/"
canonical_url: "https://docs.deno.com/runtime/reference/std/net/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:45:57.941Z"
content_hash: "81997969c36db69a0a363eef524e29ebee38256a61a561d4b529f36e0bdb3bf5"
menu_path: ["@std/net"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/msgpack/index.md", "title": "@std/msgpack"}
nav_next: {"path": "deno/runtime/reference/std/path/index.md", "title": "@std/path"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Network utilities.

```js
import { getAvailablePort } from "@std/net";

const command = new Deno.Command(Deno.execPath(), {
 args: ["test.ts", "--port", getAvailablePort().toString()],
});

// ...
```

### Add to your project

\>\_

```sh
deno add jsr:@std/net
```

[See all symbols in @std/net on](https://jsr.io/@std/net/doc)
