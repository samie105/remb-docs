---
title: "Turbopack FileSystem Caching"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:38.918Z"
content_hash: "f429bc5f72f684b782436af7ea0d4a59598a816908c1cebcae6a9761def2df0f"
menu_path: ["Turbopack FileSystem Caching"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../turbopack/index.md", "title": "turbopack"}
nav_next: {"path": "../turbopackIgnoreIssue/index.md", "title": "turbopack.ignoreIssue"}
---

# Turbopack FileSystem Caching

Last updated April 23, 2026

## Usage[](#usage)

Turbopack FileSystem Cache enables Turbopack to reduce work across `next dev` or `next build` commands. When enabled, Turbopack will save and restore data to the `.next` folder between builds, which can greatly speed up subsequent builds and dev sessions.

> **Good to know:** The FileSystem Cache feature is considered stable for development and experimental for production builds

next.config.ts

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

| Version | Changes |
| --- | --- |
| `v16.1.0` | FileSystem caching is enabled by default for development |
| `v16.0.0` | Beta release with separate flags for build and dev |
| `v15.5.0` | Persistent caching released as experimental on canary releases |

Was this helpful?
