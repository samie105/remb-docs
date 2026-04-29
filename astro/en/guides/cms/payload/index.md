---
title: "Payload CMS & Astro"
source: "https://docs.astro.build/en/guides/cms/payload/"
canonical_url: "https://docs.astro.build/en/guides/cms/payload/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:05.899Z"
content_hash: "b98d8a2c4bd32e145e94175276be70f93cd4a358eb6fcec381bc92412fbecb80"
menu_path: ["Payload CMS & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/pages-cms/index.md", "title": "Pages CMS & Astro"}
nav_next: {"path": "astro/en/guides/cms/preprcms/index.md", "title": "Prepr CMS & Astro"}
---

# Payload CMS & Astro

[PayloadCMS](https://payloadcms.com/) is a headless open-source content management system that can be used to provide content for your Astro project.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

1.  **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](../../../install-and-setup/index.md) will get you up and running in no time.
2.  **A MongoDB database** - PayloadCMS will ask you for a MongoDB connection string when creating a new project. You can set one up locally or use [MongoDBAtlas](https://www.mongodb.com/) to host a database on the web for free.
3.  **A PayloadCMS REST API** - Create a [PayloadCMS](https://payloadcms.com/docs/getting-started/installation) project and connect it to your MongoDB database during the setup.

### Configuring Astro for your PayloadCMS collection

[Section titled “Configuring Astro for your PayloadCMS collection”](#configuring-astro-for-your-payloadcms-collection)

Your Payload project template will contain a file called Posts.ts in `src/collections/`. If you did not choose a template during installation that created a content collection for you, you can create a new Payload CMS Collection by adding this configuration file manually. The example below shows this file for a collection called `posts` that requires `title`, `content`, and `slug` fields:

```
import { CollectionConfig } from "payload/types";
const Posts: CollectionConfig = {  slug: "posts",  admin: {    useAsTitle: "title",  },  access: {    read: () => true,  },
  fields: [    {      name: "title",      type: "text",      required: true,    },    {      name: "content",      type: "text",      required: true,    },    {      name: "slug",      type: "text",      required: true,    },  ],};
export default Posts;
```

1.  Import and add both `Users` (available in all PayloadCMS projects) and any other collections (e.g. `Posts`) to the available collections in the `payload.config.ts` file.
    
    ```
    import { buildConfig } from "payload/config";import path from "path";
    import Users from "./collections/Users";import Posts from "./collections/Posts";
    export default buildConfig({  serverURL: "http://localhost:4321",  admin: {    user: Users.slug,  },  collections: [Users, Posts],  typescript: {    outputFile: path.resolve(__dirname, "payload-types.ts"),  },  graphQL: {    schemaOutputFile: path.resolve(__dirname, "generated-schema.graphql"),  },});
    ```
    
    This will make a new collection called “Posts” appear in your PayloadCMS Dashboard next to the “Users” collection.
    
2.  Enter the “Posts” collection and create a new post. After saving it, you will notice the API URL appear in the bottom right corner.
    
3.  With the dev server running, open `http://localhost:4321/api/posts` in your browser. You should see a JSON file containing the post you have created as an object.
    
    ```
    {  "docs":[      {        "id":"64098b16483b0f06a7e20ed4",        "title":"Astro & PayloadCMS Title 🚀",        "content":"Astro & PayloadCMS Content",        "slug":"astro-payloadcms-slug",        "createdAt":"2023-03-09T07:30:30.837Z",        "updatedAt":"2023-03-09T07:30:30.837Z"      }  ],  "totalDocs":1,  "limit":10,  "totalPages":1,  "page":1,  "pagingCounter":1,  "hasPrevPage":false,  "hasNextPage":false,  "prevPage":null,  "nextPage":null}
    ```
    

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

Fetch your PayloadCMS data through your site’s unique REST API URL and the route for your content. (By default, PayloadCMS will mount all routes through `/api`.) Then, you can render your data properties using Astro’s `set:html=""` directive.

Together with your post, PayloadCMS will return some top-level metadata. The actual documents are nested within the `docs` array.

For example, to display a list of post titles and their content:

```
---import HomeLayout from "../layouts/HomeLayout.astro";
const res = await fetch("http://localhost:5000/api/posts") // http://localhost:4321/api/posts by defaultconst posts = await res.json()---
<HomeLayout title='Astro Blog'>  {    posts.docs.map((post) => (        <h2 set:html={post.title} />        <p set:html={post.content} />    ))  }</HomeLayout>
```

## Building a blog with PayloadCMS and Astro

[Section titled “Building a blog with PayloadCMS and Astro”](#building-a-blog-with-payloadcms-and-astro)

Create a blog index page `src/pages/index.astro` to list each of your posts with a link to its own page.

Fetching via the API returns an array of objects (posts) that include, among others, the following properties:

*   `title`
*   `content`
*   `slug`

```
---import HomeLayout from "../layouts/HomeLayout.astro";
const res = await fetch("http://localhost:5000/api/posts") // http://localhost:4321/api/posts by defaultconst posts = await res.json()---
<HomeLayout title='Astro Blog'>  <h1>Astro + PayloadCMS 🚀</h1>  <h2>Blog posts list:</h2>  <ul>    {      posts.docs.map((post) =>(        <li>          <a href={`posts/${post.slug}`} set:html={post.title} />        </li>      ))    }  </ul></HomeLayout>
```

### Using the PayloadCMS API to generate pages

[Section titled “Using the PayloadCMS API to generate pages”](#using-the-payloadcms-api-to-generate-pages)

Create a page `src/pages/posts/[slug].astro` to [dynamically generate a page](../../routing/index.md#dynamic-routes) for each post.

```
---import PostLayout from "../../layouts/PostLayout.astro"
const {title, content} = Astro.props
// The getStaticPaths() is required for static Astro sites.// If using SSR, you will not need this function.export async function getStaticPaths() {    let data = await fetch("http://localhost:5000/api/posts")    let posts = await data.json()
    return posts.docs.map((post) => {        return {            params: {slug: post.slug},            props: {title: post.title, content: post.content},        };    });}---<PostLayout title={title}>    <article>        <h1 set:html={title} />        <p set:html={content} />    </article></PostLayout>
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your site visit our [deployment guide](../../deploy/index.md) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   Check out the [official Astro Payload CMS integration](https://github.com/payloadcms/payload/tree/main/examples/astro).
*   Try this [Payload CMS & Astro Template](https://github.com/Lambdo-Labs/payloadcms-astro-template).
*   Check out [Astroad](https://github.com/mooxl/astroad) for easy development and VPS deployment with Docker.

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
    
    ### [Payload CMS](index.md)
    
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
