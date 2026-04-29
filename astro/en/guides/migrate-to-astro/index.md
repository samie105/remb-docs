---
title: "Migrate an existing project to Astro"
source: "https://docs.astro.build/en/guides/migrate-to-astro/"
canonical_url: "https://docs.astro.build/en/guides/migrate-to-astro/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:33.795Z"
content_hash: "478d02bf80824e5a8b804f8316fb2de00f3e59ccd19888d75d75ed3465f1651b"
menu_path: ["Migrate an existing project to Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/troubleshooting/index.md", "title": "Troubleshooting"}
nav_next: {"path": "astro/en/guides/migrate-to-astro/from-create-react-app/index.md", "title": "Migrating from Create React App (CRA)"}
---

# Migrate an existing project to Astro

**Ready to convert your site to Astro?** See one of our guides for migration tips.

## Migration Guides

[Section titled “Migration Guides”](#migration-guides)

*   ![](/logos/create-react-app.svg)
    
    ### [Create React App](from-create-react-app/index.md)
    
*   ![](/logos/docusaurus.svg)
    
    ### [Docusaurus](from-docusaurus/index.md)
    
*   ![](/logos/eleventy.svg)
    
    ### [Eleventy](from-eleventy/index.md)
    
*   ![](/logos/gatsby.svg)
    
    ### [Gatsby](from-gatsby/index.md)
    
*   ![](/logos/gitbook.svg)
    
    ### [GitBook](from-gitbook/index.md)
    
*   ![](/logos/gridsome.svg)
    
    ### [Gridsome](from-gridsome/index.md)
    
*   ![](/logos/hugo.svg)
    
    ### [Hugo](from-hugo/index.md)
    
*   ![](/logos/jekyll.png)
    
    ### [Jekyll](from-jekyll/index.md)
    
*   ![](/logos/nextjs.svg)
    
    ### [Next.js](from-nextjs/index.md)
    
*   ![](/logos/nuxtjs.svg)
    
    ### [NuxtJS](from-nuxtjs/index.md)
    
*   ![](/logos/pelican.svg)
    
    ### [Pelican](from-pelican/index.md)
    
*   ![](/logos/sveltekit.svg)
    
    ### [SvelteKit](from-sveltekit/index.md)
    
*   ![](/logos/vuepress.png)
    
    ### [VuePress](from-vuepress/index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [WordPress](from-wordpress/index.md)
    

Note that many of these pages are **stubs**: they’re collections of resources waiting for your contribution!

## Why migrate your site to Astro?

[Section titled “Why migrate your site to Astro?”](#why-migrate-your-site-to-astro)

Astro provides many benefits: performance, simplicity, and many of the features you want built right into the framework. When you do need to extend your site, Astro provides several [official and 3rd-party community integrations](https://astro.build/integrations).

Migrating may be less work than you think!

Depending on your existing project, you may be able to use your existing:

*   [UI framework components](../framework-components/index.md) directly in Astro.
    
*   [CSS stylesheets or libraries](../styling/index.md) including Tailwind.
    
*   [Markdown/MDX files](../markdown-content/index.md), configured using your existing [remark and rehype plugins](../markdown-content/index.md#markdown-plugins).
    
*   [Content from a CMS](../cms/index.md) through an integration or API.
    

## Which projects can I convert to Astro?

[Section titled “Which projects can I convert to Astro?”](#which-projects-can-i-convert-to-astro)

[Many existing sites can be built with Astro](../../concepts/why-astro/index.md). Astro is ideally suited for your existing content-based sites like blogs, landing pages, marketing sites and portfolios. Astro integrates with several popular headless CMSes, and allows you to connect eCommerce shop carts.

Astro allows you have a fully statically-generated website, a dynamic app with routes rendered on demand, or a combination of both with [complete control over your project rendering](../on-demand-rendering/index.md), making it a great replacement for SSGs or for sites that need to fetch some page data on the fly.

## How will my project design change?

[Section titled “How will my project design change?”](#how-will-my-project-design-change)

Depending on your existing project, you may need to think differently about:

*   Designing in [Astro Islands](../../concepts/islands/index.md#what-is-an-island) to avoid sending unnecessary JavaScript to the browser.
    
*   Providing client-side interactivity with [client-side `<script>` tags](../client-side-scripts/index.md) or [UI framework components](../framework-components/index.md).
    
*   Managing [shared state](/en/recipes/sharing-state-islands/) with Nano Stores or local storage instead of app-wide hooks or wrappers.
    

[Contribute](../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
