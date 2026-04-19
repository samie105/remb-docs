---
title: "Listen for CTRL+C"
source: "https://bun.com/docs/guides/process/ctrl-c"
canonical_url: "https://bun.com/docs/guides/process/ctrl-c"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:39.318Z"
content_hash: "09bec31f513c68d0ac85cd6c9a80f0c7f2389856cffc9b13d3a2adaba2b7c437"
menu_path: ["Listen for CTRL+C"]
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

The `ctrl+c` shortcut sends an _interrupt signal_ to the running process. This signal can be intercepted by listening for the `SIGINT` event. If you want to close the process, you must explicitly call `process.exit()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)process.ts

```
process.on("SIGINT", () => {
  console.log("Ctrl-C was pressed");
  process.exit();
});
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/process/ctrl-c.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/process/ctrl-c>)

[

Spawn a child process and communicate using IPC

Previous

](/docs/guides/process/ipc)[

Listen to OS signals

Next

](/docs/guides/process/os-signals)
