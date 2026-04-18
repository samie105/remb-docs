---
title: "How to use fonts"
source: "https://nextjs.org/docs/pages/getting-started/fonts"
canonical_url: "https://nextjs.org/docs/pages/getting-started/fonts"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:23:45.796Z"
content_hash: "e9e204ae7ffa83502c924b98d5874078d2db81104c14d579e6884272a82c0497"
menu_path: ["How to use fonts"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/getting-started/images/index.md", "title": "Image Optimization"}
nav_next: {"path": "nextjs/docs/pages/getting-started/css/index.md", "title": "How to use CSS in your application"}
---

# How to use fonts

Last updated April 15, 2026

The [`next/font`](/docs/app/api-reference/components/font) module automatically optimizes your fonts and removes external network requests for improved privacy and performance.

It includes **built-in self-hosting** for any font file. This means you can optimally load web fonts with no layout shift.

To start using `next/font`, import it from [`next/font/local`](#local-fonts) or [`next/font/google`](#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example, you can apply fonts globally in your [Custom App](/docs/pages/building-your-application/routing/custom-app) (`pages/_app`):

pages/\_app.tsx

TypeScript

JavaScriptTypeScript

```
import { Geist } from 'next/font/google'
import type { AppProps } from 'next/app'
 
const geist = Geist({
  subsets: ['latin'],
})
 
export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={geist.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

## Google fonts[](#google-fonts)

You can automatically self-host any Google Font. Fonts are included stored as static assets and served from the same domain as your deployment, meaning no requests are sent to Google by the browser when the user visits your site.

To start using a Google Font, import your chosen font from `next/font/google`:

pages/\_app.tsx

TypeScript

JavaScriptTypeScript

```
import { Geist } from 'next/font/google'
import type { AppProps } from 'next/app'
 
const geist = Geist({
  subsets: ['latin'],
})
 
export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={geist.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility. But if you can't use a variable font, you will need to specify a weight:

pages/\_app.tsx

TypeScript

JavaScriptTypeScript

```
import { Roboto } from 'next/font/google'
import type { AppProps } from 'next/app'
 
const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})
 
export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={roboto.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

## Local fonts[](#local-fonts)

To use a local font, import your font from `next/font/local` and specify the [`src`](/docs/pages/api-reference/components/font#src) of your local font file. Fonts can be stored in the [`public`](/docs/pages/api-reference/file-conventions/public-folder) folder or inside the `pages` folder. For example:

pages/\_app.tsx

TypeScript

JavaScriptTypeScript

```
import localFont from 'next/font/local'
import type { AppProps } from 'next/app'
 
const myFont = localFont({
  src: './my-font.woff2',
})
 
export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={myFont.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

If you want to use multiple files for a single font family, `src` can be an array:

```
const roboto = localFont({
  src: [
    {
      path: './Roboto-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './Roboto-Italic.woff2',
      weight: '400',
      style: 'italic',
    },
    {
      path: './Roboto-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
    {
      path: './Roboto-BoldItalic.woff2',
      weight: '700',
      style: 'italic',
    },
  ],
})
```

## API Reference

See the API Reference for the full feature set of Next.js Font

[

### Font

API Reference for the Font Module

](/docs/pages/api-reference/components/font)

Was this helpful?

supported.

Send
