---
title: "Migrating from Jekyll"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-jekyll/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-jekyll/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:56.813Z"
content_hash: "a6f5bcef51e680ff0f602143a876ab6e66127fe1dfb47c66b0261a0aa72b4223"
menu_path: ["Migrating from Jekyll"]
section_path: []
nav_prev: {"path": "../from-hugo/index.md", "title": "Migrating from Hugo"}
nav_next: {"path": "../from-nextjs/index.md", "title": "Migrating from Next.js"}
---

# Migrating from Jekyll

[Jekyll](https://jekyllrb.com) is a static site generator built on Ruby.

## Key Similarities between Jekyll and Astro

[Section titled “Key Similarities between Jekyll and Astro”](#key-similarities-between-jekyll-and-astro)

Jekyll and Astro share some similarities that will help you migrate your project:

*   Both Jekyll and Astro are static-site generators, commonly used to create blogs.
    
*   Both Jekyll and Astro allow you to write your content in Markdown and HTML. Jekyll and Astro both provide some special frontmatter YAML properties for page layout and unpublished draft posts. You can continue to use your existing Markdown files in Astro.
    
*   Both Jekyll and Astro use [file-based routing](/en/guides/routing/) for creating pages from your blog posts. Astro provides a [special `src/pages/` directory for all pages and posts](/en/basics/project-structure/#srcpages). Jekyll uses a similar special folder called `_posts/` for your Markdown blog posts, however your site pages can exist elsewhere. Creating new blog posts should feel familiar.
    

## Key Differences between Jekyll and Astro

[Section titled “Key Differences between Jekyll and Astro”](#key-differences-between-jekyll-and-astro)

When you rebuild your Jekyll site in Astro, you will notice some important differences:

*   As Jekyll is primarily a blogging platform, several blog features are built-in that you may have to build yourself in Astro. Or, choose a [blog starter template theme](https://astro.build/themes?search=&categories%5B%5D=blog) that includes these features. For example, Jekyll has built-in support for tags and categories which you will find in several Astro blog themes, but is not included in a minimal Astro project.
    
*   Jekyll uses Liquid templates for reusable layout elements and templating. Astro uses JSX-like [`.astro` files for templating and components](/en/basics/astro-components/). Any `.astro` file can be a component, a layout or an entire page, and can import and render any other Astro components. You can also build using [other UI framework components (e.g. React, Svelte, Vue, Solid)](/en/guides/framework-components/) as well as content or metadata from [other files in your project](/en/guides/imports/), such as Markdown or MDX.
    

## Switch from Jekyll to Astro

[Section titled “Switch from Jekyll to Astro”](#switch-from-jekyll-to-astro)

To convert a Jekyll blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

*   [npm](#tab-panel-1821)
*   [pnpm](#tab-panel-1822)
*   [Yarn](#tab-panel-1823)

```
npm create astro@latest -- --template blog
```

Bring your existing Markdown files as content to [create Markdown pages](/en/guides/markdown-content/), using an [Astro Markdown layout](/en/basics/layouts/#markdown-layouts) instead of a Liquid template.

Much of your existing HTML page content can be converted into [Astro pages](/en/basics/astro-pages/), and you will additionally be able to [use variables, JSX-like expressions and component imports directly in your HTML templating](/en/reference/astro-syntax/#jsx-like-expressions).

Astro does not have a `permalink` property that accepts placeholders. You may need to read more about [Astro’s page routing](/en/guides/routing/) if you want to keep your existing URL structure. Or, consider [setting redirects at a host like Netlify](https://docs.netlify.com/routing/redirects/).

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[From Jekyll to Astro](https://jackcarey.co.uk/posts/astro-rewrite/)

[Goodbye Jekyll, Hello Astro](https://kiranrao.in/blog/bye-jekyll-hello-astro/)

[Back to the Future: Our Tech Blog's Transition from Jekyll to Astro](https://alasco.tech/2023/09/06/migrating-to-astro)

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
