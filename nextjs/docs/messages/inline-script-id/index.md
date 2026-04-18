---
title: "Inline script id"
source: "https://nextjs.org/docs/messages/inline-script-id"
canonical_url: "https://nextjs.org/docs/messages/inline-script-id"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:17:49.532Z"
content_hash: "fbcc3d7e4fc72304687e994248d0a4a107995c776fa0f76fa10694727a145edd"
menu_path: ["Inline script id"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/google-font-preconnect/index.md", "title": "Google Font Preconnect"}
nav_next: {"path": "nextjs/docs/messages/middleware-upgrade-guide/index.md", "title": "Middleware Upgrade Guide"}
---

# Inline script id

> Enforce `id` attribute on `next/script` components with inline content.

## Why This Error Occurred[](#why-this-error-occurred)

`next/script` components with inline content require an `id` attribute to be defined to track and optimize the script.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Add an `id` attribute to the `next/script` component.

pages/\_app.js

```
import Script from 'next/script'
 
export default function App({ Component, pageProps }) {
  return (
    <>
      <Script id="my-script">{`console.log('Hello world!');`}</Script>
      <Component {...pageProps} />
    </>
  )
}
```

## Useful links[](#useful-links)

*   [Docs for Next.js Script component](/docs/pages/guides/scripts)

Was this helpful?

supported.

Send


