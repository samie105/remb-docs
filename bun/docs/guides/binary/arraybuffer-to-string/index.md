---
title: "Convert an ArrayBuffer to a string"
source: "https://bun.com/docs/guides/binary/arraybuffer-to-string"
canonical_url: "https://bun.com/docs/guides/binary/arraybuffer-to-string"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:32.968Z"
content_hash: "a76926b5fb3912aabd48e895bf2bde9616ed8ba80d5abf9eafaff2796064c1ba"
menu_path: ["Convert an ArrayBuffer to a string"]
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

Bun implements the Web-standard [`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder) class for converting between binary data types and strings.

```
const buf = new ArrayBuffer(64);
const decoder = new TextDecoder();
const str = decoder.decode(buf);
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/arraybuffer-to-string.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/arraybuffer-to-string>)

[

Extract social share images and Open Graph tags

Previous

](/docs/guides/html-rewriter/extract-social-meta)[

Convert an ArrayBuffer to a Buffer

Next

](/docs/guides/binary/arraybuffer-to-buffer)
