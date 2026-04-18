---
title: "@std/crypto"
source: "https://docs.deno.com/runtime/reference/std/crypto/"
canonical_url: "https://docs.deno.com/runtime/reference/std/crypto/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:02.592Z"
content_hash: "211b8b1d10e842d338cedb30c4623fa72d78234878803c86a1e9dce739441560"
menu_path: ["@std/crypto"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/collections/index.md", "title": "@std/collections"}
nav_next: {"path": "deno/deno/runtime/reference/std/csv/index.md", "title": "@std/csv"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Extensions to the [Web Crypto](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) supporting additional encryption APIs, but also delegating to the built-in APIs when possible.

```js
import { crypto } from "@std/crypto/crypto";

const message = "Hello, Deno!";
const encoder = new TextEncoder();
const data = encoder.encode(message);

await crypto.subtle.digest("BLAKE3", data);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/crypto
```

[See all symbols in @std/crypto on](https://jsr.io/@std/crypto/doc)

