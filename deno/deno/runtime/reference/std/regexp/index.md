---
title: "@std/regexp"
source: "https://docs.deno.com/runtime/reference/std/regexp/"
canonical_url: "https://docs.deno.com/runtime/reference/std/regexp/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:21.134Z"
content_hash: "de9af1c0396071ad2873e3415a788c21375cc4e5d1650043d023095c99673f6a"
menu_path: ["@std/regexp"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/random/index.md", "title": "@std/random"}
nav_next: {"path": "deno/deno/runtime/reference/std/semver/index.md", "title": "@std/semver"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Functions for tasks related to [regular expression](https://en.wikipedia.org/wiki/Regular_expression) (regexp), such as escaping text for interpolation into a regexp.

```js
import { escape } from "@std/regexp/escape";
import { assertEquals, assertMatch, assertNotMatch } from "@std/assert";

const re = new RegExp(`^${escape(".")}$`, "u");

assertEquals("^\\.$", re.source);
assertMatch(".", re);
assertNotMatch("a", re);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/regexp
```

[See all symbols in @std/regexp on](https://jsr.io/@std/regexp/doc)

