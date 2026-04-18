---
title: "Test runner"
source: "https://bun.com/docs/test"
canonical_url: "https://bun.com/docs/test"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:30.984Z"
content_hash: "65c97011915d1628e36ff84b25eeb72601dda218c2029a378f2dd0cd03686c62"
menu_path: ["Test runner"]
section_path: []
nav_prev: {"path": "bun/bun/docs/test/lifecycle/index.md", "title": "Lifecycle hooks"}
nav_next: {"path": "bun/bun/docs/test/reporters/index.md", "title": "Test Reporters"}
---

# run all tests or test suites with "addition" in the name
bun test --test-name-pattern addition
```

To run a specific file in the test runner, make sure the path starts with `./` or `/` to distinguish it from a filter name.

terminal

```
bun test ./test/specific-file.test.ts
```

The test runner runs all tests in a single process. It loads all `--preload` scripts (see [Lifecycle](bun/bun/docs/test/lifecycle/index.md) for details), then runs all tests. If a test fails, the test runner will exit with a non-zero exit code.

## CI/CD integration

`bun test` supports a variety of CI/CD integrations.

### GitHub Actions

`bun test` automatically detects if it’s running inside GitHub Actions and will emit GitHub Actions annotations to the console directly. No configuration is needed, other than installing `bun` in the workflow and running `bun test`.

#### How to install `bun` in a GitHub Actions workflow

To use `bun test` in a GitHub Actions workflow, add the following step:

.github/workflows/test.yml

```
jobs:
  build:
    name: build-app
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Install bun
        uses: oven-sh/setup-bun@v2
      - name: Install dependencies # (assuming your project has dependencies)
        run: bun install # You can use npm/yarn/pnpm instead if you prefer
      - name: Run tests
        run: bun test
```

From there, you’ll get GitHub Actions annotations.

### JUnit XML reports (GitLab, etc.)

To use `bun test` with a JUnit XML reporter, you can use the `--reporter=junit` in combination with `--reporter-outfile`.

terminal

```
bun test --reporter=junit --reporter-outfile=./bun.xml
```

This will continue to output to stdout/stderr as usual, and also write a JUnit XML report to the given path at the very end of the test run. JUnit XML is a popular format for reporting test results in CI/CD pipelines.

## Timeouts

Use the `--timeout` flag to specify a _per-test_ timeout in milliseconds. If a test times out, it will be marked as failed. The default value is `5000`.

terminal

```
# default value is 5000
bun test --timeout 20
```

## Concurrent test execution

By default, Bun runs all tests sequentially within each test file. You can enable concurrent execution to run async tests in parallel, significantly speeding up test suites with independent tests.

### `--concurrent` flag

Use the `--concurrent` flag to run all tests concurrently within their respective files:

terminal

```
bun test --concurrent
```

When this flag is enabled, all tests will run in parallel unless explicitly marked with `test.serial`.

### `--max-concurrency` flag

Control the maximum number of tests running simultaneously with the `--max-concurrency` flag:

terminal

```
# Limit to 4 concurrent tests
bun test --concurrent --max-concurrency 4

# Default: 20
bun test --concurrent
```

This helps prevent resource exhaustion when running many concurrent tests. The default value is 20.

### `test.concurrent`

Mark individual tests to run concurrently, even when the `--concurrent` flag is not used:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)math.test.ts

```
import { test, expect } from "bun:test";

// These tests run in parallel with each other
test.concurrent("concurrent test 1", async () => {
  await fetch("/api/endpoint1");
  expect(true).toBe(true);
});

test.concurrent("concurrent test 2", async () => {
  await fetch("/api/endpoint2");
  expect(true).toBe(true);
});

// This test runs sequentially
test("sequential test", () => {
  expect(1 + 1).toBe(2);
});
```

### `test.serial`

Force tests to run sequentially, even when the `--concurrent` flag is enabled:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)math.test.ts

```
import { test, expect } from "bun:test";

let sharedState = 0;

// These tests must run in order
test.serial("first serial test", () => {
  sharedState = 1;
  expect(sharedState).toBe(1);
});

test.serial("second serial test", () => {
  // Depends on the previous test
  expect(sharedState).toBe(1);
  sharedState = 2;
});

// This test can run concurrently if --concurrent is enabled
test("independent test", () => {
  expect(true).toBe(true);
});

// Chaining test qualifiers
test.failing.each([1, 2, 3])("chained qualifiers %d", input => {
  expect(input).toBe(0); // This test is expected to fail for each input
});
```

## Retry failed tests

Use the `--retry` flag to automatically retry failed tests up to a given number of times. If a test fails and then passes on a subsequent attempt, it is reported as passing.

terminal

```
bun test --retry 3
```

Per-test `{ retry: N }` overrides the global `--retry` value:

```
// Uses the global --retry value
test("uses global retry", () => {
  /* ... */
});

// Overrides --retry with its own value
test("custom retry", { retry: 1 }, () => {
  /* ... */
});
```

You can also set this in `bunfig.toml`:

bunfig.toml

```
[test]
retry = 3
```

## Rerun tests

Use the `--rerun-each` flag to run each test multiple times. This is useful for detecting flaky or non-deterministic test failures.

terminal

```
bun test --rerun-each 100
```

## Randomize test execution order

Use the `--randomize` flag to run tests in a random order. This helps detect tests that depend on shared state or execution order.

terminal

```
bun test --randomize
```

When using `--randomize`, the seed used for randomization will be displayed in the test summary:

terminal

```
bun test --randomize
```

```
# ... test output ...
 --seed=12345
 2 pass
 8 fail
Ran 10 tests across 2 files. [50.00ms]
```

### Reproducible random order with `--seed`

Use the `--seed` flag to specify a seed for the randomization. This allows you to reproduce the same test order when debugging order-dependent failures.

terminal

```
# Reproduce a previous randomized run
bun test --seed 123456
```

The `--seed` flag implies `--randomize`, so you don’t need to specify both. Using the same seed value will always produce the same test execution order, making it easier to debug intermittent failures caused by test interdependencies.

## Bail out with `--bail`

Use the `--bail` flag to abort the test run early after a pre-determined number of test failures. By default Bun will run all tests and report all failures, but sometimes in CI environments it’s preferable to terminate earlier to reduce CPU usage.

terminal

```
# bail after 1 failure
bun test --bail

# bail after 10 failure
bun test --bail=10
```

## Watch mode

Similar to `bun run`, you can pass the `--watch` flag to `bun test` to watch for changes and re-run tests.

terminal

```
bun test --watch
```

## Lifecycle hooks

Bun supports the following lifecycle hooks:

Hook

Description

`beforeAll`

Runs once before all tests.

`beforeEach`

Runs before each test.

`afterEach`

Runs after each test.

`afterAll`

Runs once after all tests.

These hooks can be defined inside test files, or in a separate file that is preloaded with the `--preload` flag.

terminal

```
bun test --preload ./setup.ts
```

See [Test > Lifecycle](bun/bun/docs/test/lifecycle/index.md) for complete documentation.

## Mocks

Create mock functions with the `mock` function.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)math.test.ts

```
import { test, expect, mock } from "bun:test";
const random = mock(() => Math.random());

test("random", () => {
  const val = random();
  expect(val).toBeGreaterThan(0);
  expect(random).toHaveBeenCalled();
  expect(random).toHaveBeenCalledTimes(1);
});
```

Alternatively, you can use `jest.fn()`, it behaves identically.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)math.test.ts

```
import { test, expect, mock } from "bun:test"; 
import { test, expect, jest } from "bun:test"; 

const random = mock(() => Math.random()); 
const random = jest.fn(() => Math.random()); 
```

See [Test > Mocks](bun/bun/docs/test/mocks/index.md) for complete documentation.

## Snapshot testing

Snapshots are supported by `bun test`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)math.test.ts

```
// example usage of toMatchSnapshot
import { test, expect } from "bun:test";

test("snapshot", () => {
  expect({ a: 1 }).toMatchSnapshot();
});
```

To update snapshots, use the `--update-snapshots` flag.

terminal

```
bun test --update-snapshots
```

See [Test > Snapshots](bun/bun/docs/test/snapshots/index.md) for complete documentation.

## UI & DOM testing

Bun is compatible with popular UI testing libraries:

*   [HappyDOM](https://github.com/capricorn86/happy-dom)
*   [DOM Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
*   [React Testing Library](https://testing-library.com/docs/react-testing-library/intro)

See [Test > DOM Testing](bun/bun/docs/test/dom/index.md) for complete documentation.

## Performance

Bun’s test runner is fast.

## AI Agent Integration

When using Bun’s test runner with AI coding assistants, you can enable quieter output to improve readability and reduce context noise. This feature minimizes test output verbosity while preserving essential failure information.

### Environment Variables

Set any of the following environment variables to enable AI-friendly output:

*   `CLAUDECODE=1` - For Claude Code
*   `REPL_ID=1` - For Replit
*   `AGENT=1` - Generic AI agent flag

### Behavior

When an AI agent environment is detected:

*   Only test failures are displayed in detail
*   Passing, skipped, and todo test indicators are hidden
*   Summary statistics remain intact

terminal

```
# Example: Enable quiet output for Claude Code
CLAUDECODE=1 bun test

# Still shows failures and summary, but hides verbose passing test output
```

This feature is particularly useful in AI-assisted development workflows where reduced output verbosity improves context efficiency while maintaining visibility into test failures.

* * *

## CLI Usage

```
bun test <patterns>
```

### Execution Control

\--timeout

number

default:"5000"

Set the per-test timeout in milliseconds (default 5000)

\--rerun-each

number

Re-run each test file `NUMBER` times, helps catch certain bugs

\--retry

number

Default retry count for all tests. Failed tests will be retried up to `NUMBER` times. Overridden by per-test `{ retry: N }`

\--concurrent

boolean

Treat all tests as `test.concurrent()` tests

\--randomize

boolean

Run tests in random order

\--seed

number

Set the random seed for test randomization

\--bail

number

default:"1"

Exit the test suite after `NUMBER` failures. If you do not specify a number, it defaults to 1.

\--max-concurrency

number

default:"20"

Maximum number of concurrent tests to execute at once (default 20)

### Test Filtering

\--todo

boolean

Include tests that are marked with `test.todo()`

\--test-name-pattern

string

Run only tests with a name that matches the given regex. Alias: `-t`

### Reporting

\--reporter

string

Test output reporter format. Available: `junit` (requires —reporter-outfile), `dots`. Default: console output.

\--reporter-outfile

string

Output file path for the reporter format (required with —reporter)

\--dots

boolean

Enable dots reporter. Shorthand for —reporter=dots

### Coverage

\--coverage

boolean

Generate a coverage profile

\--coverage-reporter

string

default:"text"

Report coverage in `text` and/or `lcov`. Defaults to `text`

\--coverage-dir

string

default:"coverage"

Directory for coverage files. Defaults to `coverage`

### Snapshots

\--update-snapshots

boolean

Update snapshot files. Alias: `-u`

## Examples

Run all test files:

terminal

```
bun test
```

Run all test files with “foo” or “bar” in the file name:

terminal

```
bun test foo bar
```

Run all test files, only including tests whose names includes “baz”:

terminal

```
bun test --test-name-pattern baz
```
