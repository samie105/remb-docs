---
title: "No Duplicate Head"
source: "https://nextjs.org/docs/messages/no-duplicate-head"
canonical_url: "https://nextjs.org/docs/messages/no-duplicate-head"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:43.179Z"
content_hash: "ec1020604217c4692a26133df618208c92a3c51724e34b15dab2d670e8dfbfa2"
menu_path: ["No Duplicate Head"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/messages/no-document-import-in-page/index.md", "title": "No Document Import in Page"}
nav_next: {"path": "nextjs/docs/messages/no-head-element/index.md", "title": "No Head Element"}
---

# No Duplicate Head

> Prevent duplicate usage of `<Head>` in `pages/_document.js`.

## Why This Error Occurred[](#why-this-error-occurred)

More than a single instance of the `<Head />` component was used in a single custom document. This can cause unexpected behavior in your application.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Only use a single `<Head />` component in your custom document in `pages/_document.js`.

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
        <Head />
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}
 
export default MyDocument
```

## Useful Links[](#useful-links)

-   [Custom Document](../../pages/building-your-application/routing/custom-document/index.md)

Was this helpful?
