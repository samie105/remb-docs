---
title: "Conflicting Public File and Page File"
source: "https://nextjs.org/docs/messages/conflicting-public-file-page"
canonical_url: "https://nextjs.org/docs/messages/conflicting-public-file-page"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:17:40.076Z"
content_hash: "5957cef18d2cc2438542d6939200a13cac5d8893d932767c6c594ba56caae7dc"
menu_path: ["Conflicting Public File and Page File"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/blocking-route/index.md", "title": "Uncached data was accessed outside of `<Suspense>`"}
nav_next: {"path": "nextjs/docs/messages/empty-generate-static-params/index.md", "title": "Empty generateStaticParams with Cache Components"}
---

# Conflicting Public File and Page File

## Why This Error Occurred[](#why-this-error-occurred)

One of your public files has the same path as a page file which is not supported. Since only one resource can reside at the URL both public files and page files must be unique.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Rename either the public file or page file that is causing the conflict.

Example conflict between public file and page file

Folder structure

```
public/
  hello
pages/
  hello.js
```

Non-conflicting public file and page file

Folder structure

```
public/
  hello.txt
pages/
  hello.js
```

## Useful Links[](#useful-links)

*   [Static file serving docs](/docs/pages/api-reference/file-conventions/public-folder)

Was this helpful?

supported.

Send
