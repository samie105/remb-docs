---
title: "DatoCMS & Astro"
source: "https://docs.astro.build/en/guides/cms/datocms/"
canonical_url: "https://docs.astro.build/en/guides/cms/datocms/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:51.568Z"
content_hash: "4249e5611ba36e53b203b171c9e85330e266507f9b859c38089d212b6b71c132"
menu_path: ["DatoCMS & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/crystallize/index.md", "title": "Crystallize & Astro"}
nav_next: {"path": "astro/en/guides/cms/decap-cms/index.md", "title": "Decap CMS & Astro"}
---

# DatoCMS & Astro

[DatoCMS](https://datocms.com/) is a web-based, headless CMS to manage digital content for your sites and apps.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this guide, you will fetch content data from DatoCMS in your Astro project, then display it on a page.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

*   **An Astro project** - If you don’t have an Astro project yet, you can follow the instructions in our [Installation guide](../../../install-and-setup/index.md).
*   **A DatoCMS account and project** - If you don’t have an account, you can [sign up for a free account](https://dashboard.datocms.com/signup).
*   **The read-only API Key for your DatoCMS project** - You can find it in the admin dashboard of your project, under “Settings” > “API Tokens”.

## Setting up the credentials

[Section titled “Setting up the credentials”](#setting-up-the-credentials)

Create a new file (if one does not already exist) named `.env` in the root of your Astro project. Add a new environment variable as follows, using the API key found in your DatoCMS admin dashboard:

```
DATOCMS_API_KEY=YOUR_API_KEY
```

For TypeScript support, declare the typing of this environment variable in the `env.d.ts` file in the `src/` folder. If this file does not exist, you can create it and add the following:

```
interface ImportMetaEnv {  readonly DATOCMS_API_KEY: string;}
```

Your root directory should now include these files:

*   Directorysrc/
    
    *   **env.d.ts**
    
*   **.env**
*   astro.config.mjs
*   package.json

Learn more about [environment variables](../../environment-variables/index.md) and `.env` files in Astro.

## Create a Model in DatoCMS

[Section titled “Create a Model in DatoCMS”](#create-a-model-in-datocms)

In the DatoCMS admin dashboard of your project, navigate to “Settings” > “Models” and create a new Model called “Home” with the “Single Instance” toggle selected. This will create a home page for your project. In this model, add a new text field for the page title.

Navigate to the “Content” tab in your project and click on your newly-created home page. You can now add a title. Save the page, and continue.

## Fetching data

[Section titled “Fetching data”](#fetching-data)

In your Astro project, navigate to the page that will fetch and display your CMS content. Add the following query to fetch the content for `home` using the DatoCMS GraphQL API.

This example displays the page title from DatoCMS on `src/pages/index.astro`:

```
---const response = await fetch('https://graphql.datocms.com/', {  method: 'POST',  headers: {    'Content-Type': 'application/json',    Accept: 'application/json',    Authorization: `Bearer ${import.meta.env.DATOCMS_API_KEY}`,  },  body: JSON.stringify({    query: `query Homepage {          home {            title          }        }      `,  }),});
const json = await response.json();const data = json.data.home;---
<h1>{data.title}</h1>
```

This GraphQL query will fetch the `title` field in the `home` page from your DatoCMS Project. When you refresh your browser, you should see the title on your page.

## Adding Dynamic modular content blocks

[Section titled “Adding Dynamic modular content blocks”](#adding-dynamic-modular-content-blocks)

If your DatosCMS project includes [modular content](https://www.datocms.com/docs/content-modelling/modular-content), then you will need to build a corresponding `.astro` component for each block of content (e.g. a text section, a video, a quotation block, etc.) that the modular field allows in your project.

The example below is a `<Text />` Astro component for displaying a “Multiple-paragraph text” block from DatoCMS.

```
---export interface TextProps {  text: string}
export interface Props {  item: TextProps}
const { item } = Astro.props;---
<div set:html={item.text} />
```

To fetch these blocks, edit your GraphQL query to include the modular content block you created in DatoCMS.

In this example, the modular content block is named **content** in DatoCMS. This query also includes the unique `_modelApiKey` of each item to check which block should be displayed in the modular field, based on which block was chosen by the content author in the DatoCMS editor. Use a switch statement in the Astro template to allow for dynamic rendering based on the data received from the query.

The following example represents a DatoCMS modular content block that allows an author to choose between a text field (`<Text />`) and an image (`<Image />`) rendered on the home page:

```
---import Image from '../components/Image.astro';import Text from '../components/Text.astro';
const response = await fetch('https://graphql.datocms.com/', {  method: 'POST',  headers: {    'Content-Type': 'application/json',    Accept: 'application/json',    Authorization: `Bearer ${import.meta.env.DATOCMS_API_KEY}`,  },  body: JSON.stringify({    query: `query Homepage {          home {            title            content {              ... on ImageRecord {                _modelApiKey               image{                url               }              }              ... on TextRecord {                _modelApiKey                text(markdown: true)              }            }          }        }      `,  }),});
const json = await response.json();const data = json.data.home;---
<h1>{data.title}</h1>{  data.content.map((item: any) => {    switch (item._modelApiKey) {      case 'image':        return <Image item={item} />;      case 'text':        return <Text item={item} />;      default:        return null;    }  })}
```

## Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](../../deploy/index.md) and follow the instructions for your preferred hosting provider.

## Publish on DatoCMS content changes

[Section titled “Publish on DatoCMS content changes”](#publish-on-datocms-content-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build when you change content in DatoCMS.

### Netlify

[Section titled “Netlify”](#netlify)

To set up a webhook in Netlify:

1.  Go to your site dashboard and click on **Build & deploy**.
    
2.  Under the **Continuous Deployment** tab, find the **Build hooks** section and click on **Add build hook**.
    
3.  Provide a name for your webhook and select the branch you want to trigger the build on. Click on **Save** and copy the generated URL.
    

### Vercel

[Section titled “Vercel”](#vercel)

To set up a webhook in Vercel:

1.  Go to your project dashboard and click on **Settings**.
    
2.  Under the **Git** tab, find the **Deploy Hooks** section.
    
3.  Provide a name for your webhook and the branch you want to trigger the build on. Click **Add** and copy the generated URL.
    

### Adding a webhook to DatoCMS

[Section titled “Adding a webhook to DatoCMS”](#adding-a-webhook-to-datocms)

In your DatoCMS project admin dashboard, navigate to the **Settings** tab and click **Webhooks**. Click the plus icon to create a new webhook and give it a name. In the URL field, paste the URL generated by your preferred hosting service. As Trigger, select whichever option suits your needs. (For example: build every time a new record is published.)

## Starter project

[Section titled “Starter project”](#starter-project)

You can also check out the [Astro blog template](https://www.datocms.com/marketplace/starters/astro-template-blog) on the DatoCMS marketplace to learn how to create a blog with Astro and DatoCMS.

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
    
    ### [DatoCMS](index.md)
    
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
