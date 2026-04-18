---
title: "@astrojs/\n\t\t\t\t\tpreact"
source: "https://docs.astro.build/en/guides/integrations-guide/preact/"
canonical_url: "https://docs.astro.build/en/guides/integrations-guide/preact/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:22.654Z"
content_hash: "bf83714aa6e1c0f11a3919c656c9a63379c7520f503f8b0efc32e309e5ee592f"
menu_path: ["@astrojs/\n\t\t\t\t\tpreact"]
section_path: []
---
# @astrojs/ preact

v5.1.1 [GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/preact/) [npm](https://www.npmjs.com/package/@astrojs/preact) [Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/preact/CHANGELOG.md)

This **[Astro integration](/en/guides/integrations/)** enables rendering and client-side hydration for your [Preact](https://preactjs.com/) components.

## Why Preact?

[Section titled “Why Preact?”](#why-preact)

Preact is a library that lets you build interactive UI components for the web. If you want to build interactive features on your site using JavaScript, you may prefer using its component format instead of using browser APIs directly.

Preact is also a great choice if you have previously used React. Preact provides the same API as React, but in a much smaller 3kB package. It even supports rendering many React components using the `compat` configuration option (see below).

**Want to learn more about Preact before using this integration?**  
Check out [“Learn Preact”](https://preactjs.com/tutorial), an interactive tutorial on their website.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/preact`, run the following from your project directory and follow the prompts:

*   [npm](#tab-panel-1712)
*   [pnpm](#tab-panel-1713)
*   [Yarn](#tab-panel-1714)

```
npx astro add preact
```

If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/preact` package:

*   [npm](#tab-panel-1715)
*   [pnpm](#tab-panel-1716)
*   [Yarn](#tab-panel-1717)

```
npm install @astrojs/preact
```

Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'preact'` (or similar) warning when you start up Astro, you’ll need to install Preact:

*   [npm](#tab-panel-1718)
*   [pnpm](#tab-panel-1719)
*   [Yarn](#tab-panel-1720)

```
npm install preact
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

```
import { defineConfig } from 'astro/config';import preact from '@astrojs/preact';
export default defineConfig({  // ...  integrations: [preact()],});
```

And add the following code to the `tsconfig.json` file.

```
{  "extends": "astro/tsconfigs/strict",  "include": [".astro/types.d.ts", "**/*"],  "exclude": ["dist"],  "compilerOptions": {    "jsx": "react-jsx",    "jsxImportSource": "preact"  }}
```

## Usage

[Section titled “Usage”](#usage)

To use your first Preact component in Astro, head to our [UI framework documentation](/en/guides/framework-components/#using-framework-components). You’ll explore:

*   📦 how framework components are loaded,
*   💧 client-side hydration options, and
*   🤝 opportunities to mix and nest frameworks together

Also check our [Astro Integration Documentation](/en/guides/integrations/) for more on integrations.

## Configuration

[Section titled “Configuration”](#configuration)

The Astro Preact integration handles how Preact components are rendered and it has its own options. Change these in the `astro.config.mjs` file which is where your project’s integration settings live.

For basic usage, you do not need to configure the Preact integration.

### `compat`

[Section titled “compat”](#compat)

**Type:** `boolean`  

**Added in:** `@astrojs/preact@0.3.0`

You can enable `preact/compat`, Preact’s compatibility layer for rendering React components without needing to install or ship React’s larger libraries to your users’ web browsers.

To do so, pass an object to the Preact integration and set `compat: true`.

```
import { defineConfig } from 'astro/config';import preact from '@astrojs/preact';
export default defineConfig({  integrations: [preact({ compat: true })],});
```

With the `compat` option enabled, the Preact integration will render React components as well as Preact components in your project and also allow you to import React components inside Preact components. Read more in [“Switching to Preact (from React)”](https://preactjs.com/guide/v10/switching-to-preact) on the Preact website.

When importing React component libraries, in order to swap out the `react` and `react-dom` dependencies as `preact/compat`, you can use [`overrides`](https://docs.npmjs.com/cli/v8/configuring-npm/package-json#overrides) to do so.

```
{  "overrides": {    "react": "npm:@preact/compat@latest",    "react-dom": "npm:@preact/compat@latest"  }}
```

Check out the [`pnpm` overrides](https://pnpm.io/package_json#pnpmoverrides) and [`yarn` resolutions](https://yarnpkg.com/configuration/manifest#resolutions) docs for their respective overrides features.

### `babel`

[Section titled “babel”](#babel)

**Type:** [`BabelOptions`](https://github.com/preactjs/preset-vite#babel-configuration)  

**Added in:** `@astrojs/preact@5.1.0` New

You can pass additional [Babel configuration options](https://babeljs.io/docs/options) to the Preact Vite plugin. This allows you to customize the Babel transformation applied to your Preact components.

For example, the following configuration tells Babel to load `.babelrc` when processing your Preact components:

```
import { defineConfig } from 'astro/config';import preact from '@astrojs/preact';
export default defineConfig({  integrations: [    preact({      babel: {        babelrc: true,      },    }),  ],});
```

### `devtools`

[Section titled “devtools”](#devtools)

**Type:** `boolean`  

**Added in:** `@astrojs/preact@3.3.0`

You can enable [Preact devtools](https://preactjs.github.io/preact-devtools/) in development by passing an object with `devtools: true` to your `preact()` integration config:

```
import { defineConfig } from 'astro/config';import preact from '@astrojs/preact';
export default defineConfig({  // ...  integrations: [preact({ devtools: true })],});
```

## Options

[Section titled “Options”](#options)

### Combining multiple JSX frameworks

[Section titled “Combining multiple JSX frameworks”](#combining-multiple-jsx-frameworks)

When you are using multiple JSX frameworks (React, Preact, Solid) in the same project, Astro needs to determine which JSX framework-specific transformations should be used for each of your components. If you have only added one JSX framework integration to your project, no extra configuration is needed.

Use the `include` (required) and `exclude` (optional) configuration options to specify which files belong to which framework. Provide an array of files and/or folders to `include` for each framework you are using. Wildcards may be used to include multiple file paths.

We recommend placing common framework components in the same folder (e.g. `/components/react/` and `/components/solid/`) to make specifying your includes easier, but this is not required:

```
import { defineConfig } from 'astro/config';import preact from '@astrojs/preact';import react from '@astrojs/react';import svelte from '@astrojs/svelte';import vue from '@astrojs/vue';import solid from '@astrojs/solid-js';
export default defineConfig({  // Enable many frameworks to support all different kinds of components.  // No `include` is needed if you are only using a single JSX framework!  integrations: [    preact({      include: ['**/preact/*'],    }),    react({      include: ['**/react/*'],    }),    solid({      include: ['**/solid/*'],    }),  ],});
```

## Examples

[Section titled “Examples”](#examples)

*   The [Astro Preact example](https://github.com/withastro/astro/tree/latest/examples/framework-preact) shows how to use an interactive Preact component in an Astro project.
*   The [Astro Nanostores example](https://github.com/withastro/astro/tree/latest/examples/with-nanostores) shows how to share state between different components — and even different frameworks! — in an Astro project.

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
