---
title: "manifest.json"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:15.449Z"
content_hash: "f4109040cb2660c198b4196baf36afcbfb9e403055d68b47e30ceedbda24320c"
menu_path: ["manifest.json"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/metadata/app-icons/index.md", "title": "favicon, icon, and apple-icon"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/metadata/opengraph-image/index.md", "title": "opengraph-image and twitter-image"}
---

# manifest.json

Last updated April 15, 2026

Add or generate a `manifest.(json|webmanifest)` file that matches the [Web Manifest Specification](https://developer.mozilla.org/docs/Web/Manifest) in the **root** of `app` directory to provide information about your web application for the browser.

## Static Manifest file[](#static-manifest-file)

app/manifest.json | app/manifest.webmanifest

```
{
  "name": "My Next.js Application",
  "short_name": "Next.js App",
  "description": "An application built with Next.js",
  "start_url": "/"
  // ...
}
```

## Generate a Manifest file[](#generate-a-manifest-file)

Add a `manifest.js` or `manifest.ts` file that returns a [`Manifest` object](#manifest-object).

> Good to know: `manifest.js` is a special Route Handlers that is cached by default unless it uses a [Request-time API](/docs/app/glossary#request-time-apis) or [dynamic config](/docs/app/guides/caching-without-cache-components#dynamic) option.

app/manifest.ts

TypeScript

JavaScriptTypeScript

```
import type { MetadataRoute } from 'next'
 
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'Next.js App',
    short_name: 'Next.js App',
    description: 'Next.js App',
    start_url: '/',
    display: 'standalone',
    background_color: '#fff',
    theme_color: '#fff',
    icons: [
      {
        src: '/favicon.ico',
        sizes: 'any',
        type: 'image/x-icon',
      },
    ],
  }
}
```

### Manifest Object[](#manifest-object)

The manifest object contains an extensive list of options that may be updated due to new web standards. For information on all the current options, refer to the `MetadataRoute.Manifest` type in your code editor if using [TypeScript](/docs/app/api-reference/config/typescript#ide-plugin) or see the [MDN](https://developer.mozilla.org/docs/Web/Manifest) docs.

[Previous

favicon, icon, and apple-icon

](/docs/app/api-reference/file-conventions/metadata/app-icons)

[Next

opengraph-image and twitter-image

](/docs/app/api-reference/file-conventions/metadata/opengraph-image)

Was this helpful?

supported.

Send


