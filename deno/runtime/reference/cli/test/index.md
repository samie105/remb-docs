---
title: "deno test"
source: "https://docs.deno.com/runtime/reference/cli/test/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/test/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:33:33.758Z"
content_hash: "2eafd70fa34afb152404b851f3df8d385bcca74400c507b5b1c5ce6b34dae903"
menu_path: ["deno test"]
section_path: []
content_language: "en"
---
**On this page**

-   [Running tests](#running-tests)
-   [Permissions](#permissions)
-   [Watch mode](#watch-mode)
-   [Parallel execution](#parallel-execution)
-   [Code coverage](#code-coverage)
-   [Reporters](#reporters)
-   [Randomize order](#randomize-order)
-   [Leak detection](#leak-detection)
-   [Testing code in documentation](#testing-code-in-documentation)
-   [Type checking options](#type-checking-options)
-   [Dependency management options](#dependency-management-options)
-   [Options](#options)
-   [Debugging options](#debugging-options)
-   [Testing options](#testing-options)
-   [File watching options](#file-watching-options)

Deno ships with a built-in test runner using the [`Deno.test()`](/api/deno/~/Deno.test) API. To learn how to write tests, see the [Testing fundamentals](/runtime/fundamentals/testing/) guide. For assertions, see [`@std/assert`](/runtime/reference/std/assert/) and [`@std/expect`](/runtime/reference/std/expect/).

## Running tests

Run all tests in the current directory and subdirectories:

\>\_

```sh
deno test
```

Run tests in specific files:

\>\_

```sh
deno test src/fetch_test.ts src/signal_test.ts
```

Run tests matching a glob pattern:

\>\_

```sh
deno test src/*.test.ts
```

Run tests whose name matches a string or pattern:

\>\_

```sh
deno test --filter "database"
deno test --filter "/^connect.*/"
```

Skip type-checking:

\>\_

```sh
deno test --no-check
```

## Permissions

Tests run with the same [permission model](/runtime/fundamentals/security/) as `deno run`. Grant permissions for your test suite:

\>\_

```sh
deno test --allow-read --allow-net
```

## Watch mode

Re-run tests automatically when files change:

\>\_

```sh
deno test --watch
```

## Parallel execution

Run test files across multiple worker threads:

\>\_

```sh
deno test --parallel
```

By default, `--parallel` uses the number of available CPUs. Use `DENO_JOBS=<N>` to control the number of threads:

\>\_

```sh
DENO_JOBS=4 deno test --parallel
```

## Code coverage

Collect coverage data and generate a report:

\>\_

```sh
deno test --coverage
```

This writes raw coverage data to a `coverage/` directory. To generate a summary from existing coverage data, use [`deno coverage`](/runtime/reference/cli/coverage/):

\>\_

```sh
deno coverage coverage/
```

You can also output an `lcov` report for use with external tools:

\>\_

```sh
deno coverage --lcov coverage/ > coverage.lcov
```

## Reporters

Choose an output format with `--reporter`:

\>\_

```sh
deno test --reporter=dot
deno test --reporter=tap
```

Write a JUnit XML report for CI systems:

\>\_

```sh
deno test --junit-path=report.xml
```

## Randomize order

Shuffle the order tests run in to catch hidden dependencies between tests:

\>\_

```sh
deno test --shuffle
```

## Leak detection

Trace the source of leaked async operations, timers, or resources:

\>\_

```sh
deno test --trace-leaks
```

## Testing code in documentation

Evaluate code blocks in JSDoc and Markdown files as tests:

\>\_

```sh
deno test --doc
```

See [Testing code in docs](/runtime/reference/documentation/) for details.

Command line usage:

```
deno test [OPTIONS] [files]... [-- [SCRIPT_ARG]...]
```

Run tests using Deno's built-in test runner.

Evaluate the given modules, run all tests declared with `Deno.test()` and report results to standard output:

```
deno test src/fetch_test.ts src/signal_test.ts
```

Directory arguments are expanded to all contained files matching the glob `{*_,*.,}test.{js,mjs,ts,mts,jsx,tsx}` or `**/__tests__/**`:

```
deno test src/
```

## Type checking options

`--check`<CHECK\_TYPE>optional

Set type-checking behavior. This subcommand type-checks local modules by default, so adding `--check` is redundant If the value of "all" is supplied, remote modules will be included. Alternatively, the 'deno check' subcommand can be used.

`--no-check`<NO\_CHECK\_TYPE>optional

Skip type-checking. If the value of "remote" is supplied, diagnostic errors from remote modules will be ignored.

## Dependency management options

`--cached-only`

Require that remote dependencies are already cached.

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`[--import-map](< https://docs.deno.com/runtime/manual/basics/import_maps>)`<FILE>

Load import map file from local file or remote URL.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.

`--no-npm`

Do not resolve npm modules.

`--no-remote`

Do not resolve remote modules.

`--node-modules-dir`<MODE>optional

Sets the node modules management mode for npm packages.

`--reload, -r`<CACHE\_BLOCKLIST>optional

Reload source code cache (recompile TypeScript) no value Reload everything jsr:@std/http/file-server,jsr:@std/assert/assert-equals Reloads specific modules npm: Reload all npm modules npm:chalk Reload specific npm module.

`--vendor`<vendor>optional

Toggles local vendor folder usage for remote modules and a node\_modules folder for npm packages.

## Options

`--allow-scripts`<PACKAGE>optional

Allow running npm lifecycle scripts for the given packages Note: Scripts will only be executed when using a node\_modules directory (`--node-modules-dir`).

`--cert`<FILE>

Load certificate authority from PEM encoded file.

`[--conditions](< https://docs.deno.com/go/conditional-exports>)`<conditions>

Use this argument to specify custom conditions for npm package exports. You can also use DENO\_CONDITIONS env var. .

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--env-file`<FILE>optional

Load environment variables from local file Only the first environment variable with a given key is used. Existing process environment variables are not overwritten, so if variables with the same names already exist in the environment, their values will be preserved. Where multiple declarations for the same environment variable exist in your .env file, the first one encountered is applied. This is determined by the order of the files you pass as arguments.

`--ext`<ext>

Set content type of the supplied file.

`--hide-stacktraces`

Hide stack traces for errors in failure test results.

`--ignore`<ignore>

Ignore files.

`--location`<HREF>

Value of globalThis.location used by some web APIs.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--no-config`

Disable automatic loading of the configuration file.

`--parallel`

Run test modules in parallel. Parallelism defaults to the number of available CPUs or the value of the DENO\_JOBS environment variable.

`--preload`<FILE>

A list of files that will be executed before the main module.

`--require`<FILE>

A list of CommonJS modules that will be executed before the main module.

`--seed`<NUMBER>

Set the random number generator seed.

`--v8-flags`<V8\_FLAGS>optional

To see a list of all available flags use `--v8-flags=--help` Flags can also be set via the DENO\_V8\_FLAGS environment variable. Any flags set with this flag are appended after the DENO\_V8\_FLAGS environment variable.

## Debugging options

`--inspect`<HOST\_PORT>optional

Activate inspector on host:port \[default: 127.0.0.1:9229\]. Host and port are optional. Using port 0 will assign a random free port.

`--inspect-brk`<HOST\_PORT>optional

Activate inspector on host:port, wait for debugger to connect and break at the start of user script.

`--inspect-wait`<HOST\_PORT>optional

Activate inspector on host:port and wait for debugger to connect before running user code.

## Testing options

`--clean`

Empty the temporary coverage profile data directory before running tests. Note: running multiple `deno test` --clean\`\` calls in series or parallel for the same coverage directory may cause race conditions.

`--coverage`<DIR>optional

Collect coverage profile data into DIR. If DIR is not specified, it uses 'coverage/'. This option can also be set via the DENO\_COVERAGE\_DIR environment variable.

`--coverage-raw-data-only`

Only collect raw coverage data, without generating a report.

`--doc`

Evaluate code blocks in JSDoc and Markdown.

`--fail-fast`<N>optional

Stop after N errors. Defaults to stopping after first failure.

`--filter`<filter>

Run tests with this string or regexp pattern in the test name.

`--junit-path`<PATH>

Write a JUnit XML test report to PATH. Use '-' to write to stdout which is the default when PATH is not provided.

`--no-run`

Cache test modules, but don't run tests.

`--permit-no-files`

Don't return an error code if no files were found.

`--reporter`<reporter>

Select reporter to use. Default to 'pretty'.

`--shuffle`<NUMBER>optional

Shuffle the order in which the tests are run.

`--trace-leaks`

Enable tracing of leaks. Useful when debugging leaking ops in test, but impacts test execution time.

## File watching options

`--no-clear-screen`

Do not clear terminal screen when under watch mode.

`--watch`<FILES>optional

Watch for file changes and restart process automatically. Local files from entry point module graph are watched by default. Additional paths might be watched by passing them as arguments to this flag.

`--watch-exclude`<FILES>optional

Exclude provided files/patterns from watch mode.
