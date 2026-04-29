---
title: "webVitalsAttribution"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:57.425Z"
content_hash: "18cca0719e1fa014fb38977ce8aeaaa2927559600b81231970d3bdfbef57cc43"
menu_path: ["webVitalsAttribution"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../webpack/index.md", "title": "Custom Webpack Config"}
nav_next: {"path": "../../typescript/index.md", "title": "TypeScript"}
---

# webVitalsAttribution

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

When debugging issues related to Web Vitals, it is often helpful if we can pinpoint the source of the problem. For example, in the case of Cumulative Layout Shift (CLS), we might want to know the first element that shifted when the single largest layout shift occurred. Or, in the case of Largest Contentful Paint (LCP), we might want to identify the element corresponding to the LCP for the page. If the LCP element is an image, knowing the URL of the image resource can help us locate the asset we need to optimize.

Pinpointing the biggest contributor to the Web Vitals score, aka [attribution](https://github.com/GoogleChrome/web-vitals/blob/4ca38ae64b8d1e899028c692f94d4c56acfc996c/README.md#attribution), allows us to obtain more in-depth information like entries for [PerformanceEventTiming](https://developer.mozilla.org/docs/Web/API/PerformanceEventTiming), [PerformanceNavigationTiming](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming) and [PerformanceResourceTiming](https://developer.mozilla.org/docs/Web/API/PerformanceResourceTiming).

Attribution is disabled by default in Next.js but can be enabled **per metric** by specifying the following in `next.config.js`.

next.config.js

```
module.exports = {
  experimental: {
    webVitalsAttribution: ['CLS', 'LCP'],
  },
}
```

Valid attribution values are all `web-vitals` metrics specified in the [`NextWebVitalsMetric`](https://github.com/vercel/next.js/blob/442378d21dd56d6e769863eb8c2cb521a463a2e0/packages/next/shared/lib/utils.ts#L43) type.

Was this helpful?
