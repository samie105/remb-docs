---
title: "distDir"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:22.099Z"
content_hash: "b53bf109e7b127dfdc0ce3f1373ffc6c1ddffe4f0f64bbaab3a5c1a499a2f16a"
menu_path: ["distDir"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/devIndicators/index.md", "title": "devIndicators"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/env/index.md", "title": "env"}
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

[Previous

devIndicators

](/docs/app/api-reference/config/next-config-js/devIndicators)

[Next

env

](/docs/app/api-reference/config/next-config-js/env)

Was this helpful?

supported.

Send




