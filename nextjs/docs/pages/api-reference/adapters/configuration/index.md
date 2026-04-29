---
title: "Configuration"
source: "https://nextjs.org/docs/pages/api-reference/adapters/configuration"
canonical_url: "https://nextjs.org/docs/pages/api-reference/adapters/configuration"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:18:23.369Z"
content_hash: "df29ae3298bd4c103b786efd1da8b234ea2c4bbc195436218c79ab4da395fc30"
menu_path: ["Configuration"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../index.md", "title": "Adapters"}
nav_next: {"path": "../creating-an-adapter/index.md", "title": "Creating an Adapter"}
---

# Configuration

Last updated April 23, 2026

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
