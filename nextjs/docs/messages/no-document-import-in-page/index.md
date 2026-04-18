---
title: "No Document Import in Page"
source: "https://nextjs.org/docs/messages/no-document-import-in-page"
canonical_url: "https://nextjs.org/docs/messages/no-document-import-in-page"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:16.464Z"
content_hash: "e8309461ad5b3cf2631034d901784f5fcac3344aaf4725498c022e1ce38e3280"
menu_path: ["No Document Import in Page"]
section_path: []
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

*   [Custom Document](/docs/pages/building-your-application/routing/custom-document)

Was this helpful?

supported.

Send


