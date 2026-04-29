---
title: "pageExtensions"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:30.312Z"
content_hash: "32a9e3c1b94a4a8666f477489edb67a16428179e845e0a791ebf8d19a3930c4d"
menu_path: ["pageExtensions"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../output/index.md", "title": "output"}
nav_next: {"path": "../poweredByHeader/index.md", "title": "poweredByHeader"}
---

# pageExtensions

Last updated April 23, 2026

You can extend the default Page extensions (`.tsx`, `.ts`, `.jsx`, `.js`) used by Next.js. Inside `next.config.js`, add the `pageExtensions` config:

next.config.js

```
module.exports = {
  pageExtensions: ['mdx', 'md', 'jsx', 'js', 'tsx', 'ts'],
}
```

Changing these values affects _all_ Next.js pages, including the following:

-   [`proxy.js`](/docs/pages/api-reference/file-conventions/proxy)
-   [`instrumentation.js`](/docs/pages/guides/instrumentation)
-   `pages/_document.js`
-   `pages/_app.js`
-   `pages/api/`

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
