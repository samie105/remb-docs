---
title: "@std/random"
source: "https://docs.deno.com/runtime/reference/std/random/"
canonical_url: "https://docs.deno.com/runtime/reference/std/random/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:46:29.809Z"
content_hash: "fe0b39f985c3b53a4ca60d76b0867624a43cc31a2fa372cfcc0473f43cfdc7ab"
menu_path: ["@std/random"]
section_path: []
content_language: "en"
nav_prev: {"path": "../path/index.md", "title": "@std/path"}
nav_next: {"path": "../regexp/index.md", "title": "@std/regexp"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

Utilities for generating random numbers.

Example of generating a random integer with fixed seed number:

```js
import { randomIntegerBetween } from "@std/random";
import { randomSeeded } from "@std/random";
import { assertEquals } from "@std/assert";

const prng = randomSeeded(1n);

assertEquals(randomIntegerBetween(1, 10, { prng }), 3);
```

Example of generating a random integer between two values:

```js
import { randomIntegerBetween } from "@std/random";
import { randomSeeded } from "@std/random";

const prng = randomSeeded(BigInt(crypto.getRandomValues(new Uint32Array(1))[0]!));

const randomInteger = randomIntegerBetween(1, 10, { prng });
```

### Add to your project

\>\_

```sh
deno add jsr:@std/random
```

[See all symbols in @std/random on](https://jsr.io/@std/random/doc)
