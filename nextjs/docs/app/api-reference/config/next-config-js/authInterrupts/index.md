---
title: "authInterrupts"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:05:49.883Z"
content_hash: "b0392dd02874188549fa0af5b864fc15b41f81c0d117d45badadebb92248c2b5"
menu_path: ["authInterrupts"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/assetPrefix/index.md", "title": "assetPrefix"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/basePath/index.md", "title": "basePath"}
---

# authInterrupts

This feature is currently available in the canary channel and subject to change. Try it out by [upgrading Next.js](../../../../getting-started/upgrading/index.md#canary-version), and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

The `authInterrupts` configuration option allows you to use [`forbidden`](../../../functions/forbidden/index.md) and [`unauthorized`](../../../functions/unauthorized/index.md) APIs in your application. While these functions are experimental, you must enable the `authInterrupts` option in your `next.config.js` file to use them:

next.config.ts

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}
 
export default nextConfig
```

[

### forbidden

API Reference for the forbidden function.

](../../../functions/forbidden/index.md)[

### unauthorized

API Reference for the unauthorized function.

](../../../functions/unauthorized/index.md)[

### forbidden.js

API reference for the forbidden.js special file.

](../../../file-conventions/forbidden/index.md)[

### unauthorized.js

API reference for the unauthorized.js special file.

](../../../file-conventions/unauthorized/index.md)

Was this helpful?
