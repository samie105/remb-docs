---
title: "Migrating from Eleventy"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-eleventy/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-eleventy/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:43.242Z"
content_hash: "63b29412fb882574d257550194ce1a40555201a68c5066a916587c25b8f7c675"
menu_path: ["Migrating from Eleventy"]
section_path: []
nav_prev: {"path": "astro/en/guides/migrate-to-astro/from-docusaurus/index.md", "title": "Migrating from Docusaurus"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-gatsby/index.md", "title": "Migrating from Gatsby"}
---

# Migrating from Eleventy

[Eleventy](https://11ty.dev) is an open-source static site generator that works with multiple template languages.

## Key Similarities between Eleventy (11ty) and Astro

[Section titled “Key Similarities between Eleventy (11ty) and Astro”](#key-similarities-between-eleventy-11ty-and-astro)

Eleventy (11ty) and Astro share some similarities that will help you migrate your project:

*   Both Astro and Eleventy are modern, JavaScript-based (Jamstack) site builders.
    
*   Astro and Eleventy both allow you to use a [headless CMS, APIs or Markdown files for data](/en/guides/data-fetching/). You can continue to use your preferred content authoring system, and will be able to keep your existing content.
    

## Key Differences between Eleventy (11ty) and Astro

[Section titled “Key Differences between Eleventy (11ty) and Astro”](#key-differences-between-eleventy-11ty-and-astro)

When you rebuild your Eleventy (11ty) site in Astro, you will notice some important differences:

*   Eleventy supports a variety of templating languages. Astro supports [including components from several popular JS Frameworks (e.g. React, Svelte, Vue, Solid)](/en/guides/framework-components/), but uses [Astro layouts, pages and components](/en/basics/astro-components/) for most page templating.
    
*   Astro uses a [`src/` directory](/en/basics/project-structure/#src) for all files, including site metadata, that are available for querying and processing during site build. Within this is a [special `src/pages/` folder for file-based routing](/en/basics/astro-pages/).
    
*   Astro uses a [`public/` folder for static assets](/en/basics/project-structure/#public) that do not need to be processed nor transformed during the build.
    
*   In Eleventy, bundling CSS, JavaScript, and other assets needs to be configured manually. [Astro handles this for you out-of-the-box](/en/concepts/why-astro/#easy-to-use).
    

## Switch from Eleventy to Astro

[Section titled “Switch from Eleventy to Astro”](#switch-from-eleventy-to-astro)

To convert an Eleventy blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

*   [npm](#tab-panel-1804)
*   [pnpm](#tab-panel-1805)
*   [Yarn](#tab-panel-1806)

```
npm create astro@latest -- --template blog
```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](/en/guides/markdown-content/).

Your Eleventy project allowed you to use a variety of templating languages to build your site. In an Astro project, your page templating will mostly be achieved with Astro components, which can be used as UI elements, layouts and even full pages. You may want to explore [Astro’s component syntax](/en/basics/astro-components/) to see how to template in Astro using components.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[This Site Is Now Built with Astro](https://aqandrew.com/blog/now-built-with-astro/) Why I switched from Eleventy.

[Website Rewrite: 2025](https://www.welchcanavan.com/posts/site-rewrite-2025/)

## More migration guides

*   ![](/logos/create-react-app.svg)
    
    ### [Create React App](/en/guides/migrate-to-astro/from-create-react-app/)
    
*   ![](/logos/docusaurus.svg)
    
    ### [Docusaurus](/en/guides/migrate-to-astro/from-docusaurus/)
    
*   ![](/logos/eleventy.svg)
    
    ### [Eleventy](/en/guides/migrate-to-astro/from-eleventy/)
    
*   ![](/logos/gatsby.svg)
    
    ### [Gatsby](/en/guides/migrate-to-astro/from-gatsby/)
    
*   ![](/logos/gitbook.svg)
    
    ### [GitBook](/en/guides/migrate-to-astro/from-gitbook/)
    
*   ![](/logos/gridsome.svg)
    
    ### [Gridsome](/en/guides/migrate-to-astro/from-gridsome/)
    
*   ![](/logos/hugo.svg)
    
    ### [Hugo](/en/guides/migrate-to-astro/from-hugo/)
    
*   ![](/logos/jekyll.png)
    
    ### [Jekyll](/en/guides/migrate-to-astro/from-jekyll/)
    
*   ![](/logos/nextjs.svg)
    
    ### [Next.js](/en/guides/migrate-to-astro/from-nextjs/)
    
*   ![](/logos/nuxtjs.svg)
    
    ### [NuxtJS](/en/guides/migrate-to-astro/from-nuxtjs/)
    
*   ![](/logos/pelican.svg)
    
    ### [Pelican](/en/guides/migrate-to-astro/from-pelican/)
    
*   ![](/logos/sveltekit.svg)
    
    ### [SvelteKit](/en/guides/migrate-to-astro/from-sveltekit/)
    
*   ![](/logos/vuepress.png)
    
    ### [VuePress](/en/guides/migrate-to-astro/from-vuepress/)
    
*   ![](/logos/wordpress.svg)
    
    ### [WordPress](/en/guides/migrate-to-astro/from-wordpress/)
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
