---
title: "@std/cache"
source: "https://docs.deno.com/runtime/reference/std/cache/"
canonical_url: "https://docs.deno.com/runtime/reference/std/cache/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:39:23.144Z"
content_hash: "b56ff2e5b12cb250e3ef84af8e8721440a3f46bed1fb31ba6559b360ee2c8109"
menu_path: ["@std/cache"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/bytes/index.md", "title": "@std/bytes"}
nav_next: {"path": "deno/runtime/reference/std/cbor/index.md", "title": "@std/cbor"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

In-memory cache utilities, such as memoization and caches with different expiration policies.

```js
import { memoize, LruCache, type MemoizationCacheResult } from "@std/cache";
import { assertEquals } from "@std/assert";

const cache = new LruCache<string, MemoizationCacheResult<bigint>>(1000);

// fibonacci function, which is very slow for n > ~30 if not memoized
const fib = memoize((n: bigint): bigint => {
  return n <= 2n ? 1n : fib(n - 1n) + fib(n - 2n);
}, { cache });

assertEquals(fib(100n), 354224848179261915075n);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/cache
```

[See all symbols in @std/cache on](https://jsr.io/@std/cache/doc)
