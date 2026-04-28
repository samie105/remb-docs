---
title: "Set the system time in Bun's test runner"
source: "https://bun.com/docs/guides/test/mock-clock"
canonical_url: "https://bun.com/docs/guides/test/mock-clock"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:46.157Z"
content_hash: "2dfd0130d6f0c00587215fcd44741512356fdce29dcdbce7c6549efd7c4d5c7b"
menu_path: ["Set the system time in Bun's test runner"]
section_path: []
nav_prev: {"path": "bun/docs/guides/test/migrate-from-jest/index.md", "title": "Migrate from Jest to Bun's test runner"}
nav_next: {"path": "bun/docs/guides/test/mock-functions/index.md", "title": "Mock functions in `bun test`"}
---

Bun’s test runner supports setting the system time programmatically with the `setSystemTime` function.

```
import { test, expect, setSystemTime } from "bun:test";

test("party like it's 1999", () => {
  const date = new Date("1999-01-01T00:00:00.000Z");
  setSystemTime(date); // it's now January 1, 1999

  const now = new Date();
  expect(now.getFullYear()).toBe(1999);
  expect(now.getMonth()).toBe(0);
  expect(now.getDate()).toBe(1);
});
```

* * *

The `setSystemTime` function is commonly used on conjunction with [Lifecycle Hooks](bun/docs/test/lifecycle/index.md) to configure a testing environment with a deterministic “fake clock”.

```
import { test, expect, beforeAll, setSystemTime } from "bun:test";

beforeAll(() => {
  const date = new Date("1999-01-01T00:00:00.000Z");
  setSystemTime(date); // it's now January 1, 1999
});

// tests...
```

* * *

To reset the system clock to the actual time, call `setSystemTime` with no arguments.

```
import { test, expect, beforeAll, setSystemTime } from "bun:test";

setSystemTime(); // reset to actual time
```

* * *

See [Docs > Test Runner > Date and time](bun/docs/test/dates-times/index.md) for complete documentation on mocking with the Bun test runner.
