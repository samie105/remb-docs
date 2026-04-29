---
title: "next.config.js"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:05:35.498Z"
content_hash: "6bd5391a0f019267760f9565796b48d94c2b7097745bdcfdb2a5aead101564af"
menu_path: ["next.config.js"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/index.md", "title": "Configuration"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/adapterPath/index.md", "title": "adapterPath"}
---

# next.config.js

Last updated April 23, 2026

Next.js can be configured through a `next.config.js` file in the root of your project directory (for example, by `package.json`) with a default export.

next.config.js

```
// @ts-check
 
/** @type {import('next').NextConfig} */
const nextConfig = {
  /* config options here */
}
 
module.exports = nextConfig
```

## ECMAScript Modules[](#ecmascript-modules)

`next.config.js` is a regular Node.js module, not a JSON file. It gets used by the Next.js server and build phases, and it's not included in the browser build.

If you need [ECMAScript modules](https://nodejs.org/api/esm.html), you can use `next.config.mjs`:

next.config.mjs

```
// @ts-check
 
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  /* config options here */
}
 
export default nextConfig
```

> **Good to know**: `next.config` with the `.cjs` or `.cts` extensions are currently **not** supported.

## Configuration as a Function[](#configuration-as-a-function)

You can also use a function:

next.config.mjs

```
// @ts-check
 
export default (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

### Async Configuration[](#async-configuration)

Since Next.js 12.1.0, you can use an async function:

next.config.js

```
// @ts-check
 
module.exports = async (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

### Phase[](#phase)

`phase` is the current context in which the configuration is loaded. You can see the [available phases](https://github.com/vercel/next.js/blob/5e6b008b561caf2710ab7be63320a3d549474a5b/packages/next/shared/lib/constants.ts#L19-L23). Phases can be imported from `next/constants`:

next.config.js

```
// @ts-check
 
const { PHASE_DEVELOPMENT_SERVER } = require('next/constants')
 
module.exports = (phase, { defaultConfig }) => {
  if (phase === PHASE_DEVELOPMENT_SERVER) {
    return {
      /* development only config options here */
    }
  }
 
  return {
    /* config options for all phases except development here */
  }
}
```

## TypeScript[](#typescript)

If you are using TypeScript in your project, you can use `next.config.ts` to use TypeScript in your configuration:

next.config.ts

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  /* config options here */
}
 
export default nextConfig
```

The commented lines are the place where you can put the configs allowed by `next.config.js`, which are [defined in this file](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/config-shared.ts).

However, none of the configs are required, and it's not necessary to understand what each config does. Instead, search for the features you need to enable or modify in this section and they will show you what to do.

> Avoid using new JavaScript features not available in your target Node.js version. `next.config.js` will not be parsed by Webpack or Babel.

This page documents all the available configuration options:

## Unit Testing (experimental)[](#unit-testing-experimental)

Starting in Next.js 15.1, the `next/experimental/testing/server` package contains utilities to help unit test `next.config.js` files.

The `unstable_getResponseFromNextConfig` function runs the [`headers`](headers/index.md), [`redirects`](redirects/index.md), and [`rewrites`](rewrites/index.md) functions from `next.config.js` with the provided request information and returns `NextResponse` with the results of the routing.

> The response from `unstable_getResponseFromNextConfig` only considers `next.config.js` fields and does not consider proxy or filesystem routes, so the result in production may be different than the unit test.

```
import {
  getRedirectUrl,
  unstable_getResponseFromNextConfig,
} from 'next/experimental/testing/server'
 
const response = await unstable_getResponseFromNextConfig({
  url: 'https://nextjs.org/test',
  nextConfig: {
    async redirects() {
      return [{ source: '/test', destination: '/test2', permanent: false }]
    },
  },
})
expect(response.status).toEqual(307)
expect(getRedirectUrl(response)).toEqual('https://nextjs.org/test2')
```

[

### adapterPath

Configure a custom adapter for Next.js to hook into the build process.

](adapterPath/index.md)[

### allowedDevOrigins

Use \`allowedDevOrigins\` to configure additional origins that can request the dev server.

](allowedDevOrigins/index.md)[

### appDir

Enable the App Router to use layouts, streaming, and more.

](appDir/index.md)[

### assetPrefix

Learn how to use the assetPrefix config option to configure your CDN.

](assetPrefix/index.md)[

### authInterrupts

Learn how to enable the experimental \`authInterrupts\` configuration option to use \`forbidden\` and \`unauthorized\`.

](authInterrupts/index.md)[

### basePath

Use \`basePath\` to deploy a Next.js application under a sub-path of a domain.

](basePath/index.md)[

### cacheComponents

Learn how to enable the cacheComponents flag in Next.js.

](cacheComponents/index.md)[

### cacheHandlers

Configure custom cache handlers for use cache directives in Next.js.

](cacheHandlers/index.md)[

### cacheLife

Learn how to set up cacheLife configurations in Next.js.

](cacheLife/index.md)[

### compress

Next.js provides gzip compression to compress rendered content and static files, it only works with the server target. Learn more about it here.

](compress/index.md)[

### crossOrigin

Use the \`crossOrigin\` option to add a crossOrigin tag on the \`script\` tags generated by \`next/script\`.

](crossOrigin/index.md)[

### cssChunking

Use the \`cssChunking\` option to control how CSS files are chunked in your Next.js application.

](cssChunking/index.md)[

### deploymentId

Configure a deployment identifier used for version skew protection and cache busting.

](deploymentId/index.md)[

### devIndicators

Configuration options for the on-screen indicator that gives context about the current route you're viewing during development.

](devIndicators/index.md)[

### distDir

Set a custom build directory to use instead of the default .next directory.

](distDir/index.md)[

### env

Learn to add and access environment variables in your Next.js application at build time.

](env/index.md)[

### expireTime

Customize stale-while-revalidate expire time for ISR enabled pages.

](expireTime/index.md)[

### exportPathMap

Customize the pages that will be exported as HTML files when using \`next export\`.

](exportPathMap/index.md)[

### generateBuildId

Configure the build id, which is used to identify the current build in which your application is being served.

](generateBuildId/index.md)[

### generateEtags

Next.js will generate etags for every page by default. Learn more about how to disable etag generation here.

](generateEtags/index.md)[

### headers

Add custom HTTP headers to your Next.js app.

](headers/index.md)[

### htmlLimitedBots

Specify a list of user agents that should receive blocking metadata.

](htmlLimitedBots/index.md)[

### httpAgentOptions

Next.js will automatically use HTTP Keep-Alive by default. Learn more about how to disable HTTP Keep-Alive here.

](httpAgentOptions/index.md)[

### images

Custom configuration for the next/image loader

](images/index.md)[

### cacheHandler

Configure the Next.js cache used for storing and revalidating data to use any external service like Redis, Memcached, or others.

](incrementalCacheHandlerPath/index.md)[

### inlineCss

Enable inline CSS support.

](inlineCss/index.md)[

### logging

Configure logging behavior in the terminal when running Next.js in development mode, including fetch logging, incoming requests, and forwarding browser console logs to the terminal.

](logging/index.md)[

### mdxRs

Use the new Rust compiler to compile MDX files in the App Router.

](mdxRs/index.md)[

### onDemandEntries

Configure how Next.js will dispose and keep in memory pages created in development.

](onDemandEntries/index.md)[

### optimizePackageImports

API Reference for optimizePackageImports Next.js Config Option

](optimizePackageImports/index.md)[

### output

Next.js automatically traces which files are needed by each page to allow for easy deployment of your application. Learn how it works here.

](output/index.md)[

### pageExtensions

Extend the default page extensions used by Next.js when resolving pages in the Pages Router.

](pageExtensions/index.md)[

### poweredByHeader

Next.js will add the \`x-powered-by\` header by default. Learn to opt-out of it here.

](poweredByHeader/index.md)[

### productionBrowserSourceMaps

Enables browser source map generation during the production build.

](productionBrowserSourceMaps/index.md)[

### proxyClientMaxBodySize

Configure the maximum request body size when using proxy.

](proxyClientMaxBodySize/index.md)[

### reactCompiler

Enable the React Compiler to automatically optimize component rendering.

](reactCompiler/index.md)[

### reactMaxHeadersLength

The maximum length of the headers that are emitted by React and added to the response.

](reactMaxHeadersLength/index.md)[

### reactStrictMode

The complete Next.js runtime is now Strict Mode-compliant, learn how to opt-in

](reactStrictMode/index.md)[

### redirects

Add redirects to your Next.js app.

](redirects/index.md)[

### rewrites

Add rewrites to your Next.js app.

](rewrites/index.md)[

### sassOptions

Configure Sass options.

](sassOptions/index.md)[

### serverActions

Configure Server Actions behavior in your Next.js application.

](serverActions/index.md)[

### serverComponentsHmrCache

Configure whether fetch responses in Server Components are cached across HMR refresh requests.

](serverComponentsHmrCache/index.md)[

### serverExternalPackages

Opt-out specific dependencies from the Server Components bundling and use native Node.js \`require\`.

](serverExternalPackages/index.md)[

### staleTimes

Learn how to override the invalidation time of the client cache.

](staleTimes/index.md)[

### staticGeneration\*

Learn how to configure static generation in your Next.js application.

](staticGeneration/index.md)[

### taint

Enable tainting Objects and Values.

](taint/index.md)[

### trailingSlash

Configure Next.js pages to resolve with or without a trailing slash.

](trailingSlash/index.md)[

### transpilePackages

Automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (\`node\_modules\`).

](transpilePackages/index.md)[

### turbopack

Configure Next.js with Turbopack-specific options

](turbopack/index.md)[

### turbopackFileSystemCache

Learn how to enable FileSystem Caching for Turbopack builds

](turbopackFileSystemCache/index.md)[

### turbopack.ignoreIssue

Suppress specific Turbopack errors and warnings from the CLI output and error overlay.

](turbopackIgnoreIssue/index.md)[

### typedRoutes

Enable support for statically typed links.

](typedRoutes/index.md)[

### typescript

Configure how Next.js handles TypeScript errors during production builds and specify a custom tsconfig file.

](typescript/index.md)[

### urlImports

Configure Next.js to allow importing modules from external URLs.

](urlImports/index.md)[

### useLightningcss

Enable experimental support for Lightning CSS.

](useLightningcss/index.md)[

### viewTransition

Enable ViewTransition API from React in App Router

](viewTransition/index.md)[

### webpack

Learn how to customize the webpack config used by Next.js

](webpack/index.md)[

### webVitalsAttribution

Learn how to use the webVitalsAttribution option to pinpoint the source of Web Vitals issues.

](webVitalsAttribution/index.md)

Was this helpful?
