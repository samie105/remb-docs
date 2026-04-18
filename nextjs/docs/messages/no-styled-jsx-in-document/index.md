---
title: "No `styled-jsx` in `_document`"
source: "https://nextjs.org/docs/messages/no-styled-jsx-in-document"
canonical_url: "https://nextjs.org/docs/messages/no-styled-jsx-in-document"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:35.047Z"
content_hash: "97c6ab3d9287b820e32b8e63d16d23739b8894527988f06c70b97e6db9794507"
menu_path: ["No `styled-jsx` in `_document`"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-script-component-in-head/index.md", "title": "No Script Component in Head"}
nav_next: {"path": "nextjs/docs/messages/no-sync-scripts/index.md", "title": "No Sync Scripts"}
---

# No \`styled-jsx\` in \`\_document\`

> Prevent usage of `styled-jsx` in `pages/_document.js`.

## Why This Error Occurred[](#why-this-error-occurred)

Custom CSS like `styled-jsx` is not allowed in a [Custom Document](/docs/pages/building-your-application/routing/custom-document).

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

If you need shared CSS for all of your pages, take a look at the [Custom `App`](/docs/pages/building-your-application/routing/custom-app) file or define a custom layout.

For example, consider the following stylesheet named `styles.css`:

styles.css

```
body {
  font-family:
    'SF Pro Text', 'SF Pro Icons', 'Helvetica Neue', 'Helvetica', 'Arial',
    sans-serif;
  padding: 20px 20px 60px;
  max-width: 680px;
  margin: 0 auto;
}
```

Create a `pages/_app.{js,tsx}` file if not already present. Then, import the `styles.css` file.

pages/\_app.js

```
import '../styles.css'
 
// This default export is required in a new `pages/_app.js` file.
export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

These styles (`styles.css`) will apply to all pages and components in your application.

## Useful Links[](#useful-links)

*   [Custom Document Caveats](/docs/pages/building-your-application/routing/custom-document#caveats)
*   [Layouts](/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)
*   [Built in CSS Support](/docs/app/getting-started/css)
*   [Custom `App`](/docs/pages/building-your-application/routing/custom-app)

Was this helpful?

supported.

Send




