---
title: "distDir"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:01.151Z"
content_hash: "11bba228622a9c3f39b8da7f756ec4f386670796f356bbb93eb7a67f637743b9"
menu_path: ["distDir"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/devIndicators/index.md", "title": "devIndicators"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/env/index.md", "title": "env"}
---

# distDir

Last updated April 23, 2026

You can specify a name to use for a custom build directory to use instead of `.next`.

Open `next.config.js` and add the `distDir` config:

next.config.js

```
module.exports = {
  distDir: 'build',
}
```

Now if you run `next build` Next.js will use `build` instead of the default `.next` folder.

> `distDir` **should not** leave your project directory. For example, `../build` is an **invalid** directory.

Was this helpful?
