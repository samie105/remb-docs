---
title: "Detect when code is executed with Bun"
source: "https://bun.com/docs/guides/util/detect-bun"
canonical_url: "https://bun.com/docs/guides/util/detect-bun"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:46.650Z"
content_hash: "2b636f50b1bf9e93649e15d3cc8f753846ba46dfd656c1ccf7779432b50c411e"
menu_path: ["Detect when code is executed with Bun"]
section_path: []
nav_prev: {"path": "../deflate/index.md", "title": "Compress and decompress data with DEFLATE"}
nav_next: {"path": "../entrypoint/index.md", "title": "Check if the current file is the entrypoint"}
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

The recommended way to detect when code is being executed with Bun is to check `process.versions.bun`. This works in both JavaScript and TypeScript without requiring any additional type definitions.

```
if (process.versions.bun) {
  // this code will only run when the file is run with Bun
}
```

* * *

Alternatively, you can check for the existence of the `Bun` global. This is similar to how you’d check for the existence of the `window` variable to detect when code is being executed in a browser.

This approach will result in a type error in TypeScript unless `@types/bun` is installed. You can install it with `bun add -d @types/bun`.

```
if (typeof Bun !== "undefined") {
  // this code will only run when the file is run with Bun
}
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/detect-bun.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/detect-bun>)

[

Upgrade Bun to the latest version

Previous

](/docs/guides/util/upgrade)[

Get the current Bun version

Next

](/docs/guides/util/version)
