---
title: "Decap CMS & Astro"
source: "https://docs.astro.build/en/guides/cms/decap-cms/"
canonical_url: "https://docs.astro.build/en/guides/cms/decap-cms/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:53.935Z"
content_hash: "adf2e6d3c7b7de54694756c305438fcf1f4921a541d89f5f1616ca3e15f26fe4"
menu_path: ["Decap CMS & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/datocms/index.md", "title": "DatoCMS & Astro"}
nav_next: {"path": "astro/en/guides/cms/directus/index.md", "title": "Directus & Astro"}
---

# Decap CMS & Astro

[Decap CMS](https://www.decapcms.org/) (formerly Netlify CMS) is an open-source, Git-based content management system.

Decap allows you to take full advantage of all of Astro’s features, including image optimization and content collections.

Decap adds a route (typically `/admin`) to your project that will load a React app to allow authorized users to manage content directly from the deployed website. Decap will commit changes directly to your Astro project’s source repository.

## Installing DecapCMS

[Section titled “Installing DecapCMS”](#installing-decapcms)

There are two options for adding Decap to Astro:

1.  [Install Decap via a package manager](https://decapcms.org/docs/install-decap-cms/#installing-with-npm) with the following command:
    
    *   [npm](#tab-panel-1479)
    *   [pnpm](#tab-panel-1480)
    *   [Yarn](#tab-panel-1481)
    
    ```
    npm install decap-cms-app
    ```
    
2.  Import the package into a `<script>` tag in your page `<body>`
    
    ```
    <body>  <!-- Include the script that builds the page and powers Decap CMS -->  <script src="https://unpkg.com/decap-cms@^3.1.2/dist/decap-cms.js"></script></body>
    ```
    

## Configuration

[Section titled “Configuration”](#configuration)

1.  Create a static admin folder at `public/admin/`
    
2.  Add `config.yml` to `public/admin/`:
    
    *   Directorypublic
        
        *   Directoryadmin
            
            *   config.yml
            
        
    
3.  To add support for content collections, configure each schema in `config.yml`. The following example configures a `blog` collection, defining a `label` for each entry’s frontmatter property:
    
    ```
    collections:  - name: "blog" # Used in routes, e.g., /admin/collections/blog    label: "Blog" # Used in the UI    folder: "src/content/blog" # The path to the folder where the documents are stored    create: true # Allow users to create new documents in this collection    fields: # The fields for each document, usually in frontmatter      - { label: "Layout", name: "layout", widget: "hidden", default: "blog" }      - { label: "Title", name: "title", widget: "string" }      - { label: "Publish Date", name: "date", widget: "datetime" }      - { label: "Featured Image", name: "thumbnail", widget: "image" }      - { label: "Rating (scale of 1-5)", name: "rating", widget: "number" }      - { label: "Body", name: "body", widget: "markdown" }
    ```
    
4.  Add the `admin` route for your React app in `src/pages/admin.html`.
    
    *   Directorypublic
        
        *   Directoryadmin
            
            *   config.yml
            
        
    *   Directorysrc
        
        *   Directorypages
            
            *   admin.html
            
        
    
    ```
    <!doctype html><html lang="en">  <head>    <meta charset="utf-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <meta name="robots" content="noindex" />    <link href="config.yml" type="text/yaml" rel="cms-config-url" />    <title>Content Manager</title>  </head>  <body>    <script src="https://unpkg.com/decap-cms@^3.1.2/dist/decap-cms.js"></script>  </body></html>
    ```
    
5.  To enable media uploads to a specific folder via the Decap editor, add an appropriate path:
    
    ```
    media_folder: "src/assets/images" # Location where files will be stored in the repopublic_folder: "src/assets/images" # The src attribute for uploaded media
    ```
    

See [the Decap CMS configuration documentation](https://decapcms.org/docs/configure-decap-cms/) for full instructions and options.

## Usage

[Section titled “Usage”](#usage)

Navigate to `yoursite.com/admin/` to use the Decap CMS editor.

## Authentication

[Section titled “Authentication”](#authentication)

### Decap CMS with Netlify Identity

[Section titled “Decap CMS with Netlify Identity”](#decap-cms-with-netlify-identity)

Decap CMS was originally developed by Netlify and has first class support for [Netlify Identity](https://docs.netlify.com/security/secure-access-to-sites/identity/).

When deploying to Netlify, configure Identity for your project via the Netlify dashboard and include the [Netlify Identity Widget](https://github.com/netlify/netlify-identity-widget) on the `admin` route of your project. Optionally include the Identity Widget on the homepage of your site if you plan to invite new users via email.

### Decap CMS with External OAuth Clients

[Section titled “Decap CMS with External OAuth Clients”](#decap-cms-with-external-oauth-clients)

When deploying to hosting providers other than Netlify, you must create your own OAuth routes.

In Astro, this can be done with on-demand rendered routes in your project configured with [an adapter](../../on-demand-rendering/index.md) enabled.

See [Decap’s OAuth Docs](https://decapcms.org/docs/external-oauth-clients/) for a list of compatible community-maintained OAuth clients.

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   Netlify Identity Template: [astro-decap-ssg-netlify](https://github.com/OliverSpeir/astro-decap-ssg-netlify-identity)
    
*   On-demand rendering OAuth Routes with Astro Template: [astro-decap-starter-ssr](https://github.com/OliverSpeir/astro-decap-starter-ssr)
    
*   Blog Post: [Author your Astro site’s content with Git-based CMSs](https://aalam.vercel.app/blog/astro-and-git-cms-netlify) by Aftab Alam
    
*   Youtube Tutorial: [Create a Custom Blog with Astro & NetlifyCMS in MINUTES!](https://www.youtube.com/watch?v=3yip2wSRX_4) by Kumail Pirzada
    

## Production Sites

[Section titled “Production Sites”](#production-sites)

The following sites use Astro + Decap CMS in production:

*   [yunielacosta.com](https://www.yunielacosta.com/) by Yuniel Acosta — [source code on GitHub](https://github.com/yacosta738/yacosta738.github.io) (Netlify CMS)
*   [portfolioris.nl](https://www.portfolioris.nl/) by Joris Hulsbosch – [source code on GitHub](https://github.com/portfolioris/portfolioris.nl)

## Themes

[Section titled “Themes”](#themes)

*    [![](/_astro/astros.CA8z6dbD_1DAx4t.webp) Astros](https://astro.build/themes/details/astros)
*    [![](/_astro/enhanced-astro-starter.BDAzOMVv_1DBCpt.webp) Enhanced Astro Starter](https://astro.build/themes/details/enhanced-astro-starter)
*    [![](/_astro/astro-decap-starter.CuC8RtgM_1x5zxf.webp) Astro Decap CMS Starter](https://astro.build/themes/details/astro-decap-cms-starter)

## More CMS guides

### Featured CMS partners

*   ![](/logos/cloudcannon.svg)
    
    ### [CloudCannon](../cloudcannon/index.md)
    
    Git-based CMS built for speed, security, and zero headaches.
    

### All CMS guides

*   ![](/logos/apostrophecms.svg)
    
    ### [ApostropheCMS](../apostrophecms/index.md)
    
*   ![](/logos/builderio.svg)
    
    ### [Builder.io](../builderio/index.md)
    
*   ![](/logos/buttercms.svg)
    
    ### [ButterCMS](../buttercms/index.md)
    
*   ![](/logos/caisy.svg)
    
    ### [Caisy](../caisy/index.md)
    
*   ![](/logos/cloudcannon.svg)
    
    ### [CloudCannon](../cloudcannon/index.md)
    
*   ![](/logos/contentful.svg)
    
    ### [Contentful](../contentful/index.md)
    
*   ![](/logos/cosmic.svg)
    
    ### [Cosmic](../cosmic/index.md)
    
*   ![](/logos/craft-cms.svg)
    
    ### [Craft CMS](../craft-cms/index.md)
    
*   ![](/logos/craft-cross-cms.svg)
    
    ### [Craft Cross CMS](../craft-cross-cms/index.md)
    
*   ![](/logos/crystallize.svg)
    
    ### [Crystallize](../crystallize/index.md)
    
*   ![](/logos/datocms.svg)
    
    ### [DatoCMS](../datocms/index.md)
    
*   ![](/logos/decap-cms.svg)
    
    ### [Decap CMS](index.md)
    
*   ![](/logos/directus.svg)
    
    ### [Directus](../directus/index.md)
    
*   ![](/logos/drupal.svg)
    
    ### [Drupal](../drupal/index.md)
    
*   ![](/logos/flotiq.svg)
    
    ### [Flotiq](../flotiq/index.md)
    
*   ![](/logos/frontmatter-cms.svg)
    
    ### [Front Matter CMS](../frontmatter-cms/index.md)
    
*   ![](/logos/ghost.png)
    
    ### [Ghost](../ghost/index.md)
    
*   ![](/logos/gitcms.svg)
    
    ### [GitCMS](../gitcms/index.md)
    
*   ![](/logos/hashnode.png)
    
    ### [Hashnode](../hashnode/index.md)
    
*   ![](/logos/hygraph.svg)
    
    ### [Hygraph](../hygraph/index.md)
    
*   ![](/logos/jekyllpad.svg)
    
    ### [JekyllPad](../jekyllpad/index.md)
    
*   ![](/logos/keystatic.svg)
    
    ### [Keystatic](../keystatic/index.md)
    
*   ![](/logos/keystonejs.svg)
    
    ### [KeystoneJS](../keystonejs/index.md)
    
*   ![](/logos/kontent-ai.svg)
    
    ### [Kontent.ai](../kontent-ai/index.md)
    
*   ![](/logos/microcms.svg)
    
    ### [microCMS](../microcms/index.md)
    
*   ![](/logos/optimizely.svg)
    
    ### [Optimizely CMS](../optimizely/index.md)
    
*   ![](/logos/pages-cms.svg)
    
    ### [Pages CMS](../pages-cms/index.md)
    
*   ![](/logos/payload.svg)
    
    ### [Payload CMS](../payload/index.md)
    
*   ![](/logos/preprcms.svg)
    
    ### [Prepr CMS](../preprcms/index.md)
    
*   ![](/logos/prismic.svg)
    
    ### [Prismic](../prismic/index.md)
    
*   ![](/logos/sanity.svg)
    
    ### [Sanity](../sanity/index.md)
    
*   ![](/logos/sitecore.svg)
    
    ### [Sitecore XM](../sitecore/index.md)
    
*   ![](/logos/sitepins.svg)
    
    ### [Sitepins](../sitepins/index.md)
    
*   ![](/logos/spinal.svg)
    
    ### [Spinal](../spinal/index.md)
    
*   ![](/logos/statamic.svg)
    
    ### [Statamic](../statamic/index.md)
    
*   ![](/logos/storyblok.svg)
    
    ### [Storyblok](../storyblok/index.md)
    
*   ![](/logos/strapi.svg)
    
    ### [Strapi](../strapi/index.md)
    
*   ![](/logos/studiocms.svg)
    
    ### [StudioCMS](../studiocms/index.md)
    
*   ![](/logos/tina-cms.svg)
    
    ### [Tina CMS](../tina-cms/index.md)
    
*   ![](/logos/umbraco.svg)
    
    ### [Umbraco](../umbraco/index.md)
    
*   ![](/logos/vault-cms.svg)
    
    ### [Vault CMS](../vault-cms/index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [Wordpress](../wordpress/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
