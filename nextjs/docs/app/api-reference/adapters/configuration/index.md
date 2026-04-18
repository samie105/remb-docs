---
title: "Configuration"
source: "https://nextjs.org/docs/app/api-reference/adapters/configuration"
canonical_url: "https://nextjs.org/docs/app/api-reference/adapters/configuration"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:05:39.295Z"
content_hash: "8e7570ba6f8d17701a1381daf68dcbd120287c38d88870542da5a5aa3424c1b4"
menu_path: ["Configuration"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/adapters/index.md", "title": "Adapters"}
nav_next: {"path": "nextjs/docs/app/api-reference/adapters/creating-an-adapter/index.md", "title": "Creating an Adapter"}
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

[Previous

Adapters

](/docs/app/api-reference/adapters)

[Next

Creating an Adapter

](/docs/app/api-reference/adapters/creating-an-adapter)

Was this helpful?

supported.

Send




