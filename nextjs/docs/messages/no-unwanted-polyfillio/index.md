---
title: "No Unwanted Polyfill.io"
source: "https://nextjs.org/docs/messages/no-unwanted-polyfillio"
canonical_url: "https://nextjs.org/docs/messages/no-unwanted-polyfillio"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:18:04.541Z"
content_hash: "a426c46c0bb156c1d9e383b1a379e40d534b2b3bb1ec8df8b8b979432e2481e1"
menu_path: ["No Unwanted Polyfill.io"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/messages/no-title-in-document-head/index.md", "title": "No Title in Document Head"}
nav_next: {"path": "nextjs/docs/messages/sync-dynamic-apis/index.md", "title": "Dynamic APIs are Asynchronous"}
---

# No Unwanted Polyfill.io

> Prevent duplicate polyfills from Polyfill.io.

## Why This Error Occurred[](#why-this-error-occurred)

You are using polyfills from Polyfill.io and including polyfills already shipped with Next.js. This unnecessarily increases page weight which can affect loading performance.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Remove all duplicate polyfills. If you need to add polyfills but are not sure if Next.js already includes it, take a look at the list of [supported browsers and features](../../architecture/supported-browsers/index.md).

## Useful Links[](#useful-links)

-   [Supported Browsers and Features](../../architecture/supported-browsers/index.md)

Was this helpful?
