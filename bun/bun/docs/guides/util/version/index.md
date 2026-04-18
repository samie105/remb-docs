---
title: "Get the current Bun version"
source: "https://bun.com/docs/guides/util/version"
canonical_url: "https://bun.com/docs/guides/util/version"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:22.851Z"
content_hash: "ab814117065ef48b469c3fe2275b5daf0677f300c389a3ba4d70b7b03db61ea6"
menu_path: ["Get the current Bun version"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/util/which-path-to-executable-bin/index.md", "title": "Get the path to an executable bin file"}
nav_next: {"path": "bun/bun/docs/guides/websocket/compression/index.md", "title": "Enable compression for WebSocket messages"}
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

Get the current version of Bun in a semver format.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
Bun.version; // => "1.3.3"
```

* * *

Get the exact `git` commit of [`oven-sh/bun`](https://github.com/oven-sh/bun) that was compiled to produce this Bun binary.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
Bun.revision; // => "49231b2cb9aa48497ab966fc0bb6b742dacc4994"
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/version.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/version>)

[

Detect when code is executed with Bun

Previous

](/docs/guides/util/detect-bun)[

Hash a password

Next

](/docs/guides/util/hash-a-password)
