---
title: "Hygraph & Astro"
source: "https://docs.astro.build/en/guides/cms/hygraph/"
canonical_url: "https://docs.astro.build/en/guides/cms/hygraph/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:29.766Z"
content_hash: "fc9e0e76410f1314a0e95743555adad5a6df5831052415b8dbc50dce023bdbf4"
menu_path: ["Hygraph & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/hashnode/index.md", "title": "Hashnode & Astro"}
nav_next: {"path": "astro/en/guides/cms/jekyllpad/index.md", "title": "JekyllPad & Astro"}
---

# Hygraph & Astro

[Hygraph](https://hygraph.com/) is a federated content management platform. It exposes a GraphQL endpoint for fetching content.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, you’ll create a [Hygraph](https://hygraph.com/) GraphQL endpoint to fetch with Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1.  **A Hygraph account and project**. If you don’t have an account, you can [sign up for free](https://app.hygraph.com/signup) and create a new project.
    
2.  **Hygraph access permissions** - In `Project Settings > API Access`, configure Public Content API permissions to allow read requests without authentication. If you haven’t set any permissions, you can click **Yes, initialize defaults** to add the required permissions to use the “High Performance Content API”.
    

### Setting up the endpoint

[Section titled “Setting up the endpoint”](#setting-up-the-endpoint)

To add your Hygraph endpoint to Astro, create a `.env` file in the root of your project with the following variable:

```
HYGRAPH_ENDPOINT=YOUR_HIGH_PERFORMANCE_API
```

Now, you should be able to use this environment variable in your project.

If you would like to have IntelliSense for your environment variables, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

```
interface ImportMetaEnv {  readonly HYGRAPH_ENDPOINT: string;}
```

Your root directory should now include these new files:

*   Directorysrc/
    
    *   **env.d.ts**
    
*   **.env**
*   astro.config.mjs
*   package.json

### Fetching data

[Section titled “Fetching data”](#fetching-data)

Fetch data from your Hygraph project by using the `HYGRAPH_ENDPOINT`.

For example, to fetch entries of a `blogPosts` content type that has a string field `title`, create a GraphQL query to fetch that content. Then, define the type of the content, and set it as the type of the response.

```
---interface Post {  title: string;}
const query = {  method: "POST",  headers: { "Content-Type": "application/json" },  body: JSON.stringify({    query: `      {        blogPosts {          title        }      }`,  }),};
const response = await fetch(import.meta.env.HYGRAPH_ENDPOINT, query);const json = await response.json();const posts: Post[] = json.data.blogPosts;---
<html lang="en">  <head>    <meta charset="utf-8" />    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />    <meta name="viewport" content="width=device-width" />    <meta name="generator" content={Astro.generator} />    <title>Astro</title>  </head>  <body>    <h1>Astro</h1>    {      posts.map((post) => (        <div>          <h2>{post.title}</h2>        </div>      ))    }  </body></html>
```

## Deploy

[Section titled “Deploy”](#deploy)

### Configuring Netlify Webhook

[Section titled “Configuring Netlify Webhook”](#configuring-netlify-webhook)

To set up a webhook in Netlify:

1.  Deploy your site to Netlify with [this guide](../../deploy/netlify/index.md). Remember to add your `HYGRAPH_ENDPOINT` to the environment variables.
    
2.  Then Go to your Hygraph project dashboard and click on **Apps**.
    
3.  Go to the marketplace and search for Netlify and follow the instructions provided.
    
4.  If all went good, now you can deploy your website with a click in the Hygraph interface.
    

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [Hygraph + Astro example with `marked` for markdown parsing](https://github.com/camunoz2/example-astrowithhygraph)

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
    
    ### [Hygraph](index.md)
    
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
