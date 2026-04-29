---
title: "Append content to a file"
source: "https://bun.com/docs/guides/write-file/append"
canonical_url: "https://bun.com/docs/guides/write-file/append"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:40.425Z"
content_hash: "761951b9e106c87baf4fe2e9f660fc3f1ec151dc84f4882d48e568019fd2667d"
menu_path: ["Append content to a file"]
section_path: []
nav_prev: {"path": "bun/docs/guides/websocket/simple/index.md", "title": "Build a simple WebSocket server"}
nav_next: {"path": "bun/docs/guides/write-file/basic/index.md", "title": "Write a string to a file"}
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

Bun implements the `node:fs` module, which includes the `fs.appendFile` and `fs.appendFileSync` functions for appending content to files.

* * *

You can use `fs.appendFile` to asynchronously append data to a file, creating the file if it does not yet exist. The content can be a string or a `Buffer`.

```
import { appendFile } from "node:fs/promises";

await appendFile("message.txt", "data to append");
```

* * *

To use the non-`Promise` API:

```
import { appendFile } from "node:fs";

appendFile("message.txt", "data to append", err => {
  if (err) throw err;
  console.log('The "data to append" was appended to file!');
});
```

* * *

To specify the encoding of the content:

```
import { appendFile } from "node:fs";

appendFile("message.txt", "data to append", "utf8", callback);
```

* * *

To append the data synchronously, use `fs.appendFileSync`:

```
import { appendFileSync } from "node:fs";

appendFileSync("message.txt", "data to append", "utf8");
```

* * *

See the [Node.js documentation](https://nodejs.org/api/fs.html#fspromisesappendfilepath-data-options) for more information.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/write-file/append.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/write-file/append>)

[

Write a Response to a file

Previous

](../response/index.md)[

Write a file incrementally

Next

](../filesink/index.md)
