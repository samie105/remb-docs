---
title: "Google Font Preconnect"
source: "https://nextjs.org/docs/messages/google-font-preconnect"
canonical_url: "https://nextjs.org/docs/messages/google-font-preconnect"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:13.727Z"
content_hash: "830f0e4c4614d6f46c02645073ac98a50ef79f129fa33da6cd2c56435f731493"
menu_path: ["Google Font Preconnect"]
section_path: []
version: "latest"
content_language: "en"
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

-   [Preconnect to required origins](https://web.dev/uses-rel-preconnect/)
-   [Preconnect and dns-prefetch](https://web.dev/preconnect-and-dns-prefetch/#resolve-domain-name-early-with-reldns-prefetch)
-   [Next.js Font Optimization](/docs/pages/api-reference/components/font)

Was this helpful?
