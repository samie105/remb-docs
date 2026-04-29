---
title: "Custom Webpack Config"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:21:10.690Z"
content_hash: "244e3f14b0acfd6b1a2b676e09ecb524c20fe013b4140aec0644de1f930916d2"
menu_path: ["Custom Webpack Config"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../useLightningcss/index.md", "title": "useLightningcss"}
nav_next: {"path": "../webVitalsAttribution/index.md", "title": "webVitalsAttribution"}
---

# Custom Webpack Config

Last updated April 23, 2026

> **Good to know**: changes to webpack config are not covered by semver so proceed at your own risk

Before continuing to add custom webpack configuration to your application make sure Next.js doesn't already support your use-case:

-   [CSS imports](/docs/app/getting-started/css)
-   [CSS modules](/docs/app/getting-started/css)
-   [Sass/SCSS imports](/docs/pages/guides/sass)
-   [Sass/SCSS modules](/docs/pages/guides/sass)
-   [Customizing babel configuration](/docs/pages/guides/babel)

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
