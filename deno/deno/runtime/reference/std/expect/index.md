---
title: "@std/expect"
source: "https://docs.deno.com/runtime/reference/std/expect/"
canonical_url: "https://docs.deno.com/runtime/reference/std/expect/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:08.135Z"
content_hash: "256e682e2ee33b60ee8c4f1381cf5c6ac7b6156d87146a7ec02798d4d440b497"
menu_path: ["@std/expect"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/encoding/index.md", "title": "@std/encoding"}
nav_next: {"path": "deno/deno/runtime/reference/std/fmt/index.md", "title": "@std/fmt"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

This module provides Jest compatible expect assertion functionality.

```js
import { expect } from "@std/expect";

const x = 6 * 7;
expect(x).toEqual(42);
expect(x).not.toEqual(0);

await expect(Promise.resolve(x)).resolves.toEqual(42);
```

Currently this module supports the following functions:

*   Common matchers:
    *   `toBe`
    *   `toEqual`
    *   `toStrictEqual`
    *   `toMatch`
    *   `toMatchObject`
    *   `toBeDefined`
    *   `toBeUndefined`
    *   `toBeNull`
    *   `toBeNaN`
    *   `toBeTruthy`
    *   `toBeFalsy`
    *   `toContain`
    *   `toContainEqual`
    *   `toHaveLength`
    *   `toBeGreaterThan`
    *   `toBeGreaterThanOrEqual`
    *   `toBeLessThan`
    *   `toBeLessThanOrEqual`
    *   `toBeCloseTo`
    *   `toBeInstanceOf`
    *   `toThrow`
    *   `toHaveProperty`
    *   `toMatchSnapshot`
    *   `toMatchInlineSnapshot`
*   Mock related matchers:
    *   `toHaveBeenCalled`
    *   `toHaveBeenCalledTimes`
    *   `toHaveBeenCalledWith`
    *   `toHaveBeenLastCalledWith`
    *   `toHaveBeenNthCalledWith`
    *   `toHaveReturned`
    *   `toHaveReturnedTimes`
    *   `toHaveReturnedWith`
    *   `toHaveLastReturnedWith`
    *   `toHaveNthReturnedWith`
*   Asymmetric matchers:
    *   [`expect.anything`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.anything)
    *   [`expect.any`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.any)
    *   [`expect.arrayContaining`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.arrayContaining)
    *   [`expect.not.arrayContaining`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.not.arrayContaining)
    *   [`expect.objectContaining`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.objectContaining)
    *   [`expect.not.objectContaining`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.not.objectContaining)
    *   [`expect.closeTo`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.closeTo)
    *   [`expect.stringContaining`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.stringContaining)
    *   [`expect.not.stringContaining`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.not.stringContaining)
    *   [`expect.stringMatching`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.stringMatching)
    *   [`expect.not.stringMatching`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.not.stringMatching)
*   Utilities:
    *   [`expect.addSnapshotSerializer`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.addSnapshotSerializer)
    *   [`expect.assertions`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.assertions)
    *   `expect.addEqualityTester`
    *   [`expect.extend`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.extend)
    *   [`expect.hasAssertions`](https://jsr.io/@std/expect@1.0.18/doc/~/expect.hasAssertions)

Only these functions are still not available:

*   Matchers:
    *   `toThrowErrorMatchingSnapshot`
    *   `toThrowErrorMatchingInlineSnapshot`

The tracking issue to add support for unsupported parts of the API is [https://github.com/denoland/std/issues/3964](https://github.com/denoland/std/issues/3964).

This module is largely inspired by [x/expect](https://github.com/allain/expect) module by [Allain Lalonde](https://github.com/allain).

### Add to your project

\>\_

```sh
deno add jsr:@std/expect
```

[See all symbols in @std/expect on](https://jsr.io/@std/expect/doc)

