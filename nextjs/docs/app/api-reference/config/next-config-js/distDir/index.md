---
title: "distDir"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:13.036Z"
content_hash: "0f36735ab4a56c4a598366be88a79398660835c70e0050fdde9e28ca6a5b59ca"
menu_path: ["distDir"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/devIndicators/index.md", "title": "devIndicators"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/env/index.md", "title": "env"}
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
