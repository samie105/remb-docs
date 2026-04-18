---
title: "distDir"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:34.474Z"
content_hash: "394e218bcfcb53a0601f7b745a21350611dd362895d3338315d4d738c0308312"
menu_path: ["distDir"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/devIndicators/index.md", "title": "devIndicators"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/env/index.md", "title": "env"}
---

# distDir

Last updated April 15, 2026

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

supported.

Send


