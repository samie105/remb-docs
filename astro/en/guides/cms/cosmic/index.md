---
title: "Cosmic & Astro"
source: "https://docs.astro.build/en/guides/cms/cosmic/"
canonical_url: "https://docs.astro.build/en/guides/cms/cosmic/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:36.778Z"
content_hash: "0e4b711d89761d177a52f4046d1706eeb13a6eba28982d05669405e6f8cc1c79"
menu_path: ["Cosmic & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/contentful/index.md", "title": "Contentful & Astro"}
nav_next: {"path": "astro/en/guides/cms/craft-cms/index.md", "title": "Craft CMS & Astro"}
---

# Cosmic & Astro

[Cosmic](https://www.cosmicjs.com/) is a [headless CMS](https://www.cosmicjs.com/headless-cms) that provides an admin dashboard to manage content and an API that can integrate with a diverse range of frontend tools.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

1.  **An Astro project**\- If you’d like to start with a fresh Astro project, read the [installation guide](/en/install-and-setup/). This guide follows a simplified version of the [Astro Headless CMS Theme](https://astro.build/themes/details/cosmic-cms-blog/) with [Tailwind CSS](https://tailwindcss.com/) for styling.
2.  **A Cosmic account and Bucket** - [Create a free Cosmic account](https://app.cosmicjs.com/signup) if you don’t have one. After creating your account, you’ll be prompted to create a new empty project. There’s also a [Simple Astro Blog template](https://www.cosmicjs.com/marketplace/templates/simple-astro-blog) available (this is the same template as the Astro Headless CMS Theme) to automatically import all of the content used in this guide.
3.  **Your Cosmic API keys** - From your Cosmic dashboard, you will need to locate both the **Bucket slug** and **Bucket read key** in order to connect to Cosmic.

## Integrating Cosmic with Astro

[Section titled “Integrating Cosmic with Astro”](#integrating-cosmic-with-astro)

### Installing Necessary Dependencies

[Section titled “Installing Necessary Dependencies”](#installing-necessary-dependencies)

Add the [Cosmic JavaScript SDK](https://www.npmjs.com/package/@cosmicjs/sdk) to fetch data from your Cosmic Bucket.

*   [npm](#tab-panel-1476)
*   [pnpm](#tab-panel-1477)
*   [Yarn](#tab-panel-1478)

```
npm install @cosmicjs/sdk
```

### Configuring API Keys

[Section titled “Configuring API Keys”](#configuring-api-keys)

Create a `.env` file at the root of your Astro project (if it does not already exist). Add both the **Bucket slug** and **Bucket read key** available from your Cosmic dashboard as public environment variables.

```
PUBLIC_COSMIC_BUCKET_SLUG=YOUR_BUCKET_SLUGPUBLIC_COSMIC_READ_KEY=YOUR_READ_KEY
```

## Fetching Data from Cosmic

[Section titled “Fetching Data from Cosmic”](#fetching-data-from-cosmic)

1.  Create a new file called `cosmic.js`. Place this file inside of the `src/lib` folder in your project.
    
2.  Add the following code to fetch data from Cosmic using the SDK and your environment variables.
    
    The example below creates a function called `getAllPosts()` to fetch metadata from Cosmic `posts` objects:
    
    ```
    import { createBucketClient } from '@cosmicjs/sdk'
    const cosmic = createBucketClient({  bucketSlug: import.meta.env.PUBLIC_COSMIC_BUCKET_SLUG,  readKey: import.meta.env.PUBLIC_COSMIC_READ_KEY})
    export async function getAllPosts() {  const data = await cosmic.objects    .find({      type: 'posts'    })    .props('title,slug,metadata,created_at')  return data.objects}
    ```
    
    Read more about [queries in the Cosmic documentation](https://www.cosmicjs.com/docs/api/queries).
    
3.  Import your query function in a `.astro` component. After fetching data, the results from the query can be used in your Astro template.
    
    The following example shows fetching metadata from Cosmic `posts` and passing these values as props to a `<Card />` component to create a list of blog posts:
    
    ```
    ---import Card from '../components/Card.astro'import { getAllPosts } from '../lib/cosmic'
    const data = await getAllPosts()---
    <section>  <ul class="grid gap-8 md:grid-cols-2">    {      data.map((post) => (        <Card          title={post.title}          href={post.slug}          body={post.metadata.excerpt}          tags={post.metadata.tags.map((tag) => tag)}        />      ))    }  </ul></section>
    ```
    
    [View source code for the Card component](https://github.com/cosmicjs/simple-astro-blog/blob/main/src/components/Card.astro)
    

## Building a Blog with Astro and Cosmic

[Section titled “Building a Blog with Astro and Cosmic”](#building-a-blog-with-astro-and-cosmic)

You can manage your Astro blog’s content using Cosmic and create webhooks to automatically redeploy your website when you update or add new content.

### Cosmic Content Objects

[Section titled “Cosmic Content Objects”](#cosmic-content-objects)

The following instructions assume that you have an **Object Type** in Cosmic called **posts**. Each individual blog post is a `post` that is defined in the Cosmic dashboard with the following Metafields:

1.  **Text input** - Author
2.  **Image** - Cover Image
3.  **Repeater** - Tags
    *   **Text input** - Title
4.  **Text area** - Excerpt
5.  **Rich Text** - Content

### Displaying a List of Blog Posts in Astro

[Section titled “Displaying a List of Blog Posts in Astro”](#displaying-a-list-of-blog-posts-in-astro)

Using the same [data-fetching method](#fetching-data-from-cosmic) as above, import the `getAllPosts()` query from your script file and await the data. This function provides metadata about each `post` which can be displayed dynamically.

The example below passes these values to a `<Card />` component to display a formatted list of blog posts:

```
---import Card from '../components/Card.astro'import { getAllPosts } from '../lib/cosmic'
const data = await getAllPosts()---
<section>  <ul class="grid gap-8 md:grid-cols-2">    {      data.map((post) => (        <Card          title={post.title}          href={post.slug}          body={post.metadata.excerpt}          tags={post.metadata.tags.map((tag) => tag)}        />      ))    }  </ul></section>
```

### Generating Individual Blog Posts with Astro

[Section titled “Generating Individual Blog Posts with Astro”](#generating-individual-blog-posts-with-astro)

To generate an individual page with full content for each blog post, create a [dynamic routing page](/en/guides/routing/#dynamic-routes) at `src/pages/blog/[slug].astro`.

This page will export a `getStaticPaths()` function to generate a page route at the `slug` returned from each `post` object. This function is called at build time and generates and renders all of your blog posts at once.

To access your data from Cosmic:

*   Query Cosmic inside of `getStaticPaths()` to fetch data about each post and provide it to the function.
*   Use each `post.slug` as a route parameter, creating the URLs for each blog post.
*   Return each `post` inside of `Astro.props`, making the post data available to HTML template portion of the page component for rendering.

The HTML markup below uses various data from Cosmic, such as the post title, cover image, and the **rich text content** (full blog post content). Use [set:html](/en/reference/directives-reference/#sethtml) on the element displaying the rich text content from Cosmic to render HTML elements on the page exactly as fetched from Cosmic.

```
---import { getAllPosts } from '../../lib/cosmic'import { Image } from 'astro:assets'
export async function getStaticPaths() {  const data = (await getAllPosts()) || []
  return data.map((post) => {    return {      params: { slug: post.slug },      props: { post }    }  })}
const { post } = Astro.props---
<article class="mx-auto max-w-screen-md pt-20">  <section class="border-b pb-8">    <h1 class="text-4xl font-bold">{post.title}</h1>    <div class="my-4"></div>    <span class="text-sm font-semibold">{post.metadata.author?.title}</span>  </section>  {    post.metadata.cover_image && (      <Image        src={post.metadata.cover_image.imgix_url}        format="webp"        width={1200}        height={675}        aspectRatio={16 / 9}        quality={50}        alt={`Cover image for the blog ${post.title}`}        class={'my-12 rounded-md shadow-lg'}      />    )  }  <div set:html={post.metadata.content} /></article>
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit the [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on Cosmic content updates

[Section titled “Rebuild on Cosmic content updates”](#rebuild-on-cosmic-content-updates)

You can set up a webhook in Cosmic directly to trigger a redeploy of your site on your hosting platform (e.g. Vercel) whenever you update or add content Objects.

Under “Settings” > “webhooks”, add the URL endpoint from Vercel and select the Object Type you would like to trigger the webhook. Click “Add webhook” to save it.

##### Netlify

[Section titled “Netlify”](#netlify)

To set up a webhook in Netlify:

1.  Go to your site dashboard and click on **Build & deploy**.
    
2.  Under the **Continuous Deployment** tab, find the **Build hooks** section and click on **Add build hook**.
    
3.  Provide a name for your webhook and select the branch you want to trigger the build on. Click on **Save** and copy the generated URL.
    

##### Vercel

[Section titled “Vercel”](#vercel)

To set up a webhook in Vercel:

1.  Go to your project dashboard and click on **Settings**.
    
2.  Under the **Git** tab, find the **Deploy Hooks** section.
    
3.  Provide a name for your webhook and the branch you want to trigger the build on. Click **Add** and copy the generated URL.
    

## Themes

[Section titled “Themes”](#themes)

*    [![](/_astro/simple-astro-blog.Dl86rePH_ZxKENW.webp) Astro Headless CMS Blog](https://astro.build/themes/details/cosmic-cms-blog/)

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


