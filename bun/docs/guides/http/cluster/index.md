---
title: "Start a cluster of HTTP servers"
source: "https://bun.com/docs/guides/http/cluster"
canonical_url: "https://bun.com/docs/guides/http/cluster"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:38.374Z"
content_hash: "741a552d80d5e5f0bcfe009bb71d8447e0e9536a52fce5473a22b474304f642b"
menu_path: ["Start a cluster of HTTP servers"]
section_path: []
nav_prev: {"path": "../../html-rewriter/extract-social-meta/index.md", "title": "Extract social share images and Open Graph tags"}
nav_next: {"path": "../fetch/index.md", "title": "Send an HTTP request using fetch"}
---

To run multiple HTTP servers concurrently, use the `reusePort` option in `Bun.serve()` which shares the same port across multiple processes. This automatically load balances incoming requests across multiple instances of Bun.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
import { serve } from "bun";

const id = Math.random().toString(36).slice(2);

serve({
  port: process.env.PORT || 8080,
  development: false,

  // Share the same port across multiple processes
  // This is the important part!
  reusePort: true,

  async fetch(request) {
    return new Response("Hello from Bun #" + id + "!\n");
  },
});
```

* * *

After saving the file, start your servers on the same port. Under the hood, this uses the Linux `SO_REUSEPORT` and `SO_REUSEADDR` socket options to ensure fair load balancing across multiple processes. [Learn more about `SO_REUSEPORT` and `SO_REUSEADDR`](https://lwn.net/Articles/542629/)

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)cluster.ts

```
import { spawn } from "bun";

const cpus = navigator.hardwareConcurrency; // Number of CPU cores
const buns = new Array(cpus);

for (let i = 0; i < cpus; i++) {
  buns[i] = spawn({
    cmd: ["bun", "./server.ts"],
    stdout: "inherit",
    stderr: "inherit",
    stdin: "inherit",
  });
}

function kill() {
  for (const bun of buns) {
    bun.kill();
  }
}

process.on("SIGINT", kill);
process.on("exit", kill);
```

* * *

Bun has also implemented the `node:cluster` module, but this is a faster and more limited alternative.
