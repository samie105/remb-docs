---
title: "Routing Information"
source: "https://nextjs.org/docs/app/api-reference/adapters/routing-information"
canonical_url: "https://nextjs.org/docs/app/api-reference/adapters/routing-information"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:04:44.772Z"
content_hash: "9d8e3ddaed8a1a2ae11404ac71f64a4cc900110d81b7a6265369fc9105a77cde"
menu_path: ["Routing Information"]
section_path: []
version: "latest"
content_language: "en"
---
[API Reference](/docs/app/api-reference)[Adapters](/docs/app/api-reference/adapters)Routing Information

# Routing Information

Last updated April 23, 2026

The `routing` object in `onBuildComplete` provides complete routing information with processed patterns ready for deployment:

## `routing.beforeMiddleware`[](#routingbeforemiddleware)

Routes applied before middleware execution. These include generated header and redirect behavior.

## `routing.beforeFiles`[](#routingbeforefiles)

Rewrite routes checked before filesystem route matching.

## `routing.afterFiles`[](#routingafterfiles)

Rewrite routes checked after filesystem route matching.

## `routing.dynamicRoutes`[](#routingdynamicroutes)

Dynamic matchers generated from route segments such as `[slug]` and catch-all routes.

## `routing.onMatch`[](#routingonmatch)

Routes that apply after a successful match, such as immutable cache headers for hashed static assets.

## `routing.fallback`[](#routingfallback)

Final rewrite routes checked when earlier phases did not produce a match.

## Common Route Fields[](#common-route-fields)

Each route entry can include:

-   `source`: Original route pattern (optional for generated internal rules)
-   `sourceRegex`: Compiled regex for matching requests
-   `destination`: Internal destination or redirect destination
-   `headers`: Headers to apply
-   `has`: Positive matching conditions
-   `missing`: Negative matching conditions
-   `status`: Redirect status code
-   `priority`: Internal route priority flag

Was this helpful?
