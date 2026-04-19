---
title: "@std/fmt"
source: "https://docs.deno.com/runtime/reference/std/fmt/"
canonical_url: "https://docs.deno.com/runtime/reference/std/fmt/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:17.788Z"
content_hash: "7a6316709cdca05fd6ed9ca53eeeeeb8a06d6cc9a073a5f0f83fcfb5b317277a"
menu_path: ["@std/fmt"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Provides utilities for formatting text of different types:

*   [Human-readable bytes](https://jsr.io/@std/fmt/doc/bytes/~)
*   [Styles for the CLI](https://jsr.io/@std/fmt/doc/colors/~)
*   [Time duration](https://jsr.io/@std/fmt/doc/duration/~)
*   [Printing formatted strings to stdout](https://jsr.io/@std/fmt/doc/printf/~)

```js
import { format } from "@std/fmt/bytes";
import { red } from "@std/fmt/colors";

console.log(red(format(1337))); // Prints "1.34 kB"
```

# Runtime compatibility

[bytes](https://jsr.io/@std/fmt/doc/bytes/~), [colors](https://jsr.io/@std/fmt/doc/colors/~), and [duration](https://jsr.io/@std/fmt/doc/duration/~) supports all major runtimes. [printf](https://jsr.io/@std/fmt/doc/printf/~) is mostly compatible with major runtimes, however some of features, such as `%v`, `%i` and `%I` format specifiers, are only available in Deno. See the API docs for details.

### Add to your project

\>\_

```sh
deno add jsr:@std/fmt
```

[See all symbols in @std/fmt on](https://jsr.io/@std/fmt/doc)
