---
title: "authInterrupts"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:06:57.645Z"
content_hash: "2a866c039ce96bd9f4f79d4b319f21ea6ecf2a9c4293013bb5208abb6cdd1f21"
menu_path: ["authInterrupts"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/assetPrefix/index.md", "title": "assetPrefix"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/basePath/index.md", "title": "basePath"}
---

# authInterrupts

This feature is currently available in the canary channel and subject to change. Try it out by [upgrading Next.js](/docs/app/getting-started/upgrading#canary-version), and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

The `authInterrupts` configuration option allows you to use [`forbidden`](/docs/app/api-reference/functions/forbidden) and [`unauthorized`](/docs/app/api-reference/functions/unauthorized) APIs in your application. While these functions are experimental, you must enable the `authInterrupts` option in your `next.config.js` file to use them:

next.config.ts

TypeScript

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

](/docs/app/api-reference/functions/forbidden)[

### unauthorized

API Reference for the unauthorized function.

](/docs/app/api-reference/functions/unauthorized)[

### forbidden.js

API reference for the forbidden.js special file.

](/docs/app/api-reference/file-conventions/forbidden)[

### unauthorized.js

API reference for the unauthorized.js special file.

](/docs/app/api-reference/file-conventions/unauthorized)

[Previous

assetPrefix

](/docs/app/api-reference/config/next-config-js/assetPrefix)

[Next

basePath

](/docs/app/api-reference/config/next-config-js/basePath)

Was this helpful?

supported.

Send




