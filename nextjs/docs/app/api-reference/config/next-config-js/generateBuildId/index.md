---
title: "generateBuildId"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:31.226Z"
content_hash: "2f273cb4dcdfca4bafcb019d6978d1f5b2fb0aac66fda9a4a8d02372d3bbced0"
menu_path: ["generateBuildId"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/exportPathMap/index.md", "title": "exportPathMap"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/generateEtags/index.md", "title": "generateEtags"}
---

# generateBuildId

Last updated April 15, 2026

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

[Previous

exportPathMap

](/docs/app/api-reference/config/next-config-js/exportPathMap)

[Next

generateEtags

](/docs/app/api-reference/config/next-config-js/generateEtags)

Was this helpful?

supported.

Send


