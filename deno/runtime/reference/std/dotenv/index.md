---
title: "@std/dotenv"
source: "https://docs.deno.com/runtime/reference/std/dotenv/"
canonical_url: "https://docs.deno.com/runtime/reference/std/dotenv/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:45.333Z"
content_hash: "f08fca352715d4d536e399e568a190cdb63f448500c20fe65e15f11e2f23de5f"
menu_path: ["@std/dotenv"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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
