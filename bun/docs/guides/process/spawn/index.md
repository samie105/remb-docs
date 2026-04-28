---
title: "Spawn a child process"
source: "https://bun.com/docs/guides/process/spawn"
canonical_url: "https://bun.com/docs/guides/process/spawn"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:00.729Z"
content_hash: "5928c21b5e33e855caa5f81cb392e58d5b7fbf3e0364e5bd26cb282e47c209b3"
menu_path: ["Spawn a child process"]
section_path: []
nav_prev: {"path": "bun/docs/guides/process/os-signals/index.md", "title": "Listen to OS signals"}
nav_next: {"path": "bun/docs/guides/process/spawn-stderr/index.md", "title": "Read stderr from a child process"}
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

Use [`Bun.spawn()`](/docs/runtime/child-process) to spawn a child process.

```
const proc = Bun.spawn(["echo", "hello"]);

// await completion
await proc.exited;
```

* * *

The second argument accepts a configuration object.

```
const proc = Bun.spawn(["echo", "Hello, world!"], {
  cwd: "/tmp",
  env: { FOO: "bar" },
  onExit(proc, exitCode, signalCode, error) {
    // exit handler
  },
});
```

* * *

By default, the `stdout` of the child process can be consumed as a `ReadableStream` using `proc.stdout`.

```
const proc = Bun.spawn(["echo", "hello"]);

const output = await proc.stdout.text();
output; // => "hello\n"
```

* * *

See [Docs > API > Child processes](/docs/runtime/child-process) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/process/spawn.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/process/spawn>)

[

Enable compression for WebSocket messages

Previous

](/docs/guides/websocket/compression)[

Read stdout from a child process

Next

](/docs/guides/process/spawn-stdout)
