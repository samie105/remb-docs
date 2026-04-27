---
title: "staticGeneration*"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:29.369Z"
content_hash: "5d57883990283c50f89866859cc3633218417686bf615fa0e57d2daccc446d49"
menu_path: ["staticGeneration*"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)staticGeneration\*

# staticGeneration\*

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

The `staticGeneration*` options allow you to configure the Static Generation process for advanced use cases.

next.config.ts

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

-   `staticGenerationRetryCount`: The number of times to retry a failed page generation before failing the build.
-   `staticGenerationMaxConcurrency`: The maximum number of pages to be processed per worker.
-   `staticGenerationMinPagesPerWorker`: The minimum number of pages to be processed before starting a new worker.

Was this helpful?
