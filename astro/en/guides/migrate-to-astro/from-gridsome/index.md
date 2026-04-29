---
title: "Migrating from Gridsome"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-gridsome/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-gridsome/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:50.339Z"
content_hash: "5bbc486bdc2cc266914acb8eaca292a2cd962eb75e4ef4b49b892a5a09486868"
menu_path: ["Migrating from Gridsome"]
section_path: []
nav_prev: {"path": "astro/en/guides/migrate-to-astro/from-gitbook/index.md", "title": "Migrating from GitBook"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-hugo/index.md", "title": "Migrating from Hugo"}
---

# Migrating from Gridsome

[Gridsome](https://gridsome.org) is an open-source static site generator built on Vue and GraphQL.

## Key Similarities between Gridsome and Astro

[Section titled “Key Similarities between Gridsome and Astro”](#key-similarities-between-gridsome-and-astro)

Gridsome and Astro share some similarities that will help you migrate your project:

*   Both Gridsome and Astro are modern JavaScript static-site generators with similar [project file structures](../../../basics/project-structure/index.md#directories-and-files).
    
*   Both Gridsome and Astro use a `src/` folder for your project files and a [special `src/pages/` folder for file-based routing](../../../basics/astro-pages/index.md). Creating and managing pages for your site should feel familiar.
    
*   Astro has [an official integration for using Vue components](../../integrations-guide/vue/index.md) and supports [installing NPM packages](../../imports/index.md#npm-packages), including several for Vue. You will be able to write Vue UI components, and may be able to keep some or all of your existing Gridsome Vue components and dependencies.
    
*   Astro and Gridsome both allow you to use a [headless CMS, APIs or Markdown files for data](../../data-fetching/index.md). You can continue to use your preferred content authoring system, and will be able to keep your existing content.
    

## Key Differences between Gridsome and Astro

[Section titled “Key Differences between Gridsome and Astro”](#key-differences-between-gridsome-and-astro)

When you rebuild your Gridsome site in Astro, you will notice some important differences:

*   Gridsome is a Vue-based single-page application (SPA). Astro sites are multi-page apps built using [`.astro` components](../../../basics/astro-components/index.md), but can also support [React, Preact, Vue.js, Svelte, SolidJS, AlpineJS](../../framework-components/index.md) and raw HTML templating.
    
*   As an SPA, Gridsome uses `vue-router` for SPA routing, and `vue-meta` for managing `<head>`. In Astro, you will create separate HTML pages and control your page `<head>` directly, or in a [layout component](../../../basics/layouts/index.md).
    
*   [Local file data](../../imports/index.md): Gridsome uses GraphQL to retrieve data from your project files. Astro uses ESM imports and [`import.meta.glob()`](../../imports/index.md#importmetaglob) to import data from local project files. Remote resources can be loaded using the standard `fetch()` API. GraphQL may be optionally added to your project, but is not included by default.
    

## Switch from Gridsome to Astro

[Section titled “Switch from Gridsome to Astro”](#switch-from-gridsome-to-astro)

To convert a Gridsome blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](../../../install-and-setup/index.md#install-from-the-cli-wizard).

*   [npm](#tab-panel-1815)
*   [pnpm](#tab-panel-1816)
*   [Yarn](#tab-panel-1817)

```
npm create astro@latest -- --template blog
```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](../../markdown-content/index.md).

Since Gridsome’s project structure is similar to Astro’s, you may be able to copy several existing files from your project into the same location in your new Astro project. However, the two project structures are not identical. You may want to examine [Astro’s project structure](../../../basics/project-structure/index.md) to see what the differences are.

Since Astro queries and imports your local files differently than Gridsome, you may want to read about how to load files using [`import.meta.glob()`](../../imports/index.md#importmetaglob) to understand how to work with your local files.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Migration from Gridsome to Astro](https://fyodor.io/migration-from-gridsome-to-astro/)

[Hello Astro!](https://thamas.hu/astro-hello)

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
    
    ### [Gridsome](index.md)
    
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
    
    ### [VuePress](../from-vuepress/index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [WordPress](../from-wordpress/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
