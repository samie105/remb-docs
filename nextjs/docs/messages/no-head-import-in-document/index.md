---
title: "No Head Import in Document"
source: "https://nextjs.org/docs/messages/no-head-import-in-document"
canonical_url: "https://nextjs.org/docs/messages/no-head-import-in-document"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:47.349Z"
content_hash: "9a3f618e64f0a6414ef756d82b7455f1bda5b42c63e6e4bbd8fc0199a57ec6fc"
menu_path: ["No Head Import in Document"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../no-head-element/index.md", "title": "No Head Element"}
nav_next: {"path": "../no-html-link-for-pages/index.md", "title": "No HTML link for pages"}
---

# No Head Import in Document

> Prevent usage of `next/head` in `pages/_document.js`.

## Why This Error Occurred[](#why-this-error-occurred)

`next/head` was imported in `pages/_document.js`. This can cause unexpected issues in your application.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Only import and use `next/document` within `pages/_document.js` to override the default `Document` component. If you are importing `next/head` to use the `Head` component, import it from `next/document` instead in order to modify `<head>` code across all pages:

pages/\_document.js

```
import Document, { Html, Head, Main, NextScript } from 'next/document'
 
class MyDocument extends Document {
  static async getInitialProps(ctx) {
    //...
  }
 
  render() {
    return (
      <Html>
        <Head></Head>
      </Html>
    )
  }
}
 
export default MyDocument
```

## Useful Links[](#useful-links)

-   [Custom Document](/docs/pages/building-your-application/routing/custom-document)

Was this helpful?
