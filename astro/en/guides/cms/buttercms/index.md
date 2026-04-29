---
title: "ButterCMS & Astro"
source: "https://docs.astro.build/en/guides/cms/buttercms/"
canonical_url: "https://docs.astro.build/en/guides/cms/buttercms/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:16.640Z"
content_hash: "dbadec6b3aba7539bc06eee42533f00a768dba87e657b96d5298d71877858638"
menu_path: ["ButterCMS & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/builderio/index.md", "title": "Builder.io & Astro"}
nav_next: {"path": "astro/en/guides/cms/caisy/index.md", "title": "Caisy & Astro"}
---

# ButterCMS & Astro

[ButterCMS](https://buttercms.com/) is a headless CMS and blog engine that allows you to publish structured content to use in your project.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, we’ll use the [ButterCMS SDK](https://www.npmjs.com/package/buttercms) to bring your data into your Astro project. To get started, you will need to have the following:

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

1.  **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](../../../install-and-setup/index.md) will get you up and running in no time.
    
2.  **A ButterCMS account**. If you don’t have an account, you can [sign up](https://buttercms.com/join/) for a free trial.
    
3.  **Your ButterCMS API Token** - You can find your API Token on the [Settings](https://buttercms.com/settings/) page.
    

### Setup

[Section titled “Setup”](#setup)

1.  Create a `.env` file in the root of your project and add your API token as an environment variable:
    
    ```
    BUTTER_TOKEN=YOUR_API_TOKEN_HERE
    ```
    
2.  Install the ButterCMS SDK as a dependency:
    
    *   [npm](#tab-panel-1467)
    *   [pnpm](#tab-panel-1468)
    *   [Yarn](#tab-panel-1469)
    
    ```
    npm install buttercms
    ```
    
3.  Create a `buttercms.js` file in a new `src/lib/` directory in your project:
    
    ```
    import Butter from "buttercms";
    export const butterClient = Butter(import.meta.env.BUTTER_TOKEN);
    ```
    

**This authenticates the SDK using your API Token and exports it to be used across your project.**

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

To fetch content, import this client and use one of its `retrieve` functions.

In this example, we [retrieve a collection](https://buttercms.com/docs/api/#retrieve-a-collection) that has three fields: a short text `name`, a number `price`, and a WYSIWYG `description`.

```
---import { butterClient } from "../lib/buttercms";const response = await butterClient.content.retrieve(["shopitem"]);
interface ShopItem {  name: string,  price: number,  description: string,}
const items = response.data.data.shopitem as ShopItem[];---<body>  {items.map(item => <div>    <h2>{item.name} - ${item.price}</h2>    <p set:html={item.description}></p>  </div>)}</body>
```

The interface mirrors the field types. The WYSIWYG `description` field loads as a string of HTML, and [`set:html`](../../../reference/directives-reference/index.md#sethtml) lets you render it.

Similarly, you can [retrieve a page](https://buttercms.com/docs/api/#get-a-single-page) and display its fields:

```
---import { butterClient } from "../lib/buttercms";const response = await butterClient.page.retrieve("*", "simple-page");const pageData = response.data.data;
interface Fields {  seo_title: string,  headline: string,  hero_image: string,}
const fields = pageData.fields as Fields;---<html>  <title>{fields.seo_title}</title>  <body>    <h1>{fields.headline}</h1>    <img src={fields.hero_image} />  </body></html>
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Astro + ButterCMS Starter Project](https://buttercms.com/starters/astro-starter-project/)
*   The [full ButterCMS API documentation](https://buttercms.com/docs/api/)
*   ButterCMS’s [JavaScript Guide](https://buttercms.com/docs/api-client/javascript/)

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   Add yours!

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
    
    ### [ButterCMS](index.md)
    
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
    
    ### [Tina CMS](../tina-cms/index.md)
    
*   ![](/logos/umbraco.svg)
    
    ### [Umbraco](../umbraco/index.md)
    
*   ![](/logos/vault-cms.svg)
    
    ### [Vault CMS](../vault-cms/index.md)
    
*   ![](/logos/wordpress.svg)
    
    ### [Wordpress](../wordpress/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
