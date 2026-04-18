---
title: "Turbopack FileSystem Caching"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:52.268Z"
content_hash: "cbf6f6772640f57215c964ba4ef98d6d88fe2b84966b14fbdebbaa1f752bf28b"
menu_path: ["Turbopack FileSystem Caching"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/turbopack/index.md", "title": "turbopack"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/turbopackIgnoreIssue/index.md", "title": "turbopack.ignoreIssue"}
---

# Turbopack FileSystem Caching

Last updated April 15, 2026

## Usage[](#usage)

Turbopack FileSystem Cache enables Turbopack to reduce work across `next dev` or `next build` commands. When enabled, Turbopack will save and restore data to the `.next` folder between builds, which can greatly speed up subsequent builds and dev sessions.

> **Good to know:** The FileSystem Cache feature is considered stable for development and experimental for production builds

next.config.ts

TypeScript

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    // Enable filesystem caching for `next dev`
    turbopackFileSystemCacheForDev: true,
    // Enable filesystem caching for `next build`
    turbopackFileSystemCacheForBuild: true,
  },
}
 
export default nextConfig
```

## Version Changes[](#version-changes)

Version

Changes

`v16.1.0`

FileSystem caching is enabled by default for development

`v16.0.0`

Beta release with separate flags for build and dev

`v15.5.0`

Persistent caching released as experimental on canary releases

[Previous

turbopack

](/docs/app/api-reference/config/next-config-js/turbopack)

[Next

turbopack.ignoreIssue

](/docs/app/api-reference/config/next-config-js/turbopackIgnoreIssue)

Was this helpful?

supported.

Send


