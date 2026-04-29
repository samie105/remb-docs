---
title: "Re-map import paths"
source: "https://bun.com/docs/guides/runtime/tsconfig-paths"
canonical_url: "https://bun.com/docs/guides/runtime/tsconfig-paths"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:23.112Z"
content_hash: "5dd8e1e73445c5e037fe442233c69aee1e0b9dec0d65d61f3a6ed1a96303c789"
menu_path: ["Re-map import paths"]
section_path: []
nav_prev: {"path": "bun/docs/guides/runtime/timezone/index.md", "title": "Set a time zone in Bun"}
nav_next: {"path": "bun/docs/guides/runtime/typescript/index.md", "title": "Install TypeScript declarations for Bun"}
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

Bun reads the `paths` field in your `tsconfig.json` to re-write import paths. This is useful for aliasing package names or avoiding long relative paths.

tsconfig.json

```
{
  "compilerOptions": {
    "paths": {
      "my-custom-name": ["zod"],
      "@components/*": ["./src/components/*"]
    }
  }
}
```

* * *

With the above `tsconfig.json`, the following imports will be re-written:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)tsconfig.ts

```
import { z } from "my-custom-name"; // imports from "zod"
import { Button } from "@components/Button"; // imports from "./src/components/Button"
```

* * *

See [Docs > Runtime > TypeScript](/docs/runtime/typescript) for more information on using TypeScript with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/tsconfig-paths.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/tsconfig-paths>)

[

Install TypeScript declarations for Bun

Previous

](../typescript/index.md)[

Debugging Bun with the VS Code extension

Next

](../vscode-debugger/index.md)
