---
title: "Read from stdin"
source: "https://bun.com/docs/guides/process/stdin"
canonical_url: "https://bun.com/docs/guides/process/stdin"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:13.264Z"
content_hash: "5d71302d46490713f11c3b00139a257cec400f6f91fb4bbb04e88acd861a7333"
menu_path: ["Read from stdin"]
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

For CLI tools, it’s often useful to read from `stdin`. In Bun, the `console` object is an `AsyncIterable` that yields lines from `stdin`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
const prompt = "Type something: ";
process.stdout.write(prompt);
for await (const line of console) {
  console.log(`You typed: ${line}`);
  process.stdout.write(prompt);
}
```

* * *

Running this file results in a never-ending interactive prompt that echoes whatever the user types.

terminal

```
bun run index.ts
```

```
Type something: hello
You typed: hello
Type something: hello again
You typed: hello again
```

* * *

Bun also exposes stdin as a `BunFile` via `Bun.stdin`. This is useful for incrementally reading large inputs that are piped into the `bun` process. There is no guarantee that the chunks will be split line-by-line.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)stdin.ts

```
for await (const chunk of Bun.stdin.stream()) {
  // chunk is Uint8Array
  // this converts it to text (assumes ASCII encoding)
  const chunkText = Buffer.from(chunk).toString();
  console.log(`Chunk: ${chunkText}`);
}
```

* * *

This will print the input that is piped into the `bun` process.

terminal

```
echo "hello" | bun run stdin.ts
```

```
Chunk: hello
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/process/stdin.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/process/stdin>)

[

Parse command-line arguments

Previous

](/docs/guides/process/argv)[

Spawn a child process and communicate using IPC

Next

](/docs/guides/process/ipc)
