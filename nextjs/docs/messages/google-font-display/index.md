---
title: "Google Font Display"
source: "https://nextjs.org/docs/messages/google-font-display"
canonical_url: "https://nextjs.org/docs/messages/google-font-display"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:17:44.968Z"
content_hash: "5fe574743aaa75a144a253be2dda6199621050a68e2c1b343e51f789e01f1c31"
menu_path: ["Google Font Display"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/empty-generate-static-params/index.md", "title": "Empty generateStaticParams with Cache Components"}
nav_next: {"path": "nextjs/docs/messages/google-font-preconnect/index.md", "title": "Google Font Preconnect"}
---

# Google Font Display

> Enforce font-display behavior with Google Fonts.

## Why This Error Occurred[](#why-this-error-occurred)

For a Google Font, the font-display descriptor was either missing or set to `auto`, `block`, or `fallback`, which are not recommended.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

For most cases, the best font display strategy for custom fonts is `optional`.

pages/index.js

```
import Head from 'next/head'
 
export default function IndexPage() {
  return (
    <div>
      <Head>
        <link
          href="https://fonts.googleapis.com/css2?family=Krona+One&display=optional"
          rel="stylesheet"
        />
      </Head>
    </div>
  )
}
```

Specifying `display=optional` minimizes the risk of invisible text or layout shift. If swapping to the custom font after it has loaded is important to you, then use `display=swap` instead.

### When Not To Use It[](#when-not-to-use-it)

If you want to specifically display a font using an `auto`, `block`, or `fallback` strategy, then you can disable this rule.

## Useful Links[](#useful-links)

*   [Controlling Font Performance with font-display](https://developer.chrome.com/blog/font-display/)
*   [Google Fonts API Docs](https://developers.google.com/fonts/docs/css2#use_font-display)
*   [CSS `font-display` property](https://www.w3.org/TR/css-fonts-4/#font-display-desc)

Was this helpful?

supported.

Send




