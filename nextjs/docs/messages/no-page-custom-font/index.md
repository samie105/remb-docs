---
title: "No Page Custom Font"
source: "https://nextjs.org/docs/messages/no-page-custom-font"
canonical_url: "https://nextjs.org/docs/messages/no-page-custom-font"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:30.557Z"
content_hash: "41f75042d3023304f4117491e2a50ed5678750dbee3e546ae9a9c386fc0987a2"
menu_path: ["No Page Custom Font"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-img-element/index.md", "title": "No img element"}
nav_next: {"path": "nextjs/docs/messages/no-script-component-in-head/index.md", "title": "No Script Component in Head"}
---

# No Page Custom Font

> Prevent page-only custom fonts.

## Why This Error Occurred[](#why-this-error-occurred)

*   The custom font you're adding was added to a page - this only adds the font to the specific page and not the entire application.
*   The custom font you're adding was added to a separate component within `pages/_document.js` - this disables automatic font optimization.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Create the file `./pages/_document.js` and add the font to a custom Document:

pages/\_document.js

```
import Document, { Html, Head, Main, NextScript } from 'next/document'
 
class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          <link
            href="https://fonts.googleapis.com/css2?family=Inter&display=optional"
            rel="stylesheet"
          />
        </Head>
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

Or as a function component:

pages/\_document.js

```
import { Html, Head, Main, NextScript } from 'next/document'
 
export default function Document() {
  return (
    <Html>
      <Head>
        <link
          href="https://fonts.googleapis.com/css2?family=Inter&display=optional"
          rel="stylesheet"
        />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

### When Not To Use It[](#when-not-to-use-it)

If you have a reason to only load a font for a particular page or don't care about font optimization, then you can disable this rule.

## Useful Links[](#useful-links)

*   [Custom Document](/docs/pages/building-your-application/routing/custom-document)
*   [Font Optimization](/docs/pages/api-reference/components/font)

Was this helpful?

supported.

Send




