---
title: "Runtime behavior"
source: "https://bun.com/docs/test/runtime-behavior"
canonical_url: "https://bun.com/docs/test/runtime-behavior"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:39.724Z"
content_hash: "2e7010b25744287f8e0e758d071ed37fb88a73236a6facaa8cb189d5e48c0edb"
menu_path: ["Runtime behavior"]
section_path: []
nav_prev: {"path": "bun/bun/docs/test/mocks/index.md", "title": "Mocks"}
nav_next: {"path": "bun/bun/docs/test/snapshots/index.md", "title": "Snapshots"}
---

# Reduces memory usage for the test runner VM
bun test --smol
```

### Debugging

terminal

```
# Attaches the debugger to the test runner process
bun test --inspect
bun test --inspect-brk
```

### Module Loading

terminal

```
# Runs scripts before test files (useful for global setup/mocks)
bun test --preload ./setup.ts

# Sets compile-time constants
bun test --define "process.env.API_URL='http://localhost:3000'"

# Configures custom loaders
bun test --loader .special:special-loader

# Uses a different tsconfig
bun test --tsconfig-override ./test-tsconfig.json

# Sets package.json conditions for module resolution
bun test --conditions development

# Loads environment variables for tests
bun test --env-file .env.test
```

```
# Affect any network requests or auto-installs during test execution
bun test --prefer-offline
bun test --frozen-lockfile
```

## Watch and Hot Reloading

### Watch Mode

When running `bun test` with the `--watch` flag, the test runner will watch for file changes and re-run affected tests.

terminal

```
bun test --watch
```

The test runner is smart about which tests to re-run:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)math.test.ts

```
import { add } from "./math.js";
import { test, expect } from "bun:test";

test("addition", () => {
  expect(add(2, 3)).toBe(5);
});
```

If you modify `math.js`, only `math.test.ts` will re-run, not all tests.

### Hot Reloading

The `--hot` flag provides similar functionality but is more aggressive about trying to preserve state between runs:

terminal

```
bun test --hot
```

For most test scenarios, `--watch` is the recommended option as it provides better isolation between test runs.

## Global Variables

The following globals are automatically available in test files without importing (though they can be imported from `bun:test` if preferred):

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
// All of these are available globally
test("global test function", () => {
  expect(true).toBe(true);
});

describe("global describe", () => {
  beforeAll(() => {
    // global beforeAll
  });

  it("global it function", () => {
    // it is an alias for test
  });
});

// Jest compatibility
jest.fn();

// Vitest compatibility
vi.fn();
```

You can also import them explicitly if you prefer:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test, it, describe, expect, beforeAll, beforeEach, afterAll, afterEach, jest, vi } from "bun:test";
```

## Process Integration

### Exit Codes

`bun test` uses standard exit codes:

*   `0`: All tests passed, no unhandled errors
*   `1`: Test failures occurred
*   `>1`: Number of unhandled errors (even if tests passed)

### Signal Handling

The test runner properly handles common signals:

terminal

```
# Gracefully stops test execution
kill -SIGTERM <test-process-pid>

# Immediately stops test execution
kill -SIGKILL <test-process-pid>
```

### Environment Detection

Bun automatically detects certain environments and adjusts behavior:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
// GitHub Actions detection
if (process.env.GITHUB_ACTIONS) {
  // Bun automatically emits GitHub Actions annotations
}

// CI detection
if (process.env.CI) {
  // Certain behaviors may be adjusted for CI environments
}
```

## Performance Considerations

### Single Process

The test runner runs all tests in a single process by default. This provides:

*   **Faster startup** - No need to spawn multiple processes
*   **Shared memory** - Efficient resource usage
*   **Simple debugging** - All tests in one process

However, this means:

*   Tests share global state (use lifecycle hooks to clean up)
*   One test crash can affect others
*   No true parallelization of individual tests

### Memory Management

terminal

```
# Monitor memory usage
bun test --smol  # Reduces memory footprint

# For large test suites, consider splitting files
bun test src/unit/
bun test src/integration/
```

### Test Isolation

Since tests run in the same process, ensure proper cleanup:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { afterEach } from "bun:test";

afterEach(() => {
  // Clean up global state
  global.myGlobalVar = undefined;
  delete process.env.TEST_VAR;

  // Reset modules if needed
  jest.resetModules();
});
```
