---
title: "Test configuration"
source: "https://bun.com/docs/test/configuration"
canonical_url: "https://bun.com/docs/test/configuration"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:22.262Z"
content_hash: "12be50da3082cdb3b091daff251d45a33e03916d3a9fac2862703d0017d17467"
menu_path: ["Test configuration"]
section_path: []
nav_prev: {"path": "bun/bun/docs/test/discovery/index.md", "title": "Finding tests"}
nav_next: {"path": "bun/bun/docs/test/dom/index.md", "title": "DOM testing"}
---

# Options go here
```

## Test Discovery

### root

The `root` option specifies a root directory for test discovery, overriding the default behavior of scanning from the project root.

bunfig.toml

```
[test]
root = "src"  # Only scan for tests in the src directory
```

This is useful when you want to:

*   Limit test discovery to specific directories
*   Exclude certain parts of your project from test scanning
*   Organize tests in a specific subdirectory structure

#### Examples

bunfig.toml

```
[test]
# Only run tests in the src directory
root = "src"

# Run tests in a specific test directory
root = "tests"

# Run tests in multiple specific directories (not currently supported - use patterns instead)
# root = ["src", "lib"]  # This syntax is not supported
```

### Preload Scripts

Load scripts before running tests using the `preload` option:

bunfig.toml

```
[test]
preload = ["./test-setup.ts", "./global-mocks.ts"]
```

This is equivalent to using `--preload` on the command line:

terminal

```
bun test --preload ./test-setup.ts --preload ./global-mocks.ts
```

#### Common Preload Use Cases

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test-setup.ts

```
// Global test setup
import { beforeAll, afterAll } from "bun:test";

beforeAll(() => {
  // Set up test database
  setupTestDatabase();
});

afterAll(() => {
  // Clean up
  cleanupTestDatabase();
});
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)global-mocks.ts

```
// Global mocks
import { mock } from "bun:test";

// Mock environment variables
process.env.NODE_ENV = "test";
process.env.API_URL = "http://localhost:3001";

// Mock external dependencies
mock.module("./external-api", () => ({
  fetchData: mock(() => Promise.resolve({ data: "test" })),
}));
```

### Path Ignore Patterns

Exclude files and directories from test discovery entirely using glob patterns. Unlike `coveragePathIgnorePatterns` which only affects coverage reports, `pathIgnorePatterns` prevents matching paths from being discovered and run as tests. This is useful when your project contains submodules, vendored code, or other directories with `*.test.ts` files that you don’t want `bun test` to pick up.

bunfig.toml

```
[test]
# Single pattern
pathIgnorePatterns = "vendor/**"

# Multiple patterns
pathIgnorePatterns = [
  "vendor/**",
  "submodules/**",
  "fixtures/**"
]
```

This is equivalent to using `--path-ignore-patterns` on the command line:

terminal

```
bun test --path-ignore-patterns 'vendor/**' --path-ignore-patterns 'fixtures/**'
```

Directories matching a pattern are pruned during scanning, so their contents are never traversed. This means ignoring a large directory tree is efficient — Bun won’t spend time reading files inside it.

#### Common Use Cases

bunfig.toml

```
[test]
pathIgnorePatterns = [
  # Git submodules with their own test suites
  "submodules/**",

  # Vendored dependencies
  "vendor/**",
  "third-party/**",

  # Test fixtures that look like tests but aren't
  "fixtures/**",
  "**/test-data/**",

  # Integration / E2E tests you want to run separately
  "**/integration/**",
  "e2e/**"
]
```

## Timeouts

### Default Timeout

Set the default timeout for all tests:

bunfig.toml

```
[test]
timeout = 10000  # 10 seconds (default is 5000ms)
```

This applies to all tests unless overridden by individual test timeouts:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
// This test will use the default timeout from bunfig.toml
test("uses default timeout", () => {
  // test implementation
});

// This test overrides the default timeout
test("custom timeout", () => {
  // test implementation
}, 30000); // 30 seconds
```

## Reporters

### JUnit Reporter

Configure the JUnit reporter output file path directly in the config file:

bunfig.toml

```
[test.reporter]
junit = "path/to/junit.xml"  # Output path for JUnit XML report
```

This complements the `--reporter=junit` and `--reporter-outfile` CLI flags:

terminal

```
# Equivalent command line usage
bun test --reporter=junit --reporter-outfile=./junit.xml
```

#### Multiple Reporters

You can use multiple reporters simultaneously:

terminal

```
# CLI approach
bun test --reporter=junit --reporter-outfile=./junit.xml

# Config file approach
```

bunfig.toml

```
[test.reporter]
junit = "./reports/junit.xml"

[test]
# Also enable coverage reporting
coverage = true
coverageReporter = ["text", "lcov"]
```

## Memory Usage

### smol Mode

Enable the `--smol` memory-saving mode specifically for the test runner:

bunfig.toml

```
[test]
smol = true  # Reduce memory usage during test runs
```

This is equivalent to using the `--smol` flag on the command line:

terminal

```
bun test --smol
```

The `smol` mode reduces memory usage by:

*   Using less memory for the JavaScript heap
*   Being more aggressive about garbage collection
*   Reducing buffer sizes where possible

This is useful for:

*   CI environments with limited memory
*   Large test suites that consume significant memory
*   Development environments with memory constraints

## Test execution

### concurrentTestGlob

Automatically run test files matching a glob pattern with concurrent test execution enabled. This is useful for gradually migrating test suites to concurrent execution or for running specific test types concurrently.

bunfig.toml

```
[test]
concurrentTestGlob = "**/concurrent-*.test.ts"  # Run files matching this pattern concurrently
```

Test files matching this pattern will behave as if the `--concurrent` flag was passed, running all tests within those files concurrently. This allows you to:

*   Gradually migrate your test suite to concurrent execution
*   Run integration tests concurrently while keeping unit tests sequential
*   Separate fast concurrent tests from tests that require sequential execution

The `--concurrent` CLI flag will override this setting when specified, forcing all tests to run concurrently regardless of the glob pattern.

#### randomize

Run tests in random order to identify tests with hidden dependencies:

bunfig.toml

```
[test]
randomize = true
```

#### seed

Specify a seed for reproducible random test order. Requires `randomize = true`:

bunfig.toml

```
[test]
randomize = true
seed = 2444615283
```

#### retry

Default retry count for all tests. Failed tests will be retried up to this many times. Per-test `{ retry: N }` overrides this value. Default `0` (no retries).

bunfig.toml

```
[test]
retry = 3
```

The `--retry` CLI flag will override this setting when specified.

#### rerunEach

Re-run each test file multiple times to identify flaky tests:

bunfig.toml

```
[test]
rerunEach = 3
```

## Coverage Options

### Basic Coverage Settings

bunfig.toml

```
[test]
# Enable coverage by default
coverage = true

# Set coverage reporter
coverageReporter = ["text", "lcov"]

# Set coverage output directory
coverageDir = "./coverage"
```

### Skip Test Files from Coverage

Exclude files matching test patterns (e.g., `*.test.ts`) from the coverage report:

bunfig.toml

```
[test]
coverageSkipTestFiles = true  # Exclude test files from coverage reports
```

### Coverage Thresholds

The coverage threshold can be specified either as a number or as an object with specific thresholds:

bunfig.toml

```
[test]
# Simple threshold - applies to lines, functions, and statements
coverageThreshold = 0.8

# Detailed thresholds
coverageThreshold = { lines = 0.9, functions = 0.8, statements = 0.85 }
```

Setting any of these enables `fail_on_low_coverage`, causing the test run to fail if coverage is below the threshold.

#### Threshold Examples

bunfig.toml

```
[test]
# Require 90% coverage across the board
coverageThreshold = 0.9

# Different requirements for different metrics
coverageThreshold = {
  lines = 0.85,      # 85% line coverage
  functions = 0.90,  # 90% function coverage
  statements = 0.80  # 80% statement coverage
}
```

### Coverage Path Ignore Patterns

Exclude specific files or file patterns from coverage reports using glob patterns:

bunfig.toml

```
[test]
# Single pattern
coveragePathIgnorePatterns = "**/*.spec.ts"

# Multiple patterns
coveragePathIgnorePatterns = [
  "**/*.spec.ts",
  "**/*.test.ts",
  "src/utils/**",
  "*.config.js",
  "generated/**",
  "vendor/**"
]
```

Files matching any of these patterns will be excluded from coverage calculation and reporting. See the [coverage documentation](bun/bun/docs/test/code-coverage/index.md) for more details and examples.

#### Common Ignore Patterns

bunfig.toml

```
[test]
coveragePathIgnorePatterns = [
  # Test files
  "**/*.test.ts",
  "**/*.spec.ts",
  "**/*.e2e.ts",

  # Configuration files
  "*.config.js",
  "*.config.ts",
  "webpack.config.*",
  "vite.config.*",

  # Build output
  "dist/**",
  "build/**",
  ".next/**",

  # Generated code
  "generated/**",
  "**/*.generated.ts",

  # Vendor/third-party
  "vendor/**",
  "third-party/**",

  # Utilities that don't need testing
  "src/utils/constants.ts",
  "src/types/**"
]
```

### Sourcemap Handling

Internally, Bun transpiles every file. That means code coverage must also go through sourcemaps before they can be reported. We expose this as a flag to allow you to opt out of this behavior, but it will be confusing because during the transpilation process, Bun may move code around and change variable names. This option is mostly useful for debugging coverage issues.

bunfig.toml

```
[test]
coverageIgnoreSourcemaps = true  # Don't use sourcemaps for coverage analysis
```

## Install Settings Inheritance

The `bun test` command inherits relevant network and installation configuration (registry, cafile, prefer, exact, etc.) from the `[install]` section of `bunfig.toml`. This is important if tests need to interact with private registries or require specific install behaviors triggered during the test run.

bunfig.toml

```
[install]
# These settings are inherited by bun test
registry = "https://npm.company.com/"
exact = true
prefer = "offline"

[test]
# Test-specific configuration
coverage = true
timeout = 10000
```

## Environment Variables

Environment variables for tests should be set using `.env` files. Bun automatically loads `.env` files from your project root. For test-specific variables, create a `.env.test` file:

.env.test

```
NODE_ENV=test
DATABASE_URL=postgresql://localhost:5432/test_db
LOG_LEVEL=error
```

Then load it with `--env-file`:

terminal

```
bun test --env-file=.env.test
```

## Complete Configuration Example

Here’s a comprehensive example showing all available test configuration options:

bunfig.toml

```
[install]
# Install settings inherited by tests
registry = "https://registry.npmjs.org/"
exact = true

[test]
# Test discovery
root = "src"
preload = ["./test-setup.ts", "./global-mocks.ts"]
pathIgnorePatterns = ["vendor/**", "submodules/**"]

# Execution settings
timeout = 10000
smol = true

# Coverage configuration
coverage = true
coverageReporter = ["text", "lcov"]
coverageDir = "./coverage"
coverageThreshold = { lines = 0.85, functions = 0.90, statements = 0.80 }
coverageSkipTestFiles = true
coveragePathIgnorePatterns = [
  "**/*.spec.ts",
  "src/utils/**",
  "*.config.js",
  "generated/**"
]

# Advanced coverage settings
coverageIgnoreSourcemaps = false

# Reporter configuration
[test.reporter]
junit = "./reports/junit.xml"
```

## CLI Override Behavior

Command-line options always override configuration file settings:

bunfig.toml

```
[test]
timeout = 5000
coverage = false
```

terminal

```
# These CLI flags override the config file
bun test --timeout 10000 --coverage
# timeout will be 10000ms and coverage will be enabled
```

## Conditional Configuration

You can use different configurations for different environments:

bunfig.toml

```
[test]
# Default test configuration
coverage = false
timeout = 5000

# Override for CI environment
[test.ci]
coverage = true
coverageThreshold = 0.8
timeout = 30000
```

Then in CI:

terminal

```
# Use CI-specific settings
bun test --config=ci
```

## Validation and Troubleshooting

### Invalid Configuration

Bun will warn about invalid configuration options:

bunfig.toml

```
[test]
invalidOption = true  # This will generate a warning
```

### Common Configuration Issues

1.  **Path Resolution**: Relative paths in config are resolved relative to the config file location
2.  **Pattern Matching**: Glob patterns use standard glob syntax
3.  **Type Mismatches**: Ensure numeric values are not quoted unless they should be strings

bunfig.toml

```
[test]
# Correct
timeout = 10000

# Incorrect - will be treated as string
timeout = "10000"
```

### Debugging Configuration

To see what configuration is being used:

terminal

```
# Show effective configuration
bun test --dry-run

# Verbose output to see configuration loading
bun test --verbose
```

