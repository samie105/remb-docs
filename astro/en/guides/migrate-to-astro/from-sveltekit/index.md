---
title: "Migrating from SvelteKit"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-sveltekit/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-sveltekit/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:12.305Z"
content_hash: "6ed7d5a800fe05befb4f9359d2ec53342317a20b0420a6a8f5e8e834ce04f710"
menu_path: ["Migrating from SvelteKit"]
section_path: []
nav_prev: {"path": "astro/en/guides/migrate-to-astro/from-pelican/index.md", "title": "Migrating from Pelican"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-vuepress/index.md", "title": "Migrating from VuePress"}
---

# Migrating from SvelteKit

[SvelteKit](https://kit.svelte.dev) is a framework for building web applications on top of Svelte.

## Key Similarities between SvelteKit and Astro

[Section titled “Key Similarities between SvelteKit and Astro”](#key-similarities-between-sveltekit-and-astro)

SvelteKit and Astro share some similarities that will help you migrate your project:

*   Both SvelteKit and Astro are modern JavaScript static-site generators and server-side rendering frameworks.
    
*   Both SvelteKit and Astro use a [`src/` folder for your project files](../../../basics/project-structure/index.md#src) and a [special folder for file-based routing](../../../basics/astro-pages/index.md). Creating and managing pages for your site should feel familiar.
    
*   Astro has [an official integration for using Svelte components](../../integrations-guide/svelte/index.md) and supports [installing NPM packages](../../imports/index.md#npm-packages), including several for Svelte. You will be able to write Svelte UI components, and may be able to keep some or all of your existing components and dependencies.
    
*   Astro and SvelteKit both allow you to use a [headless CMS, APIs or Markdown files for data](../../data-fetching/index.md). You can continue to use your preferred content authoring system, and will be able to keep your existing content.
    

## Key Differences between SvelteKit and Astro

[Section titled “Key Differences between SvelteKit and Astro”](#key-differences-between-sveltekit-and-astro)

When you rebuild your SvelteKit site in Astro, you will notice some important differences:

*   Astro sites are multi-page apps, whereas SvelteKit defaults to SPAs (single-page applications) with server-side rendering, but can also create MPAs, traditional SPAs, or you can mix and match these techniques within an app.
    
*   [Components](../../../basics/astro-components/index.md): SvelteKit uses [Svelte](https://svelte.dev). Astro pages are built using [`.astro` components](../../../basics/astro-components/index.md), but can also support [React, Preact, Vue.js, Svelte, SolidJS, AlpineJS](../../framework-components/index.md) and raw HTML templating.
    
*   [content-driven](../../../concepts/why-astro/index.md#content-driven): Astro was designed to showcase your content and to allow you to opt-in to interactivity only as needed. An existing SvelteKit app might be built for high client-side interactivity. Astro has built-in capabilities for working with your content, such as page generation, but may require advanced Astro techniques to include items that are more challenging to replicate using `.astro` components, such as dashboards.
    
*   [Markdown-ready](../../markdown-content/index.md): Astro includes built-in Markdown support, and includes a [special frontmatter YAML `layout` property](../../../basics/layouts/index.md#markdown-layouts) used per-file for page templating. If you are converting a SvelteKit Markdown-based blog, you will not have to install a separate Markdown integration and you will not set a layout via a configuration file. You can bring your existing Markdown files, but you may need to reorganize as Astro’s file-based routing does not require a folder for each page route.
    

## Switch from SvelteKit to Astro

[Section titled “Switch from SvelteKit to Astro”](#switch-from-sveltekit-to-astro)

To convert a SvelteKit blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](../../../install-and-setup/index.md#install-from-the-cli-wizard).

*   [npm](#tab-panel-1837)
*   [pnpm](#tab-panel-1838)
*   [Yarn](#tab-panel-1839)

```
npm create astro@latest -- --template blog
```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](../../markdown-content/index.md).

While file-based routing and layout components are similar in Astro, you may wish to read about [Astro’s project structure](../../../basics/project-structure/index.md) to learn where files should be located.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Rewriting my blog from SvelteKit to Astro](https://kharann.com/blog/rewriting-my-blog/)

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
    
    ### [SvelteKit](index.md)
    
*   ![](/logos/vuepress.png)
    
    ### [VuePress](../from-vuepress/index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [WordPress](../from-wordpress/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
