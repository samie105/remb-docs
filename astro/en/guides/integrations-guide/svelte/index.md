---
title: "@astrojs/\n\t\t\t\t\tsvelte"
source: "https://docs.astro.build/en/guides/integrations-guide/svelte/"
canonical_url: "https://docs.astro.build/en/guides/integrations-guide/svelte/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:49.747Z"
content_hash: "5a70e2177dbfba8681a09d871d87d50baa8c91a9d80fadc695ca2da3df96f7db"
menu_path: ["@astrojs/\n\t\t\t\t\tsvelte"]
section_path: []
nav_prev: {"path": "astro/en/guides/integrations-guide/solid-js/index.md", "title": "@astrojs/\n\t\t\t\t\tsolid-js"}
nav_next: {"path": "astro/en/guides/integrations-guide/vue/index.md", "title": "@astrojs/\n\t\t\t\t\tvue"}
---

# @astrojs/ svelte

v8.0.5 [GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/svelte/) [npm](https://www.npmjs.com/package/@astrojs/svelte) [Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/svelte/CHANGELOG.md)

This **[Astro integration](../../integrations/index.md)** enables rendering and client-side hydration for your [Svelte](https://svelte.dev/) 5 components. For Svelte 3 and 4 support, install `@astrojs/svelte@5` instead.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/svelte`, run the following from your project directory and follow the prompts:

*   [npm](#tab-panel-1748)
*   [pnpm](#tab-panel-1749)
*   [Yarn](#tab-panel-1750)

```
npx astro add svelte
```

If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/svelte` package:

*   [npm](#tab-panel-1751)
*   [pnpm](#tab-panel-1752)
*   [Yarn](#tab-panel-1753)

```
npm install @astrojs/svelte
```

Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'svelte'` (or similar) warning when you start up Astro, you’ll need to install Svelte and TypeScript:

*   [npm](#tab-panel-1754)
*   [pnpm](#tab-panel-1755)
*   [Yarn](#tab-panel-1756)

```
npm install svelte typescript
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

```
import { defineConfig } from 'astro/config';import svelte from '@astrojs/svelte';
export default defineConfig({  // ...  integrations: [svelte()],});
```

And create a new file called `svelte.config.js` in your project root directory and add the following code:

```
import { vitePreprocess } from '@astrojs/svelte';
export default {  preprocess: vitePreprocess(),}
```

## Getting started

[Section titled “Getting started”](#getting-started)

To use your first Svelte component in Astro, head to our [UI framework documentation](../../framework-components/index.md#using-framework-components). You’ll explore:

*   📦 how framework components are loaded,
*   💧 client-side hydration options, and
*   🤝 opportunities to mix and nest frameworks together

## Options

[Section titled “Options”](#options)

This integration is powered by `@sveltejs/vite-plugin-svelte`. To customize the Svelte compiler, options can be provided to the integration. See the [`@sveltejs/vite-plugin-svelte` docs](https://github.com/sveltejs/vite-plugin-svelte/blob/HEAD/docs/config.md) for more details.

You can set options either by passing them to the `svelte` integration in `astro.config.mjs` or in `svelte.config.js`. The options in `astro.config.mjs` will take precedence over the options in `svelte.config.js` if both are present:

```
import { defineConfig } from 'astro/config';import svelte from '@astrojs/svelte';
export default defineConfig({  integrations: [svelte({ extensions: ['.svelte'] })],});
```

```
export default {  extensions: ['.svelte'],};
```

## Preprocessors

[Section titled “Preprocessors”](#preprocessors)

**Added in:** `@astrojs/svelte@2.0.0`

If you’re using SCSS or Stylus in your Svelte files, you can create a `svelte.config.js` file so that they are preprocessed by Svelte, and the Svelte IDE extension can correctly parse the Svelte files.

```
import { vitePreprocess } from '@astrojs/svelte';
export default {  preprocess: vitePreprocess(),};
```

This config file will be automatically added for you when you run `astro add svelte`. See the [`@sveltejs/vite-plugin-svelte` docs](https://github.com/sveltejs/vite-plugin-svelte/blob/HEAD/docs/preprocess.md) for more details about `vitePreprocess`.

## More integrations

### Front-end frameworks

*   ![](/logos/alpine-js.svg)
    
    ### [@astrojs/alpinejs](../alpinejs/index.md)
    
*   ![](/logos/preact.svg)
    
    ### [@astrojs/preact](../preact/index.md)
    
*   ![](/logos/react.svg)
    
    ### [@astrojs/react](../react/index.md)
    
*   ![](/logos/solid.svg)
    
    ### [@astrojs/solid⁠-⁠js](../solid-js/index.md)
    
*   ![](/logos/svelte.svg)
    
    ### [@astrojs/svelte](index.md)
    
*   ![](/logos/vue.svg)
    
    ### [@astrojs/vue](../vue/index.md)
    

### Adapters

*   ![](/logos/cloudflare-pages.svg)
    
    ### [@astrojs/cloudflare](../cloudflare/index.md)
    
*   ![](/logos/netlify.svg)
    
    ### [@astrojs/netlify](/en/guides/integrations-guide/netlify/)
    
*   ![](/logos/node.svg)
    
    ### [@astrojs/node](../node/index.md)
    
*   ![](/logos/vercel.svg)
    
    ### [@astrojs/vercel](../vercel/index.md)
    

### Other integrations

*   ![](/logos/db.svg)
    
    ### [@astrojs/db](../db/index.md)
    
*   ![](/logos/markdoc.svg)
    
    ### [@astrojs/markdoc](../markdoc/index.md)
    
*   ![](/logos/mdx.svg)
    
    ### [@astrojs/mdx](../mdx/index.md)
    
*   ![](/logos/partytown.svg)
    
    ### [@astrojs/partytown](../partytown/index.md)
    
*   ![](/logos/sitemap.svg)
    
    ### [@astrojs/sitemap](../sitemap/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
