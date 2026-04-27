---
title: "No Before Interactive Script Outside Document"
source: "https://nextjs.org/docs/messages/no-before-interactive-script-outside-document"
canonical_url: "https://nextjs.org/docs/messages/no-before-interactive-script-outside-document"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:33.776Z"
content_hash: "6b9f6976a6a2e6246e89db8d1c28714f685d689f21318ad196235fbde2d2f8a9"
menu_path: ["No Before Interactive Script Outside Document"]
section_path: []
version: "latest"
content_language: "en"
---
[Docs](/docs)[Errors](/docs)No Before Interactive Script Outside Document

# No Before Interactive Script Outside Document

> Prevent usage of `next/script`'s `beforeInteractive` strategy outside of `app/layout.jsx` or `pages/_document.js`.

## Why This Error Occurred[](#why-this-error-occurred)

You cannot use the `next/script` component with the `beforeInteractive` strategy outside `app/layout.jsx` or `pages/_document.js`. That's because `beforeInteractive` strategy only works inside **`app/layout.jsx`** or **`pages/_document.js`** and is designed to load scripts that are needed by the entire site (i.e. the script will load when any page in the application has been loaded server-side).

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

### App Router[](#app-router)

If you want a global script, and you are using the App Router, move the script inside `app/layout.jsx`.

app/layout.jsx

```
import Script from 'next/script'
 
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
      <Script
        src="https://example.com/script.js"
        strategy="beforeInteractive"
      />
    </html>
  )
}
```

### Pages Router[](#pages-router)

If you want a global script, and you are using the Pages Router, move the script inside `pages/_document.js`.

pages/\_document.js

```
import { Html, Head, Main, NextScript } from 'next/document'
import Script from 'next/script'
 
export default function Document() {
  return (
    <Html>
      <Head />
      <body>
        <Main />
        <NextScript />
        <Script
          src="https://example.com/script.js"
          strategy="beforeInteractive"
        ></Script>
      </body>
    </Html>
  )
}
```

## Useful Links[](#useful-links)

-   [App Router Script Optimization](/docs/app/guides/scripts)
-   [Pages Router Script Optimization](/docs/pages/guides/scripts)

Was this helpful?
