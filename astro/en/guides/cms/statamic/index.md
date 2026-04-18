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
2.  **An Astro project** - If you still need an Astro project, our [Installation guide](/en/install-and-setup/) will get you up and running quickly.
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

To deploy your Astro site visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

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


