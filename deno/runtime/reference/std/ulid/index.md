---
title: "@std/ulid"
source: "https://docs.deno.com/runtime/reference/std/ulid/"
canonical_url: "https://docs.deno.com/runtime/reference/std/ulid/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:36.478Z"
content_hash: "b9ca96c1e8459e81e58e4013c1fef0b6f6f40021af9ccec324206bff7a7cd247"
menu_path: ["@std/ulid"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Utilities for generating and working with [Universally Unique Lexicographically Sortable Identifiers (ULIDs)](https://github.com/ulid/spec).

To generate a ULID use the [`ulid`](https://jsr.io/@std/ulid@1.0.0/doc/~/ulid) function. This will generate a ULID based on the current time.

```js
import { ulid } from "@std/ulid";

ulid(); // 01HYFKMDF3HVJ4J3JZW8KXPVTY
```

[`ulid`](https://jsr.io/@std/ulid@1.0.0/doc/~/ulid) does not guarantee that the ULIDs will be strictly increasing for the same current time. If you need to guarantee that the ULIDs will be strictly increasing, even for the same current time, use the [`monotonicUlid`](https://jsr.io/@std/ulid@1.0.0/doc/~/monotonicUlid) function.

```js
import { monotonicUlid } from "@std/ulid";

monotonicUlid(); // 01HYFKHG5F8RHM2PM3D7NSTDAS
monotonicUlid(); // 01HYFKHG5F8RHM2PM3D7NSTDAT
```

Because each ULID encodes the time it was generated, you can extract the timestamp from a ULID using the [`decodeTime`](https://jsr.io/@std/ulid@1.0.0/doc/~/decodeTime) function.

```js
import { decodeTime, ulid } from "@std/ulid";
import { assertEquals } from "@std/assert";

const timestamp = 150_000;
const ulidString = ulid(timestamp);

assertEquals(decodeTime(ulidString), timestamp);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/ulid
```

[See all symbols in @std/ulid on](https://jsr.io/@std/ulid/doc)
