---
title: "test - Node documentation"
source: "https://docs.deno.com/api/node/test/"
canonical_url: "https://docs.deno.com/api/node/test/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:13:29.316Z"
content_hash: "e45bc4cc7c9fc6c8d84e4b0dfdcad1e9356f781a73d0efcda9bcf5361b35aeea"
menu_path: ["test - Node documentation"]
section_path: []
content_language: "en"
---
### Usage in Deno

```typescript
import * as mod from "node:test";
```

The `node:test` module facilitates the creation of JavaScript tests. To access it:

```js
import test from 'node:test';
```

This module is only available under the `node:` scheme. The following will not work:

```js
import test from 'node:test';
```

Tests created via the `test` module consist of a single function that is processed in one of three ways:

1.  A synchronous function that is considered failing if it throws an exception, and is considered passing otherwise.
2.  A function that returns a `Promise` that is considered failing if the `Promise` rejects, and is considered passing if the `Promise` fulfills.
3.  A function that receives a callback function. If the callback receives any truthy value as its first argument, the test is considered failing. If a falsy value is passed as the first argument to the callback, the test is considered passing. If the test function receives a callback function and also returns a `Promise`, the test will fail.

The following example illustrates how tests are written using the `test` module.

```js
test('synchronous passing test', (t) => {
  // This test passes because it does not throw an exception.
  assert.strictEqual(1, 1);
});

test('synchronous failing test', (t) => {
  // This test fails because it throws an exception.
  assert.strictEqual(1, 2);
});

test('asynchronous passing test', async (t) => {
  // This test passes because the Promise returned by the async
  // function is settled and not rejected.
  assert.strictEqual(1, 1);
});

test('asynchronous failing test', async (t) => {
  // This test fails because the Promise returned by the async
  // function is rejected.
  assert.strictEqual(1, 2);
});

test('failing test using Promises', (t) => {
  // Promises can be used directly as well.
  return new Promise((resolve, reject) => {
    setImmediate(() => {
      reject(new Error('this will cause the test to fail'));
    });
  });
});

test('callback passing test', (t, done) => {
  // done() is the callback function. When the setImmediate() runs, it invokes
  // done() with no arguments.
  setImmediate(done);
});

test('callback failing test', (t, done) => {
  // When the setImmediate() runs, done() is invoked with an Error object and
  // the test fails.
  setImmediate(() => {
    done(new Error('callback failure'));
  });
});
```

If any tests fail, the process exit code is set to `1`.

c

[MockFunctionContext](.././test/~/MockFunctionContext "MockFunctionContext")

The `MockFunctionContext` class is used to inspect or manipulate the behavior of mocks created via the `MockTracker` APIs.

-   [callCount](.././test/~/MockFunctionContext#method_callcount_0)
-   [calls](.././test/~/MockFunctionContext#property_calls)
-   [mockImplementation](.././test/~/MockFunctionContext#method_mockimplementation_0)
-   [mockImplementationOnce](.././test/~/MockFunctionContext#method_mockimplementationonce_0)
-   [resetCalls](.././test/~/MockFunctionContext#method_resetcalls_0)
-   [restore](.././test/~/MockFunctionContext#method_restore_0)

c

[MockModuleContext](.././test/~/MockModuleContext "MockModuleContext")

No documentation available

-   [restore](.././test/~/MockModuleContext#method_restore_0)

c

[MockTimers](.././test/~/MockTimers "MockTimers")

Mocking timers is a technique commonly used in software testing to simulate and control the behavior of timers, such as `setInterval` and `setTimeout`, without actually waiting for the specified time intervals.

-   [enable](.././test/~/MockTimers#method_enable_0)
-   [reset](.././test/~/MockTimers#method_reset_0)
-   [runAll](.././test/~/MockTimers#method_runall_0)
-   [setTime](.././test/~/MockTimers#method_settime_0)
-   [tick](.././test/~/MockTimers#method_tick_0)

c

[MockTracker](.././test/~/MockTracker "MockTracker")

The `MockTracker` class is used to manage mocking functionality. The test runner module provides a top level `mock` export which is a `MockTracker` instance. Each test also provides its own `MockTracker` instance via the test context's `mock` property.

-   [fn](.././test/~/MockTracker#method_fn_0)
-   [getter](.././test/~/MockTracker#method_getter_0)
-   [method](.././test/~/MockTracker#method_method_0)
-   [module](.././test/~/MockTracker#method_module_0)
-   [reset](.././test/~/MockTracker#method_reset_0)
-   [restoreAll](.././test/~/MockTracker#method_restoreall_0)
-   [setter](.././test/~/MockTracker#method_setter_0)
-   [timers](.././test/~/MockTracker#property_timers)

c

[SuiteContext](.././test/~/SuiteContext "SuiteContext")

An instance of `SuiteContext` is passed to each suite function in order to interact with the test runner. However, the `SuiteContext` constructor is not exposed as part of the API.

-   [filePath](.././test/~/SuiteContext#property_filepath)
-   [name](.././test/~/SuiteContext#property_name)
-   [signal](.././test/~/SuiteContext#property_signal)

c

[TestContext](.././test/~/TestContext "TestContext")

An instance of `TestContext` is passed to each test function in order to interact with the test runner. However, the `TestContext` constructor is not exposed as part of the API.

-   [after](.././test/~/TestContext#method_after_0)
-   [afterEach](.././test/~/TestContext#method_aftereach_0)
-   [assert](.././test/~/TestContext#property_assert)
-   [before](.././test/~/TestContext#method_before_0)
-   [beforeEach](.././test/~/TestContext#method_beforeeach_0)
-   [diagnostic](.././test/~/TestContext#method_diagnostic_0)
-   [filePath](.././test/~/TestContext#property_filepath)
-   [fullName](.././test/~/TestContext#property_fullname)
-   [mock](.././test/~/TestContext#property_mock)
-   [name](.././test/~/TestContext#property_name)
-   [plan](.././test/~/TestContext#method_plan_0)
-   [runOnly](.././test/~/TestContext#method_runonly_0)
-   [signal](.././test/~/TestContext#property_signal)
-   [skip](.././test/~/TestContext#method_skip_0)
-   [test](.././test/~/TestContext#property_test)
-   [todo](.././test/~/TestContext#method_todo_0)
-   [waitFor](.././test/~/TestContext#method_waitfor_0)

c

[TestsStream](.././test/~/TestsStream "TestsStream")

A successful call to `run()` will return a new `TestsStream` object, streaming a series of events representing the execution of the tests.

-   [addListener](.././test/~/TestsStream#method_addlistener_0)
-   [emit](.././test/~/TestsStream#method_emit_0)
-   [on](.././test/~/TestsStream#method_on_0)
-   [once](.././test/~/TestsStream#method_once_0)
-   [prependListener](.././test/~/TestsStream#method_prependlistener_0)
-   [prependOnceListener](.././test/~/TestsStream#method_prependoncelistener_0)

f

[after](.././test/~/after "after")

This function creates a hook that runs after executing a suite.

f

[afterEach](.././test/~/afterEach "afterEach")

This function creates a hook that runs after each test in the current suite. The `afterEach()` hook is run even if the test fails.

f

[assert.register](.././test/~/assert.register "assert.register")

Defines a new assertion function with the provided name and function. If an assertion already exists with the same name, it is overwritten.

f

[before](.././test/~/before "before")

This function creates a hook that runs before executing a suite.

f

[beforeEach](.././test/~/beforeEach "beforeEach")

This function creates a hook that runs before each test in the current suite.

f

N

[default](.././test/~/default "default")

The `test()` function is the value imported from the `test` module. Each invocation of this function results in reporting the test to the `TestsStream`.

f

[default.after](.././test/~/default.after "default.after")

This function creates a hook that runs after executing a suite.

f

[default.afterEach](.././test/~/default.afterEach "default.afterEach")

This function creates a hook that runs after each test in the current suite. The `afterEach()` hook is run even if the test fails.

f

[default.assert.register](.././test/~/default.assert.register "default.assert.register")

Defines a new assertion function with the provided name and function. If an assertion already exists with the same name, it is overwritten.

f

[default.before](.././test/~/default.before "default.before")

This function creates a hook that runs before executing a suite.

f

[default.beforeEach](.././test/~/default.beforeEach "default.beforeEach")

This function creates a hook that runs before each test in the current suite.

f

N

[default.describe](.././test/~/default.describe "default.describe")

Alias for [suite](.././test/~/suite).

f

[default.describe.only](.././test/~/default.describe.only "default.describe.only")

Shorthand for marking a suite as `only`. This is the same as calling [describe](.././test/~/describe) with `options.only` set to `true`.

f

[default.describe.skip](.././test/~/default.describe.skip "default.describe.skip")

Shorthand for skipping a suite. This is the same as calling [describe](.././test/~/describe) with `options.skip` set to `true`.

f

[default.describe.todo](.././test/~/default.describe.todo "default.describe.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [describe](.././test/~/describe) with `options.todo` set to `true`.

f

N

[default.it](.././test/~/default.it "default.it")

Alias for [test](.././test/~/test).

f

[default.it.only](.././test/~/default.it.only "default.it.only")

Shorthand for marking a test as `only`. This is the same as calling [it](.././test/~/it) with `options.only` set to `true`.

f

[default.it.skip](.././test/~/default.it.skip "default.it.skip")

Shorthand for skipping a test. This is the same as calling [it](.././test/~/it) with `options.skip` set to `true`.

f

[default.it.todo](.././test/~/default.it.todo "default.it.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [it](.././test/~/it) with `options.todo` set to `true`.

f

[default.only](.././test/~/default.only "default.only")

Shorthand for marking a test as `only`. This is the same as calling [test](.././test/~/test) with `options.only` set to `true`.

f

[default.run](.././test/~/default.run "default.run")

**Note:** `shard` is used to horizontally parallelize test running across machines or processes, ideal for large-scale executions across varied environments. It's incompatible with `watch` mode, tailored for rapid code iteration by automatically rerunning tests on file changes.

f

[default.skip](.././test/~/default.skip "default.skip")

Shorthand for skipping a test. This is the same as calling [test](.././test/~/test) with `options.skip` set to `true`.

f

[default.snapshot.setDefaultSnapshotSerializers](.././test/~/default.snapshot.setDefaultSnapshotSerializers "default.snapshot.setDefaultSnapshotSerializers")

This function is used to customize the default serialization mechanism used by the test runner.

f

[default.snapshot.setResolveSnapshotPath](.././test/~/default.snapshot.setResolveSnapshotPath "default.snapshot.setResolveSnapshotPath")

This function is used to set a custom resolver for the location of the snapshot file used for snapshot testing. By default, the snapshot filename is the same as the entry point filename with `.snapshot` appended.

f

N

[default.suite](.././test/~/default.suite "default.suite")

The `suite()` function is imported from the `node:test` module.

f

[default.suite.only](.././test/~/default.suite.only "default.suite.only")

Shorthand for marking a suite as `only`. This is the same as calling [suite](.././test/~/suite) with `options.only` set to `true`.

f

[default.suite.skip](.././test/~/default.suite.skip "default.suite.skip")

Shorthand for skipping a suite. This is the same as calling [suite](.././test/~/suite) with `options.skip` set to `true`.

f

[default.suite.todo](.././test/~/default.suite.todo "default.suite.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [suite](.././test/~/suite) with `options.todo` set to `true`.

f

[default.todo](.././test/~/default.todo "default.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [test](.././test/~/test) with `options.todo` set to `true`.

f

N

[describe](.././test/~/describe "describe")

Alias for [suite](.././test/~/suite).

f

[describe.only](.././test/~/describe.only "describe.only")

Shorthand for marking a suite as `only`. This is the same as calling [describe](.././test/~/describe) with `options.only` set to `true`.

f

[describe.skip](.././test/~/describe.skip "describe.skip")

Shorthand for skipping a suite. This is the same as calling [describe](.././test/~/describe) with `options.skip` set to `true`.

f

[describe.todo](.././test/~/describe.todo "describe.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [describe](.././test/~/describe) with `options.todo` set to `true`.

f

N

[it](.././test/~/it "it")

Alias for [test](.././test/~/test).

f

[it.only](.././test/~/it.only "it.only")

Shorthand for marking a test as `only`. This is the same as calling [it](.././test/~/it) with `options.only` set to `true`.

f

[it.skip](.././test/~/it.skip "it.skip")

Shorthand for skipping a test. This is the same as calling [it](.././test/~/it) with `options.skip` set to `true`.

f

[it.todo](.././test/~/it.todo "it.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [it](.././test/~/it) with `options.todo` set to `true`.

f

[only](.././test/~/only "only")

Shorthand for marking a test as `only`. This is the same as calling [test](.././test/~/test) with `options.only` set to `true`.

f

[run](.././test/~/run "run")

**Note:** `shard` is used to horizontally parallelize test running across machines or processes, ideal for large-scale executions across varied environments. It's incompatible with `watch` mode, tailored for rapid code iteration by automatically rerunning tests on file changes.

f

[skip](.././test/~/skip "skip")

Shorthand for skipping a test. This is the same as calling [test](.././test/~/test) with `options.skip` set to `true`.

f

[snapshot.setDefaultSnapshotSerializers](.././test/~/snapshot.setDefaultSnapshotSerializers "snapshot.setDefaultSnapshotSerializers")

This function is used to customize the default serialization mechanism used by the test runner.

f

[snapshot.setResolveSnapshotPath](.././test/~/snapshot.setResolveSnapshotPath "snapshot.setResolveSnapshotPath")

This function is used to set a custom resolver for the location of the snapshot file used for snapshot testing. By default, the snapshot filename is the same as the entry point filename with `.snapshot` appended.

f

N

[suite](.././test/~/suite "suite")

The `suite()` function is imported from the `node:test` module.

f

[suite.only](.././test/~/suite.only "suite.only")

Shorthand for marking a suite as `only`. This is the same as calling [suite](.././test/~/suite) with `options.only` set to `true`.

f

[suite.skip](.././test/~/suite.skip "suite.skip")

Shorthand for skipping a suite. This is the same as calling [suite](.././test/~/suite) with `options.skip` set to `true`.

f

[suite.todo](.././test/~/suite.todo "suite.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [suite](.././test/~/suite) with `options.todo` set to `true`.

f

N

[test](.././test/~/test "test")

The `test()` function is the value imported from the `test` module. Each invocation of this function results in reporting the test to the `TestsStream`.

f

[test.after](.././test/~/test.after "test.after")

This function creates a hook that runs after executing a suite.

f

[test.afterEach](.././test/~/test.afterEach "test.afterEach")

This function creates a hook that runs after each test in the current suite. The `afterEach()` hook is run even if the test fails.

f

[test.assert.register](.././test/~/test.assert.register "test.assert.register")

Defines a new assertion function with the provided name and function. If an assertion already exists with the same name, it is overwritten.

f

[test.before](.././test/~/test.before "test.before")

This function creates a hook that runs before executing a suite.

f

[test.beforeEach](.././test/~/test.beforeEach "test.beforeEach")

This function creates a hook that runs before each test in the current suite.

f

N

[test.describe](.././test/~/test.describe "test.describe")

Alias for [suite](.././test/~/suite).

f

[test.describe.only](.././test/~/test.describe.only "test.describe.only")

Shorthand for marking a suite as `only`. This is the same as calling [describe](.././test/~/describe) with `options.only` set to `true`.

f

[test.describe.skip](.././test/~/test.describe.skip "test.describe.skip")

Shorthand for skipping a suite. This is the same as calling [describe](.././test/~/describe) with `options.skip` set to `true`.

f

[test.describe.todo](.././test/~/test.describe.todo "test.describe.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [describe](.././test/~/describe) with `options.todo` set to `true`.

f

N

[test.it](.././test/~/test.it "test.it")

Alias for [test](.././test/~/test).

f

[test.it.only](.././test/~/test.it.only "test.it.only")

Shorthand for marking a test as `only`. This is the same as calling [it](.././test/~/it) with `options.only` set to `true`.

f

[test.it.skip](.././test/~/test.it.skip "test.it.skip")

Shorthand for skipping a test. This is the same as calling [it](.././test/~/it) with `options.skip` set to `true`.

f

[test.it.todo](.././test/~/test.it.todo "test.it.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [it](.././test/~/it) with `options.todo` set to `true`.

f

[test.only](.././test/~/test.only "test.only")

Shorthand for marking a test as `only`. This is the same as calling [test](.././test/~/test) with `options.only` set to `true`.

f

[test.run](.././test/~/test.run "test.run")

**Note:** `shard` is used to horizontally parallelize test running across machines or processes, ideal for large-scale executions across varied environments. It's incompatible with `watch` mode, tailored for rapid code iteration by automatically rerunning tests on file changes.

f

[test.skip](.././test/~/test.skip "test.skip")

Shorthand for skipping a test. This is the same as calling [test](.././test/~/test) with `options.skip` set to `true`.

f

[test.snapshot.setDefaultSnapshotSerializers](.././test/~/test.snapshot.setDefaultSnapshotSerializers "test.snapshot.setDefaultSnapshotSerializers")

This function is used to customize the default serialization mechanism used by the test runner.

f

[test.snapshot.setResolveSnapshotPath](.././test/~/test.snapshot.setResolveSnapshotPath "test.snapshot.setResolveSnapshotPath")

This function is used to set a custom resolver for the location of the snapshot file used for snapshot testing. By default, the snapshot filename is the same as the entry point filename with `.snapshot` appended.

f

N

[test.suite](.././test/~/test.suite "test.suite")

The `suite()` function is imported from the `node:test` module.

f

[test.suite.only](.././test/~/test.suite.only "test.suite.only")

Shorthand for marking a suite as `only`. This is the same as calling [suite](.././test/~/suite) with `options.only` set to `true`.

f

[test.suite.skip](.././test/~/test.suite.skip "test.suite.skip")

Shorthand for skipping a suite. This is the same as calling [suite](.././test/~/suite) with `options.skip` set to `true`.

f

[test.suite.todo](.././test/~/test.suite.todo "test.suite.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [suite](.././test/~/suite) with `options.todo` set to `true`.

f

[test.todo](.././test/~/test.todo "test.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [test](.././test/~/test) with `options.todo` set to `true`.

f

[todo](.././test/~/todo "todo")

Shorthand for marking a test as `TODO`. This is the same as calling [test](.././test/~/test) with `options.todo` set to `true`.

I

[AssertSnapshotOptions](.././test/~/AssertSnapshotOptions "AssertSnapshotOptions")

No documentation available

-   [serializers](.././test/~/AssertSnapshotOptions#property_serializers)

I

[HookOptions](.././test/~/HookOptions "HookOptions")

Configuration options for hooks.

-   [signal](.././test/~/HookOptions#property_signal)
-   [timeout](.././test/~/HookOptions#property_timeout)

I

[MockFunctionCall](.././test/~/MockFunctionCall "MockFunctionCall")

No documentation available

-   [arguments](.././test/~/MockFunctionCall#property_arguments)
-   [error](.././test/~/MockFunctionCall#property_error)
-   [result](.././test/~/MockFunctionCall#property_result)
-   [stack](.././test/~/MockFunctionCall#property_stack)
-   [target](.././test/~/MockFunctionCall#property_target)
-   [this](.././test/~/MockFunctionCall#property_this)

I

[MockFunctionOptions](.././test/~/MockFunctionOptions "MockFunctionOptions")

No documentation available

-   [times](.././test/~/MockFunctionOptions#property_times)

I

[MockMethodOptions](.././test/~/MockMethodOptions "MockMethodOptions")

No documentation available

-   [getter](.././test/~/MockMethodOptions#property_getter)
-   [setter](.././test/~/MockMethodOptions#property_setter)

I

[MockModuleOptions](.././test/~/MockModuleOptions "MockModuleOptions")

No documentation available

-   [cache](.././test/~/MockModuleOptions#property_cache)
-   [defaultExport](.././test/~/MockModuleOptions#property_defaultexport)
-   [namedExports](.././test/~/MockModuleOptions#property_namedexports)

I

[MockTimersOptions](.././test/~/MockTimersOptions "MockTimersOptions")

No documentation available

-   [apis](.././test/~/MockTimersOptions#property_apis)
-   [now](.././test/~/MockTimersOptions#property_now)

I

[RunOptions](.././test/~/RunOptions "RunOptions")

No documentation available

-   [argv](.././test/~/RunOptions#property_argv)
-   [branchCoverage](.././test/~/RunOptions#property_branchcoverage)
-   [concurrency](.././test/~/RunOptions#property_concurrency)
-   [coverage](.././test/~/RunOptions#property_coverage)
-   [coverageExcludeGlobs](.././test/~/RunOptions#property_coverageexcludeglobs)
-   [coverageIncludeGlobs](.././test/~/RunOptions#property_coverageincludeglobs)
-   [execArgv](.././test/~/RunOptions#property_execargv)
-   [files](.././test/~/RunOptions#property_files)
-   [forceExit](.././test/~/RunOptions#property_forceexit)
-   [functionCoverage](.././test/~/RunOptions#property_functioncoverage)
-   [globPatterns](.././test/~/RunOptions#property_globpatterns)
-   [inspectPort](.././test/~/RunOptions#property_inspectport)
-   [isolation](.././test/~/RunOptions#property_isolation)
-   [lineCoverage](.././test/~/RunOptions#property_linecoverage)
-   [only](.././test/~/RunOptions#property_only)
-   [setup](.././test/~/RunOptions#property_setup)
-   [shard](.././test/~/RunOptions#property_shard)
-   [signal](.././test/~/RunOptions#property_signal)
-   [testNamePatterns](.././test/~/RunOptions#property_testnamepatterns)
-   [testSkipPatterns](.././test/~/RunOptions#property_testskippatterns)
-   [timeout](.././test/~/RunOptions#property_timeout)
-   [watch](.././test/~/RunOptions#property_watch)

I

[TestContextAssert](.././test/~/TestContextAssert "TestContextAssert")

No documentation available

-   [fileSnapshot](.././test/~/TestContextAssert#method_filesnapshot_0)
-   [snapshot](.././test/~/TestContextAssert#method_snapshot_0)

I

[TestContextWaitForOptions](.././test/~/TestContextWaitForOptions "TestContextWaitForOptions")

No documentation available

-   [interval](.././test/~/TestContextWaitForOptions#property_interval)
-   [timeout](.././test/~/TestContextWaitForOptions#property_timeout)

I

[TestOptions](.././test/~/TestOptions "TestOptions")

No documentation available

-   [concurrency](.././test/~/TestOptions#property_concurrency)
-   [only](.././test/~/TestOptions#property_only)
-   [plan](.././test/~/TestOptions#property_plan)
-   [signal](.././test/~/TestOptions#property_signal)
-   [skip](.././test/~/TestOptions#property_skip)
-   [timeout](.././test/~/TestOptions#property_timeout)
-   [todo](.././test/~/TestOptions#property_todo)

I

[TestShard](.././test/~/TestShard "TestShard")

No documentation available

-   [index](.././test/~/TestShard#property_index)
-   [total](.././test/~/TestShard#property_total)

N

[assert](.././test/~/assert "assert")

An object whose methods are used to configure available assertions on the `TestContext` objects in the current process. The methods from `node:assert` and snapshot testing functions are available by default.

N

[default.assert](.././test/~/default.assert "default.assert")

An object whose methods are used to configure available assertions on the `TestContext` objects in the current process. The methods from `node:assert` and snapshot testing functions are available by default.

N

[default.snapshot](.././test/~/default.snapshot "default.snapshot")

No documentation available

N

[snapshot](.././test/~/snapshot "snapshot")

No documentation available

N

[test.assert](.././test/~/test.assert "test.assert")

An object whose methods are used to configure available assertions on the `TestContext` objects in the current process. The methods from `node:assert` and snapshot testing functions are available by default.

N

[test.snapshot](.././test/~/test.snapshot "test.snapshot")

No documentation available

T

[FunctionPropertyNames](.././test/~/FunctionPropertyNames "FunctionPropertyNames")

No documentation available

T

[HookFn](.././test/~/HookFn "HookFn")

The hook function. The first argument is the context in which the hook is called. If the hook uses callbacks, the callback function is passed as the second argument.

T

[Mock](.././test/~/Mock "Mock")

No documentation available

T

[NoOpFunction](.././test/~/NoOpFunction "NoOpFunction")

No documentation available

T

[SuiteFn](.././test/~/SuiteFn "SuiteFn")

The type of a suite test function. The argument to this function is a [SuiteContext](.././test/~/SuiteContext) object.

T

[TestContextHookFn](.././test/~/TestContextHookFn "TestContextHookFn")

The hook function. The first argument is a `TestContext` object. If the hook uses callbacks, the callback function is passed as the second argument.

T

[TestFn](.././test/~/TestFn "TestFn")

The type of a function passed to [test](.././test/~/test). The first argument to this function is a [TestContext](.././test/~/TestContext) object. If the test uses callbacks, the callback function is passed as the second argument.

T

[Timer](.././test/~/Timer "Timer")

No documentation available

v

[default.mock](.././test/~/default.mock "default.mock")

No documentation available

v

[mock](.././test/~/mock "mock")

No documentation available

v

[test.mock](.././test/~/test.mock "test.mock")

No documentation available
