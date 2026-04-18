---
title: "@std/datetime"
source: "https://docs.deno.com/runtime/reference/std/datetime/"
canonical_url: "https://docs.deno.com/runtime/reference/std/datetime/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:35.546Z"
content_hash: "11a7f377ab034310d7046d2fed3d9182f70317b6311fafc4e85f6c0a36b7a668"
menu_path: ["@std/datetime"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/data-structures/index.md", "title": "@std/data-structures"}
nav_next: {"path": "deno/deno/runtime/reference/std/dotenv/index.md", "title": "@std/dotenv"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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


