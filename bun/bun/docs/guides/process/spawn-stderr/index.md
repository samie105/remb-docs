---
title: "Read stderr from a child process"
source: "https://bun.com/docs/guides/process/spawn-stderr"
canonical_url: "https://bun.com/docs/guides/process/spawn-stderr"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:07.640Z"
content_hash: "d055a259cd5db692e0e1c7a4ab45901ed6fd11e1e179b3fbc94a73a44bc1fbe8"
menu_path: ["Read stderr from a child process"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/process/spawn/index.md", "title": "Spawn a child process"}
nav_next: {"path": "bun/bun/docs/guides/process/spawn-stdout/index.md", "title": "Read stdout from a child process"}
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

When using [`Bun.spawn()`](/docs/runtime/child-process), the child process inherits the `stderr` of the spawning process. If instead you’d prefer to read and handle `stderr`, set the `stderr` option to `"pipe"`.

```
const proc = Bun.spawn(["echo", "hello"], {
  stderr: "pipe",
});

proc.stderr; // => ReadableStream
```

* * *

To read `stderr` until the child process exits, use .text()

```
const proc = Bun.spawn(["echo", "hello"], {
  stderr: "pipe",
});

const errors: string = await proc.stderr.text();
if (errors) {
  // handle errors
}
```

* * *

See [Docs > API > Child processes](/docs/runtime/child-process) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/process/spawn-stderr.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/process/spawn-stderr>)

[

Read stdout from a child process

Previous

](/docs/guides/process/spawn-stdout)[

Parse command-line arguments

Next

](/docs/guides/process/argv)

