---
title: "@std/dotenv"
source: "https://docs.deno.com/runtime/reference/std/dotenv/"
canonical_url: "https://docs.deno.com/runtime/reference/std/dotenv/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:41:30.286Z"
content_hash: "796f26c861aaf321e558b5180d5f19953c2c2e22e540e6360fd9bf722f8229ec"
menu_path: ["@std/dotenv"]
section_path: []
content_language: "en"
nav_prev: {"path": "../datetime/index.md", "title": "@std/datetime"}
nav_next: {"path": "../encoding/index.md", "title": "@std/encoding"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

Parses and loads environment variables from a `.env` file into the current process, or stringify data into a `.env` file format.

Note: The key needs to match the pattern /^\[a-zA-Z\_\]\[a-zA-Z0-9\_\]\*$/.

```js
// Automatically load environment variables from a `.env` file
import "@std/dotenv/load";
```

```js
import { parse, stringify } from "@std/dotenv";
import { assertEquals } from "@std/assert";

assertEquals(parse("GREETING=hello world"), { GREETING: "hello world" });
assertEquals(stringify({ GREETING: "hello world" }), "GREETING='hello world'");
```

### Add to your project

\>\_

```sh
deno add jsr:@std/dotenv
```

[See all symbols in @std/dotenv on](https://jsr.io/@std/dotenv/doc)
