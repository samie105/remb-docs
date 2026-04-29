---
title: "Migrating from VuePress"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-vuepress/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-vuepress/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:13.382Z"
content_hash: "9298762b285ada916e1d50d2054c0b23173bdecc3e43431be8ec0e02ba11bed8"
menu_path: ["Migrating from VuePress"]
section_path: []
nav_prev: {"path": "astro/en/guides/migrate-to-astro/from-sveltekit/index.md", "title": "Migrating from SvelteKit"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-wordpress/index.md", "title": "Migrating from WordPress"}
---

# Migrating from VuePress

[VuePress](https://vuePress.vuejs.org) is an open-source static site generator built on Vue.

## Key Similarities between VuePress and Astro

[Section titled “Key Similarities between VuePress and Astro”](#key-similarities-between-vuepress-and-astro)

VuePress and Astro share some similarities that will help you migrate your project:

*   Both VuePress and Astro are modern JavaScript static-site generators with similar project file structures. Both use a [special `src/pages/` folder for file-based routing](../../../basics/astro-pages/index.md). Creating and managing pages for your site should feel familiar.
    
*   Astro and VuePress are both designed for [content-driven websites](../../../concepts/why-astro/index.md#content-driven), with excellent built-in support for Markdown files. Writing in Markdown will feel familiar, and you will be able to keep your existing content.
    
*   Astro has [an official integration for using Vue components](../../integrations-guide/vue/index.md) and supports [installing NPM packages](../../imports/index.md#npm-packages), including several for Vue. You will be able to write Vue UI components, and may be able to keep some or all of your existing Vue components and dependencies.
    

## Key Differences between VuePress and Astro

[Section titled “Key Differences between VuePress and Astro”](#key-differences-between-vuepress-and-astro)

When you rebuild your VuePress site in Astro, you will notice some important differences.

*   VuePress is a Vue-based single-page application (SPA). Astro sites are multi-page apps built using [`.astro` components](../../../basics/astro-components/index.md), but can also support [React, Preact, Vue.js, Svelte, SolidJS, AlpineJS](../../framework-components/index.md) and raw HTML templating.
    
*   [Layout templates](../../../basics/layouts/index.md): VuePress sites are created using Markdown (`.md`) files for page content and HTML (`.html`) templates for layout. Astro is component-based, and uses Astro components, which include HTML templating for pages, layouts and individual UI elements. Astro can also create [pages from `.md` and `.mdx` files](../../markdown-content/index.md), using an Astro layout component for wrapping Markdown content in a page template.
    
*   VuePress was designed to build content-heavy, Markdown-centric sites and has some built-in, documentation-specific website features that you would have to build yourself in Astro. Instead, Astro offers some documentation-specific features through an [official docs theme](https://starlight.astro.build). This website was the inspiration for that template! You can also find more [community docs themes](https://astro.build/themes?search=&categories%5B%5D=docs) with built-in features in our Themes Showcase.
    

## Switch from VuePress to Astro

[Section titled “Switch from VuePress to Astro”](#switch-from-vuepress-to-astro)

To convert a VuePress documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community docs themes in our [theme showcase](https://astro.build/themes?search=&categories%5B%5D=docs).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](../../../install-and-setup/index.md#install-from-the-cli-wizard).

*   [npm](#tab-panel-1840)
*   [pnpm](#tab-panel-1841)
*   [Yarn](#tab-panel-1842)

```
npm create astro@latest -- --template starlight
```

Bring your existing Markdown content files to [create Markdown pages](../../markdown-content/index.md). You can still take advantage of [file-based routing](../../routing/index.md) by moving these documents from `docs` in VuePress to `src/pages/` in Astro. Create folders with names that correspond to your existing VuePress project, and you should be able to keep your existing URLs.

VuePress, or any theme you installed, probably handled much of your site layout and metadata for you. You may wish to read about [building Astro Layouts as Markdown page wrappers](../../../basics/layouts/index.md#markdown-layouts) to see how to manage templating yourself in Astro, including your page `<head>`.

You can find Astro’s docs starter, and other templates, on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

## More migration guides

*   ![](/logos/create-react-app.svg)
    
    ### [Create React App](../from-create-react-app/index.md)
    
*   ![](/logos/docusaurus.svg)
    
    ### [Docusaurus](../from-docusaurus/index.md)
    
*   ![](/logos/eleventy.svg)
    
    ### [Eleventy](../from-eleventy/index.md)
    
*   ![](/logos/gatsby.svg)
    
    ### [Gatsby](../from-gatsby/index.md)
    
*   ![](/logos/gitbook.svg)
    
    ### [GitBook](../from-gitbook/index.md)
    
*   ![](/logos/gridsome.svg)
    
    ### [Gridsome](../from-gridsome/index.md)
    
*   ![](/logos/hugo.svg)
    
    ### [Hugo](../from-hugo/index.md)
    
*   ![](/logos/jekyll.png)
    
    ### [Jekyll](../from-jekyll/index.md)
    
*   ![](/logos/nextjs.svg)
    
    ### [Next.js](../from-nextjs/index.md)
    
*   ![](/logos/nuxtjs.svg)
    
    ### [NuxtJS](../from-nuxtjs/index.md)
    
*   ![](/logos/pelican.svg)
    
    ### [Pelican](../from-pelican/index.md)
    
*   ![](/logos/sveltekit.svg)
    
    ### [SvelteKit](../from-sveltekit/index.md)
    
*   ![](/logos/vuepress.png)
    
    ### [VuePress](index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [WordPress](../from-wordpress/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
