---
title: "Hashnode & Astro"
source: "https://docs.astro.build/en/guides/cms/hashnode/"
canonical_url: "https://docs.astro.build/en/guides/cms/hashnode/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:28.186Z"
content_hash: "668ba8d7ff2cb0ef6e77c236cb5e7cc99a958bca97a379b3db43701ab511fa2a"
menu_path: ["Hashnode & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/gitcms/index.md", "title": "GitCMS & Astro"}
nav_next: {"path": "astro/en/guides/cms/hygraph/index.md", "title": "Hygraph & Astro"}
---

# Hashnode & Astro

[Hashnode](https://hashnode.com/) is a hosted CMS that allows you to create a blog or publication.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

The [Hashnode Public API](https://apidocs.hashnode.com/) is a GraphQL API that allows you to interact with Hashnode. This guide uses [`graphql-request`](https://github.com/jasonkuhrt/graphql-request), a minimal GraphQL client that works well with Astro, to bring your Hashnode data into your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started you will need to have the following:

1.  **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](../../../install-and-setup/index.md) will get you up and running in no time.
    
2.  **A Hashnode site** - You can create free personal site by visiting [Hashnode](https://hashnode.com/).
    

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

Install the `graphql-request` package using the package manager of your choice:

*   [npm](#tab-panel-1494)
*   [pnpm](#tab-panel-1495)
*   [Yarn](#tab-panel-1496)

```
npm install graphql-request
```

## Making a blog with Astro and Hashnode

[Section titled “Making a blog with Astro and Hashnode”](#making-a-blog-with-astro-and-hashnode)

This guide uses [`graphql-request`](https://github.com/jasonkuhrt/graphql-request), a minimal GraphQL client that works well with Astro, to bring your Hashnode data into your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1.  A Hashnode Blog
2.  An Astro project integrated with the [graphql-request](https://github.com/jasonkuhrt/graphql-request) package installed.

This example will create an index page that lists posts with links to dynamically-generated individual post pages.

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

1.  To fetch your site’s data with the `graphql-request` package, make a `src/lib` directory and create two new files `client.ts` & `schema.ts`:
    
    *   Directorysrc/
        
        *   Directorylib/
            
            *   **client.ts**
            *   **schema.ts**
            
        *   Directorypages/
            
            *   index.astro
            
        
    *   astro.config.mjs
    *   package.json
    
2.  Initialize an API instance with the GraphQLClient using the URL from your Hashnode Website.
    
    ```
    import { gql, GraphQLClient } from "graphql-request";import type { AllPostsData, PostData } from "./schema";
    export const getClient = () => {  return new GraphQLClient("https://gql.hashnode.com")}
    const myHashnodeURL = "astroplayground.hashnode.dev";
    export const getAllPosts = async () => {  const client = getClient();
      const allPosts = await client.request<AllPostsData>(    gql`      query allPosts {        publication(host: "${myHashnodeURL}") {          id          title          posts(first: 20) {            pageInfo{              hasNextPage              endCursor            }            edges {              node {                id                author{                  name                  profilePicture                }                title                subtitle                brief                slug                coverImage {                  url                }                tags {                  name                  slug                }                publishedAt                readTimeInMinutes              }            }          }        }      }    `  );
      return allPosts;};
    
    export const getPost = async (slug: string) => {  const client = getClient();
      const data = await client.request<PostData>(    gql`      query postDetails($slug: String!) {        publication(host: "${myHashnodeURL}") {          id          post(slug: $slug) {            id            author{              name              profilePicture            }            publishedAt            title            subtitle            readTimeInMinutes            content{              html            }            tags {              name              slug            }            coverImage {              url            }          }        }      }    `,    { slug: slug }  );
      return data.publication.post;};
    ```
    
3.  Configure `schema.ts` to define the shape of the data returned from the Hashnode API.
    
    ```
    import { z } from "astro/zod";
    export const PostSchema = z.object({    id: z.string(),    author: z.object({        name: z.string(),        profilePicture: z.string(),        }),    publishedAt: z.string(),    title: z.string(),    subtitle: z.string(),    brief: z.string(),    slug: z.string(),    readTimeInMinutes: z.number(),    content: z.object({        html: z.string(),    }),    tags: z.array(z.object({        name: z.string(),        slug: z.string(),    })),    coverImage: z.object({        url: z.string(),    }),})
    export const AllPostsDataSchema = z.object({    id: z.string(),    publication: z.object({        title: z.string(),        posts: z.object({            pageInfo: z.object({                hasNextPage: z.boolean(),                endCursor: z.string(),            }),            edges: z.array(z.object({                node: PostSchema,            })),        }),    }),})
    export const PostDataSchema = z.object({    id: z.string(),    publication: z.object({        title: z.string(),        post: PostSchema,    }),})
    export type Post = z.infer<typeof PostSchema>export type AllPostsData = z.infer<typeof AllPostsDataSchema>export type PostData = z.infer<typeof PostDataSchema>
    ```
    

### Displaying a list of posts

[Section titled “Displaying a list of posts”](#displaying-a-list-of-posts)

Fetching via `getAllPosts()` returns an array of objects containing the properties for each post such as:

*   `title` - the title of the post
*   `brief` - the HTML rendering of the content of the post
*   `coverImage.url` - the source URL of the featured image of the post
*   `slug` - the slug of the post

Use the `posts` array returned from the fetch to display a list of blog posts on the page.

```
---import { getAllPosts } from '../lib/client';
const data = await getAllPosts();const allPosts = data.publication.posts.edges;
---
<html lang="en">    <head>        <title>Astro + Hashnode</title>    </head>    <body>
        {            allPosts.map((post) => (                <div>                    <h2>{post.node.title}</h2>                    <p>{post.node.brief}</p>                    <img src={post.node.coverImage.url} alt={post.node.title} />                    <a href={`/post/${post.node.slug}`}>Read more</a>                </div>            ))        }    </body></html>
```

### Generating pages

[Section titled “Generating pages”](#generating-pages)

1.  Create the page `src/pages/post/[slug].astro` to [dynamically generate a page](../../routing/index.md#dynamic-routes) for each post.
    
    *   Directorysrc/
        
        *   Directorylib/
            
            *   client.ts
            *   schema.ts
            
        *   Directorypages/
            
            *   index.astro
            *   Directorypost/
                
                *   **\[slug\].astro**
                
            
        
    *   astro.config.mjs
    *   package.json
    
2.  Import and use `getAllPosts()` and `getPost()` to fetch the data from Hashnode and generate individual page routes for each post.
    
    ```
    ---import { getAllPosts, getPost } from '../../lib/client';
    
    export async function getStaticPaths() {  const data = await getAllPosts();  const allPosts = data.publication.posts.edges;  return allPosts.map((post) => {    return {      params: { slug: post.node.slug },    }  })}const { slug } = Astro.params;const post = await getPost(slug);
    ---
    ```
    
3.  Create the template for each page using the properties of each `post` object. The example below shows the post title and reading time, then the full post content:
    
    ```
    ---import { getAllPosts, getPost } from '../../lib/client';
    
    export async function getStaticPaths() {  const data = await getAllPosts();  const allPosts = data.publication.posts.edges;  return allPosts.map((post) => {    return {      params: { slug: post.node.slug },    }  })}const { slug } = Astro.params;const post = await getPost(slug);
    ---<!DOCTYPE html><html lang="en">    <head>        <title>{post.title}</title>    </head>    <body>        <img src={post.coverImage.url} alt={post.title} />
            <h1>{post.title}</h1>        <p>{post.readTimeInMinutes} min read</p>
            <Fragment set:html={post.content.html} />    </body></html>
    ```
    

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your site visit our [deployment guide](../../deploy/index.md) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [`astro-hashnode`](https://github.com/matthiesenxyz/astro-hashnode) on GitHub

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
    
    ### [Hashnode](index.md)
    
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
