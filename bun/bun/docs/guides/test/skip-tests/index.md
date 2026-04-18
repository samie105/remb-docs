---
title: "Skip tests with the Bun test runner"
source: "https://bun.com/docs/guides/test/skip-tests"
canonical_url: "https://bun.com/docs/guides/test/skip-tests"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:03.546Z"
content_hash: "6d65abf5b5d90fabf50bc6165c20049402fd45ee44ed9ea12d12c77c88ca6079"
menu_path: ["Skip tests with the Bun test runner"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/test/run-tests/index.md", "title": "Run your tests with the Bun test runner"}
nav_next: {"path": "bun/bun/docs/guides/test/snapshot/index.md", "title": "Use snapshot testing in `bun test`"}
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

To skip a test with the Bun test runner, use the `test.skip` function.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test } from "bun:test";

test.skip("unimplemented feature", () => {
  expect(Bun.isAwesome()).toBe(true);
});
```

* * *

Running `bun test` will not execute this test. It will be marked as skipped in the terminal output.

terminal

```
bun test
```

```
test.test.ts:
✓ add [0.03ms]
✓ multiply [0.02ms]
» unimplemented feature

 2 pass
 1 skip
 0 fail
 2 expect() calls
Ran 3 tests across 1 files. [74.00ms]
```

* * *

See also:

*   [Mark a test as a todo](/docs/guides/test/todo-tests)
*   [Docs > Test runner > Writing tests](/docs/test/writing-tests)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/skip-tests.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/skip-tests>)

[

Selectively run tests concurrently with glob patterns

Previous

](/docs/guides/test/concurrent-test-glob)[

Mark a test as a "todo" with the Bun test runner

Next

](/docs/guides/test/todo-tests)
