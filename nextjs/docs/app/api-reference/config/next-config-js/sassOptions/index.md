---
title: "sassOptions"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:15.647Z"
content_hash: "9c9dc21d14c4c3eeab66038a547ea1b08fadaa181fde7ff9ed84a0883e28bd88"
menu_path: ["sassOptions"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/rewrites/index.md", "title": "rewrites"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/serverActions/index.md", "title": "serverActions"}
---

# sassOptions

Last updated April 23, 2026

`sassOptions` allow you to configure the Sass compiler.

next.config.ts

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const sassOptions = {
  additionalData: `
    $var: red;
  `,
}
 
const nextConfig: NextConfig = {
  sassOptions: {
    ...sassOptions,
    implementation: 'sass-embedded',
  },
}
 
export default nextConfig
```

> **Good to know:**
> 
> -   `sassOptions` are not typed outside of `implementation` because Next.js does not maintain the other possible properties.
> -   The `functions` property for defining custom Sass functions is only supported with webpack. When using Turbopack, custom Sass functions are not available because Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through this option.

Was this helpful?
