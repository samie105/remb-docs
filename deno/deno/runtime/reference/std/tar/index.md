---
title: "@std/tar"
source: "https://docs.deno.com/runtime/reference/std/tar/"
canonical_url: "https://docs.deno.com/runtime/reference/std/tar/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:53.386Z"
content_hash: "32bc50b37e3d13f477850b1a2bca5d175dddcdec39991a8dfc3390c87f5f725e"
menu_path: ["@std/tar"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/streams/index.md", "title": "@std/streams"}
nav_next: {"path": "deno/deno/runtime/reference/std/testing/index.md", "title": "@std/testing"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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

