---
title: "No Title in Document Head"
source: "https://nextjs.org/docs/messages/no-title-in-document-head"
canonical_url: "https://nextjs.org/docs/messages/no-title-in-document-head"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:39.869Z"
content_hash: "429e301cd7cc8dec43a2b0892a88f7ac146f0188c75f27073938ba2fc832fc4e"
menu_path: ["No Title in Document Head"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-sync-scripts/index.md", "title": "No Sync Scripts"}
nav_next: {"path": "nextjs/docs/messages/no-unwanted-polyfillio/index.md", "title": "No Unwanted Polyfill.io"}
---

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

*   [next/head](/docs/pages/api-reference/components/head)
*   [Custom Document](/docs/pages/building-your-application/routing/custom-document)

Was this helpful?

supported.

Send




