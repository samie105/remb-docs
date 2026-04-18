---
title: "Web Standards ​"
source: "https://hono.dev/docs/concepts/web-standard"
canonical_url: "https://hono.dev/docs/concepts/web-standard"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:00.591Z"
content_hash: "64008de28e68eb3b9d5ec879c2ad0997848f08f4aca58b843116d82e63869bf0"
menu_path: ["Web Standards ​"]
section_path: []
nav_prev: {"path": "hono/docs/concepts/benchmarks/index.md", "title": "Benchmarks \u200b"}
nav_next: {"path": "hono/docs/concepts/middleware/index.md", "title": "Middleware \u200b"}
---

Hono uses only **Web Standards** like Fetch. They were originally used in the `fetch` function and consist of basic objects that handle HTTP requests and responses. In addition to `Requests` and `Responses`, there are `URL`, `URLSearchParam`, `Headers` and others.

Cloudflare Workers, Deno, and Bun also are built upon Web Standards. For example, a server that returns "Hello World" could be written as below. This could run on Cloudflare Workers and Bun.

ts

```
export default {
  async fetch() {
    return new Response('Hello World')
  },
}
```

Hono uses only Web Standards, which means that Hono can run on any runtime that supports them. In addition, we have a Node.js adapter. Hono runs on these runtimes:

*   Cloudflare Workers (`workerd`)
*   Deno
*   Bun
*   Fastly Compute
*   AWS Lambda
*   Node.js
*   Vercel (edge-light)
*   WebAssembly (w/ [WebAssembly System Interface (WASI)](https://github.com/WebAssembly/wasi) via [`wasi:http`](https://github.com/WebAssembly/wasi-http))

It also works on Netlify and other platforms. The same code runs on all platforms.

Cloudflare Workers, Deno, Shopify, and others launched [WinterCG](https://wintercg.org/) to discuss the possibility of using the Web Standards to enable "web-interoperability". Hono will follow their steps and go for **the Standard of the Web Standards**.

