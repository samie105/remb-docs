---
title: "Prepr CMS & Astro"
source: "https://docs.astro.build/en/guides/cms/preprcms/"
canonical_url: "https://docs.astro.build/en/guides/cms/preprcms/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:02.316Z"
content_hash: "428268c99741978fb44f957a5c8e74fa59dc1a0a0e5f64e6b7359fe6f21a983d"
menu_path: ["Prepr CMS & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/payload/index.md", "title": "Payload CMS & Astro"}
nav_next: {"path": "astro/en/guides/cms/prismic/index.md", "title": "Prismic & Astro"}
---

# Prepr CMS & Astro

[Prepr CMS](https://www.prepr.io/) is a headless CMS with built-in personalization.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

Prepr CMS provides a [GraphQL API](https://docs.prepr.io/reference/graphql/v1/overview) to connect your data to Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need the following:

*   A new or existing Astro project configured for [on-demand rendering](../../on-demand-rendering/index.md).
*   [A free Prepr account](https://signup.prepr.io/)
*   [A Prepr environment with existing blog posts](https://docs.prepr.io/account/set-up-environments#create-an-envirntonment). These posts must include a `title` and `content`. Other fields are optional.

### Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add the Prepr endpoint to your Astro project, create a `.env file` in the root of your project if one does not already exist and add the following variable:

```
PREPR_ENDPOINT=YOUR_PREPR_API_URL
```

You will find your `YOUR_PREPR_API_URL` value from your Prepr account settings:

1.  Go to  **Settings > Access tokens** to view both your Preview and Production access tokens.
    
2.  Use the **API URL** value from the **GraphQL Production** access token to only retrieve published content items for your Astro site.
    

### Configuring the Prepr endpoint

[Section titled “Configuring the Prepr endpoint”](#configuring-the-prepr-endpoint)

Create a new folder `src/lib/` and add a new file called `prepr.js`. This is where you will configure the Prepr endpoint. Add the following code to fetch your data from Prepr CMS:

```
export async function Prepr(query, variables) {    const response = await fetch(import.meta.env.PREPR_ENDPOINT, {        method: 'POST',        headers: {            'Content-Type': 'application/json'        },        body: JSON.stringify({ query, variables }),    })    return response}
```

Your root directory should now include these files:

*   Directorysrc/
    
    *   Directorylib/
        
        *   **prepr.js**
        
    
*   **.env**
*   astro.config.mjs
*   package.json

### Fetching data

[Section titled “Fetching data”](#fetching-data)

You will fetch your data from Prepr by writing queries to interact with its GraphQL API.

#### Create a GraphQL query to retrieve your blog articles:

[Section titled “Create a GraphQL query to retrieve your blog articles:”](#create-a-graphql-query-to-retrieve-your-blog-articles)

1.  Create a new folder `src/queries/` and add a file named `get-articles.js`.
    
2.  Add the following query to this file to retrieve all articles:
    
    ```
    const GetArticles = `query {    Articles {      items {        _id        _slug        title    }  }}`export default GetArticles
    ```
    
3.  To display a linked list of your blog posts on a page, import and execute your query, including the necessary Prepr endpoint. You will then have access to all your posts titles and their slugs to render to the page. (In the next step, you will [create individual pages for your blog posts](#creating-individual-blog-post-pages).)
    
    ```
    ---import Layout from '../layouts/Layout.astro';import { Prepr } from '../lib/prepr.js';import GetArticles from '../queries/get-articles.js';
    const response = await Prepr(GetArticles)const { data } = await response.json()const articles = data.Articles---
    <Layout title="My blog site">  <h1>    My blog site  </h1>  <ul>    {      articles.items.map((post) => (        <li>          <a href={post._slug}>{post.title}</a>        </li>      ))    }  </ul></Layout>
    ```
    

Your root directory should include these new files:

*   Directorysrc/
    
    *   Directorylib/
        
        *   prepr.js
        
    *   Directorypages/
        
        *   index.astro
        
    *   Directory**queries** /
        
        *   **get-articles.js**
        
    
*   .env
*   astro.config.mjs
*   package.json

#### Creating individual blog post pages

[Section titled “Creating individual blog post pages”](#creating-individual-blog-post-pages)

To create a page for each blog post, you will execute a new GraphQL query on a [dynamic routing](../../routing/index.md#on-demand-dynamic-routes) `.astro` page. This query will fetch a specific article by its slug and a new page will be created for each individual blog post.

1.  Create a file called `get-article-by-slug.js` in the `queries` folder and add the following to query a specific article by its slug and return data such as the article `title` and `content`:
    
    ```
    const GetArticleBySlug = `query ($slug: String) {   Article (slug: $slug) {     _id     title     content {       __typename       ... on Text {         body         text       }       ... on Assets {         items {           url         }       }     }   }}`
    export default GetArticleBySlug
    ```
    
2.  Inside the `src/pages` folder, create a file called `[…slug].astro`. Add the following code to import and execute the query from the previous step and display the retrieved article:
    
    ```
    ---import Layout from '../layouts/Layout.astro';import {Prepr} from '../lib/prepr.js';import GetArticleBySlug from '../queries/get-article-by-slug.js';
    const { slug } = Astro.params;const response = await Prepr(GetArticleBySlug, {slug})const { data } = await response.json()const article = data.Article---
    <Layout title={article.title}>  <main>    <h1>{article.title}</h1>    {      article.content.map((content) => (        <div>          {            content.__typename === "Assets" &&            <img src={content.items[0].url} width="300" height="250"/>          }          {            content.__typename === 'Text' &&            <div set:html={content.body}></div>          }        </div>      ))    }  </main></Layout>
    ```
    

Your root directory should now include these new files:

*   Directorysrc/
    
    *   Directorylib/
        
        *   prepr.js
        
    *   Directorypages/
        
        *   index.astro
        *   **\[…slug\].astro**
        
    *   Directoryqueries/
        
        *   get-articles.js
        *   **get-article-by-slug.js**
        
    
*   .env
*   astro.config.mjs
*   package.json

Now, when you click an article link from the main list of blog posts, you will be taken to a page with its individual content.

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your Prepr blog, visit our [deployment guides](../../deploy/index.md) and follow the instructions for your preferred hosting provider.

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   Follow the [Prepr CMS Astro quickstart](https://github.com/preprio/astro-quick-start) guide to make a simple blog with Astro and Prepr CMS. 
*   Check out the [Connecting Prepr CMS to Astro](https://docs.prepr.io/connecting-front-end-apps/astro) for an overview of Astro and Prepr CMS resources.

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
    
    ### [Prepr CMS](index.md)
    
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
