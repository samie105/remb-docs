---
title: "Read a file to a Uint8Array"
source: "https://bun.com/docs/guides/read-file/uint8array"
canonical_url: "https://bun.com/docs/guides/read-file/uint8array"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:52.433Z"
content_hash: "94e70a797ecf176faf11e4673f2d2f9a1bf0116379a55bed5d8eddb81f7190b4"
menu_path: ["Read a file to a Uint8Array"]
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

The `Bun.file()` function accepts a path and returns a `BunFile` instance. The `BunFile` class extends `Blob` and allows you to lazily read the file in a variety of formats. To read the file into a `Uint8Array` instance, retrieve the contents of the `BunFile` with `.bytes()`.

```
const path = "/path/to/package.json";
const file = Bun.file(path);

const byteArray = await file.bytes();

byteArray[0]; // first byteArray
byteArray.length; // length of byteArray
```

* * *

Refer to [API > Binary data > Typed arrays](/docs/runtime/binary-data#typedarray) for more information on working with `Uint8Array` and other binary data formats in Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/read-file/uint8array.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/read-file/uint8array>)

[

Read a file to a Buffer

Previous

](/docs/guides/read-file/buffer)[

Read a file to an ArrayBuffer

Next

](/docs/guides/read-file/arraybuffer)
