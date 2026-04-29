---
title: "Using Google Analytics with Next.js (through `@next/third-parties/google`)"
source: "https://nextjs.org/docs/messages/next-script-for-ga"
canonical_url: "https://nextjs.org/docs/messages/next-script-for-ga"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:29.389Z"
content_hash: "b0a0cb0a5674c38894b5e1bf2b729ddfc4bccc8e7357fe427c83e503eae820a2"
menu_path: ["Using Google Analytics with Next.js (through `@next/third-parties/google`)"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/messages/next-request-in-use-cache/index.md", "title": "Cannot access `cookies()` or `headers()` in `\"use cache\"`"}
nav_next: {"path": "nextjs/docs/messages/no-assign-module-variable/index.md", "title": "No assign module variable"}
---

# Using Google Analytics with Next.js (through \`@next/third-parties/google\`)

> Prefer `@next/third-parties/google` when using the inline script for Google Analytics and Tag Manager.

## Why This Error Occurred[](#why-this-error-occurred)

An inline script was used for Google Analytics which might impact your webpage's performance. Instead, we recommend using `next/script` through the `@next/third-parties` library.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

### Use `@next/third-parties` to add Google Analytics[](#use-nextthird-parties-to-add-google-analytics)

**`@next/third-parties`** is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries in your Next.js application. It is available with Next.js 14 (install `next@latest`).

The `GoogleAnalytics` component can be used to include [Google Analytics 4](https://developers.google.com/analytics/devguides/collection/ga4) to your page via the Google tag (`gtag.js`). By default, it fetches the original scripts after hydration occurs on the page.

> **Recommendation**: If Google Tag Manager is already included in your application, you can configure Google Analytics directly using it, rather than including Google Analytics as a separate component. Refer to the [documentation](https://developers.google.com/analytics/devguides/collection/ga4/tag-options#what-is-gtm) to learn more about the differences between Tag Manager and `gtag.js`.

To load Google Analytics for all routes, include the component directly in your root layout and pass in your measurement ID:

app/layout.tsx

JavaScriptTypeScript

```
import { GoogleAnalytics } from '@next/third-parties/google'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
      <GoogleAnalytics gaId="G-XYZ" />
    </html>
  )
}
```

To load Google Analytics for a single route, include the component in your page file:

app/page.js

```
import { GoogleAnalytics } from '@next/third-parties/google'
 
export default function Page() {
  return <GoogleAnalytics gaId="G-XYZ" />
}
```

### Use `@next/third-parties` to add Google Tag Manager[](#use-nextthird-parties-to-add-google-tag-manager)

The `GoogleTagManager` component can be used to add [Google Tag Manager](https://developers.google.com/tag-manager/quickstart) to your page.

app/layout.tsx

JavaScriptTypeScript

```
import { GoogleTagManager } from '@next/third-parties/google'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <GoogleTagManager gtmId="GTM-XYZ" />
      <body>{children}</body>
    </html>
  )
}
```

To load Google Tag Manager for a single route, include the component in your page file:

app/page.js

```
import { GoogleTagManager } from '@next/third-parties/google'
 
export default function Page() {
  return <GoogleTagManager gtmId="GTM-XYZ" />
}
```

## Good to know[](#good-to-know)

-   If you are using the Pages Router, please refer to the [`pages/` documentation](/docs/pages/guides/third-party-libraries).
-   `@next/third-parties` also supports [other third parties](../../app/guides/third-party-libraries/index.md#google-tag-manager).
-   Using `@next/third-parties` is not required. You can also use the `next/script` component directly. Refer to the [`next/script` documentation](../../app/guides/scripts/index.md) to learn more.

## Useful Links[](#useful-links)

-   [`@next/third-parties` Documentation](../../app/guides/third-party-libraries/index.md)
-   [`next/script` Documentation](../../app/guides/scripts/index.md)

Was this helpful?
