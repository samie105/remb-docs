---
title: "import, require, and test Svelte components with bun test"
source: "https://bun.com/docs/guides/test/svelte-test"
canonical_url: "https://bun.com/docs/guides/test/svelte-test"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:17.962Z"
content_hash: "f5eb121eae7adad5bcfe6097c7b89468eee4240af4fe4f2410177dfa84f3784c"
menu_path: ["import, require, and test Svelte components with bun test"]
section_path: []
nav_prev: {"path": "bun/docs/guides/test/spy-on/index.md", "title": "Spy on methods in `bun test`"}
nav_next: {"path": "bun/docs/guides/test/testing-library/index.md", "title": "Using Testing Library with Bun"}
---

# Tell Bun to load this plugin before your tests run
preload = ["./svelte-loader.ts"]

# This also works:
# test.preload = ["./svelte-loader.ts"]
```

* * *

Add an example `.svelte` file in your project.

Counter.svelte

```
<script>
  export let initialCount = 0;
  let count = initialCount;
</script>

<button on:click="{()" ="">(count += 1)}>+1</button>
```

* * *

Now you can `import` or `require` `*.svelte` files in your tests, and it will load the Svelte component as a JavaScript module.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)hello-svelte.test.ts

```
import { test, expect } from "bun:test";
import { render, fireEvent } from "@testing-library/svelte";
import Counter from "./Counter.svelte";

test("Counter increments when clicked", async () => {
  const { getByText, component } = render(Counter);
  const button = getByText("+1");

  // Initial state
  expect(component.$$.ctx[0]).toBe(0); // initialCount is the first prop

  // Click the increment button
  await fireEvent.click(button);

  // Check the new state
  expect(component.$$.ctx[0]).toBe(1);
});
```

* * *

Use `bun test` to run your tests.

terminal

```
bun test
```
