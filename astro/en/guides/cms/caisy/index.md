---
title: "Caisy & Astro"
source: "https://docs.astro.build/en/guides/cms/caisy/"
canonical_url: "https://docs.astro.build/en/guides/cms/caisy/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:21.423Z"
content_hash: "9b3652e9752995300572a545cce8443ca9d63be34d7fce9dbdb4764b312ae7ee"
menu_path: ["Caisy & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/buttercms/index.md", "title": "ButterCMS & Astro"}
nav_next: {"path": "astro/en/guides/cms/cloudcannon/index.md", "title": "CloudCannon & Astro"}
---

# Caisy & Astro

[Caisy](https://caisy.io/) is a headless CMS that exposes a GraphQL API to access content.

## Using Caisy CMS with Astro

[Section titled “Using Caisy CMS with Astro”](#using-caisy-cms-with-astro)

Use `graphql-request` and Caisy’s rich text renderer for Astro to fetch your CMS data and display your content on an Astro page:

```
---import RichTextRenderer from '@caisy/rich-text-astro-renderer';import { gql, GraphQLClient } from 'graphql-request';
const params = Astro.params;
const client = new GraphQLClient(  `https://cloud.caisy.io/api/v3/e/${import.meta.env.CAISY_PROJECT_ID}/graphql`,  {    headers: {      'x-caisy-apikey': import.meta.env.CAISY_API_KEY    }  });const gqlResponse = await client.request(  gql`    query allBlogArticle($slug: String) {      allBlogArticle(where: { slug: { eq: $slug } }) {        edges {          node {            text {              json            }            title            slug            id          }        }      }    }  `,  { slug: params.slug });
const post = gqlResponse?.allBlogArticle?.edges?.[0]?.node;---<h1>{post.title}</h1><RichTextRenderer node={post.text.json} />
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   Check out the Caisy + Astro example on [GitHub](https://github.com/caisy-io/caisy-example-astro) or [StackBlitz](https://stackblitz.com/github/caisy-io/caisy-example-astro?file=src%2Fpages%2Fblog%2F%5B...slug%5D.astro)
*   Query your documents in [draft mode](https://caisy.io/developer/docs/external-api/localization-and-preview#preview-mode-15) and multiple [locales](https://caisy.io/developer/docs/external-api/localization-and-preview#localization-in-a-graphql-query-8).
*   Use [pagination](https://caisy.io/developer/docs/external-api/queries-pagination) to query large numbers of documents.
*   Use [filter](https://caisy.io/developer/docs/external-api/external-filter-and-sorting) in your queries and [order](https://caisy.io/developer/docs/external-api/external-filter-and-sorting#sorting-8) the results

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
    
    ### [Caisy](index.md)
    
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
