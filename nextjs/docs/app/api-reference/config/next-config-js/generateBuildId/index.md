---
title: "generateBuildId"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:21.997Z"
content_hash: "27aaf7de8ff8f1e1a4e3fef5890830a5e73d1057a2e6f4c2c96843b6c553b7d2"
menu_path: ["generateBuildId"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../exportPathMap/index.md", "title": "exportPathMap"}
nav_next: {"path": "../generateEtags/index.md", "title": "generateEtags"}
---

# generateBuildId

Last updated April 23, 2026

Next.js generates an ID during `next build` to identify which version of your application is being served. The same build should be used and boot up multiple containers.

If you are rebuilding for each stage of your environment, you will need to generate a consistent build ID to use between containers. Use the `generateBuildId` command in `next.config.js`:

next.config.js

```
module.exports = {
  generateBuildId: async () => {
    // This could be anything, using the latest git hash
    return process.env.GIT_HASH
  },
}
```

Was this helpful?
