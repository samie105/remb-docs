---
title: "@std/io"
source: "https://docs.deno.com/runtime/reference/std/io/"
canonical_url: "https://docs.deno.com/runtime/reference/std/io/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:28.455Z"
content_hash: "d5c303865920c1c7764695ca25212c6e6ea45076b195a85b7d5c0526c4740609"
menu_path: ["@std/io"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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
