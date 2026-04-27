---
title: "No Title in Document Head"
source: "https://nextjs.org/docs/messages/no-title-in-document-head"
canonical_url: "https://nextjs.org/docs/messages/no-title-in-document-head"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:18:02.404Z"
content_hash: "480fc57cd073aed0528f56b2a95f1c5b54da8eee75db25236efc43b45ae9fc53"
menu_path: ["No Title in Document Head"]
section_path: []
version: "latest"
content_language: "en"
---
[Docs](/docs)[Errors](/docs)No Title in Document Head

# No Title in Document Head

> Prevent usage of `<title>` with `Head` component from `next/document`.

## Why This Error Occurred[](#why-this-error-occurred)

A `<title>` element was defined within the `Head` component imported from `next/document`, which should only be used for any `<head>` code that is common for all pages. Title tags should be defined at the page-level using `next/head` instead.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Within a page or component, import and use `next/head` to define a page title:

pages/index.js

```
import Head from 'next/head'
 
export function Home() {
  return (
    <div>
      <Head>
        <title>My page title</title>
      </Head>
    </div>
  )
}
```

## Useful Links[](#useful-links)

-   [next/head](/docs/pages/api-reference/components/head)
-   [Custom Document](/docs/pages/building-your-application/routing/custom-document)

Was this helpful?
