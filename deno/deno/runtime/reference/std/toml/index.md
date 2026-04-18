---
title: "@std/toml"
source: "https://docs.deno.com/runtime/reference/std/toml/"
canonical_url: "https://docs.deno.com/runtime/reference/std/toml/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:25.811Z"
content_hash: "100db2d0e2c2ddab646a74cb42e10ef505527a9696dca63a1ef7d0106b487170"
menu_path: ["@std/toml"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/text/index.md", "title": "@std/text"}
nav_next: {"path": "deno/deno/runtime/reference/std/ulid/index.md", "title": "@std/ulid"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

[`parse`](https://jsr.io/@std/toml@1.0.11/doc/~/parse) and [`stringify`](https://jsr.io/@std/toml@1.0.11/doc/~/stringify) for handling [TOML](https://toml.io) encoded data.

Be sure to read the supported types as not every spec is supported at the moment and the handling in TypeScript side is a bit different.

## Supported types and handling

*   [Keys](https://toml.io/en/latest#keys)
*   [String](https://toml.io/en/latest#string)
*   [Multiline String](https://toml.io/en/latest#string)
*   [Literal String](https://toml.io/en/latest#string)
*   [Integer](https://toml.io/en/latest#integer)
*   [Float](https://toml.io/en/latest#float)
*   [Boolean](https://toml.io/en/latest#boolean)
*   [Offset Date-time](https://toml.io/en/latest#offset-date-time)
*   [Local Date-time](https://toml.io/en/latest#local-date-time)
*   [Local Date](https://toml.io/en/latest#local-date)
*   [Local Time](https://toml.io/en/latest#local-time)
*   [Table](https://toml.io/en/latest#table)
*   [Inline Table](https://toml.io/en/latest#inline-table)
*   [Array of Tables](https://toml.io/en/latest#array-of-tables)

_Supported with warnings see [Warning](#Warning)._

### Warning

#### String

Due to the spec, there is no flag to detect regex properly in a TOML declaration. So the regex is stored as string.

#### Integer

For **Binary** / **Octal** / **Hexadecimal** numbers, they are stored as string to be not interpreted as Decimal.

#### Local Time

Because local time does not exist in JavaScript, the local time is stored as a string.

#### Array of Tables

At the moment only simple declarations like below are supported:

```js
[[bin]]
name = "deno"
path = "cli/main.rs"

[[bin]]
name = "deno_core"
path = "src/foo.rs"

[[nib]]
name = "node"
path = "not_found"
```

will output:

```js
{
  "bin": [
    { "name": "deno", "path": "cli/main.rs" },
    { "name": "deno_core", "path": "src/foo.rs" }
  ],
  "nib": [{ "name": "node", "path": "not_found" }]
}
```

```js
import { parse, stringify } from "@std/toml";
import { assertEquals } from "@std/assert";

const obj = {
  bin: [
    { name: "deno", path: "cli/main.rs" },
    { name: "deno_core", path: "src/foo.rs" },
  ],
  nib: [{ name: "node", path: "not_found" }],
};

const tomlString = stringify(obj);
assertEquals(tomlString, `
[[bin]]
name = "deno"
path = "cli/main.rs"

[[bin]]
name = "deno_core"
path = "src/foo.rs"

[[nib]]
name = "node"
path = "not_found"
`);

const tomlObject = parse(tomlString);
assertEquals(tomlObject, obj);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/toml
```

[See all symbols in @std/toml on](https://jsr.io/@std/toml/doc)
