---
title: "generateBuildId"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:07.023Z"
content_hash: "632dea523bf560fe954dfa2fbe5645b4637423b1df1ca99811e3de4835946450"
menu_path: ["generateBuildId"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)generateBuildId

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
