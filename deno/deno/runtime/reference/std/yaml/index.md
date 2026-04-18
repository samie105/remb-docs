---
title: "@std/yaml"
source: "https://docs.deno.com/runtime/reference/std/yaml/"
canonical_url: "https://docs.deno.com/runtime/reference/std/yaml/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:07:14.227Z"
content_hash: "2521ae487c45506361fe7f01317a5546a2c46b48cfd9b64edcce84363035d16a"
menu_path: ["@std/yaml"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/webgpu/index.md", "title": "@std/webgpu"}
nav_next: {"path": "deno/deno/runtime/reference/ts_config_migration/index.md", "title": "Configuring TypeScript"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

[`parse`](https://jsr.io/@std/yaml@1.0.12/doc/~/parse) and [`stringify`](https://jsr.io/@std/yaml@1.0.12/doc/~/stringify) for handling [YAML](https://yaml.org/) encoded data.

Ported from [js-yaml v3.13.1](https://github.com/nodeca/js-yaml/commit/665aadda42349dcae869f12040d9b10ef18d12da).

Use [`parseAll`](https://jsr.io/@std/yaml@1.0.12/doc/~/parseAll) for parsing multiple documents in a single YAML string.

This package generally supports [YAML 1.2.x](https://yaml.org/spec/1.2.2/) (latest) and some [YAML 1.1](https://yaml.org/spec/1.1/current.html) features that are commonly used in the wild.

Supported YAML 1.1 features include:

*   [Merge](https://yaml.org/type/merge.html) type (`<<` symbol)

Unsupported YAML 1.1 features include:

*   Yes, No, On, Off literals for bool type
*   Sexagesimal numbers (e.g. `3:25:45`)

```js
import { parse, stringify } from "@std/yaml";
import { assertEquals } from "@std/assert";

const data = parse(`
foo: bar
baz:
  - qux
  - quux
`);
assertEquals(data, { foo: "bar", baz: [ "qux", "quux" ] });

const yaml = stringify({ foo: "bar", baz: ["qux", "quux"] });
assertEquals(yaml, `foo: bar
baz:
  - qux
  - quux
`);
```

## Limitations

*   `binary` type is currently not stable.

### Add to your project

\>\_

```sh
deno add jsr:@std/yaml
```

[See all symbols in @std/yaml on](https://jsr.io/@std/yaml/doc)
