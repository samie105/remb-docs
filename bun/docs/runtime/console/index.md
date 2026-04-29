---
title: "Console"
source: "https://bun.com/docs/runtime/console"
canonical_url: "https://bun.com/docs/runtime/console"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:10.482Z"
content_hash: "4cfb55ef2d0801ee323d4fec58982234ec9f24c9bf71c1556d1bf37f2e5980a1"
menu_path: ["Console"]
section_path: []
nav_prev: {"path": "../color/index.md", "title": "Color"}
nav_next: {"path": "../cookies/index.md", "title": "Cookies"}
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

Bun provides a browser- and Node.js-compatible [console](https://developer.mozilla.org/en-US/docs/Web/API/console) global. This page only documents Bun-native APIs.

* * *

## 

[​

](#object-inspection-depth)

Object inspection depth

Bun allows you to configure how deeply nested objects are displayed in `console.log()` output:

*   **CLI flag**: Use `--console-depth <number>` to set the depth for a single run
*   **Configuration**: Set `console.depth` in your `bunfig.toml` for persistent configuration
*   **Default**: Objects are inspected to a depth of `2` levels

```
const nested = { a: { b: { c: { d: "deep" } } } };
console.log(nested);
// Default (depth 2): { a: { b: [Object] } }
// With depth 4: { a: { b: { c: { d: 'deep' } } } }
```

The CLI flag takes precedence over the configuration file setting.

* * *

## 

[​

](#reading-from-stdin)

Reading from stdin

In Bun, the `console` object can be used as an `AsyncIterable` to sequentially read lines from `process.stdin`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)adder.ts

```
for await (const line of console) {
  console.log(line);
}
```

This is useful for implementing interactive programs, like the following addition calculator.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)adder.ts

```
console.log(`Let's add some numbers!`);
console.write(`Count: 0\n> `);

let count = 0;
for await (const line of console) {
  count += Number(line);
  console.write(`Count: ${count}\n> `);
}
```

To run the file:

terminal

```
bun adder.ts
Let's add some numbers!
Count: 0
> 5
Count: 5
> 5
Count: 10
> 5
Count: 15
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/console.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/console>)

[

Secrets

Previous

](/docs/runtime/secrets)[

TOML

Next

](/docs/runtime/toml)
