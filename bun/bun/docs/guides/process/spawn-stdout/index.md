---
title: "Read stdout from a child process"
source: "https://bun.com/docs/guides/process/spawn-stdout"
canonical_url: "https://bun.com/docs/guides/process/spawn-stdout"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:09.197Z"
content_hash: "3eea037c605aaedcd43b402c935a9a39c7729560a72625ed6c844b76e132c38a"
menu_path: ["Read stdout from a child process"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/process/spawn-stderr/index.md", "title": "Read stderr from a child process"}
nav_next: {"path": "bun/bun/docs/guides/process/stdin/index.md", "title": "Read from stdin"}
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

When using [`Bun.spawn()`](/docs/runtime/child-process), the `stdout` of the child process can be consumed as a `ReadableStream` via `proc.stdout`.

```
const proc = Bun.spawn(["echo", "hello"]);

const output = await proc.stdout.text();
output; // => "hello"
```

* * *

To instead pipe the `stdout` of the child process to `stdout` of the parent process, set “inherit”.

```
const proc = Bun.spawn(["echo", "hello"], {
  stdout: "inherit",
});
```

* * *

See [Docs > API > Child processes](/docs/runtime/child-process) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/process/spawn-stdout.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/process/spawn-stdout>)

[

Spawn a child process

Previous

](/docs/guides/process/spawn)[

Read stderr from a child process

Next

](/docs/guides/process/spawn-stderr)
