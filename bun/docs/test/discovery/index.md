---
title: "Finding tests"
source: "https://bun.com/docs/test/discovery"
canonical_url: "https://bun.com/docs/test/discovery"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:20.543Z"
content_hash: "e47a67f768fa88f6eb3611c72fdd510c7039a3a346aeb3de47a872cbc47fe248"
menu_path: ["Finding tests"]
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

bun test’s file discovery mechanism determines which files to run as tests. Understanding how it works helps you structure your test files effectively.

## 

[​

](#default-discovery-logic)

Default Discovery Logic

By default, `bun test` recursively searches the project directory for files that match specific patterns:

*   `*.test.{js|jsx|ts|tsx}` - Files ending with `.test.js`, `.test.jsx`, `.test.ts`, or `.test.tsx`
*   `*_test.{js|jsx|ts|tsx}` - Files ending with `_test.js`, `_test.jsx`, `_test.ts`, or `_test.tsx`
*   `*.spec.{js|jsx|ts|tsx}` - Files ending with `.spec.js`, `.spec.jsx`, `.spec.ts`, or `.spec.tsx`
*   `*_spec.{js|jsx|ts|tsx}` - Files ending with `_spec.js`, `_spec.jsx`, `_spec.ts`, or `_spec.tsx`

## 

[​

](#exclusions)

Exclusions

By default, Bun test ignores:

*   `node_modules` directories
*   Hidden directories (those starting with a period `.`)
*   Files that don’t have JavaScript-like extensions (based on available loaders)

## 

[​

](#customizing-test-discovery)

Customizing Test Discovery

### 

[​

](#position-arguments-as-filters)

Position Arguments as Filters

You can filter which test files run by passing additional positional arguments to `bun test`:

terminal

```
bun test <filter> <filter> ...
```

Any test file with a path that contains one of the filters will run. These filters are simple substring matches, not glob patterns. For example, to run all tests in a `utils` directory:

terminal

```
bun test utils
```

This would match files like `src/utils/string.test.ts` and `lib/utils/array_test.js`.

### 

[​

](#specifying-exact-file-paths)

Specifying Exact File Paths

To run a specific file in the test runner, make sure the path starts with `./` or `/` to distinguish it from a filter name:

terminal

```
bun test ./test/specific-file.test.ts
```

### 

[​

](#filter-by-test-name)

Filter by Test Name

To filter tests by name rather than file path, use the `-t`/`--test-name-pattern` flag with a regex pattern:

terminal

```
# run all tests with "addition" in the name
bun test --test-name-pattern addition
```

The pattern is matched against a concatenated string of the test name prepended with the labels of all its parent describe blocks, separated by spaces. For example, a test defined as:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)math.test.ts

```
describe("Math", () => {
  describe("operations", () => {
    test("should add correctly", () => {
      // ...
    });
  });
});
```

Would be matched against the string “Math operations should add correctly”.

### 

[​

](#changing-the-root-directory)

Changing the Root Directory

By default, Bun looks for test files starting from the current working directory. You can change this with the `root` option in your `bunfig.toml`:

bunfig.toml

```
[test]
root = "src"  # Only scan for tests in the src directory
```

## 

[​

](#execution-order)

Execution Order

Tests are run in the following order:

1.  Test files are executed sequentially (not in parallel)
2.  Within each file, tests run sequentially based on their definition order

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/test/discovery.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /test/discovery>)

[

Runtime behavior

Previous

](/docs/test/runtime-behavior)[

Lifecycle hooks

Next

](/docs/test/lifecycle)
