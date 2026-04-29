---
title: "No Head Element"
source: "https://nextjs.org/docs/messages/no-head-element"
canonical_url: "https://nextjs.org/docs/messages/no-head-element"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:46.316Z"
content_hash: "6a264d69b2e8ca03398b739a43635a50e7cb51722ad03096d9a1c6ede380e135"
menu_path: ["No Head Element"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../no-duplicate-head/index.md", "title": "No Duplicate Head"}
nav_next: {"path": "../no-head-import-in-document/index.md", "title": "No Head Import in Document"}
---

# No Head Element

> Prevent usage of `<head>` element.

## Why This Error Occurred[](#why-this-error-occurred)

A `<head>` element was used to include page-level metadata, but this can cause unexpected behavior in a Next.js application. Use Next.js' built-in `next/head` component instead.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Import and use the `<Head />` component:

pages/index.js

```
import Head from 'next/head'
 
function Index() {
  return (
    <>
      <Head>
        <title>My page title</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
    </>
  )
}
 
export default Index
```

## Useful Links[](#useful-links)

-   [next/head](/docs/pages/api-reference/components/head)

Was this helpful?
