---
title: "assert - Node documentation"
source: "https://docs.deno.com/api/node/assert/"
canonical_url: "https://docs.deno.com/api/node/assert/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:54.760Z"
content_hash: "a612aef8f5b5e8706b4df54366f87f4b3892cb3e2a88a9a61856b5c197483137"
menu_path: ["assert - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/deno/index.md", "title": "Deno Namespace APIs"}
nav_next: {"path": "deno/deno/api/node/index.md", "title": "Node.js Built-in APIs"}
---

### Usage in Deno

```typescript
import * as mod from "node:assert";
```

The `node:assert` module provides a set of assertion functions for verifying invariants.

### Classes [#](#Classes)

c

[assert.AssertionError](.././assert/~/assert.AssertionError "assert.AssertionError")

Indicates the failure of an assertion. All errors thrown by the `node:assert` module will be instances of the `AssertionError` class.

*   [actual](.././assert/~/assert.AssertionError#property_actual)
*   [code](.././assert/~/assert.AssertionError#property_code)
*   [expected](.././assert/~/assert.AssertionError#property_expected)
*   [generatedMessage](.././assert/~/assert.AssertionError#property_generatedmessage)
*   [operator](.././assert/~/assert.AssertionError#property_operator)

c

[assert.CallTracker](.././assert/~/assert.CallTracker "assert.CallTracker")

This feature is deprecated and will be removed in a future version. Please consider using alternatives such as the `mock` helper function.

*   [calls](.././assert/~/assert.CallTracker#method_calls_0)
*   [getCalls](.././assert/~/assert.CallTracker#method_getcalls_0)
*   [report](.././assert/~/assert.CallTracker#method_report_0)
*   [reset](.././assert/~/assert.CallTracker#method_reset_0)
*   [verify](.././assert/~/assert.CallTracker#method_verify_0)

### Functions [#](#Functions)

f

N

[assert](.././assert/~/assert "assert")

An alias of ok.

f

[assert.deepEqual](.././assert/~/assert.deepEqual "assert.deepEqual")

**Strict assertion mode**

f

[assert.deepStrictEqual](.././assert/~/assert.deepStrictEqual "assert.deepStrictEqual")

Tests for deep equality between the `actual` and `expected` parameters. "Deep" equality means that the enumerable "own" properties of child objects are recursively evaluated also by the following rules.

f

[assert.doesNotMatch](.././assert/~/assert.doesNotMatch "assert.doesNotMatch")

Expects the `string` input not to match the regular expression.

f

[assert.doesNotReject](.././assert/~/assert.doesNotReject "assert.doesNotReject")

Awaits the `asyncFn` promise or, if `asyncFn` is a function, immediately calls the function and awaits the returned promise to complete. It will then check that the promise is not rejected.

f

[assert.doesNotThrow](.././assert/~/assert.doesNotThrow "assert.doesNotThrow")

Asserts that the function `fn` does not throw an error.

f

[assert.equal](.././assert/~/assert.equal "assert.equal")

**Strict assertion mode**

f

[assert.fail](.././assert/~/assert.fail "assert.fail")

Throws an `AssertionError` with the provided error message or a default error message. If the `message` parameter is an instance of an `Error` then it will be thrown instead of the `AssertionError`.

f

[assert.ifError](.././assert/~/assert.ifError "assert.ifError")

Throws `value` if `value` is not `undefined` or `null`. This is useful when testing the `error` argument in callbacks. The stack trace contains all frames from the error passed to `ifError()` including the potential new frames for `ifError()` itself.

f

[assert.match](.././assert/~/assert.match "assert.match")

Expects the `string` input to match the regular expression.

f

[assert.notDeepEqual](.././assert/~/assert.notDeepEqual "assert.notDeepEqual")

**Strict assertion mode**

f

[assert.notDeepStrictEqual](.././assert/~/assert.notDeepStrictEqual "assert.notDeepStrictEqual")

Tests for deep strict inequality. Opposite of deepStrictEqual.

f

[assert.notEqual](.././assert/~/assert.notEqual "assert.notEqual")

**Strict assertion mode**

f

[assert.notStrictEqual](.././assert/~/assert.notStrictEqual "assert.notStrictEqual")

Tests strict inequality between the `actual` and `expected` parameters as determined by [`Object.is()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is).

f

[assert.ok](.././assert/~/assert.ok "assert.ok")

Tests if `value` is truthy. It is equivalent to `assert.equal(!!value, true, message)`.

f

[assert.partialDeepStrictEqual](.././assert/~/assert.partialDeepStrictEqual "assert.partialDeepStrictEqual")

`assert.partialDeepStrictEqual()` Asserts the equivalence between the `actual` and `expected` parameters through a deep comparison, ensuring that all properties in the `expected` parameter are present in the `actual` parameter with equivalent values, not allowing type coercion. The main difference with `assert.deepStrictEqual()` is that `assert.partialDeepStrictEqual()` does not require all properties in the `actual` parameter to be present in the `expected` parameter. This method should always pass the same test cases as `assert.deepStrictEqual()`, behaving as a super set of it.

f

[assert.rejects](.././assert/~/assert.rejects "assert.rejects")

Awaits the `asyncFn` promise or, if `asyncFn` is a function, immediately calls the function and awaits the returned promise to complete. It will then check that the promise is rejected.

f

[assert.strictEqual](.././assert/~/assert.strictEqual "assert.strictEqual")

Tests strict equality between the `actual` and `expected` parameters as determined by [`Object.is()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is).

f

[assert.throws](.././assert/~/assert.throws "assert.throws")

Expects the function `fn` to throw an error.

### Interfaces [#](#Interfaces)

I

[assert.CallTrackerCall](.././assert/~/assert.CallTrackerCall "assert.CallTrackerCall")

No documentation available

*   [arguments](.././assert/~/assert.CallTrackerCall#property_arguments)
*   [thisArg](.././assert/~/assert.CallTrackerCall#property_thisarg)

I

[assert.CallTrackerReportInformation](.././assert/~/assert.CallTrackerReportInformation "assert.CallTrackerReportInformation")

No documentation available

*   [actual](.././assert/~/assert.CallTrackerReportInformation#property_actual)
*   [expected](.././assert/~/assert.CallTrackerReportInformation#property_expected)
*   [message](.././assert/~/assert.CallTrackerReportInformation#property_message)
*   [operator](.././assert/~/assert.CallTrackerReportInformation#property_operator)
*   [stack](.././assert/~/assert.CallTrackerReportInformation#property_stack)

### Namespaces [#](#Namespaces)

N

v

[assert.strict](.././assert/~/assert.strict "assert.strict")

In strict assertion mode, non-strict methods behave like their corresponding strict methods. For example, deepEqual will behave like deepStrictEqual.

### Type Aliases [#](<#Type Aliases>)

T

[assert.AssertPredicate](.././assert/~/assert.AssertPredicate "assert.AssertPredicate")

No documentation available

T

[assert.strict.AssertionError](.././assert/~/assert.strict.AssertionError "assert.strict.AssertionError")

No documentation available

T

[assert.strict.AssertPredicate](.././assert/~/assert.strict.AssertPredicate "assert.strict.AssertPredicate")

No documentation available

T

[assert.strict.CallTrackerCall](.././assert/~/assert.strict.CallTrackerCall "assert.strict.CallTrackerCall")

No documentation available

T

[assert.strict.CallTrackerReportInformation](.././assert/~/assert.strict.CallTrackerReportInformation "assert.strict.CallTrackerReportInformation")

No documentation available


