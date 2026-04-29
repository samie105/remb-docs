---
title: "Keystatic & Astro"
source: "https://docs.astro.build/en/guides/cms/keystatic/"
canonical_url: "https://docs.astro.build/en/guides/cms/keystatic/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:36.722Z"
content_hash: "7f1c804b1f869d930a3f8d58cbd4403c90a82883213dfaabb32a9fff1570b0ce"
menu_path: ["Keystatic & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/jekyllpad/index.md", "title": "JekyllPad & Astro"}
nav_next: {"path": "astro/en/guides/cms/keystonejs/index.md", "title": "KeystoneJS & Astro"}
---

# Keystatic & Astro

[Keystatic](https://keystatic.com/) is an open source, headless content-management system that allows you to structure your content and sync it with GitHub.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

*   An existing Astro project [with an adapter configured](../../on-demand-rendering/index.md).

## Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

Add both the Markdoc (for content entries) and the React (for the Keystatic Admin UI Dashboard) integrations to your Astro project, using the `astro add` command for your package manager.

*   [npm](#tab-panel-1500)
*   [pnpm](#tab-panel-1501)
*   [Yarn](#tab-panel-1502)

```
npx astro add react markdoc
```

You will also need two Keystatic packages:

*   [npm](#tab-panel-1503)
*   [pnpm](#tab-panel-1504)
*   [Yarn](#tab-panel-1505)

```
npm install @keystatic/core @keystatic/astro
```

## Adding the Astro integration

[Section titled “Adding the Astro integration”](#adding-the-astro-integration)

Add the Astro integration from `@keystatic/astro` in your Astro config file:

```
import { defineConfig } from 'astro/config'
import react from '@astrojs/react'import markdoc from '@astrojs/markdoc'import keystatic from '@keystatic/astro'
// https://astro.build/configexport default defineConfig({  integrations: [react(), markdoc(), keystatic()],  output: 'static',})
```

## Creating a Keystatic config file

[Section titled “Creating a Keystatic config file”](#creating-a-keystatic-config-file)

A Keystatic config file is required to define your content schema. This file will also allow you to connect a project to a specific GitHub repository (if you decide to do so).

Create a file called `keystatic.config.ts` in the root of the project and add the following code to define both your storage type (`local`) and a single content collection (`posts`):

```
import { config, fields, collection } from '@keystatic/core';
export default config({  storage: {    kind: 'local',  },
  collections: {    posts: collection({      label: 'Posts',      slugField: 'title',      path: 'src/content/posts/*',      format: { contentField: 'content' },      schema: {        title: fields.slug({ name: { label: 'Title' } }),        content: fields.markdoc({          label: 'Content',        }),      },    }),  },});
```

Keystatic is now configured to manage your content based on your schema.

## Running Keystatic locally

[Section titled “Running Keystatic locally”](#running-keystatic-locally)

To launch your Keystatic Admin UI dashboard, start Astro’s dev server:

```
npm run dev
```

Visit `http://127.0.0.1:4321/keystatic` in the browser to see the Keystatic Admin UI running.

## Creating a new post

[Section titled “Creating a new post”](#creating-a-new-post)

1.  In the Keystatic Admin UI dashboard, click on the “Posts” collection.
    
2.  Use the button to create a new post. Add the title “My First Post” and some content, then save the post.
    
3.  This post should now be visible from your “Posts” collection. You can view and edit your individual posts from this dashboard page.
    
4.  Return to view your Astro project files. You will now find a new `.mdoc` file inside the `src/content/posts` directory for this new post:
    
    *   Directorysrc/
        
        *   Directorycontent/
            
            *   Directoryposts/
                
                *   **my-first-post.mdoc**
                
            
        
    
5.  Navigate to that file in your code editor and verify that you can see the Markdown content you entered. For example:
    
    ```
    ---title: My First Post---
    This is my very first post. I am **super** excited!
    ```
    

## Rendering Keystatic content

[Section titled “Rendering Keystatic content”](#rendering-keystatic-content)

[Query and display your posts and collections](../../content-collections/index.md#querying-build-time-collections), just as you would in any Astro project.

### Displaying a collection list

[Section titled “Displaying a collection list”](#displaying-a-collection-list)

The following example displays a list of each post title, with a link to an individual post page.

```
---import { getCollection } from 'astro:content'
const posts = await getCollection('posts')---<ul>  {posts.map(post => (    <li>      <a href={`/posts/${post.id}`}>{post.data.title}</a>    </li>  ))}</ul>
```

### Displaying a single entry

[Section titled “Displaying a single entry”](#displaying-a-single-entry)

To display content from an individual post, you can import and use the `<Content />` component to [render your content to HTML](../../content-collections/index.md#rendering-body-content):

```
---import { getEntry } from 'astro:content'
const post = await getEntry('posts', 'my-first-post')const { Content } = await post.render()---
<main>  <h1>{post.data.title}</h1>  <Content /></main>
```

For more information on querying, filtering, displaying your collections content and more, see the full content [collections documentation](../../content-collections/index.md).

## Deploying Keystatic + Astro

[Section titled “Deploying Keystatic + Astro”](#deploying-keystatic--astro)

To deploy your website, visit our [deployment guides](../../deploy/index.md) and follow the instructions for your preferred hosting provider.

You’ll also probably want to [connect Keystatic to GitHub](https://keystatic.com/docs/connect-to-github) so you can manage content on the deployed instance of the project.

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   Check out [the official Keystatic guide](https://keystatic.com/docs/installation-astro)
*   [Keystatic starter template](https://github.com/Thinkmill/keystatic/tree/main/templates/astro)

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
    
    ### [Keystatic](index.md)
    
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
