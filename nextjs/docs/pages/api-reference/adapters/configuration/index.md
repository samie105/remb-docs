---
title: "Configuration"
source: "https://nextjs.org/docs/pages/api-reference/adapters/configuration"
canonical_url: "https://nextjs.org/docs/pages/api-reference/adapters/configuration"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:19:01.700Z"
content_hash: "4b0c0b60c6f5f386ef20fe76fd161bdd3b7da2bacb2a0a8f03f532e185e0de98"
menu_path: ["Configuration"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/adapters/index.md", "title": "Adapters"}
nav_next: {"path": "nextjs/docs/pages/api-reference/adapters/creating-an-adapter/index.md", "title": "Creating an Adapter"}
---

# Configuration

Last updated April 15, 2026

To use an adapter, specify the path to your adapter module in `adapterPath`:

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  adapterPath: require.resolve('./my-adapter.js'),
}
 
module.exports = nextConfig
```

Alternatively `NEXT_ADAPTER_PATH` can be set to enable zero-config usage in deployment platforms.

Was this helpful?

supported.

Send
