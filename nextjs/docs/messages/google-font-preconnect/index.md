---
title: "Google Font Preconnect"
source: "https://nextjs.org/docs/messages/google-font-preconnect"
canonical_url: "https://nextjs.org/docs/messages/google-font-preconnect"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:17:45.454Z"
content_hash: "3485397f308e978469ba0d6b5a88fe8ea9c11099023fd30f5f20eb99f19c3713"
menu_path: ["Google Font Preconnect"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/google-font-display/index.md", "title": "Google Font Display"}
nav_next: {"path": "nextjs/docs/messages/inline-script-id/index.md", "title": "Inline script id"}
---

# Google Font Preconnect

> **Note**: Next.js automatically adds `<link rel="preconnect" />` after version `12.0.1`.

> Ensure `preconnect` is used with Google Fonts.

## Why This Error Occurred[](#why-this-error-occurred)

A preconnect resource hint was not used with a request to the Google Fonts domain. Adding `preconnect` is recommended to initiate an early connection to the origin.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Add `rel="preconnect"` to the Google Font domain `<link>` tag:

pages/\_document.js

```
<link rel="preconnect" href="https://fonts.gstatic.com" />
```

> **Note**: a **separate** link with `dns-prefetch` can be used as a fallback for browsers that don't support `preconnect` although this is not required.

## Useful Links[](#useful-links)

*   [Preconnect to required origins](https://web.dev/uses-rel-preconnect/)
*   [Preconnect and dns-prefetch](https://web.dev/preconnect-and-dns-prefetch/#resolve-domain-name-early-with-reldns-prefetch)
*   [Next.js Font Optimization](/docs/pages/api-reference/components/font)

Was this helpful?

supported.

Send




