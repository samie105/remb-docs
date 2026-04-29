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
nav_prev: {"path": "../from-gridsome/index.md", "title": "Migrating from Gridsome"}
nav_next: {"path": "../from-jekyll/index.md", "title": "Migrating from Jekyll"}
---

# Migrating from Hugo

[Hugo](https://gohugo.io) is an open-source static site generator built on Go.

## Key Similarities between Hugo and Astro

[Section titled “Key Similarities between Hugo and Astro”](#key-similarities-between-hugo-and-astro)

Hugo and Astro share some similarities that will help you migrate your project:

*   Hugo and Astro are both modern static-site generators, ideally suited to [content-driven websites](/en/concepts/why-astro/#content-driven) like blogs.
    
*   Hugo and Astro both allow you to [author your content in Markdown](/en/guides/markdown-content/). However, Hugo includes several special frontmatter properties and allows you to write frontmatter in YAML, TOML or JSON. Even though many of your existing Hugo frontmatter properties will not be “special” in Astro, you can continue to use your existing Markdown files and YAML (or TOML) frontmatter values.
    
*   Hugo and Astro both allow you to enhance your site with a variety of [integrations and external packages](https://astro.build/integrations/).
    

## Key Differences between Hugo and Astro

[Section titled “Key Differences between Hugo and Astro”](#key-differences-between-hugo-and-astro)

When you rebuild your Hugo site in Astro, you will notice some important differences:

*   Hugo uses Go Templating for page templating. [Astro syntax](/en/basics/astro-components/) is a JSX-like superset of HTML.
    
*   Astro does not use shortcodes for dynamic content in standard Markdown files, but [Astro’s MDX integration](/en/guides/integrations-guide/mdx/) does allow you to use JSX and import components in MDX files.
    
*   While Hugo can use “partials” for reusable layout elements, [Astro is entirely component-based](/en/basics/astro-components/). Any `.astro` file can be a component, a layout or an entire page, and can import and render any other Astro components. Astro components can also include [other UI framework components (e.g. React, Svelte, Vue, Solid)](/en/guides/framework-components/) as well as content or metadata from [other files in your project](/en/guides/imports/), such as Markdown or MDX.
    

## Switch from Hugo to Astro

[Section titled “Switch from Hugo to Astro”](#switch-from-hugo-to-astro)

To convert a Hugo blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

*   [npm](#tab-panel-1818)
*   [pnpm](#tab-panel-1819)
*   [Yarn](#tab-panel-1820)

```
npm create astro@latest -- --template blog
```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](/en/guides/markdown-content/). Astro allows YAML or TOML frontmatter in these files, so if you are using JSON frontmatter, you will need to convert it.

To continue to use dynamic content such as variables, expressions or UI components within your Markdown content, add Astro’s optional MDX integration and convert your existing Markdown files to [MDX pages](/en/guides/markdown-content/). MDX supports YAML and TOML frontmatter, so you can keep your existing frontmatter properties. But, you must replace any shortcode syntax with [MDX’s own syntax](https://mdxjs.com/docs/what-is-mdx/#mdx-syntax), which allows JSX expressions and/or component imports.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Elio Struyf's migration story from Hugo to Astro](https://www.eliostruyf.com/migration-story-hugo-astro/)

[Hugo Vs Astro - Which Static Site Generator To Choose In 2023](https://onebite.dev/hugo-vs-astro-which-static-site-generator-to-choose-in-2023/)

[Lessons from an AI-assisted migration to Astro](https://bennet.org/blog/lessons-from-ai-assisted-migration-to-astro/)

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
