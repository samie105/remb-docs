---
title: "test/reporters - Node documentation"
source: "https://docs.deno.com/api/node/test/reporters/"
canonical_url: "https://docs.deno.com/api/node/test/reporters/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:38.999Z"
content_hash: "d744fbc0b156b4c05b94ac208533b9a0e3ead2133b420c399d2d72b2ec2f5a1e"
menu_path: ["test/reporters - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/test/index.md", "title": "test - Node documentation"}
nav_next: {"path": "deno/deno/api/node/timers/index.md", "title": "timers - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:test/reporters";
```

The `node:test/reporters` module exposes the builtin-reporters for `node:test`. To access it:

```js
import test from 'node:test/reporters';
```

This module is only available under the `node:` scheme. The following will not work:

```js
import test from 'node:test/reporters';
```

### Classes [#](#Classes)

c

[LcovReporter](../.././test/reporters/~/LcovReporter "LcovReporter")

No documentation available

c

[SpecReporter](../.././test/reporters/~/SpecReporter "SpecReporter")

No documentation available

### Functions [#](#Functions)

f

[dot](../.././test/reporters/~/dot "dot")

The `dot` reporter outputs the test results in a compact format, where each passing test is represented by a `.`, and each failing test is represented by a `X`.

f

[junit](../.././test/reporters/~/junit "junit")

The `junit` reporter outputs test results in a jUnit XML format.

f

[tap](../.././test/reporters/~/tap "tap")

The `tap` reporter outputs the test results in the [TAP](https://testanything.org/) format.

### Interfaces [#](#Interfaces)

I

[ReporterConstructorWrapper](../.././test/reporters/~/ReporterConstructorWrapper "ReporterConstructorWrapper")

No documentation available

### Type Aliases [#](<#Type Aliases>)

T

[TestEvent](../.././test/reporters/~/TestEvent "TestEvent")

No documentation available

T

[TestEventGenerator](../.././test/reporters/~/TestEventGenerator "TestEventGenerator")

No documentation available

### Variables [#](#Variables)

v

[lcov](../.././test/reporters/~/lcov "lcov")

The `lcov` reporter outputs test coverage when used with the [`--experimental-test-coverage`](https://nodejs.org/docs/latest-v22.x/api/cli.html#--experimental-test-coverage) flag.

v

[spec](../.././test/reporters/~/spec "spec")

The `spec` reporter outputs the test results in a human-readable format.

