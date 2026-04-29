---
title: "Headless Statamic & Astro"
source: "https://docs.astro.build/en/guides/cms/statamic/"
canonical_url: "https://docs.astro.build/en/guides/cms/statamic/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:27.054Z"
content_hash: "675b54c47780331f10b3e0525c63f883bf222b583c8043a5f9f092da5545e4d4"
menu_path: ["Headless Statamic & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/spinal/index.md", "title": "Spinal & Astro"}
nav_next: {"path": "astro/en/guides/cms/storyblok/index.md", "title": "Storyblok & Astro"}
---

# Headless Statamic & Astro

[Statamic](https://statamic.com/) is a modern, flat-file CMS. It allows developers to easily create dynamic websites and applications while offering content editors an intuitive and user-friendly interface for managing content.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

Statamic comes with a built-in [REST API](https://statamic.dev/rest-api) and [GraphQL API](https://statamic.dev/graphql) to connect your data to Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1.  REST API and GraphQL API are only available in a pro version of Statamic. You can try the Pro version free on your [local machine](https://statamic.dev/tips/how-to-enable-statamic-pro#trial-mode).
2.  **An Astro project** - If you still need an Astro project, our [Installation guide](../../../install-and-setup/index.md) will get you up and running quickly.
3.  **A Statamic site** - If you need a Statamic website, [this guide](https://statamic.dev/quick-start-guide) will help you get started. Remember to [enable REST API](https://statamic.dev/rest-api#enable-the-api) or [GraphQL API](https://statamic.dev/graphql#enable-graphql) by adding `STATAMIC_API_ENABLED=true` or `STATAMIC_GRAPHQL_ENABLED=true` in the `.env` file and enable required resources in the API configuration file.

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

#### REST API

[Section titled “REST API”](#rest-api)

Fetch your Statamic data from your site’s REST API URL. By default, it’s `https://[YOUR-SITE]/api/`. Then, you can render your data properties using Astro’s `set:html={}` directive.

For example, to display a list of titles and their content from a selected [collection](https://statamic.dev/collections):

```
---const res = await fetch("https://[YOUR-SITE]/api/collections/posts/entries?sort=-date")const posts = await res.json()---<h1>Astro + Statamic 🚀</h1>{  posts.map((post) => (      <h2 set:html={post.title} />      <p set:html={post.content} />  ))}
```

#### GraphQL

[Section titled “GraphQL”](#graphql)

Fetch your Statamic data with your site’s GraphQL API URL. By default, it’s `https://[YOUR-SITE]/graphql/`. Then, you can render your data properties using Astro’s `set:html={}` directive.

For example, to display a list of titles and their content from a selected [collection](https://statamic.dev/collections):

```
---const graphqlQuery = {  query: `    query Entries($page: Int, $locale: String) {      entries(        collection: "posts"        sort: "date asc"        limit: 20        page: $page        filter: { locale: $locale }      ) {        current_page        has_more_pages        data {          title          ... on Entry_Posts_Post {              content            }        }      }    }  `,  variables: {    page: page,    locale: locale,  },};
const res = await fetch("https://[YOUR-SITE]/graphql", {  method: "POST",  headers: { "Content-Type": "application/json" },  body: JSON.stringify(graphqlQuery),})
const { data } = await res.json();const entries = data?.entries;---<h1>Astro + Statamic 🚀</h1>{  entries.data.map((post) => (      <h2 set:html={post.title} />      <p set:html={post.content} />  ))}
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your Astro site visit our [deployment guides](../../deploy/index.md) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [How to build a static site using Statamic as headless CMS](https://buddy.works/guides/statamic-rest-api)
*   [Implementing Astro live previews in headless Statamic](https://maciekpalmowski.dev/implementing-live-previews-in-headless-statamic-when-using-astro/)

## Themes

[Section titled “Themes”](#themes)

*    [![](/_astro/creek.CgpBUanV_Mku4I.webp) Creek](https://astro.build/themes/details/creek/)

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
    
    ### [Statamic](index.md)
    
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
