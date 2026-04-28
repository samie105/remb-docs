---
title: "Spawn a child process and communicate using IPC"
source: "https://bun.com/docs/guides/process/ipc"
canonical_url: "https://bun.com/docs/guides/process/ipc"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:51.848Z"
content_hash: "7bf4fbbdea0941d3749b3b9e02ece7b6ab86bf76a61f507bb09c2a3972679120"
menu_path: ["Spawn a child process and communicate using IPC"]
section_path: []
nav_prev: {"path": "bun/docs/guides/process/ctrl-c/index.md", "title": "Listen for CTRL+C"}
nav_next: {"path": "bun/docs/guides/process/nanoseconds/index.md", "title": "Get the process uptime in nanoseconds"}
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

Use [`Bun.spawn()`](/docs/runtime/child-process) to spawn a child process. When spawning a second `bun` process, you can open a direct inter-process communication (IPC) channel between the two processes.

This API is only compatible with other `bun` processes. Use `process.execPath` to get a path to the currently running `bun` executable.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)parent.ts

```
const child = Bun.spawn(["bun", "child.ts"], {
  ipc(message) {
    /**
     * The message received from the sub process
     **/
  },
});
```

* * *

The parent process can send messages to the subprocess using the `.send()` method on the returned `Subprocess` instance. A reference to the sending subprocess is also available as the second argument in the `ipc` handler.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)parent.ts

```
const childProc = Bun.spawn(["bun", "child.ts"], {
  ipc(message, childProc) {
    /**
     * The message received from the sub process
     **/
    childProc.send("Respond to child");
  },
});

childProc.send("I am your father"); // The parent can send messages to the child as well
```

* * *

Meanwhile the child process can send messages to its parent using with `process.send()` and receive messages with `process.on("message")`. This is the same API used for `child_process.fork()` in Node.js.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)child.ts

```
process.send("Hello from child as string");
process.send({ message: "Hello from child as object" });

process.on("message", message => {
  // print message from parent
  console.log(message);
});
```

* * *

All messages are serialized using the JSC `serialize` API, which allows for the same set of [transferrable types](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Transferable_objects) supported by `postMessage` and `structuredClone`, including strings, typed arrays, streams, and objects.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)child.ts

```
// send a string
process.send("Hello from child as string");

// send an object
process.send({ message: "Hello from child as object" });
```

* * *

See [Docs > API > Child processes](/docs/runtime/child-process) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/process/ipc.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/process/ipc>)

[

Read from stdin

Previous

](/docs/guides/process/stdin)[

Listen for CTRL+C

Next

](/docs/guides/process/ctrl-c)
