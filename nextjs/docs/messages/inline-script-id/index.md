---
title: "Inline script id"
source: "https://nextjs.org/docs/messages/inline-script-id"
canonical_url: "https://nextjs.org/docs/messages/inline-script-id"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:15.868Z"
content_hash: "ad649d096010a49169117c482f7ea8514aa1e094fce4cd04e01690674e33e53b"
menu_path: ["Inline script id"]
section_path: []
version: "latest"
content_language: "en"
---
[Docs](/docs)[Errors](/docs)Inline script id

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

-   [Docs for Next.js Script component](/docs/pages/guides/scripts)

Was this helpful?
