---
title: "Bail early with the Bun test runner"
source: "https://bun.com/docs/guides/test/bail"
canonical_url: "https://bun.com/docs/guides/test/bail"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:24.335Z"
content_hash: "e9f1e993b32944042aa31ae1114e1254440e0f8f2fef2f93ee095bef29d960de"
menu_path: ["Bail early with the Bun test runner"]
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

Use the `--bail` flag to bail on a test run after a single failure. This is useful for aborting as soon as possible in a continuous integration environment.

terminal

```
bun test --bail
```

* * *

To bail after a certain threshold of failures, optionally specify a number after the flag.

terminal

```
# bail after 10 failures
bun test --bail=10
```

* * *

See [Docs > Test runner](/docs/test) for complete documentation of `bun test`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/bail.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/bail>)

[

Set a per-test timeout with the Bun test runner

Previous

](/docs/guides/test/timeout)[

Re-run tests multiple times with the Bun test runner

Next

](/docs/guides/test/rerun-each)
