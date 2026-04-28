---
title: "Spy on methods in `bun test`"
source: "https://bun.com/docs/guides/test/spy-on"
canonical_url: "https://bun.com/docs/guides/test/spy-on"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:13.224Z"
content_hash: "55d4f3ae101bc7fa019991b78904c84bea2a8c36c1f6570427d9541a974bbff6"
menu_path: ["Spy on methods in `bun test`"]
section_path: []
nav_prev: {"path": "bun/docs/guides/test/snapshot/index.md", "title": "Use snapshot testing in `bun test`"}
nav_next: {"path": "bun/docs/guides/test/svelte-test/index.md", "title": "import, require, and test Svelte components with bun test"}
---

Use the `spyOn` utility to track method calls with Bun’s test runner.

```
import { test, expect, spyOn } from "bun:test";

const leo = {
  name: "Leonardo",
  sayHi(thing: string) {
    console.log(`Sup I'm ${this.name} and I like ${thing}`);
  },
};

const spy = spyOn(leo, "sayHi");
```

* * *

Once the spy is created, it can be used to write `expect` assertions relating to method calls.

```
import { test, expect, spyOn } from "bun:test";

const leo = {
  name: "Leonardo",
  sayHi(thing: string) {
    console.log(`Sup I'm ${this.name} and I like ${thing}`);
  },
};

const spy = spyOn(leo, "sayHi");

test("turtles", () => { 
  expect(spy).toHaveBeenCalledTimes(0); 
  leo.sayHi("pizza"); 
  expect(spy).toHaveBeenCalledTimes(1); 
  expect(spy.mock.calls).toEqual([["pizza"]]); 
}); 
```

* * *

See [Docs > Test Runner > Mocks](bun/docs/test/mocks/index.md) for complete documentation on mocking with the Bun test runner.

Was this page helpful?
