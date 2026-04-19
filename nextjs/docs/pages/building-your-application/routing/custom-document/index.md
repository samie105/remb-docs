---
title: "Custom Document"
source: "https://nextjs.org/docs/pages/building-your-application/routing/custom-document"
canonical_url: "https://nextjs.org/docs/pages/building-your-application/routing/custom-document"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:23:23.750Z"
content_hash: "9f730c14feea7b83409bc3ff3af606644c9d1205173899ed12beb5b6d24e7fd7"
menu_path: ["Custom Document"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/building-your-application/routing/custom-app/index.md", "title": "Custom App"}
nav_next: {"path": "nextjs/docs/pages/building-your-application/routing/api-routes/index.md", "title": "API Routes"}
---

# Custom Document

Last updated April 15, 2026

A custom `Document` can update the `<html>` and `<body>` tags used to render a [Page](/docs/pages/building-your-application/routing/pages-and-layouts).

To override the default `Document`, create the file `pages/_document` as shown below:

pages/\_document.tsx

TypeScript

JavaScriptTypeScript

```
import { Html, Head, Main, NextScript } from 'next/document'
 
export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

> **Good to know**:
> 
> *   `_document` is only rendered on the server, so event handlers like `onClick` cannot be used in this file.
> *   `<Html>`, `<Head />`, `<Main />` and `<NextScript />` are required for the page to be properly rendered.

## Caveats[](#caveats)

*   The `<Head />` component used in `_document` is not the same as [`next/head`](/docs/pages/api-reference/components/head). The `<Head />` component used here should only be used for any `<head>` code that is common for all pages. For all other cases, such as `<title>` tags, we recommend using [`next/head`](/docs/pages/api-reference/components/head) in your pages or components.
*   React components outside of `<Main />` will not be initialized by the browser. Do _not_ add application logic here or custom CSS (like `styled-jsx`). If you need shared components in all your pages (like a menu or a toolbar), read [Layouts](/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern) instead.
*   `Document` currently does not support Next.js [Data Fetching methods](/docs/pages/building-your-application/data-fetching) like [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props) or [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props).

## Customizing `renderPage`[](#customizing-renderpage)

Customizing `renderPage` is advanced and only needed for libraries like CSS-in-JS to support server-side rendering. This is not needed for built-in `styled-jsx` support.

**We do not recommend using this pattern.** Instead, consider [incrementally adopting](/docs/app/guides/migrating/app-router-migration) the App Router, which allows you to more easily fetch data for pages and layouts.

pages/\_document.tsx

TypeScript

JavaScriptTypeScript

```
import Document, {
  Html,
  Head,
  Main,
  NextScript,
  DocumentContext,
  DocumentInitialProps,
} from 'next/document'
 
class MyDocument extends Document {
  static async getInitialProps(
    ctx: DocumentContext
  ): Promise<DocumentInitialProps> {
    const originalRenderPage = ctx.renderPage
 
    // Run the React rendering logic synchronously
    ctx.renderPage = () =>
      originalRenderPage({
        // Useful for wrapping the whole react tree
        enhanceApp: (App) => App,
        // Useful for wrapping in a per-page basis
        enhanceComponent: (Component) => Component,
      })
 
    // Run the parent `getInitialProps`, it now includes the custom `renderPage`
    const initialProps = await Document.getInitialProps(ctx)
 
    return initialProps
  }
 
  render() {
    return (
      <Html lang="en">
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

> **Good to know**:
> 
> *   `getInitialProps` in `_document` is not called during client-side transitions.
> *   The `ctx` object for `_document` is equivalent to the one received in [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props#context-object), with the addition of `renderPage`.

Was this helpful?

supported.

Send
