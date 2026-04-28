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
nav_prev: {"path": "bun/docs/test/dates-times/index.md", "title": "Dates and times"}
nav_next: {"path": "bun/docs/test/dom/index.md", "title": "DOM testing"}
---

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
