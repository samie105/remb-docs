---
title: "Custom Webpack Config"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:58.638Z"
content_hash: "a526db3bddd706199df830502e2a6642cff8748b6de7d8957c48fe92b5343926"
menu_path: ["Custom Webpack Config"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/viewTransition/index.md", "title": "viewTransition"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/webVitalsAttribution/index.md", "title": "webVitalsAttribution"}
---

# Custom Webpack Config

Last updated April 23, 2026

> **Good to know**: changes to webpack config are not covered by semver so proceed at your own risk

Before continuing to add custom webpack configuration to your application make sure Next.js doesn't already support your use-case:

-   [CSS imports](../../../../getting-started/css/index.md)
-   [CSS modules](../../../../getting-started/css/index.md#css-modules)
-   [Sass/SCSS imports](../../../../guides/sass/index.md)
-   [Sass/SCSS modules](../../../../guides/sass/index.md)

Some commonly asked for features are available as plugins:

-   [@next/mdx](https://github.com/vercel/next.js/tree/canary/packages/next-mdx)
-   [@next/bundle-analyzer](https://github.com/vercel/next.js/tree/canary/packages/next-bundle-analyzer)

In order to extend our usage of `webpack`, you can define a function that extends its config inside `next.config.js`, like so:

next.config.js

```
module.exports = {
  webpack: (
    config,
    { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
  ) => {
    // Important: return the modified config
    return config
  },
}
```

> The `webpack` function is executed three times, twice for the server (nodejs / edge runtime) and once for the client. This allows you to distinguish between client and server configuration using the `isServer` property.

The second argument to the `webpack` function is an object with the following properties:

-   `buildId`: `String` - The build id, used as a unique identifier between builds.
-   `dev`: `Boolean` - Indicates if the compilation will be done in development.
-   `isServer`: `Boolean` - It's `true` for server-side compilation, and `false` for client-side compilation.
-   `nextRuntime`: `String | undefined` - The target runtime for server-side compilation; either `"edge"` or `"nodejs"`, it's `undefined` for client-side compilation.
-   `defaultLoaders`: `Object` - Default loaders used internally by Next.js:
    -   `babel`: `Object` - Default `babel-loader` configuration.

Example usage of `defaultLoaders.babel`:

```
// Example config for adding a loader that depends on babel-loader
// This source was taken from the @next/mdx plugin source:
// https://github.com/vercel/next.js/tree/canary/packages/next-mdx
module.exports = {
  webpack: (config, options) => {
    config.module.rules.push({
      test: /\.mdx/,
      use: [
        options.defaultLoaders.babel,
        {
          loader: '@mdx-js/loader',
          options: pluginOptions.options,
        },
      ],
    })
 
    return config
  },
}
```

#### `nextRuntime`[](#nextruntime)

Notice that `isServer` is `true` when `nextRuntime` is `"edge"` or `"nodejs"`, `nextRuntime` `"edge"` is currently for proxy and Server Components in edge runtime only.

Was this helpful?
