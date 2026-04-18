---
title: "Watch Mode"
source: "https://bun.com/docs/runtime/watch-mode"
canonical_url: "https://bun.com/docs/runtime/watch-mode"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:01.132Z"
content_hash: "a3094a26a13e6fce000909ce08dca8703d472ed6e0ced837a4bc6758f559ba61"
menu_path: ["Watch Mode"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/transpiler/index.md", "title": "Transpiler"}
nav_next: {"path": "bun/bun/docs/runtime/web-apis/index.md", "title": "Web APIs"}
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

Bun supports two kinds of automatic reloading via CLI flags:

*   `--watch` mode, which hard restarts Bun’s process when imported files change.
*   `--hot` mode, which soft reloads the code (without restarting the process) when imported files change.

* * *

## 

[​

](#watch-mode)

`--watch` mode

Watch mode can be used with `bun test` or when running TypeScript, JSX, and JavaScript files. To run a file in `--watch` mode:

terminal

```
bun --watch index.tsx
```

To run your tests in `--watch` mode:

terminal

```
bun --watch test
```

In `--watch` mode, Bun keeps track of all imported files and watches them for changes. When a change is detected, Bun restarts the process, preserving the same set of CLI arguments and environment variables used in the initial run. If Bun crashes, `--watch` will attempt to automatically restart the process.

**⚡️ Reloads are fast.** The filesystem watchers you’re probably used to have several layers of libraries wrapping the native APIs or worse, rely on polling.Instead, Bun uses operating system native filesystem watcher APIs like kqueue or inotify to detect changes to files. Bun also applies several optimizations to scale to larger projects (such as setting a high rlimit for file descriptors, statically allocated file path buffers, reuse file descriptors when possible, etc).

The following examples show Bun live-reloading a file as it is edited, with VSCode configured to save the file [on each keystroke](https://code.visualstudio.com/docs/editor/codebasics#_save-auto-save).

terminal

```
bun run --watch watchy.tsx
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)watchy.tsx

```
import { serve } from "bun";

console.log("I restarted at:", Date.now());

serve({
  port: 4003,
  fetch(request) {
    return new Response("Sup");
  },
});
```

In this example, Bun is

![bun watch gif](https://user-images.githubusercontent.com/709451/228439002-7b9fad11-0db2-4e48-b82d-2b88c8625625.gif)

Running `bun test` in watch mode and `save-on-keypress` enabled:

terminal

```
bun --watch test
```

![bun test gif](https://user-images.githubusercontent.com/709451/228396976-38a23864-4a1d-4c96-87cc-04e5181bf459.gif)

The **`--no-clear-screen`** flag is useful in scenarios where you don’t want the terminal to clear, such as when running multiple `bun build --watch` commands simultaneously using tools like `concurrently`. Without this flag, the output of one instance could clear the output of others, potentially hiding errors from one instance beneath the output of another. The `--no-clear-screen` flag, similar to TypeScript’s `--preserveWatchOutput`, prevents this issue. It can be used in combination with `--watch`, for example: `bun build --watch --no-clear-screen`.

* * *

## 

[​

](#hot-mode)

`--hot` mode

Use `bun --hot` to enable hot reloading when executing code with Bun. This is distinct from `--watch` mode in that Bun does not hard-restart the entire process. Instead, it detects code changes and updates its internal module cache with the new code.

This is not the same as hot reloading in the browser! Many frameworks provide a “hot reloading” experience, where you can edit & save your frontend code (say, a React component) and see the changes reflected in the browser without refreshing the page. Bun’s `--hot` is the server-side equivalent of this experience. To get hot reloading in the browser, use a framework like [Vite](https://vite.dev).

terminal

```
bun --hot server.ts
```

Starting from the entrypoint (`server.ts` in the example above), Bun builds a registry of all imported source files (excluding those in `node_modules`) and watches them for changes. When a change is detected, Bun performs a “soft reload”. All files are re-evaluated, but all global state (notably, the `globalThis` object) is persisted.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
// make TypeScript happy
declare global {
  var count: number;
}

globalThis.count ??= 0;
console.log(`Reloaded ${globalThis.count} times`);
globalThis.count++;

// prevent `bun run` from exiting
setInterval(function () {}, 1000000);
```

If you run this file with `bun --hot server.ts`, you’ll see the reload count increment every time you save the file.

terminal

```
bun --hot index.ts
```

```
Reloaded 1 times
Reloaded 2 times
Reloaded 3 times
```

Traditional file watchers like `nodemon` restart the entire process, so HTTP servers and other stateful objects are lost. By contrast, `bun --hot` is able to reflect the updated code without restarting the process.

### 

[​

](#http-servers)

HTTP servers

This makes it possible, for instance, to update your HTTP request handler without shutting down the server itself. When you save the file, your HTTP server will be reloaded with the updated code without the process being restarted. This results in seriously fast refresh speeds.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
globalThis.count ??= 0;
globalThis.count++;

Bun.serve({
  fetch(req: Request) {
    return new Response(`Reloaded ${globalThis.count} times`);
  },
  port: 3000,
});
```

**Note** — In a future version of Bun, support for Vite’s `import.meta.hot` is planned to enable better lifecycle management for hot reloading and to align with the ecosystem.

Implementation details

On hot reload, Bun:

*   Resets the internal `require` cache and ES module registry (`Loader.registry`)
*   Runs the garbage collector synchronously (to minimize memory leaks, at the cost of runtime performance)
*   Re-transpiles all of your code from scratch (including sourcemaps)
*   Re-evaluates the code with JavaScriptCore

This implementation isn’t particularly optimized. It re-transpiles files that haven’t changed. It makes no attempt at incremental compilation. It’s a starting point.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/watch-mode.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/watch-mode>)

[

Bun Runtime

Previous

](/docs/runtime)[

Debugging

Next

](/docs/runtime/debugger)

![bun watch gif](https://user-images.githubusercontent.com/709451/228439002-7b9fad11-0db2-4e48-b82d-2b88c8625625.gif)

![bun test gif](https://user-images.githubusercontent.com/709451/228396976-38a23864-4a1d-4c96-87cc-04e5181bf459.gif)


