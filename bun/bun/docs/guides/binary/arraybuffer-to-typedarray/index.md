---
title: "Convert an ArrayBuffer to a Uint8Array"
source: "https://bun.com/docs/guides/binary/arraybuffer-to-typedarray"
canonical_url: "https://bun.com/docs/guides/binary/arraybuffer-to-typedarray"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:28.675Z"
content_hash: "f84b968a29dee1d2c1c6f47d5266468131c69e44f747b10b5b8413bef3d7c9ee"
menu_path: ["Convert an ArrayBuffer to a Uint8Array"]
section_path: []
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

A `Uint8Array` is a _typed array_, meaning it is a mechanism for viewing the data in an underlying `ArrayBuffer`.

```
const buffer = new ArrayBuffer(64);
const arr = new Uint8Array(buffer);
```

* * *

Instances of other typed arrays can be created similarly.

```
const buffer = new ArrayBuffer(64);

const arr1 = new Uint8Array(buffer);
const arr2 = new Uint16Array(buffer);
const arr3 = new Uint32Array(buffer);
const arr4 = new Float32Array(buffer);
const arr5 = new Float64Array(buffer);
const arr6 = new BigInt64Array(buffer);
const arr7 = new BigUint64Array(buffer);
```

* * *

To create a typed array that only views a portion of the underlying buffer, pass the offset and length to the constructor.

```
const buffer = new ArrayBuffer(64);
const arr = new Uint8Array(buffer, 0, 16); // view first 16 bytes
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/arraybuffer-to-typedarray.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/arraybuffer-to-typedarray>)

[

Convert an ArrayBuffer to an array of numbers

Previous

](/docs/guides/binary/arraybuffer-to-array)[

Convert a Buffer to a string

Next

](/docs/guides/binary/buffer-to-string)
