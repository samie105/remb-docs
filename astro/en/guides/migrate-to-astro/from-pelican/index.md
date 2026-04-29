---
title: "Migrating from Pelican"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-pelican/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-pelican/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:06.912Z"
content_hash: "f2a38fdead8aa86c2b0559a2fbb83efa6b4c4c7cd860fab48d70b2aeff4612db"
menu_path: ["Migrating from Pelican"]
section_path: []
nav_prev: {"path": "astro/en/guides/migrate-to-astro/from-nuxtjs/index.md", "title": "Migrating from NuxtJS"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-sveltekit/index.md", "title": "Migrating from SvelteKit"}
---

# Migrating from Pelican

[Pelican](https://getpelican.com) is an open-source static site generator built on Python.

## Key Similarities between Pelican and Astro

[Section titled “Key Similarities between Pelican and Astro”](#key-similarities-between-pelican-and-astro)

Pelican and Astro share some similarities that will help you migrate your project:

*   Pelican and Astro are both static-site generators, ideally suited to [content-driven websites](../../../concepts/why-astro/index.md#content-driven) like blogs.
    
*   Pelican and Astro both have built-in support for [writing in Markdown](../../markdown-content/index.md), including frontmatter YAML properties for page metadata. However, Astro has very few reserved frontmatter properties compared to Pelican. Even though many of your existing Pelican frontmatter properties will not be “special” in Astro, you can continue to use your existing Markdown files and frontmatter values.
    

## Key Differences between Pelican and Astro

[Section titled “Key Differences between Pelican and Astro”](#key-differences-between-pelican-and-astro)

When you rebuild your Pelican site in Astro, you will notice some important differences:

*   Pelican supports writing content in Markdown and reStructured Text (`.rst`). Astro supports [creating pages from Markdown and MDX](../../markdown-content/index.md) files, but does not support reStructured Text.
    
*   Pelican uses HTML files and Jinja syntax for templating. [Astro syntax](../../../basics/astro-components/index.md) is a JSX-like superset of HTML. All valid HTML is valid `.astro` syntax.
    
*   Pelican was designed to build content-rich websites like blogs and has some built-in, blog features that you would have to build yourself in Astro. Instead, Astro offers some of these features included in an [official blog theme](https://github.com/withastro/astro/tree/latest/examples/blog).
    

## Switch from Pelican to Astro

[Section titled “Switch from Pelican to Astro”](#switch-from-pelican-to-astro)

To convert a Pelican documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](../../../install-and-setup/index.md#install-from-the-cli-wizard).

*   [npm](#tab-panel-1834)
*   [pnpm](#tab-panel-1835)
*   [Yarn](#tab-panel-1836)

```
npm create astro@latest -- --template starlight
```

Bring your existing Markdown content files to [create Markdown pages](../../markdown-content/index.md). You can still take advantage of [file-based routing](../../routing/index.md) by copying these documents from Pelican’s `content/` folder into `src/pages/` in Astro. You may wish to read about [Astro’s project structure](../../../basics/project-structure/index.md) to learn where files should be located.

Pelican may have handled much of your site layout and metadata for you. You may wish to read about [building Astro Layouts as Markdown page wrappers](../../../basics/layouts/index.md#markdown-layouts) to see how to manage templating yourself in Astro, including your page `<head>`.

Like Pelican, Astro has many plugins that extend its functionality. Explore the [official list of integrations](../../integrations/index.md) for adding features such as MDX support, and find hundreds more of community-maintained integrations in the [Astro Integrations Directory](https://astro.build/integrations/). You can even use the [Astro Integration API](../../../reference/integrations-reference/index.md) to build your own custom integration to extend your project’s features.

To convert other types of sites, such as a portfolio or a blog, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

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
    
    ### [Pelican](index.md)
    
*   ![](/logos/sveltekit.svg)
    
    ### [SvelteKit](../from-sveltekit/index.md)
    
*   ![](/logos/vuepress.png)
    
    ### [VuePress](../from-vuepress/index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [WordPress](../from-wordpress/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
