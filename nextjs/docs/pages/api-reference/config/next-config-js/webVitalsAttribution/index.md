---
title: "webVitalsAttribution"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:21:07.559Z"
content_hash: "f112dffbb96497cdbdbcd7a390b85625dcfe481973cf8748107cd550ba3bcd8a"
menu_path: ["webVitalsAttribution"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)webVitalsAttribution

# webVitalsAttribution

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
