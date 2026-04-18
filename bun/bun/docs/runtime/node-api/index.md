---
title: "Node-API"
source: "https://bun.com/docs/runtime/node-api"
canonical_url: "https://bun.com/docs/runtime/node-api"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:00.541Z"
content_hash: "6fe8eee05a6cd435e47405edb0b2c290665eb2148a3d27ae0e726a1da2f9f8fc"
menu_path: ["Node-API"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/networking/udp/index.md", "title": "UDP"}
nav_next: {"path": "bun/bun/docs/runtime/nodejs-compat/index.md", "title": "Node.js Compatibility"}
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

Node-API is an interface for building native add-ons to Node.js. Bun implements 95% of this interface from scratch, so most existing Node-API extensions will work with Bun out of the box. Track the completion status of it in [this issue](https://github.com/oven-sh/bun/issues/158). As in Node.js, `.node` files (Node-API modules) can be required directly in Bun.

```
const napi = require("./my-node-module.node");
```

Alternatively, use `process.dlopen`:

```
let mod = { exports: {} };
process.dlopen(mod, "./my-node-module.node");
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/node-api.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/node-api>)

[

Cron

Previous

](/docs/runtime/cron)[

FFI

Next

](/docs/runtime/ffi)
