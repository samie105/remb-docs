---
title: "Mock functions in `bun test`"
source: "https://bun.com/docs/guides/test/mock-functions"
canonical_url: "https://bun.com/docs/guides/test/mock-functions"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:51.728Z"
content_hash: "8a3eb708b87c46b6ddbcc465bfa5e91baf92cf7eab2111de7183fd217a341bb9"
menu_path: ["Mock functions in `bun test`"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/test/mock-clock/index.md", "title": "Set the system time in Bun's test runner"}
nav_next: {"path": "bun/bun/docs/guides/test/rerun-each/index.md", "title": "Re-run tests multiple times with the Bun test runner"}
---

Create mocks with the `mock` function from `bun:test`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test, expect, mock } from "bun:test";

const random = mock(() => Math.random());
```

* * *

The mock function can accept arguments.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test, expect, mock } from "bun:test";

const random = mock((multiplier: number) => multiplier * Math.random());
```

* * *

The result of `mock()` is a new function that’s been decorated with some additional properties.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { mock } from "bun:test";

const random = mock((multiplier: number) => multiplier * Math.random());

random(2);
random(10);

random.mock.calls;
// [[ 2 ], [ 10 ]]

random.mock.results;
//  [
//    { type: "return", value: 0.6533907460954099 },
//    { type: "return", value: 0.6452713933037312 }
//  ]
```

* * *

These extra properties make it possible to write `expect` assertions about usage of the mock function, including how many times it was called, the arguments, and the return values.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test, expect, mock } from "bun:test";

const random = mock((multiplier: number) => multiplier * Math.random());

test("random", async () => {
  const a = random(1);
  const b = random(2);
  const c = random(3);

  expect(random).toHaveBeenCalled();
  expect(random).toHaveBeenCalledTimes(3);
  expect(random.mock.calls).toEqual([[1], [2], [3]]);
  expect(random.mock.results[0]).toEqual({ type: "return", value: a });
});
```

* * *

See [Docs > Test Runner > Mocks](bun/bun/docs/test/mocks/index.md) for complete documentation on mocking with the Bun test runner.


