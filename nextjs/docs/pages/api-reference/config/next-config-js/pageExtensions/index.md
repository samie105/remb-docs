---
title: "pageExtensions"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:21:05.130Z"
content_hash: "ff303c43335bbffa6b844a821ef10e9ce2475e02fb9a09eb87a3607778ff16bd"
menu_path: ["pageExtensions"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/output/index.md", "title": "output"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/poweredByHeader/index.md", "title": "poweredByHeader"}
---

# pageExtensions

Last updated April 15, 2026

You can extend the default Page extensions (`.tsx`, `.ts`, `.jsx`, `.js`) used by Next.js. Inside `next.config.js`, add the `pageExtensions` config:

next.config.js

```
module.exports = {
  pageExtensions: ['mdx', 'md', 'jsx', 'js', 'tsx', 'ts'],
}
```

Changing these values affects _all_ Next.js pages, including the following:

*   [`proxy.js`](/docs/pages/api-reference/file-conventions/proxy)
*   [`instrumentation.js`](/docs/pages/guides/instrumentation)
*   `pages/_document.js`
*   `pages/_app.js`
*   `pages/api/`

For example, if you reconfigure `.ts` page extensions to `.page.ts`, you would need to rename pages like `proxy.page.ts`, `instrumentation.page.ts`, `_app.page.ts`.

## Including non-page files in the `pages` directory[](#including-non-page-files-in-the-pages-directory)

You can colocate test files or other files used by components in the `pages` directory. Inside `next.config.js`, add the `pageExtensions` config:

next.config.js

```
module.exports = {
  pageExtensions: ['page.tsx', 'page.ts', 'page.jsx', 'page.js'],
}
```

Then, rename your pages to have a file extension that includes `.page` (e.g. rename `MyPage.tsx` to `MyPage.page.tsx`). Ensure you rename _all_ Next.js pages, including the files mentioned above.

Was this helpful?

supported.

Send




