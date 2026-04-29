---
title: "Using Testing Library with Bun"
source: "https://bun.com/docs/guides/test/testing-library"
canonical_url: "https://bun.com/docs/guides/test/testing-library"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:21.766Z"
content_hash: "95b9f14da0f8bee1bd771aea861ad53aa0f0be140e04a3ceb70f97144e256ecf"
menu_path: ["Using Testing Library with Bun"]
section_path: []
nav_prev: {"path": "../svelte-test/index.md", "title": "import, require, and test Svelte components with bun test"}
nav_next: {"path": "../timeout/index.md", "title": "Set a per-test timeout with the Bun test runner"}
---

You can use [Testing Library](https://testing-library.com/) with Bun’s test runner.

* * *

As a prerequisite to using Testing Library you will need to install [Happy Dom](https://github.com/capricorn86/happy-dom). ([see Bun’s Happy DOM guide for more information](../happy-dom/index.md)).

terminal

```
bun add -D @happy-dom/global-registrator
```

* * *

Next you should install the Testing Library packages you are planning on using. For example, if you are setting up testing for React your installs may look like this. You will also need to install `@testing-library/jest-dom` to get matchers working later.

terminal

```
bun add -D @testing-library/react @testing-library/dom @testing-library/jest-dom
```

* * *

Next you will need to create a preload script for Happy DOM and for Testing Library. For more details about the Happy DOM setup script see [Bun’s Happy DOM guide](../happy-dom/index.md).

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)happydom.ts

```
import { GlobalRegistrator } from "@happy-dom/global-registrator";

GlobalRegistrator.register();
```

* * *

For Testing Library, you will want to extend Bun’s `expect` function with Testing Library’s matchers. Optionally, to better match the behavior of test-runners like Jest, you may want to run cleanup after each test.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)testing-library.ts

```
import { afterEach, expect } from "bun:test";
import { cleanup } from "@testing-library/react";
import * as matchers from "@testing-library/jest-dom/matchers";

expect.extend(matchers);

// Optional: cleans up `render` after each test
afterEach(() => {
  cleanup();
});
```

* * *

Next, add these preload scripts to your `bunfig.toml` (you can also have everything in a single `preload.ts` script if you prefer).

bunfig.toml

```
[test]
preload = ["./happydom.ts", "./testing-library.ts"]
```

* * *

If you are using TypeScript, you will also need to use declaration merging to get the new matcher types to show up in your editor. To do this, create a type declaration file that extends `Matchers` like this.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)matchers.d.ts

```
import { TestingLibraryMatchers } from "@testing-library/jest-dom/matchers";
import { Matchers, AsymmetricMatchers } from "bun:test";

declare module "bun:test" {
  interface Matchers<T> extends TestingLibraryMatchers<typeof expect.stringContaining, T> {}
  interface AsymmetricMatchers extends TestingLibraryMatchers {}
}
```

* * *

You should now be able to use Testing Library in your tests

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)myComponent.test.tsx

```
import { test, expect } from "bun:test";
import { screen, render } from "@testing-library/react";
import { MyComponent } from "./myComponent";

test("Can use Testing Library", () => {
  render(MyComponent);
  const myComponent = screen.getByTestId("my-component");
  expect(myComponent).toBeInTheDocument();
});
```

* * *

Refer to the [Testing Library docs](https://testing-library.com/), [Happy DOM repo](https://github.com/capricorn86/happy-dom) and [Docs > Test runner > DOM](../../../test/dom/index.md) for complete documentation on writing browser tests with Bun.
