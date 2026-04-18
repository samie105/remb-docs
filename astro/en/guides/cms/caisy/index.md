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
