---
title: "devIndicators"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:32.321Z"
content_hash: "16de2d3b58c44fed6d5e5a5199db246ed3052c01d3779d3e456d925fdb5b10a5"
menu_path: ["devIndicators"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/deploymentId/index.md", "title": "deploymentId"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/distDir/index.md", "title": "distDir"}
---

# devIndicators

Last updated April 15, 2026

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

You can confirm if a route is [prerendered](/docs/app/glossary#prerendering) or [dynamically rendered](/docs/app/glossary#dynamic-rendering) by building your application using `next build --debug`, and checking the output in your terminal. Static (or prerendered) routes will display a `○` symbol, whereas dynamic routes will display a `ƒ` symbol. For example:

Build Output

```
Route (app)
┌ ○ /_not-found
└ ƒ /products/[id]
 
○  (Static)   prerendered as static content
ƒ  (Dynamic)  server-rendered on demand
```

When exporting [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props) or [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props) from a page, it will be marked as dynamic.

## Version History[](#version-history)

Version

Changes

`v16.0.0`

`appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been removed.

`v15.2.0`

Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated.

`v15.0.0`

Static on-screen indicator added with `appIsrStatus` option.

Was this helpful?

supported.

Send
