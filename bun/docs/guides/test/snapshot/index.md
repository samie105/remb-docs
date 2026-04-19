---
title: "Use snapshot testing in `bun test`"
source: "https://bun.com/docs/guides/test/snapshot"
canonical_url: "https://bun.com/docs/guides/test/snapshot"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:08.773Z"
content_hash: "1fee1963495b1f7806b4963f4d9f079db3a3240e04230155a690d28033fa7f55"
menu_path: ["Use snapshot testing in `bun test`"]
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

Bun’s test runner supports Jest-style snapshot testing via `.toMatchSnapshot()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)snap.test.ts

```
import { test, expect } from "bun:test";

test("snapshot", () => {
  expect({ foo: "bar" }).toMatchSnapshot();
});
```

* * *

The first time this test is executed, Bun will evaluate the value passed into `expect()` and write it to disk in a directory called `__snapshots__` that lives alongside the test file. (Note the `snapshots: +1 added` line in the output.)

terminal

```
bun test test/snap
```

```
test/snap.test.ts:
✓ snapshot [1.48ms]

 1 pass
 0 fail
 snapshots: +1 added
 1 expect() calls
Ran 1 tests across 1 files. [82.00ms]
```

* * *

The `__snapshots__` directory contains a `.snap` file for each test file in the directory.

File Tree

```
test
├── __snapshots__
│   └── snap.test.ts.snap
└── snap.test.ts
```

* * *

The `snap.test.ts.snap` file is a JavaScript file that exports a serialized version of the value passed into `expect()`. The `{foo: "bar"}` object has been serialized to JSON.

snap.test.ts.snap

```
// Bun Snapshot v1, https://bun.com/docs/test/snapshots

exports[`snapshot 1`] = `
{
  "foo": "bar",
}
`;
```

* * *

Later, when this test file is executed again, Bun will read the snapshot file and compare it to the value passed into `expect()`. If the values are different, the test will fail.

terminal

```
bun test
```

```
bun test v1.3.3 (9c68abdb)
test/snap.test.ts:
✓ snapshot [1.05ms]

 1 pass
 0 fail
 1 snapshots, 1 expect() calls
Ran 1 tests across 1 files. [101.00ms]
```

* * *

To update snapshots, use the `--update-snapshots` flag.

terminal

```
bun test --update-snapshots
```

```
bun test v1.3.3 (9c68abdb)
test/snap.test.ts:
✓ snapshot [0.86ms]

 1 pass
 0 fail
 snapshots: +1 added  # the snapshot was regenerated
 1 expect() calls
Ran 1 tests across 1 files. [102.00ms]
```

* * *

See [Docs > Test Runner > Snapshots](/docs/test/snapshots) for complete documentation on snapshots with the Bun test runner.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/snapshot.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/snapshot>)

[

Set the system time in Bun's test runner

Previous

](/docs/guides/test/mock-clock)[

Update snapshots in \`bun test\`

Next

](/docs/guides/test/update-snapshots)
