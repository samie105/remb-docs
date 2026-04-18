---
title: "Flotiq & Astro"
source: "https://docs.astro.build/en/guides/cms/flotiq/"
canonical_url: "https://docs.astro.build/en/guides/cms/flotiq/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:11.031Z"
content_hash: "07d94d9db2064fa2c2e37d49f0d1d246123ade6d22804243d46ec2651a94a340"
menu_path: ["Flotiq & Astro"]
section_path: []
---
# Flotiq & Astro

[Flotiq](https://flotiq.com?utm_campaign=flotiq_at_astro_headless_cms&utm_medium=referral&utm_source=astro) is a headless CMS designed for various frontends, such as static sites, mobile, and web applications. Developers and content creators manage and deliver content through REST and GraphQL-based APIs.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

This guide will use the Flotiq headless CMS API with an Astro project to display content on your website.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

1.  **An Astro project** - You can create a new project using the `npm create astro@latest` command.
2.  **A Flotiq account** - If you don’t have an account, [sign up for free](https://editor.flotiq.com/register?utm_campaign=flotiq_at_astro_headless_cms&utm_medium=referral&utm_source=astro).
3.  **Flotiq read-only API key** - Find out [how to obtain your key](https://flotiq.com/docs/API/?utm_campaign=flotiq_at_astro_headless_cms&utm_medium=referral&utm_source=astro).

### Setting up the Environment variables

[Section titled “Setting up the Environment variables”](#setting-up-the-environment-variables)

Add the read-only API key from your Flotiq account to the `.env` file in the root of your Astro project:

```
FLOTIQ_API_KEY=__YOUR_FLOTIQ_API_KEY__
```

### Defining a Content Type in Flotiq

[Section titled “Defining a Content Type in Flotiq”](#defining-a-content-type-in-flotiq)

First, you need to define an example [Content Type Definition](https://flotiq.com/docs/panel/content-types/?utm_campaign=flotiq_at_astro_headless_cms&utm_medium=referral&utm_source=astro) in Flotiq to store data.

Log in to your Flotiq account and create a custom Content Type Definition with the following example `Blog Post` configuration:

*   **Label**: Blog Post
*   **API Name**: blogpost
*   **Fields**:
    *   **Title**: text, required
    *   **Slug**: text, required
    *   **Content**: rich text, required

Then, create one or more example [Content Objects](https://flotiq.com/docs/panel/content-objects/?utm_campaign=flotiq_at_astro_headless_cms&utm_medium=referral&utm_source=astro) using this `Blog Post` type.

### Installing the Flotiq TypeScript SDK

[Section titled “Installing the Flotiq TypeScript SDK”](#installing-the-flotiq-typescript-sdk)

To connect your project with Flotiq, install the [Flotiq SDK](https://github.com/flotiq/flotiq-api-ts) using the package manager of your choice:

*   [npm](#tab-panel-1485)
*   [pnpm](#tab-panel-1486)
*   [Yarn](#tab-panel-1487)

```
npm install flotiq-api-ts
```

Next, configure the SDK using your credentials. Create a new file named `flotiq.ts` inside the `src/lib` directory of your project:

```
import { FlotiqApi } from "flotiq-api-ts";
export const flotiq = new FlotiqApi(import.meta.env.FLOTIQ_API_KEY);
```

This configuration can now be used throughout your project.

### Fetching and Displaying Data from Flotiq

[Section titled “Fetching and Displaying Data from Flotiq”](#fetching-and-displaying-data-from-flotiq)

1.  Fetch the `Blog Post` data on an Astro page using your content’s custom API `BlogpostAPI`:
    
    ```
    ---import { flotiq } from "../lib/flotiq";
    const posts = await flotiq.BlogpostAPI.list();---
    ```
    
2.  Display the content in your Astro template. You will have access to the `title`, `slug`, and `content` of your posts as well as other `internal` post data:
    
    ```
    ---import { flotiq } from "../lib/flotiq";
    const posts = await flotiq.BlogpostAPI.list();---<html lang="en">  <head>    <title>Astro</title>  </head>  <body>    {posts.data?.map((post) => (      <section>        <a href={`/posts/${post.slug}`}>          <h2>{post.title}</h2>        </a>        <div>{post.internal?.createdAt}</div>        <div set:html={post.content}/>      </section>    ))}  </body></html>
    ```
    
3.  Start the dev server and visit your page preview at `http://localhost:4321` to see the list of your blog posts. Each post will link to a page that does not yet exist. These will be created in the next step.
    

### Generating Individual Pages

[Section titled “Generating Individual Pages”](#generating-individual-pages)

Astro supports both prerendering all your pages ahead of time, or creating routes on demand when they are requested. Follow the instructions for either [static site generation](#static-site-generation) or [on-demand rendering](#on-demand-rendering) to build the page routes for your blog posts.

#### Static Site Generation

[Section titled “Static Site Generation”](#static-site-generation)

In static site generation (SSG) mode, use the `getStaticPaths()` method to fetch all possible blog post paths from Flotiq.

1.  Create a new file `[slug].astro` in the `/src/pages/posts/` directory. Fetch all blog posts and return them within the `getStaticPaths()` method:
    
    ```
    ---import type { Blogpost } from "flotiq-api-ts";import { flotiq } from "../../lib/flotiq";
    export async function getStaticPaths() {  const posts = await flotiq.BlogpostAPI.list();  return posts.data?.map((post) => ({    params: { slug: post.slug },    props: post  })) || []}---
    ```
    
2.  Add the templating to display an individual post:
    
    ```
    ---import type { Blogpost } from "flotiq-api-ts";import { flotiq } from "../../lib/flotiq";
    export async function getStaticPaths() {  const posts = await flotiq.BlogpostAPI.list();  return posts.data?.map((post) => ({    params: { slug: post.slug },    props: post  })) || []}const post: Blogpost = Astro.props;---<html lang="en">  <title>{post.title}</title>  <body>    <h1>{post.title}</h1>    <div set:html={post.content}/>  </body></html>
    ```
    
3.  Visit `http://localhost:4321` and click on a linked blog post in your list. You will now be able to navigate to the individual post’s page.
    

#### On-demand Rendering

[Section titled “On-demand Rendering”](#on-demand-rendering)

If you are using [SSR](/en/guides/on-demand-rendering/) mode, you will need to fetch a single post based on its `slug`.

1.  Create a new file `[slug].astro` in the `/src/pages/posts/` directory. Fetch the post by its `slug` field, including logic to display a 404 page when the route is not found:
    
    ```
    ---import type { Blogpost } from "flotiq-api-ts";import { flotiq } from "../../lib/flotiq";
    const { slug } = Astro.params;let post: Blogpost;
    const blogpostList = await flotiq.BlogpostAPI.list({  filters: JSON.stringify({    slug: {      type: 'equals',      filter: slug,    }  }),  limit: 1});
    if (blogpostList.data?.[0]) {  post = blogpostList.data[0]} else {  return Astro.redirect('/404');}---
    ```
    
2.  Add the templating to display an individual post:
    
    ```
    ---import type { Blogpost } from "flotiq-api-ts";import { flotiq } from "../../lib/flotiq";
    const { slug } = Astro.params;let post: Blogpost;
    const blogpostList = await flotiq.BlogpostAPI.list({  filters: JSON.stringify({    slug: {      type: 'equals',      filter: slug,    }  }),  limit: 1});
    if (blogpostList.data?.[0]) {  post = blogpostList.data[0]} else {  return Astro.redirect('/404');}---<html lang="en">  <title>{post.title}</title>  <body>    <h1>{post.title}</h1>    <div set:html={post.content}/>  </body></html>
    ```
    
3.  Visit `http://localhost:4321` and click on a linked blog post in your list. You will now be able to navigate to the individual post’s page.
    

### Refreshing the SDK After Content Type Changes

[Section titled “Refreshing the SDK After Content Type Changes”](#refreshing-the-sdk-after-content-type-changes)

When using the Flotiq TypeScript SDK (`flotiq-api-ts`), all your data types are accurately mapped into the Astro project.

If you make changes to the structure of your content types (such as adding a new field or modifying an existing one), you’ll need to refresh the SDK to ensure that your project reflects the latest model updates.

To do this, run the rebuild command for your package manager:

*   [npm](#tab-panel-1488)
*   [pnpm](#tab-panel-1489)
*   [Yarn](#tab-panel-1490)

```
npm rebuild flotiq-api-ts
```

This will update the SDK, aligning object types, fields, and API methods with your current data model.

## Publishing Your Site

[Section titled “Publishing Your Site”](#publishing-your-site)

To deploy your website, visit Astro’s [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

### Redeploy on Flotiq Changes

[Section titled “Redeploy on Flotiq Changes”](#redeploy-on-flotiq-changes)

To update your published site, configure Flotiq to send a webhook your hosting provider to trigger a rebuild whenever your content changes.

In Flotiq, you can define which Content Type and events it should trigger on, and configure it accordingly. See the [Flotiq Webhooks documentation](https://flotiq.com/docs/panel/webhooks/async-co-webhook/?utm_campaign=flotiq_at_astro_headless_cms&utm_medium=referral&utm_source=astro) for more details.

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Flotiq documentation](https://flotiq.com/docs/?utm_campaign=flotiq_at_astro_headless_cms&utm_medium=referral&utm_source=astro)

## Community resources

[Section titled “Community resources”](#community-resources)

*   [Flotiq x Astro](https://maciekpalmowski.dev/blog/flotiq-cms-astro/) by Maciek Palmowski

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
