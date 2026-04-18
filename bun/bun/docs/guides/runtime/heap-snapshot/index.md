---
title: "Inspect memory usage using V8 heap snapshots"
source: "https://bun.com/docs/guides/runtime/heap-snapshot"
canonical_url: "https://bun.com/docs/guides/runtime/heap-snapshot"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:36.568Z"
content_hash: "2c7e288a7b2733a3bc615afd4e85aa9eeab7eb64b87d517852e7d3b050b85708"
menu_path: ["Inspect memory usage using V8 heap snapshots"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/runtime/delete-file/index.md", "title": "Delete files"}
nav_next: {"path": "bun/bun/docs/guides/runtime/import-html/index.md", "title": "Import a HTML file as text"}
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

Bun implements V8’s heap snapshot API, which allows you to create snapshots of the heap at runtime. This helps debug memory leaks in your JavaScript/TypeScript application.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)snapshot.ts

```
import v8 from "node:v8";

// Creates a heap snapshot file with an auto-generated name
const snapshotPath = v8.writeHeapSnapshot();
console.log(`Heap snapshot written to: ${snapshotPath}`);
```

* * *

## 

[​

](#inspect-memory-in-chrome-devtools)

Inspect memory in Chrome DevTools

To view V8 heap snapshots in Chrome DevTools:

1.  Open Chrome DevTools (F12 or right-click and select “Inspect”)
2.  Go to the “Memory” tab
3.  Click the “Load” button (folder icon)
4.  Select your `.heapsnapshot` file

![Chrome DevTools Memory Tab](https://mintcdn.com/bun-1dd33a4e/o4ey1PfJcT885lrd/images/chrome-devtools-memory.png?fit=max&auto=format&n=o4ey1PfJcT885lrd&q=85&s=8f11aeea8ad1f70974bb963f83c4decf)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/heap-snapshot.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/heap-snapshot>)

[

Debugging Bun with the web debugger

Previous

](/docs/guides/runtime/web-debugger)[

Build-time constants with --define

Next

](/docs/guides/runtime/build-time-constants)


