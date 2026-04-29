---
title: "Import a TOML file"
source: "https://bun.com/docs/guides/runtime/import-toml"
canonical_url: "https://bun.com/docs/guides/runtime/import-toml"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:57.582Z"
content_hash: "59660b53407b3dd8c07e00f192bf84cec55c4b5b6535ec5b5dfccc6f221b5ec5"
menu_path: ["Import a TOML file"]
section_path: []
nav_prev: {"path": "bun/docs/guides/runtime/import-json5/index.md", "title": "Import a JSON5 file"}
nav_next: {"path": "bun/docs/guides/runtime/import-yaml/index.md", "title": "Import a YAML file"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](../../../index.md)[Package Manager

](../../../pm/cli/install/index.md)[Bundler

](../../../bundler/index.md)[Test Runner

](../../../test/index.md)[Guides

](../../index.md)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](../../../feedback/index.md)

Bun natively supports importing `.toml` files.

data.toml

```
name = "bun"
version = "1.0.0"

[author]
name = "John Dough"
email = "john@dough.com"
```

* * *

Import the file like any other source file.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)data.ts

```
import data from "./data.toml";

data.name; // => "bun"
data.version; // => "1.0.0"
data.author.name; // => "John Dough"
```

* * *

See [Docs > Runtime > TypeScript](/docs/runtime/typescript) for more information on using TypeScript with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/import-toml.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/import-toml>)

[

Import a JSON file

Previous

](../import-json/index.md)[

Import a YAML file

Next

](../import-yaml/index.md)
