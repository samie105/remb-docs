---
title: "Write browser DOM tests with Bun and happy-dom"
source: "https://bun.com/docs/guides/test/happy-dom"
canonical_url: "https://bun.com/docs/guides/test/happy-dom"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:39.725Z"
content_hash: "6e6201bce863ded029142de94228cc70d0ccb468a8e1f55bc6298fac808a073b"
menu_path: ["Write browser DOM tests with Bun and happy-dom"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/test/coverage-threshold/index.md", "title": "Set a code coverage threshold with the Bun test runner"}
nav_next: {"path": "bun/bun/docs/guides/test/migrate-from-jest/index.md", "title": "Migrate from Jest to Bun's test runner"}
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

You can write and run browser tests with Bun’s test runner in conjunction with [Happy DOM](https://github.com/capricorn86/happy-dom). Happy DOM implements mocked versions of browser APIs like `document` and `location`.

* * *

To get started, install `happy-dom`.

terminal

```
bun add -d @happy-dom/global-registrator
```

* * *

This module exports a “registrator” that injects the mocked browser APIs to the global scope.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)happydom.ts

```
import { GlobalRegistrator } from "@happy-dom/global-registrator";

GlobalRegistrator.register();
```

* * *

We need to make sure this file is executed before any of our test files. That’s a job for Bun’s built-in _preload_ functionality. Create a `bunfig.toml` file in the root of your project (if it doesn’t already exist) and add the following lines. The `./happydom.ts` file should contain the registration code above.

bunfig.toml

```
[test]
preload = "./happydom.ts"
```

* * *

Now running `bun test` inside our project will automatically execute `happydom.ts` first. We can start writing tests that use browser APIs.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)dom.test.ts

```
import { test, expect } from "bun:test";

test("set button text", () => {
  document.body.innerHTML = `<button>My button</button>`;
  const button = document.querySelector("button");
  expect(button?.innerText).toEqual("My button");
});
```

* * *

With Happy DOM properly configured, this test runs as expected.

terminal

```
bun test
```

```

dom.test.ts:
✓ set button text [0.82ms]

 1 pass
 0 fail
 1 expect() calls
Ran 1 tests across 1 files. 1 total [125.00ms]
```

* * *

Refer to the [Happy DOM repo](https://github.com/capricorn86/happy-dom) and [Docs > Test runner > DOM](/docs/test/dom) for complete documentation on writing browser tests with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/test/happy-dom.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/test/happy-dom>)

[

Using Testing Library with Bun

Previous

](/docs/guides/test/testing-library)[

import, require, and test Svelte components with bun test

Next

](/docs/guides/test/svelte-test)

