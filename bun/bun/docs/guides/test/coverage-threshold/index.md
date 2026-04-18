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
nav_prev: {"path": "bun/docs/guides/test/coverage/index.md", "title": "Generate code coverage reports with the Bun test runner"}
nav_next: {"path": "bun/bun/docs/guides/test/happy-dom/index.md", "title": "Write browser DOM tests with Bun and happy-dom"}
---

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


