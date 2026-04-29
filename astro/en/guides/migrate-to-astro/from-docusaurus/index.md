---
title: "Migrating from Docusaurus"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-docusaurus/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-docusaurus/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:38.265Z"
content_hash: "808e917f24215dc381fca492f1d81733f05d7a740c50a01416bec1b515554b94"
menu_path: ["Migrating from Docusaurus"]
section_path: []
nav_prev: {"path": "astro/en/guides/migrate-to-astro/from-create-react-app/index.md", "title": "Migrating from Create React App (CRA)"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-eleventy/index.md", "title": "Migrating from Eleventy"}
---

# Migrating from Docusaurus

[Docusaurus](https://Docusaurus.io) is a popular documentation website builder built on React.

## Key Similarities between Docusaurus and Astro

[Section titled “Key Similarities between Docusaurus and Astro”](#key-similarities-between-docusaurus-and-astro)

Docusaurus and Astro share some similarities that will help you migrate your project:

*   Both Astro and Docusaurus are modern, JavaScript-based (Jamstack) site builders intended for [content-driven websites](../../../concepts/why-astro/index.md#content-driven), like documentation sites.
    
*   Both Astro and Docusaurus support [MDX pages](../../markdown-content/index.md). You should be able to use your existing `.mdx` files with Astro.
    
*   Both Astro and Docusaurus use [file-based routing](../../routing/index.md) to generate page routes automatically for any MDX file located in `src/pages`. Using Astro’s file structure for your existing content and when adding new pages should feel familiar.
    
*   Astro has an [official integration for using React components](../../integrations-guide/react/index.md). Note that in Astro, React files **must** have a `.jsx` or `.tsx` extension.
    
*   Astro supports [installing NPM packages](../../imports/index.md#npm-packages), including several for React. You may be able to keep some or all of your existing React components and dependencies.
    
*   [Astro’s JSX-like syntax](../../../basics/astro-components/index.md#the-component-template) should feel familiar if you are used to writing React.
    

## Key Differences between Docusaurus and Astro

[Section titled “Key Differences between Docusaurus and Astro”](#key-differences-between-docusaurus-and-astro)

When you rebuild your Docusaurus site in Astro, you will notice some important differences:

*   Docusaurus is a React-based single-page application (SPA). Astro sites are multi-page apps built using [`.astro` components](../../../basics/astro-components/index.md), but can also support [React, Preact, Vue.js, Svelte, SolidJS, AlpineJS](../../framework-components/index.md) and raw HTML templating.
    
*   Docusaurus was designed to build documentation websites and has some built-in, documentation-specific website features that you would have to build yourself in Astro. Instead, Astro offers some of these features through [Starlight: an official docs theme](https://starlight.astro.build). This website was the inspiration for Starlight, and now runs on it! You can also find more [community docs themes](https://astro.build/themes?search=&categories%5B%5D=docs) with built-in features in our Themes Showcase.
    
*   Docusaurus sites use MDX pages for content. Astro’s docs theme uses Markdown (`.md`) files by default and does not require you to use MDX. You can optionally [install Astro’s MDX integration](../../integrations-guide/mdx/index.md) (included in our Starlight theme by default) and use `.mdx` files in addition to standard Markdown files.
    

## Switch from Docusaurus to Astro

[Section titled “Switch from Docusaurus to Astro”](#switch-from-docusaurus-to-astro)

To convert a Docusaurus documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community docs themes in our [theme showcase](https://astro.build/themes?search=&categories%5B%5D=docs).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](../../../install-and-setup/index.md#install-from-the-cli-wizard).

*   [npm](#tab-panel-1801)
*   [pnpm](#tab-panel-1802)
*   [Yarn](#tab-panel-1803)

```
npm create astro@latest -- --template starlight
```

Astro’s MDX integration is included by default, so you can [bring your existing content files to Starlight](https://starlight.astro.build/getting-started/#add-content) right away.

You can find Astro’s docs starter, and other official templates, on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Speeding up documentation by 10 times (Russian)](https://habr.com/ru/articles/880220/)

## More migration guides

*   ![](/logos/create-react-app.svg)
    
    ### [Create React App](../from-create-react-app/index.md)
    
*   ![](/logos/docusaurus.svg)
    
    ### [Docusaurus](index.md)
    
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
    
    ### [VuePress](../from-vuepress/index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [WordPress](../from-wordpress/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
