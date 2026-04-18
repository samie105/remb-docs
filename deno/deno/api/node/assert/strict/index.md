---
title: "namespace assert.strict"
source: "https://docs.deno.com/api/node/assert/strict/"
canonical_url: "https://docs.deno.com/api/node/assert/strict/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:16:06.946Z"
content_hash: "a334f45bee005d969c12ae8d809c8ffba6e0c0fcd4005a59d7bd4ba6124f1d19"
menu_path: ["namespace assert.strict"]
section_path: []
nav_prev: {"path": "deno/deno/api/web/all_symbols/index.md", "title": "All Symbols - Web documentation"}
nav_next: {"path": "deno/deno/api/index.md", "title": "Deno Namespace APIs"}
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

### Type Aliases [#](<#Type Aliases>)

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

### Type [#](#type)


