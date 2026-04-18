---
title: "Mark a test as a \"todo\" with the Bun test runner"
source: "https://bun.com/docs/guides/test/todo-tests"
canonical_url: "https://bun.com/docs/guides/test/todo-tests"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:27.606Z"
content_hash: "7cda773ff535358354dc51bb03e2ae9afb9eef7bd0b02b65f9f5d4876c2bfb9e"
menu_path: ["Mark a test as a \"todo\" with the Bun test runner"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/test/timeout/index.md", "title": "Set a per-test timeout with the Bun test runner"}
nav_next: {"path": "bun/bun/docs/guides/test/update-snapshots/index.md", "title": "Update snapshots in `bun test`"}
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

To remind yourself to write a test later, use the `test.todo` function. There’s no need to provide a test implementation.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test, expect } from "bun:test";

// write this later
test.todo("unimplemented feature");
```

* * *

The output of `bun test` indicates how many `todo` tests were encountered.

terminal

```
bun test
```

```
test.test.ts:
✓ add [0.03ms]
✓ multiply [0.02ms]
✎ unimplemented feature

 2 pass
 1 todo
 0 fail
 2 expect() calls
Ran 3 tests across 1 files. [74.00ms]
```

* * *

Optionally, you can provide a test implementation.

```
import { test, expect } from "bun:test";

test.todo("unimplemented feature", () => {
  expect(Bun.isAwesome()).toBe(true);
});
```

* * *

If an implementation is provided, it will not be run unless the `--todo` flag is passed. If the `--todo` flag is passed, the test will be executed and _expected to fail_ by test runner! If a todo test passes, the `bun test` run will return a non-zero exit code to signal the failure.

terminal

```
bun test --todo
```

```
my.test.ts:
✗ unimplemented feature
  ^ this test is marked as todo but passes. Remove `.todo` or check that test is correct.

 0 pass
 1 fail
 1 expect() calls
$ echo $?
1 # this is the exit code of the previous command
```

* * *

See also:

*   [Skip a test](/docs/guides/test/skip-tests)
*   [Docs > Test runner > Writing tests](/docs/test/writing-tests)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/todo-tests.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/todo-tests>)

[

Skip tests with the Bun test runner

Previous

](/docs/guides/test/skip-tests)[

Set a per-test timeout with the Bun test runner

Next

](/docs/guides/test/timeout)


