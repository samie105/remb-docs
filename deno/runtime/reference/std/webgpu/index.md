---
title: "@std/webgpu"
source: "https://docs.deno.com/runtime/reference/std/webgpu/"
canonical_url: "https://docs.deno.com/runtime/reference/std/webgpu/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:49:10.041Z"
content_hash: "41790bc83183de57f77e8cc9441921bf36fc599cf13a1869f31f86475d8a3ce4"
menu_path: ["@std/webgpu"]
section_path: []
content_language: "en"
nav_prev: {"path": "../uuid/index.md", "title": "@std/uuid"}
nav_next: {"path": "../yaml/index.md", "title": "@std/yaml"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

Utilities for interacting with the [WebGPU API](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API).

```js
import { createTextureWithData } from "@std/webgpu";

const adapter = await navigator.gpu.requestAdapter();
const device = await adapter?.requestDevice()!;

createTextureWithData(device, {
  format: "bgra8unorm-srgb",
  size: {
    width: 3,
    height: 2,
  },
  usage: GPUTextureUsage.COPY_SRC,
}, new Uint8Array([1, 1, 1, 1, 1, 1, 1]));
```

### Add to your project

\>\_

```sh
deno add jsr:@std/webgpu
```

[See all symbols in @std/webgpu on](https://jsr.io/@std/webgpu/doc)
