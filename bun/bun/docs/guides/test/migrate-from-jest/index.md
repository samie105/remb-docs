---
title: "Migrate from Jest to Bun's test runner"
source: "https://bun.com/docs/guides/test/migrate-from-jest"
canonical_url: "https://bun.com/docs/guides/test/migrate-from-jest"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:43.113Z"
content_hash: "3fd6e6579302f197feae8d49bde81a3a807bd8e0e81e393211a0907c77142247"
menu_path: ["Migrate from Jest to Bun's test runner"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/test/happy-dom/index.md", "title": "Write browser DOM tests with Bun and happy-dom"}
nav_next: {"path": "bun/bun/docs/guides/test/mock-clock/index.md", "title": "Set the system time in Bun's test runner"}
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

In many cases, Bun’s test runner can run Jest test suites with no code changes. Just run `bun test` instead of `npx jest`, `yarn test`, etc.

terminal

```
npx jest
yarn test
bun test
```

* * *

There’s often no need for code changes.

*   Bun internally re-writes imports from `@jest/globals` to use the `bun:test` equivalents.
*   If you’re relying on Jest to inject `test`, `expect`, etc. as globals, Bun does that too.

But if you’d rather switch to the `bun:test` imports, you can do that too.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test, expect } from "@jest/globals"; 
import { test, expect } from "bun:test"; 
```

* * *

Since Bun v1.2.19, you can enable **TypeScript support** for global test functions with a single triple-slash directive. This makes migrating from Jest even easier since you only need to add the directive once in your entire project: Add this directive to _just one file_ in your project, such as:

*   A `global.d.ts` file in your project root
*   Your test `preload.ts` setup file (if using `preload` in bunfig.toml)
*   Any single `.ts` file that TypeScript includes in your compilation

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)global.d.ts

```
/// <reference types="bun-types/test-globals" />
```

* * *

Once added, all test files in your project automatically get TypeScript support for Jest globals:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)math.test.ts

```
describe("my test suite", () => {
  test("should work", () => {
    expect(1 + 1).toBe(2);
  });

  beforeAll(() => {
    // setup code
  });

  afterEach(() => {
    // cleanup code
  });
});
```

* * *

Bun implements the vast majority of Jest’s matchers, but compatibility isn’t 100% yet. Refer to the full compatibility table at [Docs > Test runner > Writing tests](/docs/test/writing-tests#matchers). Some notable missing features:

*   `expect().toHaveReturned()`

* * *

If you’re using `testEnvironment: "jsdom"` to run your tests in a browser-like environment, you should follow the [DOM testing with Bun and happy-dom](/docs/guides/test/happy-dom) guide to inject browser APIs into the global scope. This guide relies on [`happy-dom`](https://github.com/capricorn86/happy-dom), which is a leaner and faster alternative to [`jsdom`](https://github.com/jsdom/jsdom). At the moment jsdom does not work in Bun due to its internal use of V8 APIs. Track support for it [here](https://github.com/oven-sh/bun/issues/3554).

bunfig.toml

```
[test]
preload = ["./happy-dom.ts"]
```

* * *

Replace `bail` in your Jest config with the `--bail` CLI flag.

terminal

```
bun test --bail=3
```

* * *

Replace `collectCoverage` with the `--coverage` CLI flag.

terminal

```
bun test --coverage
```

* * *

Replace `testTimeout` with the `--test-timeout` CLI flag.

terminal

```
bun test --timeout 10000
```

* * *

Many other flags become irrelevant or obsolete when using `bun test`.

*   `transform` — Bun supports TypeScript & JSX. Other file types can be configured with [Plugins](/docs/runtime/plugins).
*   `extensionsToTreatAsEsm`
*   `haste` — Bun uses it’s own internal source maps
*   `watchman`, `watchPlugins`, `watchPathIgnorePatterns` — use `--watch` to run tests in watch mode
*   `verbose` — set `logLevel: "debug"` in [`bunfig.toml`](/docs/runtime/bunfig#loglevel)

* * *

Settings that aren’t mentioned here are not supported or have no equivalent. Please [file a feature request](https://github.com/oven-sh/bun) if something important is missing.

* * *

See also:

*   [Mark a test as a todo](/docs/guides/test/todo-tests)
*   [Docs > Test runner > Writing tests](/docs/test/writing-tests)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/migrate-from-jest.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/migrate-from-jest>)

[

Run tests in watch mode with Bun

Previous

](/docs/guides/test/watch-mode)[

Mock functions in \`bun test\`

Next

](/docs/guides/test/mock-functions)
