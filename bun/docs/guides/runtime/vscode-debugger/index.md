---
title: "Debugging Bun with the VS Code extension"
source: "https://bun.com/docs/guides/runtime/vscode-debugger"
canonical_url: "https://bun.com/docs/guides/runtime/vscode-debugger"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:28.172Z"
content_hash: "7a96e8d0f36e684031a8c70dde9183fd9e0ecc904b6086b9d7af34f92249cf16"
menu_path: ["Debugging Bun with the VS Code extension"]
section_path: []
nav_prev: {"path": "bun/docs/guides/runtime/typescript/index.md", "title": "Install TypeScript declarations for Bun"}
nav_next: {"path": "bun/docs/guides/runtime/web-debugger/index.md", "title": "Debugging Bun with the web debugger"}
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

VSCode extension support is currently buggy. We recommend the [Web Debugger](/docs/guides/runtime/web-debugger) for now.

Bun speaks the [WebKit Inspector Protocol](https://github.com/oven-sh/bun/blob/main/packages/bun-inspector-protocol/src/protocol/jsc/index.d.ts) so you can debug your code with an interactive debugger.

* * *

To install the extension, visit the [Bun for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=oven.bun-vscode) page on the VS Code marketplace website, then click Install.

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/7c8c80e6-d49e-457a-a45e-45ebed946d56)

* * *

Alternatively, search `bun-vscode` in the Extensions tab of VS Code.

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/664b4c40-944c-4076-a4c2-f812aebd3dc9)

* * *

Make sure you are installing the extension published by the verified Oven organization.

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/73e6b09f-9ff1-4d85-b725-c5eb7215b6ae)

* * *

Once installed, two new Bun-specific commands will appear in the Command Palette. To open the palette, click View > Command Palette, or type `Ctrl+Shift+P` (Windows, Linux) or `Cmd+Shift+P` on (Mac).

* * *

The `Bun: Run File` command will execute your code and print the output to the Debug Console in VS Code. Breakpoints will be ignored; this is similar to executing the file with `bun <file>` from the command line.

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/1b2c7fd9-fbb9-486a-84d0-eb7ec135ded3)

* * *

The `Bun: Debug File` command will execute your code and print the output to the Debug Console in VS Code. You can set breakpoints in your code by clicking to the left of a line number; a red dot should appear. When you run the file with `Bun: Debug File`, execution will pause at the breakpoint. You can inspect the variables in scope and step through the code line-by-line using the VS Code controls.

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/c579a36c-eb21-4a58-bc9c-74612aad82af)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/vscode-debugger.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/vscode-debugger>)

[

Re-map import paths

Previous

](/docs/guides/runtime/tsconfig-paths)[

Debugging Bun with the web debugger

Next

](/docs/guides/runtime/web-debugger)

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/7c8c80e6-d49e-457a-a45e-45ebed946d56)

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/664b4c40-944c-4076-a4c2-f812aebd3dc9)

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/73e6b09f-9ff1-4d85-b725-c5eb7215b6ae)

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/1b2c7fd9-fbb9-486a-84d0-eb7ec135ded3)

![VS Code extension](https://github.com/oven-sh/bun/assets/3084745/c579a36c-eb21-4a58-bc9c-74612aad82af)
