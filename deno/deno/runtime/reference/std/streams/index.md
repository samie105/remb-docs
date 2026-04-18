---
title: "@std/streams"
source: "https://docs.deno.com/runtime/reference/std/streams/"
canonical_url: "https://docs.deno.com/runtime/reference/std/streams/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:37.418Z"
content_hash: "cfcf58023fa0ae301ea61c7c97188f083a677e2b315824be75461e9de050a7dd"
menu_path: ["@std/streams"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/semver/index.md", "title": "@std/semver"}
nav_next: {"path": "deno/deno/runtime/reference/std/tar/index.md", "title": "@std/tar"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Utilities for working with the [Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API).

Includes buffering and conversion.

```js
import { toText } from "@std/streams";
import { assertEquals } from "@std/assert";

const stream = ReadableStream.from(["Hello, world!"]);
const text = await toText(stream);

assertEquals(text, "Hello, world!");
```

### Add to your project

\>\_

```sh
deno add jsr:@std/streams
```

[See all symbols in @std/streams on](https://jsr.io/@std/streams/doc)


