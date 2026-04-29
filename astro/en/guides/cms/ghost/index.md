---
title: "Ghost & Astro"
source: "https://docs.astro.build/en/guides/cms/ghost/"
canonical_url: "https://docs.astro.build/en/guides/cms/ghost/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:20.154Z"
content_hash: "b60a6e3fe62dcbd7a7c4c665a79bf46ed7e1f03e4cd3dede728098e3d1c39126"
menu_path: ["Ghost & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/frontmatter-cms/index.md", "title": "Front Matter CMS & Astro"}
nav_next: {"path": "astro/en/guides/cms/gitcms/index.md", "title": "GitCMS & Astro"}
---

# Ghost & Astro

[Ghost](https://github.com/TryGhost/Ghost) is an open-source, headless content management system built on Node.js.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, we’ll use the [Ghost content API](https://ghost.org/docs/content-api/) to bring your data into your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started you will need to have the following:

1.  **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](../../../install-and-setup/index.md) will get you up and running in no time.
    
2.  **A Ghost site** - It is assumed that you have a site set up with Ghost. If you don’t you can set one up on a [local environment.](https://ghost.org/docs/install/local/)
    
3.  **Content API Key** - You can make an integration under your site’s `Settings > Integrations`. From there you can find your `Content API key`
    

### Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add your site’s credentials to Astro, create an `.env` file in the root of your project with the following variable:

```
CONTENT_API_KEY=YOUR_API_KEY
```

Now, you should be able to use this environment variable in your project.

If you would like to have IntelliSense for your environment variable, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

```
interface ImportMetaEnv {  readonly CONTENT_API_KEY: string;}
```

Your root directory should now include these new files:

*   Directorysrc/
    
    *   **env.d.ts**
    
*   **.env**
*   astro.config.mjs
*   package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect with Ghost, install the official content API wrapper [`@tryghost/content-api`](https://www.npmjs.com/package/@tryghost/content-api) using the command below for your preferred package manager, and optionally, a helpful package containing type definitions if you are using TypeScript:

*   [npm](#tab-panel-1491)
*   [pnpm](#tab-panel-1492)
*   [Yarn](#tab-panel-1493)

```
npm install @tryghost/content-apinpm install --save @types/tryghost__content-api
```

## Making a blog with Astro and Ghost

[Section titled “Making a blog with Astro and Ghost”](#making-a-blog-with-astro-and-ghost)

With the setup above, you are now able to create a blog that uses Ghost as the CMS.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1.  A Ghost blog
2.  An Astro project integrated with the [Ghost content API](https://www.npmjs.com/package/@tryghost/content-api) - See [integrating with Astro](index.md#integrating-with-astro) for more details on how to set up an Astro project with Ghost.

This example will create an index page that lists posts with links to dynamically-generated individual post pages.

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

You can fetch your site’s data with the Ghost content API package.

First, create a `ghost.ts` file under a `lib` directory.

*   Directorysrc/
    
    *   Directorylib/
        
        *   **ghost.ts**
        
    *   Directorypages/
        
        *   index.astro
        
    
*   astro.config.mjs
*   package.json

Initialize an API instance with the Ghost API using the API key from the Ghost dashboard’s Integrations page.

```
import GhostContentAPI from '@tryghost/content-api';
// Create API instance with site credentialsexport const ghostClient = new GhostContentAPI({    url: 'http://127.0.0.1:2368', // This is the default URL if your site is running on a local environment    key: import.meta.env.CONTENT_API_KEY,    version: 'v5.0',});
```

### Displaying a list of posts

[Section titled “Displaying a list of posts”](#displaying-a-list-of-posts)

The page `src/pages/index.astro` will display a list of posts, each with a description and link to its own page.

*   Directorysrc/
    
    *   Directorylib/
        
        *   ghost.ts
        
    *   Directorypages/
        
        *   **index.astro**
        
    
*   astro.config.mjs
*   package.json

Import `ghostClient()` in the Astro frontmatter to use the `posts.browse()` method to access blog posts from Ghost. Set `limit: all` to retrieve all posts.

```
---import { ghostClient } from '../lib/ghost';const posts = await ghostClient.posts    .browse({        limit: 'all',    })    .catch((err) => {        console.error(err);    });---
```

Fetching via the content API returns an array of objects containing the [properties for each post](https://ghost.org/docs/content-api/#posts) such as:

*   `title` - the title of the post
*   `html` - the HTML rendering of the content of the post
*   `feature_image` - the source URL of the featured image of the post
*   `slug` - the slug of the post

Use the `posts` array returned from the fetch to display a list of blog posts on the page.

```
---import { ghostClient } from '../lib/ghost';const posts = await ghostClient.posts    .browse({        limit: 'all',    })    .catch((err) => {        console.error(err);    });---
<html lang="en">    <head>        <title>Astro + Ghost 👻</title>    </head>    <body>
        {            posts.map((post) => (                <a href={`/post/${post.slug}`}>                    <h1> {post.title} </h1>                </a>            ))        }    </body></html>
```

### Generating pages

[Section titled “Generating pages”](#generating-pages)

The page `src/pages/post/[slug].astro` [dynamically generates a page](../../routing/index.md#dynamic-routes) for each post.

*   Directorysrc/
    
    *   Directorylib/
        
        *   ghost.ts
        
    *   Directorypages/
        
        *   index.astro
        *   Directorypost/
            
            *   **\[slug\].astro**
            
        
    
*   astro.config.mjs
*   package.json

Import `ghostClient()` to access blog posts using `posts.browse()` and return a post as props to each of your dynamic routes.

```
---import { ghostClient } from '../../lib/ghost';
export async function getStaticPaths() {    const posts = await ghostClient.posts        .browse({            limit: 'all',        })        .catch((err) => {            console.error(err);        });
    return posts.map((post) => {        return {            params: {                slug: post.slug,            },            props: {                post: post,            },        };    });}
const { post } = Astro.props;---
```

Create the template for each page using the properties of each `post` object.

```
---import { ghostClient } from '../../lib/ghost';export async function getStaticPaths() {    const posts = await ghostClient.posts        .browse({            limit: 'all',        })        .catch((err) => {            console.error(err);        });    return posts.map((post) => {        return {            params: {                slug: post.slug,            },            props: {                post: post,            },        };    });}const { post } = Astro.props;---<!DOCTYPE html><html lang="en">    <head>        <title>{post.title}</title>    </head>    <body>        <img src={post.feature_image} alt={post.title} />
        <h1>{post.title}</h1>        <p>{post.reading_time} min read</p>
        <Fragment set:html={post.html} />    </body></html>
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your site visit our [deployment guide](../../deploy/index.md) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Ghost CMS & Astro Tutorial](https://matthiesen.xyz/blog/astro-ghostcms)

[Astro + Ghost + Tailwind CSS](https://andr.ec/posts/astro-ghost-blog/)

[Building a Corporate site with Astro and Ghost](https://artabric.com/post/building-a-corporate-site-with-astro-and-ghost/)

[\`astro-starter-ghost\`](https://github.com/PhilDL/astro-starter-ghost)

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
    
    ### [Ghost](index.md)
    
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
