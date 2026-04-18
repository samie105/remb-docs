---
title: "Working with integrations"
source: "https://docs.astro.build/en/guides/integrations/"
canonical_url: "https://docs.astro.build/en/guides/integrations/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:11.768Z"
content_hash: "15fe91fdd119d243d2ba6a9e459bc7f9ffdd3e9c0e9a4330ccc78fcd2cf11ae5"
menu_path: ["Working with integrations"]
section_path: []
nav_prev: {"path": "astro/en/guides/environment-variables/index.md", "title": "Using environment variables"}
nav_next: {"path": "astro/en/guides/build-with-ai/index.md", "title": "Building Astro sites with AI tools"}
---

# Working with integrations

**Astro integrations** add new functionality and behaviors for your project with only a few lines of code. You can use an official integration, [integrations built by the community](#finding-more-integrations) or even [build a custom integration yourself](#building-your-own-integration).

Integrations can…

*   Unlock React, Vue, Svelte, Solid, and other popular UI frameworks with a [renderer](/en/guides/framework-components/).
*   Enable on-demand rendering with an [SSR adapter](/en/guides/on-demand-rendering/).
*   Integrate tools like MDX, and Partytown with a few lines of code.
*   Add new features to your project, like automatic sitemap generation.
*   Write custom code that hooks into the build process, dev server, and more.

## Official integrations

[Section titled “Official integrations”](#official-integrations)

The following integrations are maintained by Astro.

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
    

## Automatic integration setup

[Section titled “Automatic integration setup”](#automatic-integration-setup)

Astro includes an `astro add` command to automate the setup of official integrations. Several community plugins can also be added using this command. Please check each integration’s own documentation to see whether `astro add` is supported, or whether you must [install manually](#manual-installation).

Run the `astro add` command using the package manager of your choice and our automatic integration wizard will update your configuration file and install any necessary dependencies.

*   [npm](#tab-panel-1631)
*   [pnpm](#tab-panel-1632)
*   [Yarn](#tab-panel-1633)

```
npx astro add react
```

It’s even possible to add multiple integrations at the same time!

*   [npm](#tab-panel-1634)
*   [pnpm](#tab-panel-1635)
*   [Yarn](#tab-panel-1636)

```
npx astro add react sitemap partytown
```

### Manual installation

[Section titled “Manual installation”](#manual-installation)

Astro integrations are always added through the `integrations` property in your `astro.config.mjs` file.

There are three common ways to import an integration into your Astro project:

1.  [Install an npm package integration](#installing-an-npm-package).
    
2.  Import your own integration from a local file inside your project.
    
3.  Write your integration inline, directly in your config file.
    
    ```
    import { defineConfig } from 'astro/config';import installedIntegration from '@astrojs/vue';import localIntegration from './my-integration.js';
    export default defineConfig({  integrations: [    // 1. Imported from an installed npm package    installedIntegration(),    // 2. Imported from a local JS file    localIntegration(),    // 3. An inline object    { name: 'namespace:id', hooks: { /* ... */ } },  ]});
    ```
    

Check out the [Integration API](/en/reference/integrations-reference/) reference to learn all of the different ways that you can write an integration.

#### Installing an npm package

[Section titled “Installing an npm package”](#installing-an-npm-package)

Install an npm package integration using a package manager, and then update `astro.config.mjs` manually.

For example, to install the `@astrojs/sitemap` integration:

1.  Install the integration to your project dependencies using your preferred package manager:
    
    *   [npm](#tab-panel-1640)
    *   [pnpm](#tab-panel-1641)
    *   [Yarn](#tab-panel-1642)
    
    ```
    npm install @astrojs/sitemap
    ```
    
2.  Import the integration to your `astro.config.mjs` file, and add it to your `integrations[]` array, along with any configuration options:
    
    ```
    import { defineConfig } from 'astro/config';import sitemap from '@astrojs/sitemap';
    export default defineConfig({  // ...  integrations: [sitemap()],  // ...});
    ```
    
    Note that different integrations may have different configuration settings. Read each integration’s documentation, and apply any necessary config options to your chosen integration in `astro.config.mjs`.
    

### Custom options

[Section titled “Custom options”](#custom-options)

Integrations are almost always authored as factory functions that return the actual integration object. This lets you pass arguments and options to the factory function that customize the integration for your project.

```
integrations: [  // Example: Customize your integration with function arguments  sitemap({ filter: true })]
```

### Toggle an integration

[Section titled “Toggle an integration”](#toggle-an-integration)

Falsy integrations are ignored, so you can toggle integrations on & off without worrying about left-behind `undefined` and boolean values.

```
integrations: [  // Example: Skip building a sitemap on Windows  process.platform !== 'win32' && sitemap()]
```

## Upgrading integrations

[Section titled “Upgrading integrations”](#upgrading-integrations)

To upgrade all official integrations at once, run the `@astrojs/upgrade` command. This will upgrade both Astro and all official integrations to their latest versions.

### Automatic upgrading

[Section titled “Automatic upgrading”](#automatic-upgrading)

*   [npm](#tab-panel-1643)
*   [pnpm](#tab-panel-1644)
*   [Yarn](#tab-panel-1645)

```
# Upgrade Astro and official integrations together to latestnpx @astrojs/upgrade
```

### Manual upgrading

[Section titled “Manual upgrading”](#manual-upgrading)

To upgrade one or more integrations manually, use the appropriate command for your package manager.

*   [npm](#tab-panel-1646)
*   [pnpm](#tab-panel-1647)
*   [Yarn](#tab-panel-1648)

```
# Example: upgrade React and Partytown integrationsnpm install @astrojs/react@latest @astrojs/partytown@latest
```

## Removing an integration

[Section titled “Removing an integration”](#removing-an-integration)

1.  To remove an integration, first uninstall the integration from your project.
    
    *   [npm](#tab-panel-1649)
    *   [pnpm](#tab-panel-1650)
    *   [Yarn](#tab-panel-1651)
    
    ```
    npm uninstall @astrojs/react
    ```
    
2.  Next, remove the integration from your `astro.config.*` file:
    
    ```
    import { defineConfig } from 'astro/config';import react from '@astrojs/react';
    export default defineConfig({  integrations: [    react()  ]});
    ```
    

## Finding more integrations

[Section titled “Finding more integrations”](#finding-more-integrations)

You can find many integrations developed by the community in the [Astro Integrations Directory](https://astro.build/integrations/). Follow links there for detailed usage and configuration instructions.

## Building your own integration

[Section titled “Building your own integration”](#building-your-own-integration)

Astro’s Integration API is inspired by Rollup and Vite, and designed to feel familiar to anyone who has ever written a Rollup or Vite plugin before.

Check out the [Integration API](/en/reference/integrations-reference/) reference to learn what integrations can do and how to write one yourself.

## Publishing your integration to npm

[Section titled “Publishing your integration to npm”](#publishing-your-integration-to-npm)

Publishing an Astro component is a great way to reuse your existing work across your projects, and to share with the wider Astro community at large. Astro components can be published directly to and installed from npm, just like any other JavaScript package.

Looking for inspiration? Check out some of our favorite [themes](https://astro.build/themes/) and [components](https://astro.build/integrations/) from the Astro community. You can also [search npm](https://www.npmjs.com/search?q=keywords:astro-component,withastro) to see the entire public catalog.

### Quick start

[Section titled “Quick start”](#quick-start)

To get started developing your component quickly, you can use a template already set up for you.

*   [npm](#tab-panel-1652)
*   [pnpm](#tab-panel-1653)
*   [Yarn](#tab-panel-1654)

```
# Initialize the Astro Component template in a new directorynpm create astro@latest my-new-component-directory -- --template component
```

### Creating a package

[Section titled “Creating a package”](#creating-a-package)

To create a new package, configure your development environment to use **workspaces** within your project. This will allow you to develop your component alongside a working copy of Astro.

*   Directorymy-new-component-directory/
    
    *   Directorydemo/
        
        *   … for testing and demonstration
        
    *   package.json
    *   Directorypackages/
        
        *   Directorymy-component/
            
            *   index.js
            *   package.json
            *   … additional files used by the package
            
        
    

This example, named `my-project`, creates a project with a single package, named `my-component`, and a `demo/` directory for testing and demonstrating the component.

This is configured in the project root’s `package.json` file:

```
{  "name": "my-project",  "workspaces": ["demo", "packages/*"]}
```

In this example, multiple packages can be developed together from the `packages` directory. These packages can also be referenced from `demo`, where you can install a working copy of Astro.

*   [npm](#tab-panel-1655)
*   [pnpm](#tab-panel-1656)
*   [Yarn](#tab-panel-1657)

```
npm create astro@latest demo -- --template minimal
```

There are two initial files that will make up your individual package: `package.json` and `index.js`.

#### `package.json`

[Section titled “package.json”](#packagejson)

The `package.json` in the package directory includes all of the information related to your package, including its description, dependencies, and any other package metadata.

```
{  "name": "my-component",  "description": "Component description",  "version": "1.0.0",  "homepage": "https://github.com/owner/project#readme",  "type": "module",  "exports": {    ".": "./index.js",    "./astro": "./MyAstroComponent.astro",    "./react": "./MyReactComponent.jsx"  },  "files": ["index.js", "MyAstroComponent.astro", "MyReactComponent.jsx"],  "keywords": ["astro-component", "withastro", "... etc", "... etc"]}
```

##### `description`

[Section titled “description”](#description)

A short description of your component used to help others know what it does.

```
{  "description": "An Astro Element Generator"}
```

##### `type`

[Section titled “type”](#type)

The module format used by Node.js and Astro to interpret your `index.js` files.

```
{  "type": "module"}
```

Use `"type": "module"` so that your `index.js` can be used as an entrypoint with `import` and `export` .

##### `homepage`

[Section titled “homepage”](#homepage)

The url to the project homepage.

```
{  "homepage": "https://github.com/owner/project#readme"}
```

This is a great way to direct users to an online demo, documentation, or homepage for your project.

##### `exports`

[Section titled “exports”](#exports)

The entry points of a package when imported by name.

```
{  "exports": {    ".": "./index.js",    "./astro": "./MyAstroComponent.astro",    "./react": "./MyReactComponent.jsx"  }}
```

In this example, importing `my-component` would use `index.js`, while importing `my-component/astro` or `my-component/react` would use `MyAstroComponent.astro` or `MyReactComponent.jsx` respectively.

##### `files`

[Section titled “files”](#files)

An optional optimization to exclude unnecessary files from the bundle shipped to users via npm. Note that **only files listed here will be included in your package**, so if you add or change files necessary for your package to work, you must update this list accordingly.

```
{  "files": ["index.js", "MyAstroComponent.astro", "MyReactComponent.jsx"]}
```

##### `keywords`

[Section titled “keywords”](#keywords)

An array of keywords relevant to your component, used to help others [find your component on npm](https://www.npmjs.com/search?q=keywords:astro-component,withastro) and in any other search catalogs.

Add `astro-component`, `astro-integration`, or `withastro` as a special keyword to maximize its discoverability in the Astro ecosystem.

```
{  "keywords": ["astro-component", "withastro", "... etc", "... etc"]}
```

* * *

#### `index.js`

[Section titled “index.js”](#indexjs)

The main **package entrypoint** used whenever your package is imported.

```
export { default as MyAstroComponent } from './MyAstroComponent.astro';export { default as MyReactComponent } from './MyReactComponent.jsx';
```

This allows you to package multiple components together into a single interface.

##### Example: Using named imports

[Section titled “Example: Using named imports”](#example-using-named-imports)

```
---import { MyAstroComponent } from 'my-component';import { MyReactComponent } from 'my-component';---<MyAstroComponent /><MyReactComponent />
```

##### Example: Using namespace imports

[Section titled “Example: Using namespace imports”](#example-using-namespace-imports)

```
---import * as Example from 'example-astro-component';---<Example.MyAstroComponent /><Example.MyReactComponent />
```

##### Example: Using individual imports

[Section titled “Example: Using individual imports”](#example-using-individual-imports)

```
---import MyAstroComponent from 'example-astro-component/astro';import MyReactComponent from 'example-astro-component/react';---<MyAstroComponent /><MyReactComponent />
```

* * *

### Developing your package

[Section titled “Developing your package”](#developing-your-package)

Astro does not have a dedicated “package mode” for development. Instead, you should use a demo project to develop and test your package inside of your project. This can be a private website only used for development, or a public demo/documentation website for your package.

If you are extracting components from an existing project, you can even continue to use that project to develop your now-extracted components.

### Testing your component

[Section titled “Testing your component”](#testing-your-component)

Astro does not currently ship a test runner. _(If you are interested in helping out with this, [join us on Discord!](https://astro.build/chat))_

In the meantime, our current recommendation for testing is:

1.  Add a test `fixtures` directory to your `demo/src/pages` directory.
    
2.  Add a new page for every test that you’d like to run.
    
3.  Each page should include some different component usage that you’d like to test.
    
4.  Run `astro build` to build your fixtures, then compare the output of the `dist/__fixtures__/` directory to what you expected.
    
    *   Directorymy-project/demo/src/pages/\_\_fixtures\_\_/
        
        *   test-name-01.astro
        *   test-name-02.astro
        *   test-name-03.astro
        
    

### Publishing your component

[Section titled “Publishing your component”](#publishing-your-component)

Once you have your package ready, you can publish it to npm using the `npm publish` command. If that fails, make sure that you have logged in via `npm login` and that your `package.json` is correct. If it succeeds, you’re done!

Notice that there was no `build` step for Astro packages. Any file type that Astro supports natively, such as `.astro`, `.ts`, `.jsx`, and `.css`, can be published directly without a build step.

If you need another file type that isn’t natively supported by Astro, add a build step to your package. This advanced exercise is left up to you.

### Integrations library

[Section titled “Integrations library”](#integrations-library)

Share your hard work by adding your integration to our [integrations library](https://astro.build/integrations/)!

#### `package.json` data

[Section titled “package.json data”](#packagejson-data)

The library is automatically updated weekly, pulling in every package published to npm with the `astro-component`, `astro-integration`, or `withastro` keyword.

The integrations library reads the `name`, `description`, `repository`, and `homepage` data from your `package.json`.

Avatars are a great way to highlight your brand in the library! Once your package is published you can [file a GitHub issue](https://github.com/withastro/astro.build/issues/new/choose) with your avatar attached and we will add it to your listing.

#### Categories

[Section titled “Categories”](#categories)

In addition to the required `astro-component`, `astro-integration`, or `withastro` keyword, special keywords are also used to automatically organize packages. Including any of the keywords below will add your integration to the matching category in our integrations library.

category

keywords

Accessibility

`a11y`, `accessibility`

Adapters

`astro-adapter`

Analytics

`analytics`

CSS + UI

`css`, `ui`, `icon`, `icons`, `renderer`

Frameworks

`renderer`

Content Loaders

`astro-loader`

Images + Media

`media`, `image`, `images`, `video`, `audio`

Performance + SEO

`performance`, `perf`, `seo`, `optimization`

Dev Toolbar

`devtools`, `dev-overlay`, `dev-toolbar`

Utilities

`tooling`, `utils`, `utility`

Packages that don’t include any keyword matching a category will be shown as `Uncategorized`.

### Share

[Section titled “Share”](#share)

We encourage you to share your work, and we really do love seeing what our talented Astronauts create. Come and share what you create with us in our [Discord](https://astro.build/chat) or mention [@astrodotbuild](https://twitter.com/astrodotbuild) in a Tweet!

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
