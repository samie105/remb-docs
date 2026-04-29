---
title: "Tina CMS & Astro"
source: "https://docs.astro.build/en/guides/cms/tina-cms/"
canonical_url: "https://docs.astro.build/en/guides/cms/tina-cms/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:44.622Z"
content_hash: "071e83ad919101ac3e2fce70b462e18fd763013da0c717bb744ea935827ede17"
menu_path: ["Tina CMS & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/studiocms/index.md", "title": "StudioCMS & Astro"}
nav_next: {"path": "astro/en/guides/cms/umbraco/index.md", "title": "Umbraco & Astro"}
---

# Tina CMS & Astro

[Tina CMS](https://tina.io/) is a Git-backed headless content management system.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

To get started, you’ll need an existing Astro project.

1.  Run the following command to install Tina into your Astro project.
    
    *   [npm](#tab-panel-1518)
    *   [pnpm](#tab-panel-1519)
    *   [Yarn](#tab-panel-1520)
    
    ```
    npx @tinacms/cli@latest init
    ```
    
    *   When prompted for a Cloud ID, press Enter to skip. You’ll generate one later if you want to use Tina Cloud.
    *   When prompted “What framework are you using”, choose **Other**.
    *   When asked where public assets are stored, press Enter.
    
    After this has finished, you should now have a `.tina` folder in the root of your project and a generated `hello-world.md` file at `content/posts`.
    
2.  Change the `dev` script in `package.json`:
    
    *   [npm](#tab-panel-1521)
    *   [pnpm](#tab-panel-1522)
    *   [Yarn](#tab-panel-1523)
    
    ```
    {    "scripts": {        "dev": "astro dev",        "dev": "tinacms dev -c \"astro dev\""    }}
    ```
    
3.  TinaCMS is now set up in local mode. Test this by running the `dev` script, then navigating to `/admin/index.html#/collections/post`.
    
    Editing the “Hello, World!” post will update the `content/posts/hello-world.md` file in your project directory.
    
4.  Set up your Tina collections by editing the `schema.collections` property in `.tina/config.ts`.
    
    For example, you can add a required “date posted” frontmatter property to our posts:
    
    ```
    import { defineConfig } from "tinacms";
    // Your hosting provider likely exposes this as an environment variableconst branch = process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "main";
    export default defineConfig({  branch,  clientId: null, // Get this from tina.io  token: null, // Get this from tina.io  build: {    outputFolder: "admin",    publicFolder: "public",  },  media: {    tina: {      mediaRoot: "images",      publicFolder: "public",    },  },  schema: {    collections: [      {        name: "posts",        label: "Posts",        path: "src/content/posts",        format: 'mdx',        fields: [          {            type: "string",            name: "title",            label: "Title",            isTitle: true,            required: true,          },          {            type: "datetime",            name: "posted",            label: "Date Posted",            required: true,          },          {            type: "rich-text",            name: "body",            label: "Body",            isBody: true,          },        ],      },    ],  },});
    ```
    
    Learn more about Tina collections [in the Tina docs](https://tina.io/docs/reference/collections/).
    
5.  In production, TinaCMS can commit changes directly to your GitHub repository. To set up TinaCMS for production, you can choose to use [Tina Cloud](https://tina.io/docs/tina-cloud/) or self-host the [Tina Data Layer](https://tina.io/docs/self-hosted/overview/). You can [read more about registering for Tina Cloud](https://app.tina.io/register) in the Tina Docs.
    

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [TinaCMS Astro integration guide](https://tina.io/docs/frameworks/astro/).

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [Astro Tina Starter with visual editing](https://github.com/dawaltconley/tina-astro) by Jeff See + Dylan Awalt-Conley
*   [Astro Tina Starter with basic editing](https://github.com/tombennet/astro-tina-starter/tree/main) by Tom Bennet
*   [Using Astro’s Image Optimization with Tina](https://joschua.io/posts/2023/08/16/how-to-use-astro-assets-with-tina-cms/)

## Themes

[Section titled “Themes”](#themes)

*    [![](/_astro/resume01.CAukhX1f_17VSJx.webp) Resume01](https://astro.build/themes/details/resume01/)
*    [![](/_astro/qurno.Dxy77_Dt_Zooq2x.webp) Qurno Blog](https://astro.build/themes/details/qurno-astro/)

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
    
    ### [Decap CMS](../decap-cms/index.md)
    
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
    
    ### [Tina CMS](index.md)
    
*   ![](/logos/umbraco.svg)
    
    ### [Umbraco](../umbraco/index.md)
    
*   ![](/logos/vault-cms.svg)
    
    ### [Vault CMS](../vault-cms/index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [Wordpress](../wordpress/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
