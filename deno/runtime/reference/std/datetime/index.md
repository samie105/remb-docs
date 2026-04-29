---
title: "@std/datetime"
source: "https://docs.deno.com/runtime/reference/std/datetime/"
canonical_url: "https://docs.deno.com/runtime/reference/std/datetime/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:41:10.953Z"
content_hash: "3a5a6823a3b561e757dc0698ffb30b7783329de9e2d4ce73e8ea4572c1f6d1aa"
menu_path: ["@std/datetime"]
section_path: []
content_language: "en"
nav_prev: {"path": "../data-structures/index.md", "title": "@std/data-structures"}
nav_next: {"path": "../dotenv/index.md", "title": "@std/dotenv"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

Utilities for dealing with [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) objects.

```js
import { dayOfYear, isLeap, difference, HOUR, MINUTE, SECOND } from "@std/datetime";
import { assertEquals } from "@std/assert";

assertEquals(dayOfYear(new Date("2019-03-11T03:24:00")), 70);
assertEquals(isLeap(1970), false);

const date0 = new Date("2018-05-14");
const date1 = new Date("2020-05-13");
assertEquals(difference(date0, date1).years, 1);

assertEquals(HOUR / MINUTE, 60);
assertEquals(MINUTE / SECOND, 60);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/datetime
```

[See all symbols in @std/datetime on](https://jsr.io/@std/datetime/doc)
