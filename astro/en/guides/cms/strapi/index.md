---
title: "Strapi & Astro"
source: "https://docs.astro.build/en/guides/cms/strapi/"
canonical_url: "https://docs.astro.build/en/guides/cms/strapi/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:41.651Z"
content_hash: "edc77e50fa8e6bf7ef2f4df98f9762e10b6df6b6b51976386843ed4ec89c2311"
menu_path: ["Strapi & Astro"]
section_path: []
nav_prev: {"path": "../storyblok/index.md", "title": "Storyblok & Astro"}
nav_next: {"path": "../studiocms/index.md", "title": "StudioCMS & Astro"}
---

# Strapi & Astro

[Strapi](https://strapi.io/) is an open-source, customizable, headless CMS.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

This guide will build a wrapper function to connect Strapi with Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1.  **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.
2.  **A Strapi CMS server** - You can [set up a Strapi server on a local environment](https://docs.strapi.io/dev-docs/quick-start).

### Adding the Strapi URL in `.env`

[Section titled “Adding the Strapi URL in .env”](#adding-the-strapi-url-in-env)

To add your Strapi URL to Astro, create a `.env` file in the root of your project (if one does not already exist) and add the following variable:

```
STRAPI_URL="http://127.0.0.1:1337" # or use your IP address
```

Restart the dev server to use this environment variable in your Astro project.

If you would like to have IntelliSense for your environment variable, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

```
interface ImportMetaEnv {  readonly STRAPI_URL: string;}
```

Your root directory should now include the new file(s):

*   Directorysrc/
    
    *   **env.d.ts**
    
*   **.env**
*   astro.config.mjs
*   package.json

Learn more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

### Creating the API wrapper

[Section titled “Creating the API wrapper”](#creating-the-api-wrapper)

Create a new file at `src/lib/strapi.ts` and add the following wrapper function to interact with the Strapi API:

```
interface Props {  endpoint: string;  query?: Record<string, string>;  wrappedByKey?: string;  wrappedByList?: boolean;}
/** * Fetches data from the Strapi API * @param endpoint - The endpoint to fetch from * @param query - The query parameters to add to the url * @param wrappedByKey - The key to unwrap the response from * @param wrappedByList - If the response is a list, unwrap it * @returns */export default async function fetchApi<T>({  endpoint,  query,  wrappedByKey,  wrappedByList,}: Props): Promise<T> {  if (endpoint.startsWith('/')) {    endpoint = endpoint.slice(1);  }
  const url = new URL(`${import.meta.env.STRAPI_URL}/api/${endpoint}`);
  if (query) {    Object.entries(query).forEach(([key, value]) => {      url.searchParams.append(key, value);    });  }  const res = await fetch(url.toString());  let data = await res.json();
  if (wrappedByKey) {    data = data[wrappedByKey];  }
  if (wrappedByList) {    data = data[0];  }
  return data as T;}
```

This function requires an object with the following properties:

1.  `endpoint` - The endpoint you are fetching.
2.  `query` - The query parameters to add to the end of URL
3.  `wrappedByKey` - The `data` key in the object that wraps your `Response`.
4.  `wrappedByList` - A parameter to “unwrap” the list returned by Strapi, and return only the first item.

### Optional: Creating the Article interface

[Section titled “Optional: Creating the Article interface”](#optional-creating-the-article-interface)

If you are using TypeScript, create the following Article interface to correspond to the Strapi content types at `src/interfaces/article.ts`:

```
export default interface Article {  documentId: number;  title: string;  description: string;  content: string;  slug: string;  createdAt: string;  updatedAt: string;  publishedAt: string;}
```

*   Directorysrc/
    
    *   Directoryinterfaces/
        
        *   **article.ts**
        
    *   Directorylib/
        
        *   strapi.ts
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

### Displaying a list of articles

[Section titled “Displaying a list of articles”](#displaying-a-list-of-articles)

1.  Update your home page `src/pages/index.astro` to display a list of blog posts, each with a description and a link to its own page.
    
2.  Import the wrapper function and the interface. Add the following API call to fetch your articles and return a list:
    
    ```
    ---import fetchApi from '../lib/strapi';import type Article from '../interfaces/article';
    const articles = await fetchApi<Article[]>({  endpoint: 'articles', // the content type to fetch  wrappedByKey: 'data', // the key to unwrap the response});---
    ```
    
    The API call requests data from `http://localhost:1337/api/articles` and returns `articles`: an array of json objects representing your data:
    
    ```
    [  {    documentId: 1,    title: "What's inside a Black Hole",    description: "Maybe the answer is in this article, or not...",    content: "Well, we don't know yet...",    slug: "what-s-inside-a-black-hole",    createdAt: "2023-05-28T13:19:46.421Z",    updatedAt: "2023-05-28T13:19:46.421Z",    publishedAt: "2023-05-28T13:19:45.826Z"  },  // ...]
    ```
    
3.  Using data from the `articles` array returned by the API, display your Strapi blog posts in a list. These posts will link to their own individual pages, which you will create in the next step.
    
    ```
    ---import fetchApi from '../lib/strapi';import type Article from '../interfaces/article';
    const articles = await fetchApi<Article[]>({  endpoint: 'articles?populate=image',  wrappedByKey: 'data',});---
    <!DOCTYPE html><html lang="en">  <head>    <title>Strapi & Astro</title>  </head>
      <body>    <main>      <ul>        {          articles.map((article) => (            <li>              <a href={`/blog/${article.slug}/`}>                {article.title}              </a>            </li>          ))        }      </ul>    </main>  </body></html>
    ```
    

### Generating article pages

[Section titled “Generating article pages”](#generating-article-pages)

Create the file `src/pages/blog/[slug].astro` to [dynamically generate a page](/en/guides/routing/#dynamic-routes) for each article.

*   Directorysrc/
    
    *   Directoryinterfaces/
        
        *   article.ts
        
    *   Directorylib/
        
        *   strapi.ts
        
    *   Directorypages/
        
        *   index.astro
        *   Directoryblog/
            
            *   **\[slug\].astro**
            
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

#### Static site generation

[Section titled “Static site generation”](#static-site-generation)

In Astro’s default static mode (SSG), use [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths) to fetch your list of articles from Strapi.

```
---import fetchApi from '../../lib/strapi';import type Article from '../../interfaces/article';
export async function getStaticPaths() {  const articles = await fetchApi<Article[]>({    endpoint: 'articles',    wrappedByKey: 'data',  });
  return articles.map((article) => ({    params: { slug: article.slug },    props: article,  }));}type Props = Article;
const article = Astro.props;---
```

Create the template for each page using the properties of each post object.

```
---import fetchApi from '../../lib/strapi';import type Article from '../../interfaces/article';
export async function getStaticPaths() {  const articles = await fetchApi<Article[]>({    endpoint: 'articles',    wrappedByKey: 'data',  });
  return articles.map((article) => ({    params: { slug: article.slug },    props: article,  }));}type Props = Article;
const article = Astro.props;---
<!DOCTYPE html><html lang="en">  <head>    <title>{article.title}</title>  </head>
  <body>    <main>      <img src={import.meta.env.STRAPI_URL + article.image.data.url} />
      <h1>{article.title}</h1>
      <!-- Render plain text -->      <p>{article.content}</p>      <!-- Render markdown -->      <MyMarkdownComponent>        {article.content}      </MyMarkdownComponent>      <!-- Render html -->      <Fragment set:html={article.content} />    </main>  </body></html>
```

#### On-demand rendering

[Section titled “On-demand rendering”](#on-demand-rendering)

If you’ve [opted into on-demand rendering with an adapter](/en/guides/on-demand-rendering/), [generate your dynamic routes](/en/guides/routing/#on-demand-dynamic-routes) using the following code:

Create the `src/pages/blog/[slug].astro` file:

```
---import fetchApi from '../../../lib/strapi';import type Article from '../../../interfaces/article';
const { slug } = Astro.params;
let article: Article;
try {  article = await fetchApi<Article>({    endpoint: 'articles',    wrappedByKey: 'data',    wrappedByList: true,    query: {      'filters[slug][$eq]': slug || '',    },  });} catch (error) {  return Astro.redirect('/404');}---
<!DOCTYPE html><html lang="en">  <head>    <title>{article.title}</title>  </head>
  <body>    <main>      <img src={import.meta.env.STRAPI_URL + article.image.data.url} />
      <h1>{article.title}</h1>
      <!-- Render plain text -->      <p>{article.content}</p>      <!-- Render markdown -->      <MyMarkdownComponent>        {article.content}      </MyMarkdownComponent>      <!-- Render html -->      <Fragment set:html={article.content} />    </main>  </body></html>
```

This file will fetch and render the page data from Strapi that matches the dynamic `slug` parameter.

Since you are using a redirect to `/404`, create a 404 page in `src/pages`:

```
<html lang="en">  <head>    <title>Not found</title>  </head>  <body>    <p>Sorry, this page does not exist.</p>    <img src="https://http.cat/404" />  </body></html>
```

If the article is not found, the user will be redirected to this 404 page and be greeted by a lovely cat.

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on changes

[Section titled “Rebuild on changes”](#rebuild-on-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build from Strapi.

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
    

##### Adding a webhook to Strapi

[Section titled “Adding a webhook to Strapi”](#adding-a-webhook-to-strapi)

Follow [the Strapi webhooks guide](https://strapi.io/blog/webhooks) to create a webhook in your Strapi admin panel.

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Strapi Blog Guide For React](https://strapi.io/blog/build-a-blog-with-next-react-js-strapi) by Strapi

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
