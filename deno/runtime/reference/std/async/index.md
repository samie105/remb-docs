---
title: "@std/async"
source: "https://docs.deno.com/runtime/reference/std/async/"
canonical_url: "https://docs.deno.com/runtime/reference/std/async/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:38:51.307Z"
content_hash: "8d781078ae1e365aca22e87f69597d1ebddfcf7d2c1a740baf0b68b9d3608966"
menu_path: ["@std/async"]
section_path: []
content_language: "en"
nav_prev: {"path": "../assert/index.md", "title": "Standard Assertions (@std/assert)"}
nav_next: {"path": "../bytes/index.md", "title": "@std/bytes"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Provide helpers with asynchronous tasks, like [`delay`](https://jsr.io/@std/async@1.3.0/doc/~/delay), [`debounce`](https://jsr.io/@std/async@1.3.0/doc/~/debounce), [`retry`](https://jsr.io/@std/async@1.3.0/doc/~/retry), or [`pooledMap`](https://jsr.io/@std/async@1.3.0/doc/~/pooledMap).

```js
import { delay } from "@std/async/delay";

await delay(100); // waits for 100 milliseconds
```

### Add to your project

\>\_

```sh
deno add jsr:@std/async
```

[See all symbols in @std/async on](https://jsr.io/@std/async/doc)
