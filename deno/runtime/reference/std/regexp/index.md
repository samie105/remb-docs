---
title: "@std/regexp"
source: "https://docs.deno.com/runtime/reference/std/regexp/"
canonical_url: "https://docs.deno.com/runtime/reference/std/regexp/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:46:49.961Z"
content_hash: "f641e493a0b992ce331ee8748beae992275b70c8109acc63a6adcf070dfae41a"
menu_path: ["@std/regexp"]
section_path: []
content_language: "en"
---
**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

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
