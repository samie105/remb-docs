---
title: "Migrating from WordPress"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-wordpress/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-wordpress/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:17.885Z"
content_hash: "d9c27dac5e52e1a5c55a7fc6137df308c51a2046a7f8cb8c1acfbca064fe7b18"
menu_path: ["Migrating from WordPress"]
section_path: []
nav_prev: {"path": "../from-vuepress/index.md", "title": "Migrating from VuePress"}
nav_next: {"path": "../../../contribute/index.md", "title": "Contribute to Astro"}
---

# Migrating from WordPress

[WordPress](https://wordpress.org) is an open-source, personal publishing system built on PHP and MySQL.

## Key Similarities between WordPress and Astro

[Section titled “Key Similarities between WordPress and Astro”](#key-similarities-between-wordpress-and-astro)

WordPress and Astro share some similarities that will help you migrate your project:

*   Both WordPress and Astro are ideal for [content-driven websites](/en/concepts/why-astro/#content-driven) like blogs and support writing your content in Markdown (requires a plugin in WordPress). Although the process for adding new content is different, [writing in Markdown files](/en/guides/markdown-content/) for your Astro blog should feel familiar if you have used Markdown syntax in your WordPress editor.
    
*   Both WordPress and Astro encourage you to [think about the design of your site in “blocks”](/en/concepts/islands/) (components). In Astro you will probably [write more of your own code to create these blocks](/en/basics/astro-components/) rather than rely on pre-built plugins. But thinking about the individual pieces of your site and how they are presented on the page should feel familiar.
    

## Key Differences between WordPress and Astro

[Section titled “Key Differences between WordPress and Astro”](#key-differences-between-wordpress-and-astro)

When you rebuild your WordPress site in Astro, you will notice some important differences:

*   A WordPress site is edited using an online dashboard. In Astro, you will use a [code editor](/en/editor-setup/) and development environment to maintain your site. You can develop locally on your machine, or choose a cloud editor/development environment like StackBlitz or CodeSandbox.
    
*   WordPress has an extensive plugin and theme market. In Astro, you will find some themes and [integrations](https://astro.build/integrations/) available, but you may now have to build many of your existing features yourself instead of looking for third-party solutions. Or, you can choose to start with an [Astro theme](https://astro.build/themes) with built-in features!
    
*   WordPress stores your content in a database. In Astro, you will have individual files (typically Markdown or MDX) in your [project directory](/en/basics/project-structure/) for each page’s content. Or, you can choose to use a [CMS for your content](/en/guides/cms/), even your existing WordPress site, and use Astro to fetch and present the data.
    

## Switch from WordPress to Astro

[Section titled “Switch from WordPress to Astro”](#switch-from-wordpress-to-astro)

To convert a WordPress blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

*   [npm](#tab-panel-1843)
*   [pnpm](#tab-panel-1844)
*   [Yarn](#tab-panel-1845)

```
npm create astro@latest -- --template blog
```

You can continue to [use your existing WordPress blog as your CMS for Astro](/en/guides/cms/wordpress/), which means you will keep using your WordPress dashboard for writing your posts. Your content will be managed at WordPress, but all other aspects of your Astro site will be built in your code editing environment, and you will [deploy your Astro site](/en/guides/deploy/) separately from your WordPress site. (Be sure to update your domain at your host to keep the same website URL!)

You may wish to take [Astro’s Build a Blog Tutorial](/en/tutorial/0-introduction/) if you are new to working in a code editor and using GitHub to store and deploy your site. It will walk you through all the accounts and setup you need! You will also learn how to [build Astro components yourself](/en/tutorial/3-components/), and it will show you how to [add blog posts directly in Astro](/en/tutorial/2-pages/2/) if you choose not to use WordPress to write your content.

If you want to move all of your existing post content to Astro, you may find this [tool for exporting Markdown from WordPress helpful](https://github.com/lonekorean/wordpress-export-to-markdown). You may need to make some adjustments to the result if you have to [convert a large or complicated WordPress site to Markdown](https://swizec.com/blog/how-to-export-a-large-wordpress-site-to-markdown/).

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in StackBlitz and CodeSandbox online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Goodbye Wordpress, hello Astro!](https://trib.tv/posts/2025/wordpress-to-astro/)

[How I Migrated from Wordpress to Astro](https://itsthatlady.dev/blog/migrate-from-wordpress-to-astro/)

[How and Why I Moved My Blog from WordPress to Astro and Markdown](https://levelup.gitconnected.com/how-and-why-i-moved-my-blog-from-wordpress-to-astro-and-markdown-3549672d5a86)

[How I Migrated From Wordpress to Astro: Boosted Pagespeed Scores to 100% and Cut 100% Hosting cost](https://devaradise.com/wordpress-to-static-website-astro/)

[WordPress to Astro site conversion](https://share.transistor.fm/s/d86496cd)

[How to Convert a Wordpress blog to an Astro Static Site](https://blog.okturtles.org/2024/10/convert-wordpress-to-static-site/)

[Why I switched from WordPress to Astro](https://dev.to/fratzinger/why-i-switched-from-wordpress-to-astro-5ge)

[Why I ditched WordPress for Astro](https://vbartalis.xyz/en/blog/why-i-ditched-wordpress-for-astro-js/)

[DeWP: utility to use your WordPress data in Astro projects](https://delucis.github.io/dewp/)

[Astro vs. WordPress: Rendering Patterns of the Modern Web](https://andrewkepson.com/blog/headless-wordpress/astro-vs-wordpress-rendering-patterns/)

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
