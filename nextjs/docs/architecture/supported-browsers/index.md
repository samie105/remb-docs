---
title: "Supported Browsers"
source: "https://nextjs.org/docs/architecture/supported-browsers"
canonical_url: "https://nextjs.org/docs/architecture/supported-browsers"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:17:21.821Z"
content_hash: "51bdcaf79156991f1d3a2e208b26a865149e70b8f301bc30455a11dd97f61954"
menu_path: ["Supported Browsers"]
section_path: []
nav_prev: {"path": "nextjs/docs/architecture/nextjs-compiler/index.md", "title": "Next.js Compiler"}
nav_next: {"path": "nextjs/docs/community/index.md", "title": "Next.js Community"}
---

# Supported Browsers

Last updated April 15, 2026

Next.js supports **modern browsers** with zero configuration.

*   Chrome 111+
*   Edge 111+
*   Firefox 111+
*   Safari 16.4+

## Browserslist[](#browserslist)

If you would like to target specific browsers or features, Next.js supports [Browserslist](https://browsersl.ist) configuration in your `package.json` file. Next.js uses the following Browserslist configuration by default:

package.json

```
{
  "browserslist": ["chrome 111", "edge 111", "firefox 111", "safari 16.4"]
}
```

## Polyfills[](#polyfills)

We inject [widely used polyfills](https://github.com/vercel/next.js/blob/canary/packages/next-polyfill-nomodule/src/index.js), including:

*   [**fetch()**](https://developer.mozilla.org/docs/Web/API/Fetch_API) — Replacing: `whatwg-fetch` and `unfetch`.
*   [**URL**](https://developer.mozilla.org/docs/Web/API/URL) — Replacing: the [`url` package (Node.js API)](https://nodejs.org/api/url.html).
*   [**Object.assign()**](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) — Replacing: `object-assign`, `object.assign`, and `core-js/object/assign`.

If any of your dependencies include these polyfills, they’ll be eliminated automatically from the production build to avoid duplication.

In addition, to reduce bundle size, Next.js will only load these polyfills for browsers that require them. The majority of the web traffic globally will not download these polyfills.

### Custom Polyfills[](#custom-polyfills)

If your own code or any external npm dependencies require features not supported by your target browsers (such as IE 11), you need to add polyfills yourself.

#### In App Router[](#in-app-router)

To include polyfills, you can import them into the [`instrumentation-client.js` file](/docs/app/api-reference/file-conventions/instrumentation-client).

instrumentation-client.ts

```
import './polyfills'
```

#### In Pages Router[](#in-pages-router)

In this case, you should add a top-level import for the **specific polyfill** you need in your [Custom `<App>`](/docs/pages/building-your-application/routing/custom-app) or the individual component.

pages/\_app.tsx

TypeScript

JavaScriptTypeScript

```
import './polyfills'
 
import type { AppProps } from 'next/app'
 
export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

#### Conditionally loading polyfills[](#conditionally-loading-polyfills)

The best approach is to isolate unsupported features to specific UI sections and conditionally load the polyfill if needed.

hooks/analytics.ts

TypeScript

JavaScriptTypeScript

```
import { useCallback } from 'react'
 
export const useAnalytics = () => {
  const tracker = useCallback(async (data: unknown) => {
    if (!('structuredClone' in globalThis)) {
      import('polyfills/structured-clone').then((mod) => {
        globalThis.structuredClone = mod.default
      })
    }
 
    /* Do some work that uses structured clone */
  }, [])
 
  return tracker
}
```

## JavaScript Language Features[](#javascript-language-features)

Next.js allows you to use the latest JavaScript features out of the box. In addition to [ES6 features](https://github.com/lukehoban/es6features), Next.js also supports:

*   [Async/await](https://github.com/tc39/ecmascript-asyncawait) (ES2017)
*   [Object Rest/Spread Properties](https://github.com/tc39/proposal-object-rest-spread) (ES2018)
*   [Dynamic `import()`](https://github.com/tc39/proposal-dynamic-import) (ES2020)
*   [Optional Chaining](https://github.com/tc39/proposal-optional-chaining) (ES2020)
*   [Nullish Coalescing](https://github.com/tc39/proposal-nullish-coalescing) (ES2020)
*   [Class Fields](https://github.com/tc39/proposal-class-fields) and [Static Properties](https://github.com/tc39/proposal-static-class-features) (ES2022)
*   and more!

### TypeScript Features[](#typescript-features)

Next.js has built-in TypeScript support. [Learn more here](/docs/pages/api-reference/config/typescript).

### Customizing Babel Config (Advanced)[](#customizing-babel-config-advanced)

You can customize babel configuration. [Learn more here](/docs/pages/guides/babel).

[Previous

Next.js Compiler

](/docs/architecture/nextjs-compiler)

[Next

Community

](/docs/community)

Was this helpful?

supported.

Send


