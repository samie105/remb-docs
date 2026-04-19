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
