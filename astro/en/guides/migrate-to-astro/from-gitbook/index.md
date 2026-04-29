---
title: "Migrating from GitBook"
source: "https://docs.astro.build/en/guides/migrate-to-astro/from-gitbook/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/from-gitbook/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:47.990Z"
content_hash: "640d91a50a366739315dc8b34d25d443fc75bb35ffbfdb9c6333de1a4bd45515"
menu_path: ["Migrating from GitBook"]
section_path: []
nav_prev: {"path": "astro/en/guides/migrate-to-astro/from-gatsby/index.md", "title": "Migrating from Gatsby"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-gridsome/index.md", "title": "Migrating from Gridsome"}
---

# Migrating from GitBook

[GitBook](https://gitbook.com) is a web-based platform for creating and publishing documentation and books in a collaborative manner, with version control integration and customizable features.

## Key Similarities between GitBook and Astro

[Section titled “Key Similarities between GitBook and Astro”](#key-similarities-between-gitbook-and-astro)

GitBook and Astro share some similarities that will help you migrate your project:

*   Both Astro and GitBook support [Markdown](../../markdown-content/index.md). You can migrate all your existing documentation utilizing GitBook’s Git Sync feature.
    
*   Both Astro and GitBook use some form of [file-based routing](../../routing/index.md). Using Astro’s file structure for your existing content and when adding new pages should feel familiar.
    

## Key Differences between GitBook and Astro

[Section titled “Key Differences between GitBook and Astro”](#key-differences-between-gitbook-and-astro)

When you migrate your GitBook docs to Astro, you will notice some important differences:

*   A GitBook site is edited using an online dashboard. In Astro, you will use a [code editor](../../../editor-setup/index.md) and development environment to maintain your site. You can develop locally on your machine, or choose a cloud editor/development environment like StackBlitz or CodeSandbox.
    
*   GitBook stores your content in a database. In Astro, you will have individual files (typically Markdown or MDX) in your [project directory](../../../basics/project-structure/index.md) for each page’s content. Or, you can choose to use a [CMS for your content](../../cms/index.md) and use Astro to fetch and present the data.
    
*   GitBook uses a custom syntax on top of Markdown for content. Astro supports Markdoc via the optional [Markdoc integration](../../integrations-guide/markdoc/index.md), which features a similar syntax to the one you would use in GitBook.
    

## Switch from GitBook to Astro

[Section titled “Switch from GitBook to Astro”](#switch-from-gitbook-to-astro)

To convert a GitBook documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community docs themes in our [theme showcase](https://astro.build/themes?search=&categories%5B%5D=docs).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](../../../install-and-setup/index.md#install-from-the-cli-wizard).

*   [npm](#tab-panel-1812)
*   [pnpm](#tab-panel-1813)
*   [Yarn](#tab-panel-1814)

```
npm create astro@latest -- --template starlight
```

Once you have a new Astro project, you can sync your existing GitBook content to your new Astro project. GitBook has a [Git Sync feature](https://docs.gitbook.com/product-tour/git-sync) that will automatically sync your GitBook content to a GitHub/GitLab repository.

To sync directly to the docs template’s content collection, specify `src/content/docs/en` or `src/content/docs` as the project directory.

After syncing the content, you will now have a copy of your GitBook content in your Astro repository. Disable git sync to prevent future syncing with GitBook.

Note that although you now have your content migrated to your Astro project, it will not be immediately usable. To use this content in your Astro site, you will need to spend some time manually changing GitBook’s syntax into a format compatible with Astro. In particular:

*   Astro’s [Markdoc integration](../../integrations-guide/markdoc/index.md) requires that the file extension be `.mdoc`. This is to avoid conflicts with other Markdown extensions like `.mdx` and `.md`.
*   GitBook syntax differs from Markdoc where the `/` prefix denoting a closing tag is replaced with `end` for GitBook files. You will need to update this notation throughout your files.
*   Some features of GitBook rely on custom components. These components will not exist in Astro and must be created and added to your project through [Markdoc’s config `tags` attribute](../../integrations-guide/markdoc/index.md#use-astro-components-as-markdoc-tags) or removed from your files.

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
    
    ### [GitBook](index.md)
    
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
