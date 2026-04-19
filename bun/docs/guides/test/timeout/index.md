---
title: "Set a per-test timeout with the Bun test runner"
source: "https://bun.com/docs/guides/test/timeout"
canonical_url: "https://bun.com/docs/guides/test/timeout"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:25.003Z"
content_hash: "2f1de17814d490c25e284d9c7ff04577e43d02a0b861d423c0c726ac74dd1bac"
menu_path: ["Set a per-test timeout with the Bun test runner"]
section_path: []
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

Use the `--timeout` flag to set a timeout for each test in milliseconds. If any test exceeds this timeout, it will be marked as failed. The default timeout is `5000` (5 seconds).

terminal

```
bun test --timeout 3000 # 3 seconds
```

* * *

See [Docs > Test runner](/docs/test) for complete documentation of `bun test`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/timeout.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/timeout>)

[

Mark a test as a "todo" with the Bun test runner

Previous

](/docs/guides/test/todo-tests)[

Bail early with the Bun test runner

Next

](/docs/guides/test/bail)
