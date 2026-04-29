---
title: "Welcome to Bun"
source: "https://bun.com/docs"
canonical_url: "https://bun.com/docs"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:15.229Z"
content_hash: "93681463043e48077973443a9ac057a07762d12660e11e6f7c4354d62714a277"
menu_path: ["Welcome to Bun"]
section_path: []
nav_prev: {"path": "installation/index.md", "title": "Installation"}
nav_next: {"path": "bundler/index.md", "title": "Bundler"}
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

* * *

## 

[​

](#get-started)

Get Started

Bun ships as a single, dependency-free binary and includes a runtime, package manager, test runner, and bundler. New to Bun?

* * *

## 

[​

](#what’s-inside)

What’s Inside

*   Runtime: Execute JavaScript/TypeScript files and package scripts with near-zero overhead.
*   Package Manager: Fast installs, workspaces, overrides, and audits with `bun install`.
*   Test Runner: Jest-compatible, TypeScript-first tests with snapshots, DOM, and watch mode.
*   Bundler: Native bundling for JS/TS/JSX with splitting, plugins, and HTML imports.

Explore each area using the cards above. Each section is structured with an overview, quick examples, reference, and best practices for fast scanning and deep dives.

* * *

## 

[​

](#what-is-bun)

What is Bun?

Bun is an all-in-one toolkit for JavaScript and TypeScript apps. It ships as a single executable called `bun`. At its core is the _Bun runtime_, a fast JavaScript runtime designed as **a drop-in replacement for Node.js**. It’s written in Zig and powered by JavaScriptCore under the hood, dramatically reducing startup times and memory usage.

terminal

```
bun run index.tsx  # TS and JSX supported out of the box
```

The `bun` command-line tool also implements a test runner, script runner, and Node.js-compatible package manager, all significantly faster than existing tools and usable in existing Node.js projects with little to no changes necessary.

terminal

```
bun run start                 # run the `start` script
bun install <pkg>             # install a package
bun build ./index.tsx         # bundle a project for browsers
bun test                      # run tests
bunx cowsay 'Hello, world!'   # execute a package
```

## 

[​

](#what-is-a-runtime)

What is a runtime?

JavaScript (or, more formally, ECMAScript) is just a _specification_ for a programming language. Anyone can write a JavaScript _engine_ that ingests a valid JavaScript program and executes it. The two most popular engines in use today are V8 (developed by Google) and JavaScriptCore (developed by Apple). Both are open source. But most JavaScript programs don’t run in a vacuum. They need a way to access the outside world to perform useful tasks. This is where _runtimes_ come in. They implement additional APIs that are then made available to the JavaScript programs they execute.

### 

[​

](#browsers)

Browsers

Notably, browsers ship with JavaScript runtimes that implement a set of Web-specific APIs that are exposed via the global `window` object. Any JavaScript code executed by the browser can use these APIs to implement interactive or dynamic behavior in the context of the current webpage.

### 

[​

](#node-js)

Node.js

Similarly, Node.js is a JavaScript runtime that can be used in non-browser environments, like servers. JavaScript programs executed by Node.js have access to a set of Node.js-specific [globals](https://nodejs.org/api/globals.html) like `Buffer`, `process`, and `__dirname` in addition to built-in modules for performing OS-level tasks like reading/writing files (`node:fs`) and networking (`node:net`, `node:http`). Node.js also implements a CommonJS-based module system and resolution algorithm that pre-dates JavaScript’s native module system. Bun is designed as a faster, leaner, more modern replacement for Node.js.

## 

[​

](#design-goals)

Design goals

Bun is designed from the ground-up with today’s JavaScript ecosystem in mind.

*   **Speed**. Bun processes start [4x faster than Node.js](https://twitter.com/jarredsumner/status/1499225725492076544) currently (try it yourself!)
*   **TypeScript & JSX support**. You can directly execute `.jsx`, `.ts`, and `.tsx` files; Bun’s transpiler converts these to vanilla JavaScript before execution.
*   **ESM & CommonJS compatibility**. The world is moving towards ES modules (ESM), but millions of packages on npm still require CommonJS. Bun recommends ES modules, but supports CommonJS.
*   **Web-standard APIs**. Bun implements standard Web APIs like `fetch`, `WebSocket`, and `ReadableStream`. Bun is powered by the JavaScriptCore engine, which is developed by Apple for Safari, so some APIs like [`Headers`](https://developer.mozilla.org/en-US/docs/Web/API/Headers) and [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL) directly use [Safari’s implementation](https://github.com/oven-sh/bun/blob/HEAD/src/bun.js/bindings/webcore/JSFetchHeaders.cpp).
*   **Node.js compatibility**. In addition to supporting Node-style module resolution, Bun aims for full compatibility with built-in Node.js globals (`process`, `Buffer`) and modules (`path`, `fs`, `http`, etc.) _This is an ongoing effort that is not complete._ Refer to the [compatibility page](/docs/runtime/nodejs-compat) for the current status.

Bun is more than a runtime. The long-term goal is to be a cohesive, infrastructural toolkit for building apps with JavaScript/TypeScript, including a package manager, transpiler, bundler, script runner, test runner, and more.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/index.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: />)

[

Installation

Next

](/docs/installation)
