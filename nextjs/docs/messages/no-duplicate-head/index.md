---
title: "No Duplicate Head"
source: "https://nextjs.org/docs/messages/no-duplicate-head"
canonical_url: "https://nextjs.org/docs/messages/no-duplicate-head"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:17.425Z"
content_hash: "bfa48f05f99b91831cd253019cd473192c2e2a94b875cc9c6875d241d5a74c12"
menu_path: ["No Duplicate Head"]
section_path: []
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

*   [Custom Document](/docs/pages/building-your-application/routing/custom-document)

Was this helpful?

supported.

Send
