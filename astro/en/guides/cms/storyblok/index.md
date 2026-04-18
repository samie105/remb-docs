---
title: "Storyblok & Astro"
source: "https://docs.astro.build/en/guides/cms/storyblok/"
canonical_url: "https://docs.astro.build/en/guides/cms/storyblok/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:35.060Z"
content_hash: "874360dfbc5d0539aaf7b8031769c78e9bd39af1d956458051fd69a7847421ad"
menu_path: ["Storyblok & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/cms/statamic/index.md", "title": "Headless Statamic & Astro"}
nav_next: {"path": "astro/en/guides/cms/strapi/index.md", "title": "Strapi & Astro"}
---

# Storyblok & Astro

[Storyblok](https://www.storyblok.com/) is a component-based headless CMS that allows you to manage your content using reusable components called Bloks.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, you will use the [Storyblok integration](https://github.com/storyblok/monoblok/tree/main/packages/astro) to connect Storyblok to Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1.  **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.
    
2.  **A Storyblok account and space** - If you don’t have an account yet, [sign up for free](https://app.storyblok.com/#/signup) and create a new space.
    
3.  **Storyblok Preview token** - This token will be used to fetch drafts and published versions of your content. You can find and generate your API token in the Access Tokens tab of your Storyblok space settings.
    

### Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add your Storyblok credentials to Astro, create a `.env` file in the root of your project with the following variable:

```
STORYBLOK_TOKEN=YOUR_PREVIEW_TOKEN
```

Now, you should be able to use these environment variables in your project.

Your root directory should now include this new file:

*   Directorysrc/
    
    *   …
    
*   **.env**
*   astro.config.mjs
*   package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect Astro with your Storyblok space, install the official [Storyblok integration](https://github.com/storyblok/monoblok/tree/main/packages/astro) using the command below for your preferred package manager:

*   [npm](#tab-panel-1515)
*   [pnpm](#tab-panel-1516)
*   [Yarn](#tab-panel-1517)

```
npm install @storyblok/astro vite
```

### Configuring Storyblok

[Section titled “Configuring Storyblok”](#configuring-storyblok)

Modify your Astro config file to include the Storyblok integration:

```
import { defineConfig } from 'astro/config';import { storyblok } from '@storyblok/astro';import { loadEnv } from 'vite';
const env = loadEnv("", process.cwd(), 'STORYBLOK');
export default defineConfig({  integrations: [    storyblok({      accessToken: env.STORYBLOK_TOKEN,      components: {        // Add your components here      },      apiOptions: {        // Choose your Storyblok space region        region: 'us', // optional,  or 'eu' (default)      },    })  ],});
```

The Storyblok integration requires an object with the following properties:

1.  `accessToken` - This references the Storyblok API token that you added in the previous step.
    
2.  `components` - An object that maps Storyblok component names to paths to your local components. This is required to render your Storyblok Bloks in Astro.
    
3.  `apiOptions` - An object containing [Storyblok API options](https://www.storyblok.com/docs/packages/storyblok-astro#api).
    

### Connecting Bloks to Astro components

[Section titled “Connecting Bloks to Astro components”](#connecting-bloks-to-astro-components)

To connect your Bloks to Astro, create a new folder named `storyblok` in the `src` directory. This folder will contain all the Astro components that will match your Bloks in your Storyblok Blok library.

In this example, you have a `blogPost` Blok content type in your Storyblok library with the following fields:

*   `title` - A text field
*   `description` - A text field
*   `content` - A rich text field

Our goal is to create the equivalent Astro component that will use these fields to render its content. To do this, create a new file named `BlogPost.astro` inside `src/storyblok` with the following content:

```
---import { storyblokEditable, renderRichText } from '@storyblok/astro'
const { blok } = Astro.propsconst content = renderRichText(blok.content)---
<article {...storyblokEditable(blok)}>  <h1>{blok.title}</h1>  <p>{blok.description}</p>  <Fragment set:html={content} /></article>
```

The `blok` property contains the data that you will receive from Storyblok. It also contains the fields that were defined in the `blogPost` content type Blok in Storyblok.

To render our content, the integration provides utility functions such as:

*   `storyblokEditable` - it adds the necessary attributes to the elements so that you can edit them in Storyblok.
*   `renderRichText` - it transforms the rich text field into HTML.

Your root directory should include this new file:

*   Directorysrc/
    
    *   Directorystoryblok/
        
        *   **BlogPost.astro**
        
    
*   .env
*   astro.config.mjs
*   package.json

Finally, to connect the `blogPost` Blok to the `BlogPost` component, add a new property to your components object in your Astro config file.

*   The key is the name of the Blok in Storyblok. In this case, it is `blogPost`.
*   The value is the path to the component. In this case, it is `storyblok/BlogPost`.

```
import { defineConfig } from 'astro/config';import { storyblok } from '@storyblok/astro';import { loadEnv } from 'vite';
const env = loadEnv("", process.cwd(), 'STORYBLOK');
export default defineConfig({  integrations: [    storyblok({      accessToken: env.STORYBLOK_TOKEN,      components: {        blogPost: 'storyblok/BlogPost',      },      apiOptions: {        region: 'us',      },    })  ],});
```

### Fetching data

[Section titled “Fetching data”](#fetching-data)

To test the setup, in Storyblok create a new story with the `blogPost` content type named `test-post`. In Astro, create a new page in the `src/pages/` directory named `test-post.astro` with the following content:

```
---import { useStoryblokApi } from '@storyblok/astro'import StoryblokComponent from '@storyblok/astro/StoryblokComponent.astro'
const storyblokApi = useStoryblokApi()
const { data } = await storyblokApi.get("cdn/stories/test-post", {  version: import.meta.env.DEV ? "draft" : "published",});
const content = data.story.content;---<StoryblokComponent blok={content} />
```

To query your data, use the `useStoryblokApi` hook. This will initialize a new client instance using your integration configuration.

To render your content, pass the `content` property of the Story to the `StoryblokComponent` as a `blok` prop. This component will render the Bloks that are defined inside the `content` property. In this case, it will render the `BlogPost` component.

## Making a blog with Astro and Storyblok

[Section titled “Making a blog with Astro and Storyblok”](#making-a-blog-with-astro-and-storyblok)

With the integration set up, you can now create a blog with Astro and Storyblok.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1.  **A Storyblok space** - For this tutorial, we recommend using a new space. If you already have a space with Bloks, feel free to use them, but you will need to modify the code to match the Blok names and content types.
    
2.  **An Astro project integrated with Storyblok** - See [integrating with Astro](#integrating-with-astro) for instructions on how to set up the integration.
    

### Creating a blok library

[Section titled “Creating a blok library”](#creating-a-blok-library)

To create Bloks, go to the Storyblok app and click on the **Block Library** tab. Click on the \+ New blok button and create the following Bloks:

1.  `blogPost` - A content type Blok with the following fields:
    
    *   `title` - A text field
    *   `description` - A text field
    *   `content` - A rich text field
2.  `blogPostList` - An empty nestable Blok
    
3.  `page` - A content type Blok with the following fields:
    
    *   `body` - A nestable Blok

### Creating content

[Section titled “Creating content”](#creating-content)

To add new content, go to the content section by clicking on the **Content** tab. Using the Blok library that you created in the previous step, create the following stories:

1.  `home` - A content type story with the `page` Blok. Inside the `body` field, add a `blogPostList` Blok.
    
2.  `blog/no-javascript` - A story with the `blogPost` content type inside the blog folder.
    
    ```
    title: No JavaScriptdescription: A sample blog postcontent: Hi there! This blog post doesn't use JavaScript.
    ```
    
3.  `blog/astro-is-amazing` - A story with the `blogPost` content type inside the blog folder.
    
    ```
    title: Astro is amazingdescription: We love Astrocontent: Hi there! This blog post was build with Astro.
    ```
    

Now that you have your content ready, return to your Astro project and start building your blog.

### Connecting Bloks to components

[Section titled “Connecting Bloks to components”](#connecting-bloks-to-components)

To connect your newly created Bloks to Astro components, create a new folder named `storyblok` in your `src` directory and add the following files:

`Page.astro` is a nestable Block content type component that will recursively render all the Bloks inside the `body` property of the `page` Blok. It also adds the `storyblokEditable` attributes to the parent element which will allow us to edit the page in Storyblok.

```
---import { storyblokEditable } from '@storyblok/astro'import StoryblokComponent from "@storyblok/astro/StoryblokComponent.astro";const { blok } = Astro.props---
<main {...storyblokEditable(blok)}>  {    blok.body?.map((blok) => {      return <StoryblokComponent blok={blok} />    })  }</main>
```

`BlogPost.astro` will render the `title`, `description` and `content` properties of the `blogPost` Blok.

To transform the `content` property from a rich text field to HTML, you can use the `renderRichText` helper function.

```
---import { storyblokEditable, renderRichText } from '@storyblok/astro'const { blok } = Astro.propsconst content = renderRichText(blok.content)---<article {...storyblokEditable(blok)}>  <h1>{blok.title}</h1>  <p>{blok.description}</p>  <Fragment set:html={content} /></article>
```

`BlogPostList.astro` is a nestable Blok content type component that will render a list of blog post previews.

It uses the `useStoryblokApi` hook to fetch all the stories with the content type of `blogPost`. It uses the `version` query parameter to fetch the draft versions of the stories when in development mode and the published versions when building for production.

`Astro.props` is used to set up the editor in Storyblok. Additional props can also be passed to your component here, if needed.

```
---import { storyblokEditable } from '@storyblok/astro'import { useStoryblokApi } from '@storyblok/astro'
const storyblokApi = useStoryblokApi();
const { data } = await storyblokApi.get('cdn/stories', {  version: import.meta.env.DEV ? "draft" : "published",  content_type: 'blogPost',})
const posts = data.stories.map(story => {  return {    title: story.content.title,    date: new Date(story.published_at).toLocaleDateString("en-US", {dateStyle: "full"}),    description: story.content.description,    slug: story.full_slug,  }})
const { blok } = Astro.props---
<ul {...storyblokEditable(blok)}>  {posts.map(post => (    <li>      <time>{post.date}</time>      <a href={post.slug}>{post.title}</a>      <p>{post.description}</p>    </li>  ))}</ul>
```

Finally, add your components to the `components` property of the `storyblok` config object in `astro.config.mjs`. The key is the name of the Blok in Storyblok, and the value is the path to the component relative to `src`.

```
import { defineConfig } from 'astro/config';import { storyblok } from '@storyblok/astro';import { loadEnv } from 'vite';
const env = loadEnv("", process.cwd(), 'STORYBLOK');
export default defineConfig({  integrations: [    storyblok({      accessToken: env.STORYBLOK_TOKEN,      components: {        blogPost: 'storyblok/BlogPost',        blogPostList: 'storyblok/BlogPostList',        page: 'storyblok/Page',      },      apiOptions: {        region: 'us',      },    })  ],});
```

### Generating pages

[Section titled “Generating pages”](#generating-pages)

To create a route for a specific `page`, you can fetch its content directly from the Storyblok API and pass it to the `StoryblokComponent` component. Remember to make sure you have added the `Page` component to your astro.config.mjs.

Create an `index.astro` file in `src/pages/` to render the `home` page:

```
---import { useStoryblokApi } from '@storyblok/astro'import StoryblokComponent from '@storyblok/astro/StoryblokComponent.astro'import BaseLayout from '../layouts/BaseLayout.astro'
const storyblokApi = useStoryblokApi();const { data } = await storyblokApi.get('cdn/stories/home', {  version: import.meta.env.DEV ? "draft" : "published",});const content = data.story.content;---<html lang="en">  <head>    <title>Storyblok & Astro</title>  </head>  <body>    <StoryblokComponent blok={content} />  </body></html>
```

To generate pages for all of your blog posts, create a `.astro` page that will create dynamic routes. This approach varies depending on whether your routes are prerendered (the default in Astro) or [rendered on demand](/en/guides/on-demand-rendering/).

#### Static site generation

[Section titled “Static site generation”](#static-site-generation)

If you are using Astro’s default static site generation, you will use [dynamic routes](/en/guides/routing/#dynamic-routes) and the `getStaticPaths` function to generate your project pages.

Create a new directory `src/pages/blog/` and add a new file called `[...slug].astro` with the following code:

```
---import { useStoryblokApi } from '@storyblok/astro'import StoryblokComponent from '@storyblok/astro/StoryblokComponent.astro'
export async function getStaticPaths() {  const sbApi = useStoryblokApi();
  const { data } = await sbApi.get("cdn/stories", {    content_type: "blogPost",    version: import.meta.env.DEV ? "draft" : "published",  });
  const stories = Object.values(data.stories);
  return stories.map((story) => {    return {      params: { slug: story.slug },    };  });}
const sbApi = useStoryblokApi();const { slug } = Astro.params;const { data } = await sbApi.get(`cdn/stories/blog/${slug}`, {  version: import.meta.env.DEV ? "draft" : "published",});
const story = data.story;---
<html lang="en">  <head>    <title>Storyblok & Astro</title>  </head>  <body>    <StoryblokComponent blok={story.content} />  </body></html>
```

This file will generate a page for each story, with the slug and content fetched from the Storyblok API.

#### On-demand rendering

[Section titled “On-demand rendering”](#on-demand-rendering)

If you are [rendering your routes on demand with an adapter](/en/guides/on-demand-rendering/), you will use dynamic routes to fetch the page data from Storyblok.

Create a new directory `src/pages/blog/` and add a new file called `[...slug].astro` with the following code:

```
---import { useStoryblokApi } from '@storyblok/astro'import StoryblokComponent from '@storyblok/astro/StoryblokComponent.astro'const storyblokApi = useStoryblokApi()const slug = Astro.params.slug;let content;try {  const { data } = await storyblokApi.get(`cdn/stories/blog/${slug}`, {    version: import.meta.env.DEV ? "draft" : "published",  });  content = data.story.content} catch (error) {  return Astro.redirect('/404')}---<html lang="en">  <head>    <title>Storyblok & Astro</title>  </head>  <body>    <StoryblokComponent blok={content} />  </body></html>
```

This file will fetch and render the page data from Storyblok that matches the dynamic `slug` parameter.

Since you are using a redirect to `/404`, create a 404 page in `src/pages`:

```
<html lang="en">  <head>    <title>Not found</title>  </head>  <body>    <p>Sorry, this page does not exist.</p>  </body></html>
```

If the story is not found, the request will be redirected to the 404 page.

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on Storyblok changes

[Section titled “Rebuild on Storyblok changes”](#rebuild-on-storyblok-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build from Storyblok events.

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
    

##### Adding a webhook to Storyblok

[Section titled “Adding a webhook to Storyblok”](#adding-a-webhook-to-storyblok)

In your Storyblok space **Settings**, click on the **Webhooks** tab. Paste the webhook URL you copied in the **Story published & unpublished** field and hit Save to create a webhook.

Now, whenever you publish a new story, a new build will be triggered and your blog will be updated.

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Storyblok Astro Integration](https://www.storyblok.com/mp/announcing-storyblok-astro) to add Storyblok to your project.
*   [Storyblok Astro guide](https://www.storyblok.com/docs/guides/astro/)
*   [Storyblok Astro package reference](https://www.storyblok.com/docs/packages/storyblok-astro)

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [Getting the Visual Editor to work for Storyblok + Astro](https://dev.to/sandrarodgers/getting-the-visual-editor-to-work-for-storyblok-astro-2gja) by Sandra Rodgers
*   [Astro + Storyblok: SSR preview for instant visual editing](https://dev.to/jgierer12/astro-storyblok-ssr-preview-for-instant-visual-editing-3g9m) by Jonas Gierer
*   [Astro-Storyblok Previews Site with Netlify’s Branch Deploys Feature](https://dev.to/sandrarodgers/astro-storyblok-previews-site-with-netlifys-branch-deploys-feature-44dh) by Sandra Rodgers

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

