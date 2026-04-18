---
title: "sassOptions"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:29.876Z"
content_hash: "cfacd34bf03af65e1a4648350723fe38157ad76e418985f2a298150ff63a8b28"
menu_path: ["sassOptions"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/rewrites/index.md", "title": "rewrites"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/serverActions/index.md", "title": "serverActions"}
---

# sassOptions

Last updated April 15, 2026

`sassOptions` allow you to configure the Sass compiler.

next.config.ts

TypeScript

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
> *   `sassOptions` are not typed outside of `implementation` because Next.js does not maintain the other possible properties.
> *   The `functions` property for defining custom Sass functions is only supported with webpack. When using Turbopack, custom Sass functions are not available because Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through this option.

[Previous

rewrites

](/docs/app/api-reference/config/next-config-js/rewrites)

[Next

serverActions

](/docs/app/api-reference/config/next-config-js/serverActions)

Was this helpful?

supported.

Send




