---
title: "Set a code coverage threshold with the Bun test runner"
source: "https://bun.com/docs/guides/test/coverage-threshold"
canonical_url: "https://bun.com/docs/guides/test/coverage-threshold"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:36.607Z"
content_hash: "cf15ad8b612b9ef62f77d9ff09c5a3ef51cb3170325b05fa690ec1ee57564ea6"
menu_path: ["Set a code coverage threshold with the Bun test runner"]
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

Bun’s test runner supports built-in code coverage reporting via the `--coverage` flag.

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

To set a minimum coverage threshold, add the following line to your `bunfig.toml`. This requires that 90% of your codebase is covered by tests.

bunfig.toml

```
[test]
# to require 90% line-level and function-level coverage
coverageThreshold = 0.9
```

* * *

If your test suite does not meet this threshold, `bun test` will exit with a non-zero exit code to signal a failure.

terminal

```
bun test --coverage
```

```
<test output>
$ echo $?
1 # this is the exit code of the previous command
```

* * *

Different thresholds can be set for line-level and function-level coverage.

bunfig.toml

```
[test]
# to set different thresholds for lines and functions
coverageThreshold = { lines = 0.5, functions = 0.7 }
```

* * *

See [Docs > Test runner > Coverage](/docs/test/code-coverage) for complete documentation on code coverage reporting in Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/coverage-threshold.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/coverage-threshold>)

[

Generate code coverage reports with the Bun test runner

Previous

](/docs/guides/test/coverage)[

Selectively run tests concurrently with glob patterns

Next

](/docs/guides/test/concurrent-test-glob)
