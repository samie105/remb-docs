---
title: "@astrojs/\n\t\t\t\t\talpinejs"
source: "https://docs.astro.build/en/guides/integrations-guide/alpinejs/"
canonical_url: "https://docs.astro.build/en/guides/integrations-guide/alpinejs/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:37.644Z"
content_hash: "65ec82502416488d20a490738a05ed0bf6e1329a8614758f1d9d79afe3aa69d1"
menu_path: ["@astrojs/\n\t\t\t\t\talpinejs"]
section_path: []
nav_prev: {"path": "astro/en/reference/error-reference/index.md", "title": "Error reference"}
nav_next: {"path": "astro/en/guides/integrations-guide/preact/index.md", "title": "@astrojs/\n\t\t\t\t\tpreact"}
---

# @astrojs/ alpinejs

v0.5.0 [GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/alpinejs/) [npm](https://www.npmjs.com/package/@astrojs/alpinejs) [Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/alpinejs/CHANGELOG.md)

This **[Astro integration](/en/guides/integrations/)** adds [Alpine.js](https://alpinejs.dev/) to your project so that you can use Alpine.js anywhere on your page.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/alpinejs`, run the following from your project directory and follow the prompts:

*   [npm](#tab-panel-1658)
*   [pnpm](#tab-panel-1659)
*   [Yarn](#tab-panel-1660)

```
npx astro add alpinejs
```

If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/alpinejs` package.

*   [npm](#tab-panel-1661)
*   [pnpm](#tab-panel-1662)
*   [Yarn](#tab-panel-1663)

```
npm install @astrojs/alpinejs
```

Most package managers will install associated peer dependencies as well. However, if you see a `Cannot find package 'alpinejs'` (or similar) warning when you start up Astro, you’ll need to manually install Alpine.js yourself:

*   [npm](#tab-panel-1664)
*   [pnpm](#tab-panel-1665)
*   [Yarn](#tab-panel-1666)

```
npm install alpinejs @types/alpinejs
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

```
import { defineConfig } from 'astro/config';import alpinejs from '@astrojs/alpinejs';
export default defineConfig({  // ...  integrations: [alpinejs()],});
```

## Configuration Options

[Section titled “Configuration Options”](#configuration-options)

### `entrypoint`

[Section titled “entrypoint”](#entrypoint)

**Type:** `string`  

**Added in:** `@astrojs/alpinejs@0.4.0`

You can extend Alpine by setting the `entrypoint` option to a root-relative import specifier (e.g. `entrypoint: "/src/entrypoint"`).

The default export of this file should be a function that accepts an Alpine instance prior to starting. This allows the use of custom directives, plugins and other customizations for advanced use cases.

```
import { defineConfig } from 'astro/config';import alpinejs from '@astrojs/alpinejs';
export default defineConfig({  // ...  integrations: [alpinejs({ entrypoint: '/src/entrypoint' })],});
```

```
import type { Alpine } from 'alpinejs'import intersect from '@alpinejs/intersect'
export default (Alpine: Alpine) => {    Alpine.plugin(intersect)}
```

## Usage

[Section titled “Usage”](#usage)

Once the integration is installed, you can use [Alpine.js](https://alpinejs.dev/) directives and syntax inside any Astro component. The Alpine.js script is automatically added and enabled on every page of your website so no client directives are needed. Add plugin scripts to the page `<head>`.

The following example adds [Alpine’s Collapse plugin](https://alpinejs.dev/plugins/collapse) to expand and collapse paragraph text:

```
------<html>  <head>    <!-- ... -->    <script defer src="https://cdn.jsdelivr.net/npm/@alpinejs/collapse@3.x.x/dist/cdn.min.js"></script>  </head>  <body>    <!-- ... -->    <div x-data="{ expanded: false }">      <button @click="expanded = ! expanded">Toggle Content</button>
      <p id="foo" x-show="expanded" x-collapse>        Lorem ipsum      </p>    </div>  </body></html>
```

## Intellisense for TypeScript

[Section titled “Intellisense for TypeScript”](#intellisense-for-typescript)

The `@astrojs/alpine` integration adds `Alpine` to [the global window object](/en/guides/typescript/#window-and-globalthis). For IDE autocompletion, add the following to your `src/env.d.ts`:

```
interface Window {  Alpine: import('alpinejs').Alpine;}
```

## Examples

[Section titled “Examples”](#examples)

*   The [Astro Alpine.js example](https://github.com/withastro/astro/tree/main/examples/framework-alpine) shows how to use Alpine.js in an Astro project.

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


