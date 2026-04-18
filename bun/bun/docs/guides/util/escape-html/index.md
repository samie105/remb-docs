---
title: "Escape an HTML string"
source: "https://bun.com/docs/guides/util/escape-html"
canonical_url: "https://bun.com/docs/guides/util/escape-html"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:51.456Z"
content_hash: "5645a0e0aafe2cc0ef1c5ec25b4e88921533aea1c529f57bfe64f9a76275d391"
menu_path: ["Escape an HTML string"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/util/entrypoint/index.md", "title": "Check if the current file is the entrypoint"}
nav_next: {"path": "bun/bun/docs/guides/util/file-url-to-path/index.md", "title": "Convert a file URL to an absolute path"}
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

The `Bun.escapeHTML()` utility can be used to escape HTML characters in a string. The following replacements are made.

*   `"` becomes `"&quot;"`
*   `&` becomes `"&amp;"`
*   `'` becomes `"&#x27;"`
*   `<` becomes `"&lt;"`
*   `>` becomes `"&gt;"`

This function is optimized for large input. Non-string types will be converted to a string before escaping.

```
Bun.escapeHTML("<script>alert('Hello World!')</script>");
// &lt;script&gt;alert(&#x27;Hello World!&#x27;)&lt;&#x2F;script&gt;
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/escape-html.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/escape-html>)

[

Compress and decompress data with DEFLATE

Previous

](/docs/guides/util/deflate)[

Check if two objects are deeply equal

Next

](/docs/guides/util/deep-equals)

