---
title: "Sleep for a fixed number of milliseconds"
source: "https://bun.com/docs/guides/util/sleep"
canonical_url: "https://bun.com/docs/guides/util/sleep"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:16.087Z"
content_hash: "6c16536d0deff09ab3ff66df7e02374f09aab801a573428c0151502ffed76d94"
menu_path: ["Sleep for a fixed number of milliseconds"]
section_path: []
nav_prev: {"path": "bun/docs/guides/util/path-to-file-url/index.md", "title": "Convert an absolute path to a file URL"}
nav_next: {"path": "bun/docs/guides/util/upgrade/index.md", "title": "Upgrade Bun to the latest version"}
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

The `Bun.sleep` method provides a convenient way to create a void `Promise` that resolves in a fixed number of milliseconds.

```
// sleep for 1 second
await Bun.sleep(1000);
```

* * *

Internally, this is equivalent to the following snippet that uses [`setTimeout`](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout).

```
await new Promise(resolve => setTimeout(resolve, ms));
```

* * *

See [Docs > API > Utils](../../../runtime/utils/index.md) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/sleep.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/sleep>)

[

Check if two objects are deeply equal

Previous

](../deep-equals/index.md)[

Convert a file URL to an absolute path

Next

](../file-url-to-path/index.md)
