---
title: "No Head Element"
source: "https://nextjs.org/docs/messages/no-head-element"
canonical_url: "https://nextjs.org/docs/messages/no-head-element"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:21.144Z"
content_hash: "eb115d7f5dde0a93ee2bf2ddeec5cc0d48b6b4b4a50e561d6ee6a500d3a64d3e"
menu_path: ["No Head Element"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-duplicate-head/index.md", "title": "No Duplicate Head"}
nav_next: {"path": "nextjs/docs/messages/no-head-import-in-document/index.md", "title": "No Head Import in Document"}
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

*   [next/head](/docs/pages/api-reference/components/head)

Was this helpful?

supported.

Send
