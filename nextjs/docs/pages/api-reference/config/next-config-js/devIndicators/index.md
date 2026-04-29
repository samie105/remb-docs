---
title: "devIndicators"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:19:57.985Z"
content_hash: "bb2bf508c8d050e1b36e5a3623b5eb6e8c3c78c995fded9a2ecc1bc678519031"
menu_path: ["devIndicators"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../deploymentId/index.md", "title": "deploymentId"}
nav_next: {"path": "../distDir/index.md", "title": "distDir"}
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

| Version | Changes |
| --- | --- |
| `v16.0.0` | `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been removed. |
| `v15.2.0` | Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated. |
| `v15.0.0` | Static on-screen indicator added with `appIsrStatus` option. |

Was this helpful?
