---
title: "@std/collections"
source: "https://docs.deno.com/runtime/reference/std/collections/"
canonical_url: "https://docs.deno.com/runtime/reference/std/collections/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:44.788Z"
content_hash: "661f8cc05992c9e280325d545af88f7f8e6ba68fbef2e37323a6d78e59dfbf85"
menu_path: ["@std/collections"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Pure functions for common tasks around collection types like arrays and objects.

Inspired by [Kotlin's Collections](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/) package and [Lodash](https://lodash.com/).

```js
import { intersect, sample, pick } from "@std/collections";
import { assertEquals, assertArrayIncludes } from "@std/assert";

const lisaInterests = ["Cooking", "Music", "Hiking"];
const kimInterests = ["Music", "Tennis", "Cooking"];

assertEquals(intersect(lisaInterests, kimInterests), ["Cooking", "Music"]);

assertArrayIncludes(lisaInterests, [sample(lisaInterests)]);

const cat = { name: "Lulu", age: 3, breed: "Ragdoll" };

assertEquals(pick(cat, ["name", "breed"]), { name: "Lulu", breed: "Ragdoll"});
```

### Add to your project

\>\_

```sh
deno add jsr:@std/collections
```

[See all symbols in @std/collections on](https://jsr.io/@std/collections/doc)
