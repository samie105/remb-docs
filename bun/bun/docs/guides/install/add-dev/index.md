---
title: "Add a development dependency"
source: "https://bun.com/docs/guides/install/add-dev"
canonical_url: "https://bun.com/docs/guides/install/add-dev"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:08.755Z"
content_hash: "6804b2f762080373a16c0a74a94b931152c2f07c4310d6c1460828590b11549d"
menu_path: ["Add a development dependency"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/index.md", "title": "Guides"}
nav_next: {"path": "bun/bun/docs/guides/install/add-git/index.md", "title": "Add a Git dependency"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

To add an npm package as a development dependency, use `bun add --development`.

terminal

```
bun add zod --dev
bun add zod -d # shorthand
```

* * *

This will add the package to `devDependencies` in `package.json`.

```
{
  "devDependencies": {
    "zod": "^3.0.0"
  }
}
```

* * *

See [Docs > Package manager](/docs/pm/cli/install) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/add-dev.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/add-dev>)

[

Add a dependency

Previous

](/docs/guides/install/add)[

Add an optional dependency

Next

](/docs/guides/install/add-optional)

