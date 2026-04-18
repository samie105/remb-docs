---
title: "No Unwanted Polyfill.io"
source: "https://nextjs.org/docs/messages/no-unwanted-polyfillio"
canonical_url: "https://nextjs.org/docs/messages/no-unwanted-polyfillio"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:40.850Z"
content_hash: "f7c728a0d0d8fdc8d92f2fe5099c3726acb80d5009ca5da0bbf45e27757395b8"
menu_path: ["No Unwanted Polyfill.io"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-title-in-document-head/index.md", "title": "No Title in Document Head"}
nav_next: {"path": "nextjs/docs/messages/sync-dynamic-apis/index.md", "title": "Dynamic APIs are Asynchronous"}
---

# No Unwanted Polyfill.io

> Prevent duplicate polyfills from Polyfill.io.

## Why This Error Occurred[](#why-this-error-occurred)

You are using polyfills from Polyfill.io and including polyfills already shipped with Next.js. This unnecessarily increases page weight which can affect loading performance.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Remove all duplicate polyfills. If you need to add polyfills but are not sure if Next.js already includes it, take a look at the list of [supported browsers and features](/docs/architecture/supported-browsers).

## Useful Links[](#useful-links)

*   [Supported Browsers and Features](/docs/architecture/supported-browsers)

Was this helpful?

supported.

Send
