---
title: "generateBuildId"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:41.651Z"
content_hash: "4c58a8c748c35d5f5ff5f7fd3037a020ca66e4b69b7e2f574e8c9a086bbaafef"
menu_path: ["generateBuildId"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/exportPathMap/index.md", "title": "exportPathMap"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/generateEtags/index.md", "title": "generateEtags"}
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

Was this helpful?

supported.

Send


