---
title: "staticGeneration*"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:39.627Z"
content_hash: "555e2fbc07844bb68486071c9d3e4e34e0516f5a34ce127ae3df860ab0653d4b"
menu_path: ["staticGeneration*"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/staleTimes/index.md", "title": "staleTimes"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/taint/index.md", "title": "taint"}
---

# staticGeneration\*

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

The `staticGeneration*` options allow you to configure the Static Generation process for advanced use cases.

next.config.ts

TypeScript

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    staticGenerationRetryCount: 1,
    staticGenerationMaxConcurrency: 8,
    staticGenerationMinPagesPerWorker: 25,
  },
}
 
export default nextConfig
```

## Config Options[](#config-options)

The following options are available:

*   `staticGenerationRetryCount`: The number of times to retry a failed page generation before failing the build.
*   `staticGenerationMaxConcurrency`: The maximum number of pages to be processed per worker.
*   `staticGenerationMinPagesPerWorker`: The minimum number of pages to be processed before starting a new worker.

[Previous

staleTimes

](/docs/app/api-reference/config/next-config-js/staleTimes)

[Next

taint

](/docs/app/api-reference/config/next-config-js/taint)

Was this helpful?

supported.

Send


