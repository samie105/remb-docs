---
title: "Run tests in watch mode with Bun"
source: "https://bun.com/docs/guides/test/watch-mode"
canonical_url: "https://bun.com/docs/guides/test/watch-mode"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:35.731Z"
content_hash: "539e0a52fe283a886a70f054fba3db79e95113ec3618fb7af3b78b4018bc7f05"
menu_path: ["Run tests in watch mode with Bun"]
section_path: []
nav_prev: {"path": "bun/docs/guides/test/update-snapshots/index.md", "title": "Update snapshots in `bun test`"}
nav_next: {"path": "bun/docs/guides/util/base64/index.md", "title": "Encode and decode base64 strings"}
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

Use the `--watch` flag to run your tests in watch mode.

terminal

```
bun test --watch
```

* * *

This will restart the running Bun process whenever a file change is detected. It’s fast. In this example, the editor is configured to save the file on every keystroke.

![Running tests in watch mode in
Bun](https://github.com/oven-sh/bun/assets/3084745/dc49a36e-ba82-416f-b960-1c883a924248)

* * *

See [Docs > Test Runner](../../../test/index.md) for complete documentation on the test runner.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/watch-mode.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/watch-mode>)

[

Run your tests with the Bun test runner

Previous

](../run-tests/index.md)[

Migrate from Jest to Bun's test runner

Next

](../migrate-from-jest/index.md)

![Running tests in watch mode in
Bun](https://github.com/oven-sh/bun/assets/3084745/dc49a36e-ba82-416f-b960-1c883a924248)
