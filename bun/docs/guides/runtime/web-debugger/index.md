---
title: "Debugging Bun with the web debugger"
source: "https://bun.com/docs/guides/runtime/web-debugger"
canonical_url: "https://bun.com/docs/guides/runtime/web-debugger"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:33.554Z"
content_hash: "ec276e992e44eecf1a3e0dfe94d8af78f4a46c1052eff864b5d1b07eb30259cf"
menu_path: ["Debugging Bun with the web debugger"]
section_path: []
nav_prev: {"path": "bun/docs/guides/runtime/vscode-debugger/index.md", "title": "Debugging Bun with the VS Code extension"}
nav_next: {"path": "bun/docs/guides/streams/node-readable-to-arraybuffer/index.md", "title": "Convert a Node.js Readable to an ArrayBuffer"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](../../../index.md)[Package Manager

](../../../pm/cli/install/index.md)[Bundler

](../../../bundler/index.md)[Test Runner

](../../../test/index.md)[Guides

](../../index.md)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](../../../feedback/index.md)

Bun speaks the [WebKit Inspector Protocol](https://github.com/oven-sh/bun/blob/main/packages/bun-inspector-protocol/src/protocol/jsc/index.d.ts). To enable debugging when running code with Bun, use the `--inspect` flag. For demonstration purposes, consider the following web server.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
Bun.serve({
  fetch(req) {
    console.log(req.url);
    return new Response("Hello, world!");
  },
});
```

* * *

Let’s run this file with the `--inspect` flag. This automatically starts a WebSocket server on an available port that can be used to introspect the running Bun process. Various debugging tools can connect to this server to provide an interactive debugging experience. Bun hosts a web-based debugger at [debug.bun.sh](https://debug.bun.sh). It is a modified version of WebKit’s [Web Inspector Interface](https://webkit.org/web-inspector/web-inspector-interface/), which will look familiar to Safari users.

terminal

```
bun --inspect server.ts
```

```
------------------ Bun Inspector ------------------
Listening at:
  ws://localhost:6499/0tqxs9exrgrm

Inspect in browser:
  https://debug.bun.sh/#localhost:6499/0tqxs9exrgrm
------------------ Bun Inspector ------------------
```

* * *

Open the provided `debug.bun.sh` URL in your browser to start a debugging session. From this interface, you’ll be able to view the source code of the running file, view and set breakpoints, and execute code with the built-in console.

![Screenshot of Bun debugger, Console
tab](https://github.com/oven-sh/bun/assets/3084745/e6a976a8-80cc-4394-8925-539025cc025d)

* * *

Let’s set a breakpoint. Navigate to the Sources tab; you should see the code from earlier. Click on the line number `3` to set a breakpoint on our `console.log(req.url)` statement.

![screenshot of Bun debugger](https://github.com/oven-sh/bun/assets/3084745/3b69c7e9-25ff-4f9d-acc4-caa736862935)

* * *

Then visit [`http://localhost:3000`](http://localhost:3000) in your web browser. This will send an HTTP request to our `localhost` web server. It will seem like the page isn’t loading. Why? Because the program has paused execution at the breakpoint we set earlier. Note how the UI has changed.

![screenshot of Bun debugger](https://github.com/oven-sh/bun/assets/3084745/8b565e58-5445-4061-9bc4-f41090dfe769)

* * *

At this point there’s a lot we can do to introspect the current execution environment. We can use the console at the bottom to run arbitrary code in the context of the program, with full access to the variables in scope at our breakpoint.

![Bun debugger console](https://github.com/oven-sh/bun/assets/3084745/f4312b76-48ba-4a7d-b3b6-6205968ac681)

* * *

On the right side of the Sources pane, we can see all local variables currently in scope, and drill down to see their properties and methods. Here, we’re inspecting the `req` variable.

![Bun debugger variables panel](https://github.com/oven-sh/bun/assets/3084745/63d7f843-5180-489c-aa94-87c486e68646)

* * *

In the upper left of the Sources pane, we can control the execution of the program.

![Bun debugger controls](https://github.com/oven-sh/bun/assets/3084745/41b76deb-7371-4461-9d5d-81b5a6d2f7a4)

* * *

Here’s a cheat sheet explaining the functions of the control flow buttons.

*   _Continue script execution_ — continue running the program until the next breakpoint or exception.
*   _Step over_ — The program will continue to the next line.
*   _Step into_ — If the current statement contains a function call, the debugger will “step into” the called function.
*   _Step out_ — If the current statement is a function call, the debugger will finish executing the call, then “step out” of the function to the location where it was called.

![Debugger control buttons cheat
sheet](https://github-production-user-asset-6210df.s3.amazonaws.com/3084745/261510346-6a94441c-75d3-413a-99a7-efa62365f83d.png)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/web-debugger.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/web-debugger>)

[

Debugging Bun with the VS Code extension

Previous

](../vscode-debugger/index.md)[

Inspect memory usage using V8 heap snapshots

Next

](../heap-snapshot/index.md)

![Screenshot of Bun debugger, Console
tab](https://github.com/oven-sh/bun/assets/3084745/e6a976a8-80cc-4394-8925-539025cc025d)

![screenshot of Bun debugger](https://github.com/oven-sh/bun/assets/3084745/3b69c7e9-25ff-4f9d-acc4-caa736862935)

![screenshot of Bun debugger](https://github.com/oven-sh/bun/assets/3084745/8b565e58-5445-4061-9bc4-f41090dfe769)

![Bun debugger console](https://github.com/oven-sh/bun/assets/3084745/f4312b76-48ba-4a7d-b3b6-6205968ac681)

![Bun debugger variables panel](https://github.com/oven-sh/bun/assets/3084745/63d7f843-5180-489c-aa94-87c486e68646)

![Bun debugger controls](https://github.com/oven-sh/bun/assets/3084745/41b76deb-7371-4461-9d5d-81b5a6d2f7a4)

![Debugger control buttons cheat
sheet](https://github-production-user-asset-6210df.s3.amazonaws.com/3084745/261510346-6a94441c-75d3-413a-99a7-efa62365f83d.png)
