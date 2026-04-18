---
title: "Update snapshots in `bun test`"
source: "https://bun.com/docs/guides/test/update-snapshots"
canonical_url: "https://bun.com/docs/guides/test/update-snapshots"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:32.593Z"
content_hash: "46fd9f39bae81003511a6460caec0ad75bd284526b0e86e71599f9a27a3cec69"
menu_path: ["Update snapshots in `bun test`"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/test/todo-tests/index.md", "title": "Mark a test as a \"todo\" with the Bun test runner"}
nav_next: {"path": "bun/bun/docs/guides/test/watch-mode/index.md", "title": "Run tests in watch mode with Bun"}
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

Bun’s test runner supports Jest-style snapshot testing via `.toMatchSnapshot()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)snap.test.ts

```
import { test, expect } from "bun:test";

test("snapshot", () => {
  expect({ foo: "bar" }).toMatchSnapshot();
});
```

* * *

The first time this test is executed, Bun will write a snapshot file to disk in a directory called `__snapshots__` that lives alongside the test file.

File Tree

```
test
├── __snapshots__
│   └── snap.test.ts.snap
└── snap.test.ts
```

* * *

To regenerate snapshots, use the `--update-snapshots` flag.

terminal

```
bun test --update-snapshots
```

```
test/snap.test.ts:
✓ snapshot [0.86ms]

 1 pass
 0 fail
 snapshots: +1 added # the snapshot was regenerated
 1 expect() calls
Ran 1 tests across 1 files. [102.00ms]
```

* * *

See [Docs > Test Runner > Snapshots](/docs/test/snapshots) for complete documentation on snapshots with the Bun test runner.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/update-snapshots.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/update-snapshots>)

[

Use snapshot testing in \`bun test\`

Previous

](/docs/guides/test/snapshot)[

Generate code coverage reports with the Bun test runner

Next

](/docs/guides/test/coverage)


