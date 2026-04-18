---
title: "@std/media-types"
source: "https://docs.deno.com/runtime/reference/std/media-types/"
canonical_url: "https://docs.deno.com/runtime/reference/std/media-types/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:04:26.353Z"
content_hash: "30fafc5ab99bd1f84778d11758d52bd752c60308555cc855b468283758f3e831"
menu_path: ["@std/media-types"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/log/index.md", "title": "@std/log"}
nav_next: {"path": "deno/deno/runtime/reference/std/msgpack/index.md", "title": "@std/msgpack"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Utility functions for media types (MIME types).

This API is inspired by the GoLang [`mime`](https://pkg.go.dev/mime) package and [jshttp/mime-types](https://github.com/jshttp/mime-types), and is designed to integrate and improve the APIs from [x/media\_types](https://deno.land/x/media_types).

The `vendor` folder contains copy of the [jshttp/mime-db](https://github.com/jshttp/mime-types) `db.json` file, along with its license.

```js
import { contentType, allExtensions, getCharset } from "@std/media-types";
import { assertEquals } from "@std/assert";

assertEquals(allExtensions("application/json"), ["json", "map"]);

assertEquals(contentType(".json"), "application/json; charset=UTF-8");

assertEquals(getCharset("text/plain"), "UTF-8");
```

### Add to your project

\>\_

```sh
deno add jsr:@std/media-types
```

[See all symbols in @std/media-types on](https://jsr.io/@std/media-types/doc)


