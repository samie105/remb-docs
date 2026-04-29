---
title: "No Document Import in Page"
source: "https://nextjs.org/docs/messages/no-document-import-in-page"
canonical_url: "https://nextjs.org/docs/messages/no-document-import-in-page"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:42.510Z"
content_hash: "1a88a888cb7994241815a5249f8d24976126c27eee039ff29629a7764f2bb202"
menu_path: ["No Document Import in Page"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/messages/no-css-tags/index.md", "title": "No CSS Tags"}
nav_next: {"path": "nextjs/docs/messages/no-duplicate-head/index.md", "title": "No Duplicate Head"}
---

# No Document Import in Page

> Prevent importing `next/document` outside of `pages/_document.js`.

## Why This Error Occurred[](#why-this-error-occurred)

`next/document` was imported in a page outside of `pages/_document.js` (or `pages/_document.tsx` if you are using TypeScript). This can cause unexpected issues in your application.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Only import and use `next/document` within `pages/_document.js` (or `pages/_document.tsx`) to override the default `Document` component:

pages/\_document.js

```
import Document, { Html, Head, Main, NextScript } from 'next/document'
 
class MyDocument extends Document {
  //...
}
 
export default MyDocument
```

## Useful Links[](#useful-links)

-   [Custom Document](../../pages/building-your-application/routing/custom-document/index.md)

Was this helpful?
