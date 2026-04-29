---
title: "Generate code coverage reports with the Bun test runner"
source: "https://bun.com/docs/guides/test/coverage"
canonical_url: "https://bun.com/docs/guides/test/coverage"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:33.239Z"
content_hash: "6470241ebf4b897464a50c0608470ddf63a7adfec50b4622dca06e9af49ae938"
menu_path: ["Generate code coverage reports with the Bun test runner"]
section_path: []
nav_prev: {"path": "bun/docs/guides/test/concurrent-test-glob/index.md", "title": "Selectively run tests concurrently with glob patterns"}
nav_next: {"path": "bun/docs/guides/test/coverage-threshold/index.md", "title": "Set a code coverage threshold with the Bun test runner"}
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

Bun’s test runner supports built-in _code coverage reporting_. Use it to see how much of your codebase is covered by tests and find areas that are not currently well-tested.

* * *

Pass the `--coverage` flag to `bun test` to enable this feature. This will print a coverage report after the test run. The coverage report lists the source files that were executed during the test run, the percentage of functions and lines that were executed, and the line ranges that were not executed during the run.

terminal

```
bun test --coverage
```

```

test.test.ts:
✓ math > add [0.71ms]
✓ math > multiply [0.03ms]
✓ random [0.13ms]
-------------|---------|---------|-------------------
File         | % Funcs | % Lines | Uncovered Line #s
-------------|---------|---------|-------------------
All files    |   66.67 |   77.78 |
 math.ts     |   50.00 |   66.67 |
 random.ts   |   50.00 |   66.67 |
-------------|---------|---------|-------------------

 3 pass
 0 fail
 3 expect() calls
```

* * *

To always enable coverage reporting by default, add the following line to your `bunfig.toml`:

bunfig.toml

```
[test]
coverage = true # always enable coverage
```

* * *

Refer to [Docs > Test runner > Coverage](../../../test/code-coverage/index.md) for complete documentation on code coverage reporting in Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/coverage.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/coverage>)

[

Update snapshots in \`bun test\`

Previous

](../update-snapshots/index.md)[

Set a code coverage threshold with the Bun test runner

Next

](../coverage-threshold/index.md)
