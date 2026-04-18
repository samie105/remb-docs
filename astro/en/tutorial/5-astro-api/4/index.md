---
title: "Add an RSS feed"
source: "https://docs.astro.build/en/tutorial/5-astro-api/4/"
canonical_url: "https://docs.astro.build/en/tutorial/5-astro-api/4/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:56.098Z"
content_hash: "3b44a411ad16e3243eda801569ea2e46ea35f026c9a6bfc836c8914b749dcf30"
menu_path: ["Add an RSS feed"]
section_path: []
---
# Add an RSS feed

Get ready to…

*   Install an Astro package for creating an RSS feed for your website
*   Create a feed that can be subscribed to and read by RSS feed readers

## Install Astro’s RSS package

[Section titled “Install Astro’s RSS package”](#install-astros-rss-package)

Astro provides a custom package to quickly add an RSS feed to your website.

This official package generates a non-HTML document with information about all of your blog posts that can be read by **feed readers** like Feedly, The Old Reader, and more. This document is updated every time your site is rebuilt.

Individuals can subscribe to your feed in a feed reader, and receive a notification when you publish a new blog post on your site, making it a popular blog feature.

1.  In your terminal, quit the Astro development server (Ctrl + C) and run the following command to install Astro’s RSS package.
    
    *   [npm](#tab-panel-2070)
    *   [pnpm](#tab-panel-2071)
    *   [Yarn](#tab-panel-2072)
    
    ```
    npm install @astrojs/rss
    ```
    
2.  Restart the dev server to begin working on your Astro project again.
    
    *   [npm](#tab-panel-2073)
    *   [pnpm](#tab-panel-2074)
    *   [Yarn](#tab-panel-2075)
    
    ```
    npm run dev
    ```
    

## Create an `.xml` feed document

[Section titled “Create an .xml feed document”](#create-an-xml-feed-document)

1.  Create a new file in `src/pages/` called `rss.xml.js`
    
2.  Copy the following code into this new document. Customize the `title` and `description` properties, and if necessary, specify a different language in `customData`:
    
    ```
    import rss, { pagesGlobToRssItems } from '@astrojs/rss';
    export async function GET(context) {  return rss({    title: 'Astro Learner | Blog',    description: 'My journey learning Astro',    site: context.site,    items: await pagesGlobToRssItems(import.meta.glob('./**/*.md')),    customData: `<language>en-us</language>`,  });}
    ```
    
3.  Add the `site` property to the Astro config with your site’s own unique Netlify URL.
    
    ```
    import { defineConfig } from "astro/config";
    export default defineConfig({  site: "https://example.com"});
    ```
    
4.  Visit `http://localhost:4321/rss.xml` and verify that you can see (unformatted) text on the page with an `item` for each of your `.md` files. Each item should contain blog post information such as `title`, `url`, and `description`.
    

## Checklist

[Section titled “Checklist”](#checklist)

 *    I can install an Astro package using the command line.
*    I can create an RSS feed for my website.

### Resources

[Section titled “Resources”](#resources)

*   [RSS item generation in Astro](/en/recipes/rss/#using-glob-imports)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
