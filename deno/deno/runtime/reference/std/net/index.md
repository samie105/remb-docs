---
title: "@std/net"
source: "https://docs.deno.com/runtime/reference/std/net/"
canonical_url: "https://docs.deno.com/runtime/reference/std/net/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:04:49.142Z"
content_hash: "bf984db02f0996bc69f2d0bd3ad9aefae8d994196d3d044cf0d7737ae473c28d"
menu_path: ["@std/net"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/msgpack/index.md", "title": "@std/msgpack"}
nav_next: {"path": "deno/deno/runtime/reference/std/path/index.md", "title": "@std/path"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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
