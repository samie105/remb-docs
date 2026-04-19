---
title: "No HTML link for pages"
source: "https://nextjs.org/docs/messages/no-html-link-for-pages"
canonical_url: "https://nextjs.org/docs/messages/no-html-link-for-pages"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:25.768Z"
content_hash: "0236df5c42263a8665b53eac6c2e67fbaa9a4877b9c2b037840a5b8de41709bd"
menu_path: ["No HTML link for pages"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-head-import-in-document/index.md", "title": "No Head Import in Document"}
nav_next: {"path": "nextjs/docs/messages/no-img-element/index.md", "title": "No img element"}
---

# No HTML link for pages

> Prevent usage of `<a>` elements to navigate to internal Next.js pages.

## Why This Error Occurred[](#why-this-error-occurred)

An `<a>` element was used to navigate to a page route without using the `next/link` component, causing unnecessary full-page refreshes.

The `Link` component is required to enable client-side route transitions between pages and provide a single-page app experience.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Make sure to import the `Link` component and wrap anchor elements that route to different page routes.

**Before:**

pages/index.js

```
function Home() {
  return (
    <div>
      <a href="/about">About Us</a>
    </div>
  )
}
```

**After:**

pages/index.js

```
import Link from 'next/link'
 
function Home() {
  return (
    <div>
      <Link href="/about">About Us</Link>
    </div>
  )
}
 
export default Home
```

### Options[](#options)

#### `pagesDir`[](#pagesdir)

This rule can normally locate your `pages` directory automatically.

If you're working in a monorepo, we recommend configuring the [`rootDir`](/docs/pages/api-reference/config/eslint#specifying-a-root-directory-within-a-monorepo) setting in `eslint-plugin-next`, which `pagesDir` will use to locate your `pages` directory.

In some cases, you may also need to configure this rule directly by providing a `pages` directory. This can be a path or an array of paths.

eslint.config.json

```
{
  "rules": {
    "@next/next/no-html-link-for-pages": ["error", "packages/my-app/pages/"]
  }
}
```

## Useful Links[](#useful-links)

*   [next/link API Reference](/docs/pages/api-reference/components/link)

Was this helpful?

supported.

Send
