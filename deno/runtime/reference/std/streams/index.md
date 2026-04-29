---
title: "@std/streams"
source: "https://docs.deno.com/runtime/reference/std/streams/"
canonical_url: "https://docs.deno.com/runtime/reference/std/streams/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:47:21.776Z"
content_hash: "599bfddf352ff3515ebc7f50e54889ec05b259fcf79c97b43bb45ff76bdf9aae"
menu_path: ["@std/streams"]
section_path: []
content_language: "en"
nav_prev: {"path": "../semver/index.md", "title": "@std/semver"}
nav_next: {"path": "../tar/index.md", "title": "@std/tar"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

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
