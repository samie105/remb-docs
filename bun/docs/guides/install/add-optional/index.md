---
title: "Add an optional dependency"
source: "https://bun.com/docs/guides/install/add-optional"
canonical_url: "https://bun.com/docs/guides/install/add-optional"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:23.228Z"
content_hash: "f0e8597ff099360598b45b004c860a554954b1d43aea9b51503a5e0162439912"
menu_path: ["Add an optional dependency"]
section_path: []
nav_prev: {"path": "../add-git/index.md", "title": "Add a Git dependency"}
nav_next: {"path": "../add-peer/index.md", "title": "Add a peer dependency"}
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

To add an npm package as an optional dependency, use the `--optional` flag.

terminal

```
bun add zod --optional
```

* * *

This will add the package to `optionalDependencies` in `package.json`.

package.json

```
{
  "optionalDependencies": {
    "zod": "^3.0.0"
  }
}
```

* * *

See [Docs > Package manager](/docs/pm/cli/install) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/add-optional.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/add-optional>)

[

Add a development dependency

Previous

](/docs/guides/install/add-dev)[

Add a peer dependency

Next

](/docs/guides/install/add-peer)
