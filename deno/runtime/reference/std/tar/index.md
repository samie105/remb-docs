---
title: "@std/tar"
source: "https://docs.deno.com/runtime/reference/std/tar/"
canonical_url: "https://docs.deno.com/runtime/reference/std/tar/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:47:34.530Z"
content_hash: "49c7c4a9ee3c8f41e8c65fe81ad9e8b11a8b73efcd8f6df5c5fa786cb3590bf8"
menu_path: ["@std/tar"]
section_path: []
content_language: "en"
nav_prev: {"path": "../streams/index.md", "title": "@std/streams"}
nav_next: {"path": "../testing/index.md", "title": "@std/testing"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

Streaming utilities for working with tar archives.

Files are not compressed, only collected into the archive.

```js
import { UntarStream } from "@std/tar/untar-stream";
import { dirname, normalize } from "@std/path";

for await (
  const entry of (await Deno.open("./out.tar.gz"))
    .readable
    .pipeThrough(new DecompressionStream("gzip"))
    .pipeThrough(new UntarStream())
) {
  const path = normalize(entry.path);
  await Deno.mkdir(dirname(path), { recursive: true });
  await entry.readable?.pipeTo((await Deno.create(path)).writable);
}
```

### Add to your project

\>\_

```sh
deno add jsr:@std/tar
```

[See all symbols in @std/tar on](https://jsr.io/@std/tar/doc)
