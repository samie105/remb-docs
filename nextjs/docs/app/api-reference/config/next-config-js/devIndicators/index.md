---
title: "devIndicators"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:12.574Z"
content_hash: "08c431f2b865f4b18fa1ad5fd5a50a0ffd8b37b12341c7acfb9b42989ea21e76"
menu_path: ["devIndicators"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/deploymentId/index.md", "title": "deploymentId"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/distDir/index.md", "title": "distDir"}
---

# devIndicators

Last updated April 23, 2026

`devIndicators` allows you to configure the on-screen indicator that gives context about the current route you're viewing during development.

Types

```
  devIndicators: false | {
    position?: 'bottom-right'
    | 'bottom-left'
    | 'top-right'
    | 'top-left', // defaults to 'bottom-left',
  },
```

Setting `devIndicators` to `false` will hide the indicator, however Next.js will continue to surface any build or runtime errors that were encountered.

## Troubleshooting[](#troubleshooting)

### Indicator not marking a route as static[](#indicator-not-marking-a-route-as-static)

If you expect a route to be static and the indicator has marked it as dynamic, it's likely the route has opted out of prerendering.

You can confirm if a route is [prerendered](../../../../glossary/index.md#prerendering) or [dynamically rendered](../../../../glossary/index.md#dynamic-rendering) by building your application using `next build --debug`, and checking the output in your terminal. Static (or prerendered) routes will display a `○` symbol, whereas dynamic routes will display a `ƒ` symbol. For example:

Build Output

```
Route (app)
┌ ○ /_not-found
└ ƒ /products/[id]
 
○  (Static)   prerendered as static content
ƒ  (Dynamic)  server-rendered on demand
```

There are two reasons a route might opt out of prerendering:

-   The presence of [Request-time APIs](../../../../glossary/index.md#request-time-apis) which rely on request information.
-   An [uncached data request](../../../../getting-started/fetching-data/index.md), like a call to an ORM or database driver.

Check your route for any of these conditions, and if you are not able to statically render the route, then consider using [`loading.js`](../../../file-conventions/loading/index.md) or [`<Suspense />`](https://react.dev/reference/react/Suspense) to leverage [streaming](../../../../getting-started/linking-and-navigating/index.md#streaming).

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v16.0.0` | `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been removed. |
| `v15.2.0` | Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated. |
| `v15.0.0` | Static on-screen indicator added with `appIsrStatus` option. |

Was this helpful?
