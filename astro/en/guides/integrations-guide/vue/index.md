---
title: "@astrojs/\n\t\t\t\t\tvue"
source: "https://docs.astro.build/en/guides/integrations-guide/vue/"
canonical_url: "https://docs.astro.build/en/guides/integrations-guide/vue/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:59.675Z"
content_hash: "4a99edf75679625d99534d21a7d87fe78080fcf6197f976e928f29daa2dadd3e"
menu_path: ["@astrojs/\n\t\t\t\t\tvue"]
section_path: []
nav_prev: {"path": "../svelte/index.md", "title": "@astrojs/\n\t\t\t\t\tsvelte"}
nav_next: {"path": "../cloudflare/index.md", "title": "@astrojs/\n\t\t\t\t\tcloudflare"}
---

# @astrojs/ vue

v6.0.1 [GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/vue/) [npm](https://www.npmjs.com/package/@astrojs/vue) [Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/vue/CHANGELOG.md)

This **[Astro integration](/en/guides/integrations/)** enables rendering and client-side hydration for your [Vue 3](https://vuejs.org/) components.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/vue`, run the following from your project directory and follow the prompts:

*   [npm](#tab-panel-1766)
*   [pnpm](#tab-panel-1767)
*   [Yarn](#tab-panel-1768)

```
npx astro add vue
```

If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/vue` package:

*   [npm](#tab-panel-1769)
*   [pnpm](#tab-panel-1770)
*   [Yarn](#tab-panel-1771)

```
npm install @astrojs/vue
```

Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'vue'` (or similar) warning when you start up Astro, you’ll need to install Vue:

*   [npm](#tab-panel-1772)
*   [pnpm](#tab-panel-1773)
*   [Yarn](#tab-panel-1774)

```
npm install vue
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

```
import { defineConfig } from 'astro/config';import vue from '@astrojs/vue';
export default defineConfig({  // ...  integrations: [vue()],});
```

## Getting started

[Section titled “Getting started”](#getting-started)

To use your first Vue component in Astro, head to our [UI framework documentation](/en/guides/framework-components/#using-framework-components). You’ll explore:

*   📦 how framework components are loaded,
*   💧 client-side hydration options, and
*   🤝 opportunities to mix and nest frameworks together

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

For help, check out the `#support` channel on [Discord](https://astro.build/chat). Our friendly Support Squad members are here to help!

You can also check our [Astro Integration Documentation](/en/guides/integrations/) for more on integrations.

## Contributing

[Section titled “Contributing”](#contributing)

This package is maintained by Astro’s Core team. You’re welcome to submit an issue or PR!

## Options

[Section titled “Options”](#options)

This integration is powered by `@vitejs/plugin-vue`. To customize the Vue compiler, options can be provided to the integration. See the `@vitejs/plugin-vue` [docs](https://www.npmjs.com/package/@vitejs/plugin-vue) for more details.

```
import { defineConfig } from 'astro/config';import vue from '@astrojs/vue';
export default defineConfig({  // ...  integrations: [    vue({      template: {        compilerOptions: {          // treat any tag that starts with ion- as custom elements          isCustomElement: (tag) => tag.startsWith('ion-'),        },      },      // ...    }),  ],});
```

### `appEntrypoint`

[Section titled “appEntrypoint”](#appentrypoint)

**Type:** `string`  

**Added in:** `@astrojs/vue@1.2.0`

You can extend the Vue `app` instance setting the `appEntrypoint` option to a root-relative import specifier (for example, `appEntrypoint: "/src/pages/_app"`).

The default export of this file should be a function that accepts a Vue `App` instance prior to rendering, allowing the use of [custom Vue plugins](https://vuejs.org/guide/reusability/plugins.html), `app.use`, and other customizations for advanced use cases.

```
import { defineConfig } from 'astro/config';import vue from '@astrojs/vue';
export default defineConfig({  // ...  integrations: [vue({ appEntrypoint: '/src/pages/_app' })],});
```

```
import type { App } from 'vue';import i18nPlugin from 'my-vue-i18n-plugin';
export default (app: App) => {  app.use(i18nPlugin);};
```

### `jsx`

[Section titled “jsx”](#jsx)

**Type:** `boolean | object`  

**Added in:** `@astrojs/vue@1.2.0`

You can use Vue JSX by setting `jsx: true`.

```
import { defineConfig } from 'astro/config';import vue from '@astrojs/vue';
export default defineConfig({  // ...  integrations: [vue({ jsx: true })],});
```

This will enable rendering for both Vue and Vue JSX components. To customize the Vue JSX compiler, pass an options object instead of a boolean. See the `@vitejs/plugin-vue-jsx` [docs](https://www.npmjs.com/package/@vitejs/plugin-vue-jsx) for more details.

```
import { defineConfig } from 'astro/config';import vue from '@astrojs/vue';
export default defineConfig({  // ...  integrations: [    vue({      jsx: {        // treat any tag that starts with ion- as custom elements        isCustomElement: (tag) => tag.startsWith('ion-'),      },    }),  ],});
```

### `devtools`

[Section titled “devtools”](#devtools)

**Type:** `boolean | object`  

**Added in:** `@astrojs/vue@4.2.0`

You can enable [Vue DevTools](https://devtools-next.vuejs.org/) in development by passing an object with `devtools: true` to your `vue()` integration config:

```
import { defineConfig } from 'astro/config';import vue from '@astrojs/vue';
export default defineConfig({  // ...  integrations: [vue({ devtools: true })],});
```

#### Customizing Vue DevTools

[Section titled “Customizing Vue DevTools”](#customizing-vue-devtools)

**Added in:** `@astrojs/vue@4.3.0`

For more customization, you can instead pass options that the [Vue DevTools Vite Plugin](https://devtools-next.vuejs.org/guide/vite-plugin#options) supports. (Note: `appendTo` is not supported.)

For example, you can set `launchEditor` to your preferred editor if you are not using Visual Studio Code:

```
import { defineConfig } from "astro/config";import vue from "@astrojs/vue";
export default defineConfig({  // ...  integrations: [    vue({      devtools: { launchEditor: "webstorm" },    }),  ],});
```

## More integrations

### Front-end frameworks

*   ![](/logos/alpine-js.svg)
    
    ### [@astrojs/alpinejs](/en/guides/integrations-guide/alpinejs/)
    
*   ![](/logos/preact.svg)
    
    ### [@astrojs/preact](/en/guides/integrations-guide/preact/)
    
*   ![](/logos/react.svg)
    
    ### [@astrojs/react](/en/guides/integrations-guide/react/)
    
*   ![](/logos/solid.svg)
    
    ### [@astrojs/solid⁠-⁠js](/en/guides/integrations-guide/solid-js/)
    
*   ![](/logos/svelte.svg)
    
    ### [@astrojs/svelte](/en/guides/integrations-guide/svelte/)
    
*   ![](/logos/vue.svg)
    
    ### [@astrojs/vue](/en/guides/integrations-guide/vue/)
    

### Adapters

*   ![](/logos/cloudflare-pages.svg)
    
    ### [@astrojs/cloudflare](/en/guides/integrations-guide/cloudflare/)
    
*   ![](/logos/netlify.svg)
    
    ### [@astrojs/netlify](/en/guides/integrations-guide/netlify/)
    
*   ![](/logos/node.svg)
    
    ### [@astrojs/node](/en/guides/integrations-guide/node/)
    
*   ![](/logos/vercel.svg)
    
    ### [@astrojs/vercel](/en/guides/integrations-guide/vercel/)
    

### Other integrations

*   ![](/logos/db.svg)
    
    ### [@astrojs/db](/en/guides/integrations-guide/db/)
    
*   ![](/logos/markdoc.svg)
    
    ### [@astrojs/markdoc](/en/guides/integrations-guide/markdoc/)
    
*   ![](/logos/mdx.svg)
    
    ### [@astrojs/mdx](/en/guides/integrations-guide/mdx/)
    
*   ![](/logos/partytown.svg)
    
    ### [@astrojs/partytown](/en/guides/integrations-guide/partytown/)
    
*   ![](/logos/sitemap.svg)
    
    ### [@astrojs/sitemap](/en/guides/integrations-guide/sitemap/)
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
