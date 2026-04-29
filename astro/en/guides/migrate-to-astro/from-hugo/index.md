---
title: "Migrating from Hugo"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-hugo/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-hugo/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:57.946Z"
content_hash: "775bbf9b8974d6c5703132969013cdf316c78b49a6e16fc7c8c0da9dcefd3bb8"
menu_path: ["Migrating from Hugo"]
section_path: []
nav_prev: {"path": "astro/en/guides/migrate-to-astro/from-gridsome/index.md", "title": "Migrating from Gridsome"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-jekyll/index.md", "title": "Migrating from Jekyll"}
---

# Migrating from Hugo

[Hugo](https://gohugo.io) is an open-source static site generator built on Go.

## Key Similarities between Hugo and Astro

[Section titled “Key Similarities between Hugo and Astro”](#key-similarities-between-hugo-and-astro)

Hugo and Astro share some similarities that will help you migrate your project:

*   Hugo and Astro are both modern static-site generators, ideally suited to [content-driven websites](../../../concepts/why-astro/index.md#content-driven) like blogs.
    
*   Hugo and Astro both allow you to [author your content in Markdown](../../markdown-content/index.md). However, Hugo includes several special frontmatter properties and allows you to write frontmatter in YAML, TOML or JSON. Even though many of your existing Hugo frontmatter properties will not be “special” in Astro, you can continue to use your existing Markdown files and YAML (or TOML) frontmatter values.
    
*   Hugo and Astro both allow you to enhance your site with a variety of [integrations and external packages](https://astro.build/integrations/).
    

## Key Differences between Hugo and Astro

[Section titled “Key Differences between Hugo and Astro”](#key-differences-between-hugo-and-astro)

When you rebuild your Hugo site in Astro, you will notice some important differences:

*   Hugo uses Go Templating for page templating. [Astro syntax](../../../basics/astro-components/index.md) is a JSX-like superset of HTML.
    
*   Astro does not use shortcodes for dynamic content in standard Markdown files, but [Astro’s MDX integration](../../integrations-guide/mdx/index.md) does allow you to use JSX and import components in MDX files.
    
*   While Hugo can use “partials” for reusable layout elements, [Astro is entirely component-based](../../../basics/astro-components/index.md). Any `.astro` file can be a component, a layout or an entire page, and can import and render any other Astro components. Astro components can also include [other UI framework components (e.g. React, Svelte, Vue, Solid)](../../framework-components/index.md) as well as content or metadata from [other files in your project](../../imports/index.md), such as Markdown or MDX.
    

## Switch from Hugo to Astro

[Section titled “Switch from Hugo to Astro”](#switch-from-hugo-to-astro)

To convert a Hugo blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](../../../install-and-setup/index.md#install-from-the-cli-wizard).

*   [npm](#tab-panel-1818)
*   [pnpm](#tab-panel-1819)
*   [Yarn](#tab-panel-1820)

```
npm create astro@latest -- --template blog
```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](../../markdown-content/index.md). Astro allows YAML or TOML frontmatter in these files, so if you are using JSON frontmatter, you will need to convert it.

To continue to use dynamic content such as variables, expressions or UI components within your Markdown content, add Astro’s optional MDX integration and convert your existing Markdown files to [MDX pages](../../markdown-content/index.md). MDX supports YAML and TOML frontmatter, so you can keep your existing frontmatter properties. But, you must replace any shortcode syntax with [MDX’s own syntax](https://mdxjs.com/docs/what-is-mdx/#mdx-syntax), which allows JSX expressions and/or component imports.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Elio Struyf's migration story from Hugo to Astro](https://www.eliostruyf.com/migration-story-hugo-astro/)

[Hugo Vs Astro - Which Static Site Generator To Choose In 2023](https://onebite.dev/hugo-vs-astro-which-static-site-generator-to-choose-in-2023/)

[Lessons from an AI-assisted migration to Astro](https://bennet.org/blog/lessons-from-ai-assisted-migration-to-astro/)

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
    
    ### [Hugo](index.md)
    
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
