---
title: "Listen to OS signals"
source: "https://bun.com/docs/guides/process/os-signals"
canonical_url: "https://bun.com/docs/guides/process/os-signals"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:55.079Z"
content_hash: "8d81996bbc0be912ae4d94e56ab4930bd3761b1d577205280f30c7c5ae7cd331"
menu_path: ["Listen to OS signals"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/process/ipc/index.md", "title": "Spawn a child process and communicate using IPC"}
nav_next: {"path": "bun/bun/docs/guides/process/spawn/index.md", "title": "Spawn a child process"}
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

Bun supports the Node.js `process` global, including the `process.on()` method for listening to OS signals.

```
process.on("SIGINT", () => {
  console.log("Received SIGINT");
});
```

* * *

If you don’t know which signal to listen for, you listen to the [`"beforeExit"`](https://nodejs.org/api/process.html#event-beforeexit) and [`"exit"`](https://nodejs.org/api/process.html#event-exit) events.

```
process.on("beforeExit", code => {
  console.log(`Event loop is empty!`);
});

process.on("exit", code => {
  console.log(`Process is exiting with code ${code}`);
});
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/process/os-signals.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/process/os-signals>)

[

Listen for CTRL+C

Previous

](/docs/guides/process/ctrl-c)[

Get the process uptime in nanoseconds

Next

](/docs/guides/process/nanoseconds)

