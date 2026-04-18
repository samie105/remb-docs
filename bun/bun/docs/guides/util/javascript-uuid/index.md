---
title: "Generate a UUID"
source: "https://bun.com/docs/guides/util/javascript-uuid"
canonical_url: "https://bun.com/docs/guides/util/javascript-uuid"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:06.315Z"
content_hash: "bffcf039dca66f16b9b2a1c2df5d406cd91cf734951cc6a32debde8350b3701b"
menu_path: ["Generate a UUID"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/util/import-meta-path/index.md", "title": "Get the absolute path of the current file"}
nav_next: {"path": "bun/bun/docs/guides/util/main/index.md", "title": "Get the absolute path to the current entrypoint"}
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

Use `crypto.randomUUID()` to generate a UUID v4. This API works in Bun, Node.js, and browsers. It requires no dependencies.

```
crypto.randomUUID();
// => "123e4567-e89b-42d3-a456-426614174000"
```

* * *

In Bun, you can also use `Bun.randomUUIDv7()` to generate a [UUID v7](https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-01.html).

```
Bun.randomUUIDv7();
// => "0196a000-bb12-7000-905e-8039f5d5b206"
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/javascript-uuid.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/javascript-uuid>)

[

Hash a password

Previous

](/docs/guides/util/hash-a-password)[

Encode and decode base64 strings

Next

](/docs/guides/util/base64)


