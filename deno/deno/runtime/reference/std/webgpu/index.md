---
title: "@std/webgpu"
source: "https://docs.deno.com/runtime/reference/std/webgpu/"
canonical_url: "https://docs.deno.com/runtime/reference/std/webgpu/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:58.057Z"
content_hash: "020b01a95cf8a1f2e52ab9a45aadd6b391fe36617b463a41b43e368391253c36"
menu_path: ["@std/webgpu"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/uuid/index.md", "title": "@std/uuid"}
nav_next: {"path": "deno/deno/runtime/reference/std/yaml/index.md", "title": "@std/yaml"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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
