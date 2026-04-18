---
title: "Run a Shell Command"
source: "https://bun.com/docs/guides/runtime/shell"
canonical_url: "https://bun.com/docs/guides/runtime/shell"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:15.082Z"
content_hash: "109610d2542791cafdf834cea268190e4a3356cf566ecef72626879ba48bcf89"
menu_path: ["Run a Shell Command"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/runtime/set-env/index.md", "title": "Set environment variables"}
nav_next: {"path": "bun/bun/docs/guides/runtime/timezone/index.md", "title": "Set a time zone in Bun"}
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

Bun Shell is a cross-platform bash-like shell built in to Bun. It runs shell commands in JavaScript and TypeScript. To get started, import the `$` function from the `bun` package and use it to run shell commands.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)foo.ts

```
import { $ } from "bun";

await $`echo Hello, world!`; // => "Hello, world!"
```

* * *

The `$` function is a tagged template literal that runs the command and returns a promise that resolves with the command’s output.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)foo.ts

```
import { $ } from "bun";

const output = await $`ls -l`.text();
console.log(output);
```

* * *

To get each line of the output as an array, use the `lines` method.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)foo.ts

```
import { $ } from "bun";

for await (const line of $`ls -l`.lines()) {
  console.log(line);
}
```

* * *

See [Docs > API > Shell](/docs/runtime/shell) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/shell.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/shell>)

[

Get the process uptime in nanoseconds

Previous

](/docs/guides/process/nanoseconds)[

Set a time zone in Bun

Next

](/docs/guides/runtime/timezone)
