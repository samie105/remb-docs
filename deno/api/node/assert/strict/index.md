---
title: "namespace assert.strict"
source: "https://docs.deno.com/api/node/assert/strict/"
canonical_url: "https://docs.deno.com/api/node/assert/strict/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T18:02:56.270Z"
content_hash: "b3c4a8d61e82665e95a43e4c00d62fd2326c983b769fa6ca7ac4319984f55bf8"
menu_path: ["namespace assert.strict"]
section_path: []
content_language: "en"
nav_prev: {"path": "../index.md", "title": "assert - Node documentation"}
nav_next: {"path": "../../async_hooks/index.md", "title": "async_hooks - Node documentation"}
---

# namespace assert.strict

In strict assertion mode, non-strict methods behave like their corresponding strict methods. For example, [deepEqual](../.././assert/~/assert.deepEqual) will behave like [deepStrictEqual](../.././assert/~/assert.deepStrictEqual).

In strict assertion mode, error messages for objects display a diff. In legacy assertion mode, error messages for objects display the objects, often truncated.

To use strict assertion mode:

```js
import { strict as assert } from 'node:assert';
import assert from 'node:assert/strict';
```

Example error diff:

```js
import { strict as assert } from 'node:assert';

assert.deepEqual([[[1, 2, 3]], 4, 5], [[[1, 2, '3']], 4, 5]);
// AssertionError: Expected inputs to be strictly deep-equal:
// + actual - expected ... Lines skipped
//
//   [
//     [
// ...
//       2,
// +     3
// -     '3'
//     ],
// ...
//     5
//   ]
```

To deactivate the colors, use the `NO_COLOR` or `NODE_DISABLE_COLORS` environment variables. This will also deactivate the colors in the REPL. For more on color support in terminal environments, read the tty `getColorDepth()` documentation.

T

[assert.strict.AssertionError](../.././assert/~/assert.strict.AssertionError "assert.strict.AssertionError")

No documentation available

T

[assert.strict.AssertPredicate](../.././assert/~/assert.strict.AssertPredicate "assert.strict.AssertPredicate")

No documentation available

T

[assert.strict.CallTrackerCall](../.././assert/~/assert.strict.CallTrackerCall "assert.strict.CallTrackerCall")

No documentation available

T

[assert.strict.CallTrackerReportInformation](../.././assert/~/assert.strict.CallTrackerReportInformation "assert.strict.CallTrackerReportInformation")

No documentation available

# variable assert.strict
