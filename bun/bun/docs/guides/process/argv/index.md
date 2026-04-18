---
title: "Parse command-line arguments"
source: "https://bun.com/docs/guides/process/argv"
canonical_url: "https://bun.com/docs/guides/process/argv"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:35.266Z"
content_hash: "036d2f85f668b43bbac255fb5d3374dc9948b6fc032734767e5e10db409dfa72"
menu_path: ["Parse command-line arguments"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/install/yarnlock/index.md", "title": "Generate a yarn-compatible lockfile"}
nav_next: {"path": "bun/bun/docs/guides/process/ctrl-c/index.md", "title": "Listen for CTRL+C"}
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

The _argument vector_ is the list of arguments passed to the program when it is run. It is available as `Bun.argv`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)cli.ts

```
console.log(Bun.argv);
```

* * *

Running this file with arguments results in the following:

terminal

```
bun run cli.ts --flag1 --flag2 value
```

```
[ '/path/to/bun', '/path/to/cli.ts', '--flag1', '--flag2', 'value' ]
```

* * *

To parse `argv` into a more useful format, `util.parseArgs` would be helpful. Example:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)cli.ts

```
import { parseArgs } from "util";

const { values, positionals } = parseArgs({
  args: Bun.argv,
  options: {
    flag1: {
      type: "boolean",
    },
    flag2: {
      type: "string",
    },
  },
  strict: true,
  allowPositionals: true,
});

console.log(values);
console.log(positionals);
```

* * *

then it outputs

terminal

```
bun run cli.ts --flag1 --flag2 value
```

```
{
  flag1: true,
  flag2: "value",
}
[ "/path/to/bun", "/path/to/cli.ts" ]
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/process/argv.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/process/argv>)

[

Read stderr from a child process

Previous

](/docs/guides/process/spawn-stderr)[

Read from stdin

Next

](/docs/guides/process/stdin)


