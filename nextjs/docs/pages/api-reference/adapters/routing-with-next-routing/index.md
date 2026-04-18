---
title: "Routing with @next/routing"
source: "https://nextjs.org/docs/pages/api-reference/adapters/routing-with-next-routing"
canonical_url: "https://nextjs.org/docs/pages/api-reference/adapters/routing-with-next-routing"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:19:17.351Z"
content_hash: "72beb69e6ef6b44d5a8662d2c9e87fdb933d192cd8b75b3038080e5f840dec70"
menu_path: ["Routing with @next/routing"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/adapters/testing-adapters/index.md", "title": "Testing Adapters"}
nav_next: {"path": "nextjs/docs/pages/api-reference/adapters/implementing-ppr-in-an-adapter/index.md", "title": "Implementing PPR in an Adapter"}
---

# Routing with @next/routing

Last updated April 15, 2026

You can use [`@next/routing`](https://www.npmjs.com/package/@next/routing) to reproduce Next.js route matching behavior with data from `onBuildComplete`.

`@next/routing` is experimental and will stabilize with the adapters API.

```
import { resolveRoutes } from '@next/routing'
 
const pathnames = [
  ...outputs.pages,
  ...outputs.pagesApi,
  ...outputs.appPages,
  ...outputs.appRoutes,
  ...outputs.staticFiles,
].map((output) => output.pathname)
 
const result = await resolveRoutes({
  url: new URL(requestUrl),
  buildId,
  basePath: config.basePath || '',
  i18n: config.i18n,
  headers: new Headers(requestHeaders),
  requestBody, // ReadableStream
  pathnames,
  routes: routing,
  invokeMiddleware: async (ctx) => {
    // platform-specific middleware invocation
    return {}
  },
})
 
if (result.resolvedPathname) {
  console.log('Resolved pathname:', result.resolvedPathname)
  console.log('Resolved query:', result.resolvedQuery)
  console.log('Invocation target:', result.invocationTarget)
}
```

`resolveRoutes()` returns:

*   `middlewareResponded`: `true` when middleware already sent a response (the adapter should not invoke an entrypoint).
*   `externalRewrite`: A `URL` when routing resolved to an external rewrite destination.
*   `redirect`: An object with `url` (`URL`) and `status` when the request should be redirected.
*   `resolvedPathname`: The route pathname selected by Next.js routing. For dynamic routes, this is the matched route template such as `/blog/[slug]`.
*   `resolvedQuery`: The final query after rewrites or middleware have added or replaced search params.
*   `invocationTarget`: The concrete pathname and query to invoke for the matched route.
*   `resolvedHeaders`: A `Headers` object containing any headers added or modified during routing.
*   `status`: An HTTP status code set by routing (for example from a redirect or rewrite rule).
*   `routeMatches`: A record of named matches extracted from dynamic route segments.

For example, if `/blog/post-1?draft=1` matches `/blog/[slug]?slug=post-1`, `resolvedPathname` is `/blog/[slug]` while `invocationTarget.pathname` is `/blog/post-1`.

Was this helpful?

supported.

Send


