---
title: "@std/front-matter"
source: "https://docs.deno.com/runtime/reference/std/front-matter/"
canonical_url: "https://docs.deno.com/runtime/reference/std/front-matter/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:23.662Z"
content_hash: "86fa21a4ba5a7928e50f11d25959d2f425a0c5adeb826d6331911655db325d73"
menu_path: ["@std/front-matter"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/fmt/index.md", "title": "@std/fmt"}
nav_next: {"path": "deno/deno/runtime/reference/std/fs/index.md", "title": "@std/fs"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Extracts [front matter](https://daily-dev-tips.com/posts/what-exactly-is-frontmatter/) from strings. Adapted from [jxson/front-matter](https://github.com/jxson/front-matter/blob/36f139ef797bd9e5196a9ede03ef481d7fbca18e/index.js).

## Supported formats

### JSON

```js
import { test, extractJson } from "@std/front-matter";
import { assertEquals } from "@std/assert";

const str = "---json\n{\"and\": \"this\"}\n---\ndeno is awesome";

assertEquals(test(str), true);
assertEquals(extractJson(str), {
  frontMatter: "{\"and\": \"this\"}",
  body: "deno is awesome",
  attrs: { and: "this" }
});
```

[`extract`](https://jsr.io/@std/front-matter@1.0.9/doc/~/extractJson) and [`test`](https://jsr.io/@std/front-matter@1.0.9/doc/~/test) support the following delimiters.

```js
---json
{
  "and": "this"
}
---
```

```js
{
  "is": "JSON"
}
```

### TOML

```js
import { test, extractToml } from "@std/front-matter";
import { assertEquals } from "@std/assert";

const str = "---toml\nmodule = 'front_matter'\n---\ndeno is awesome";

assertEquals(test(str), true);
assertEquals(extractToml(str), {
  frontMatter: "module = 'front_matter'",
  body: "deno is awesome",
  attrs: { module: "front_matter" }
});
```

[`extract`](https://jsr.io/@std/front-matter@1.0.9/doc/~/extractToml) and [`test`](https://jsr.io/@std/front-matter@1.0.9/doc/~/test) support the following delimiters.

```js
---toml
this = 'is'
---
```

```js
= toml =
parsed = 'as'
toml = 'data'
= toml =
```

```js
+++
is = 'that'
not = 'cool?'
+++
```

### YAML

```js
import { test, extractYaml } from "@std/front-matter";
import { assertEquals } from "@std/assert";

const str = "---yaml\nmodule: front_matter\n---\ndeno is awesome";

assertEquals(test(str), true);
assertEquals(extractYaml(str), {
  frontMatter: "module: front_matter",
  body: "deno is awesome",
  attrs: { module: "front_matter" }
});
```

[`extract`](https://jsr.io/@std/front-matter@1.0.9/doc/~/extractYaml) and [`test`](https://jsr.io/@std/front-matter@1.0.9/doc/~/test) support the following delimiters.

```js
---
these: are
---
```

```js
---yaml
all: recognized
---
```

```js
= yaml =
as: yaml
= yaml =
```

### Add to your project

\>\_

```sh
deno add jsr:@std/front-matter
```

[See all symbols in @std/front-matter on](https://jsr.io/@std/front-matter/doc)

