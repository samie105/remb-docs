---
title: "Convert a DataView to a string"
source: "https://bun.com/docs/guides/binary/dataview-to-string"
canonical_url: "https://bun.com/docs/guides/binary/dataview-to-string"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:09.881Z"
content_hash: "c2f23c2f9adaf6701fd967d1373c8bc068ff34a4a7cfa93ef8d9bfe938b6c969"
menu_path: ["Convert a DataView to a string"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/binary/buffer-to-typedarray/index.md", "title": "Convert a Buffer to a Uint8Array"}
nav_next: {"path": "bun/bun/docs/guides/binary/typedarray-to-blob/index.md", "title": "Convert a Uint8Array to a Blob"}
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

If a [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) contains ASCII-encoded text, you can convert it to a string using the [`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder) class.

```
const dv: DataView = ...;
const decoder = new TextDecoder();
const str = decoder.decode(dv);
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/dataview-to-string.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/dataview-to-string>)

[

Convert a Uint8Array to a ReadableStream

Previous

](/docs/guides/binary/typedarray-to-readablestream)[

Convert a ReadableStream to a string

Next

](/docs/guides/streams/to-string)


