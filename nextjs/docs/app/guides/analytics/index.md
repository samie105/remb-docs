---
title: "How to add analytics to your Next.js application"
source: "https://nextjs.org/docs/app/guides/analytics"
canonical_url: "https://nextjs.org/docs/app/guides/analytics"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:13:59.798Z"
content_hash: "a0adbdc5da71fef30b9856b43969ddd2e9adc6029a5dd6202cd48e2964ba908d"
menu_path: ["How to add analytics to your Next.js application"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/ai-agents/index.md", "title": "How to set up your Next.js project for AI coding agents"}
nav_next: {"path": "nextjs/docs/app/guides/authentication/index.md", "title": "How to implement authentication in Next.js"}
---

# How to add analytics to your Next.js application

Last updated April 15, 2026

Next.js has built-in support for measuring and reporting performance metrics. You can either use the [`useReportWebVitals`](/docs/app/api-reference/functions/use-report-web-vitals) hook to manage reporting yourself, or alternatively, Vercel provides a [managed service](https://vercel.com/analytics?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) to automatically collect and visualize metrics for you.

## Client Instrumentation[](#client-instrumentation)

For more advanced analytics and monitoring needs, Next.js provides a `instrumentation-client.js|ts` file that runs before your application's frontend code starts executing. This is ideal for setting up global analytics, error tracking, or performance monitoring tools.

To use it, create an `instrumentation-client.js` or `instrumentation-client.ts` file in your application's root directory:

instrumentation-client.js

```
// Initialize analytics before the app starts
console.log('Analytics initialized')
 
// Set up global error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

## Build Your Own[](#build-your-own)

app/\_components/web-vitals.js

```
'use client'
 
import { useReportWebVitals } from 'next/web-vitals'
 
export function WebVitals() {
  useReportWebVitals((metric) => {
    console.log(metric)
  })
}
```

app/layout.js

```
import { WebVitals } from './_components/web-vitals'
 
export default function Layout({ children }) {
  return (
    <html>
      <body>
        <WebVitals />
        {children}
      </body>
    </html>
  )
}
```

> Since the `useReportWebVitals` hook requires the `'use client'` directive, the most performant approach is to create a separate component that the root layout imports. This confines the client boundary exclusively to the `WebVitals` component.

View the [API Reference](/docs/app/api-reference/functions/use-report-web-vitals) for more information.

## Web Vitals[](#web-vitals)

[Web Vitals](https://web.dev/vitals/) are a set of useful metrics that aim to capture the user experience of a web page. The following web vitals are all included:

*   [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
*   [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
*   [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
*   [First Input Delay](https://web.dev/fid/) (FID)
*   [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
*   [Interaction to Next Paint](https://web.dev/inp/) (INP)

You can handle all the results of these metrics using the `name` property.

app/\_components/web-vitals.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { useReportWebVitals } from 'next/web-vitals'
 
export function WebVitals() {
  useReportWebVitals((metric) => {
    switch (metric.name) {
      case 'FCP': {
        // handle FCP results
      }
      case 'LCP': {
        // handle LCP results
      }
      // ...
    }
  })
}
```

## Sending results to external systems[](#sending-results-to-external-systems)

You can send results to any endpoint to measure and track real user performance on your site. For example:

```
useReportWebVitals((metric) => {
  const body = JSON.stringify(metric)
  const url = 'https://example.com/analytics'
 
  // Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url, body)
  } else {
    fetch(url, { body, method: 'POST', keepalive: true })
  }
})
```

> **Good to know**: If you use [Google Analytics](https://analytics.google.com/analytics/web/), using the `id` value can allow you to construct metric distributions manually (to calculate percentiles, etc.)

> ```
> useReportWebVitals((metric) => {
>   // Use `window.gtag` if you initialized Google Analytics as this example:
>   // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>   window.gtag('event', metric.name, {
>     value: Math.round(
>       metric.name === 'CLS' ? metric.value * 1000 : metric.value
>     ), // values must be integers
>     event_label: metric.id, // id unique to current page load
>     non_interaction: true, // avoids affecting bounce rate.
>   })
> })
> ```
> 
> Read more about [sending results to Google Analytics](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics).

[Previous

AI Coding Agents

](/docs/app/guides/ai-agents)

[Next

Authentication

](/docs/app/guides/authentication)

Was this helpful?

supported.

Send




