---
title: "instrumentation-client.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:09:56.718Z"
content_hash: "a8f5ea1b002c560632b43c4320ffade77dabde3ed9df86d07a7b0fbf93f8aec5"
menu_path: ["instrumentation-client.js"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/instrumentation/index.md", "title": "instrumentation.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/intercepting-routes/index.md", "title": "Intercepting Routes"}
---

# instrumentation-client.js

Last updated April 15, 2026

The `instrumentation-client.js|ts` file allows you to add monitoring, analytics code, and other side-effects that run before your application becomes interactive. This is useful for setting up performance tracking, error monitoring, polyfills, or any other client-side observability tools.

To use it, place the file in the **root** of your application or inside a `src` folder.

## Usage[](#usage)

Unlike [server-side instrumentation](/docs/app/guides/instrumentation), you do not need to export any specific functions. You can write your monitoring code directly in the file:

instrumentation-client.ts

TypeScript

JavaScriptTypeScript

```
// Set up performance monitoring
performance.mark('app-init')
 
// Initialize analytics
console.log('Analytics initialized')
 
// Set up error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

**Error handling:** Implement try-catch blocks around your instrumentation code to ensure robust monitoring. This prevents individual tracking failures from affecting other instrumentation features.

## Router navigation tracking[](#router-navigation-tracking)

You can export an `onRouterTransitionStart` function to receive notifications when navigation begins:

instrumentation-client.ts

TypeScript

JavaScriptTypeScript

```
performance.mark('app-init')
 
export function onRouterTransitionStart(
  url: string,
  navigationType: 'push' | 'replace' | 'traverse'
) {
  console.log(`Navigation started: ${navigationType} to ${url}`)
  performance.mark(`nav-start-${Date.now()}`)
}
```

The `onRouterTransitionStart` function receives two parameters:

*   `url: string` - The URL being navigated to
*   `navigationType: 'push' | 'replace' | 'traverse'` - The type of navigation

## Performance considerations[](#performance-considerations)

Keep instrumentation code lightweight.

Next.js monitors initialization time in development and will log warnings if it takes longer than 16ms, which could impact smooth page loading.

## Execution timing[](#execution-timing)

The `instrumentation-client.js` file executes at a specific point in the application lifecycle:

1.  **After** the HTML document is loaded
2.  **Before** React hydration begins
3.  **Before** user interactions are possible

This timing makes it ideal for setting up error tracking, analytics, and performance monitoring that needs to capture early application lifecycle events.

## Examples[](#examples)

### Error tracking[](#error-tracking)

Initialize error tracking before React starts and add navigation breadcrumbs for better debugging context.

instrumentation-client.ts

TypeScript

JavaScriptTypeScript

```
import Monitor from './lib/monitoring'
 
Monitor.initialize()
 
export function onRouterTransitionStart(url: string) {
  Monitor.pushEvent({
    message: `Navigation to ${url}`,
    category: 'navigation',
  })
}
```

### Analytics tracking[](#analytics-tracking)

Initialize analytics and track navigation events with detailed metadata for user behavior analysis.

instrumentation-client.ts

TypeScript

JavaScriptTypeScript

```
import { analytics } from './lib/analytics'
 
analytics.init()
 
export function onRouterTransitionStart(url: string, navigationType: string) {
  analytics.track('page_navigation', {
    url,
    type: navigationType,
    timestamp: Date.now(),
  })
}
```

### Performance monitoring[](#performance-monitoring)

Track Time to Interactive and navigation performance using the Performance Observer API and performance marks.

instrumentation-client.ts

TypeScript

JavaScriptTypeScript

```
const startTime = performance.now()
 
const observer = new PerformanceObserver(
  (list: PerformanceObserverEntryList) => {
    for (const entry of list.getEntries()) {
      if (entry instanceof PerformanceNavigationTiming) {
        console.log('Time to Interactive:', entry.loadEventEnd - startTime)
      }
    }
  }
)
 
observer.observe({ entryTypes: ['navigation'] })
 
export function onRouterTransitionStart(url: string) {
  performance.mark(`nav-start-${url}`)
}
```

### Polyfills[](#polyfills)

Load polyfills before application code runs. Use static imports for immediate loading and dynamic imports for conditional loading based on feature detection.

instrumentation-client.ts

TypeScript

JavaScriptTypeScript

```
import './lib/polyfills'
 
if (!window.ResizeObserver) {
  import('./lib/polyfills/resize-observer').then((mod) => {
    window.ResizeObserver = mod.default
  })
}
```

## Version history[](#version-history)

Version

Changes

`v15.3`

`instrumentation-client` introduced

[Previous

instrumentation.js

](/docs/app/api-reference/file-conventions/instrumentation)

[Next

Intercepting Routes

](/docs/app/api-reference/file-conventions/intercepting-routes)

Was this helpful?

supported.

Send


