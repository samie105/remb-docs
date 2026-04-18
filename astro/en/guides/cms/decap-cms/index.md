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

In Astro, this can be done with on-demand rendered routes in your project configured with [an adapter](/en/guides/on-demand-rendering/) enabled.

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
    
    ### [CloudCannon](/en/guides/cms/cloudcannon/)
    
    Git-based CMS built for speed, security, and zero headaches.
    

### All CMS guides

*   ![](/logos/apostrophecms.svg)
    
    ### [ApostropheCMS](/en/guides/cms/apostrophecms/)
    
*   ![](/logos/builderio.svg)
    
    ### [Builder.io](/en/guides/cms/builderio/)
    
*   ![](/logos/buttercms.svg)
    
    ### [ButterCMS](/en/guides/cms/buttercms/)
    
*   ![](/logos/caisy.svg)
    
    ### [Caisy](/en/guides/cms/caisy/)
    
*   ![](/logos/cloudcannon.svg)
    
    ### [CloudCannon](/en/guides/cms/cloudcannon/)
    
*   ![](/logos/contentful.svg)
    
    ### [Contentful](/en/guides/cms/contentful/)
    
*   ![](/logos/cosmic.svg)
    
    ### [Cosmic](/en/guides/cms/cosmic/)
    
*   ![](/logos/craft-cms.svg)
    
    ### [Craft CMS](/en/guides/cms/craft-cms/)
    
*   ![](/logos/craft-cross-cms.svg)
    
    ### [Craft Cross CMS](/en/guides/cms/craft-cross-cms/)
    
*   ![](/logos/crystallize.svg)
    
    ### [Crystallize](/en/guides/cms/crystallize/)
    
*   ![](/logos/datocms.svg)
    
    ### [DatoCMS](/en/guides/cms/datocms/)
    
*   ![](/logos/decap-cms.svg)
    
    ### [Decap CMS](/en/guides/cms/decap-cms/)
    
*   ![](/logos/directus.svg)
    
    ### [Directus](/en/guides/cms/directus/)
    
*   ![](/logos/drupal.svg)
    
    ### [Drupal](/en/guides/cms/drupal/)
    
*   ![](/logos/flotiq.svg)
    
    ### [Flotiq](/en/guides/cms/flotiq/)
    
*   ![](/logos/frontmatter-cms.svg)
    
    ### [Front Matter CMS](/en/guides/cms/frontmatter-cms/)
    
*   ![](/logos/ghost.png)
    
    ### [Ghost](/en/guides/cms/ghost/)
    
*   ![](/logos/gitcms.svg)
    
    ### [GitCMS](/en/guides/cms/gitcms/)
    
*   ![](/logos/hashnode.png)
    
    ### [Hashnode](/en/guides/cms/hashnode/)
    
*   ![](/logos/hygraph.svg)
    
    ### [Hygraph](/en/guides/cms/hygraph/)
    
*   ![](/logos/jekyllpad.svg)
    
    ### [JekyllPad](/en/guides/cms/jekyllpad/)
    
*   ![](/logos/keystatic.svg)
    
    ### [Keystatic](/en/guides/cms/keystatic/)
    
*   ![](/logos/keystonejs.svg)
    
    ### [KeystoneJS](/en/guides/cms/keystonejs/)
    
*   ![](/logos/kontent-ai.svg)
    
    ### [Kontent.ai](/en/guides/cms/kontent-ai/)
    
*   ![](/logos/microcms.svg)
    
    ### [microCMS](/en/guides/cms/microcms/)
    
*   ![](/logos/optimizely.svg)
    
    ### [Optimizely CMS](/en/guides/cms/optimizely/)
    
*   ![](/logos/pages-cms.svg)
    
    ### [Pages CMS](/en/guides/cms/pages-cms/)
    
*   ![](/logos/payload.svg)
    
    ### [Payload CMS](/en/guides/cms/payload/)
    
*   ![](/logos/preprcms.svg)
    
    ### [Prepr CMS](/en/guides/cms/preprcms/)
    
*   ![](/logos/prismic.svg)
    
    ### [Prismic](/en/guides/cms/prismic/)
    
*   ![](/logos/sanity.svg)
    
    ### [Sanity](/en/guides/cms/sanity/)
    
*   ![](/logos/sitecore.svg)
    
    ### [Sitecore XM](/en/guides/cms/sitecore/)
    
*   ![](/logos/sitepins.svg)
    
    ### [Sitepins](/en/guides/cms/sitepins/)
    
*   ![](/logos/spinal.svg)
    
    ### [Spinal](/en/guides/cms/spinal/)
    
*   ![](/logos/statamic.svg)
    
    ### [Statamic](/en/guides/cms/statamic/)
    
*   ![](/logos/storyblok.svg)
    
    ### [Storyblok](/en/guides/cms/storyblok/)
    
*   ![](/logos/strapi.svg)
    
    ### [Strapi](/en/guides/cms/strapi/)
    
*   ![](/logos/studiocms.svg)
    
    ### [StudioCMS](/en/guides/cms/studiocms/)
    
*   ![](/logos/tina-cms.svg)
    
    ### [Tina CMS](/en/guides/cms/tina-cms/)
    
*   ![](/logos/umbraco.svg)
    
    ### [Umbraco](/en/guides/cms/umbraco/)
    
*   ![](/logos/vault-cms.svg)
    
    ### [Vault CMS](/en/guides/cms/vault-cms/)
    
*   ![](/logos/wordpress.svg)
    
    ### [Wordpress](/en/guides/cms/wordpress/)
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

