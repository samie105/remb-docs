---
title: "@std/testing"
source: "https://docs.deno.com/runtime/reference/std/testing/"
canonical_url: "https://docs.deno.com/runtime/reference/std/testing/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:47:53.676Z"
content_hash: "ddee6eb5726e0ba483c9c858426908abcd7769435deea6c0d8e5f4b35c40d71b"
menu_path: ["@std/testing"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/tar/index.md", "title": "@std/tar"}
nav_next: {"path": "deno/runtime/reference/std/text/index.md", "title": "@std/text"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

This package provides utilities for testing.

-   [BDD style testing](https://jsr.io/@std/testing/doc/bdd/~)
-   [Test doubles (mocking)](https://jsr.io/@std/testing/doc/mock/~)
-   [Faking time and timers](https://jsr.io/@std/testing/doc/time/~)
-   [Snapshot testing](https://jsr.io/@std/testing/doc/snapshot/~)
-   [Type assertions](https://jsr.io/@std/testing/doc/types/~)

```js
import { assertSpyCalls, spy } from "@std/testing/mock";
import { FakeTime } from "@std/testing/time";

function secondInterval(cb: () => void): number {
  return setInterval(cb, 1000);
}

Deno.test("secondInterval calls callback every second and stops after being cleared", () => {
  using time = new FakeTime();

  const cb = spy();
  const intervalId = secondInterval(cb);
  assertSpyCalls(cb, 0);
  time.tick(500);
  assertSpyCalls(cb, 0);
  time.tick(500);
  assertSpyCalls(cb, 1);
  time.tick(3500);
  assertSpyCalls(cb, 4);

  clearInterval(intervalId);
  time.tick(1000);
  assertSpyCalls(cb, 4);
});
```

### Add to your project

\>\_

```sh
deno add jsr:@std/testing
```

[See all symbols in @std/testing on](https://jsr.io/@std/testing/doc)
