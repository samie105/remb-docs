---
title: "Front Matter CMS & Astro"
source: "https://docs.astro.build/en/guides/cms/frontmatter-cms/"
canonical_url: "https://docs.astro.build/en/guides/cms/frontmatter-cms/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:12.611Z"
content_hash: "4c54b24629551b4a2157bbc3f60dd90a7ee67670d37ed1e59a9a314a25bd7ca2"
menu_path: ["Front Matter CMS & Astro"]
section_path: []
nav_prev: {"path": "../flotiq/index.md", "title": "Flotiq & Astro"}
nav_next: {"path": "../ghost/index.md", "title": "Ghost & Astro"}
---

# Front Matter CMS & Astro

[Front Matter CMS](https://frontmatter.codes/) brings the CMS to your editor, allowing you to create and preview content in real-time in Visual Studio Code.

## Integration with Astro

[Section titled “Integration with Astro”](#integration-with-astro)

In this section, we’ll walk through how to add Front Matter CMS to your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

*   Visual Studio Code
*   Use the [Astro Blog template](https://github.com/withastro/astro/tree/main/examples/blog) to provide the base configuration and sample content to start with Front Matter CMS.

### Install the Front Matter CMS extension

[Section titled “Install the Front Matter CMS extension”](#install-the-front-matter-cms-extension)

You can get the extension from the [Visual Studio Code Marketplace - Front Matter](https://marketplace.visualstudio.com/items?itemName=eliostruyf.vscode-front-matter) or by clicking on the following link: [open Front Matter CMS extension in VS Code](vscode:extension/eliostruyf.vscode-front-matter)

### Project initialization

[Section titled “Project initialization”](#project-initialization)

Once Front Matter CMS is installed, you will get a new icon in the Activity Bar. It will open the **Front Matter CMS** panel in the primary sidebar when you click on it. Follow the next steps to initialize your project:

*   Click on the **Initialize project** button in the Front Matter panel
    
*   The welcome screen will open, and you can start initializing the project
    
*   Click on the first step to **Initialize project**
    
*   As Astro is one of the supported frameworks, you can select it from the list
    
*   Register your content folders, in this case, the `src/content/blog` folder.
    
*   You will be asked to enter the name of the folder. By default, it takes the folder name.
    
*   Click on **Show the dashboard** to open the content dashboard
    

### Project configuration

[Section titled “Project configuration”](#project-configuration)

Once the project is initialized, you will get a `frontmatter.json` configuration file and a `.frontmatter` folder in the root of your project.

*   Directory.frontmatter/
    
    *   Directorydatabase/
        
        *   mediaDb.json
        
    
*   Directorysrc/
    
    *   …
    
*   astro.config.mjs
*   **frontmatter.json**
*   package.json

#### Content-type configuration

[Section titled “Content-type configuration”](#content-type-configuration)

Content-types are the way Front Matter CMS manages your content. Each content-type contains a set of fields, which can be defined per type of content you want to use for your website.

The fields correspond to the front matter of your page content.

You can configure the content-types in the `frontmatter.json` file.

*   Open the `frontmatter.json` file
*   Replace the `frontMatter.taxonomy.contentTypes` array with the following content-types configuration:

```
"frontMatter.taxonomy.contentTypes": [  {    "name": "default",    "pageBundle": false,    "previewPath": "'blog'",    "filePrefix": null,    "fields": [      {        "title": "Title",        "name": "title",        "type": "string",        "single": true      },      {        "title": "Description",        "name": "description",        "type": "string"      },      {        "title": "Publishing date",        "name": "pubDate",        "type": "datetime",        "default": "{{now}}",        "isPublishDate": true      },      {        "title": "Content preview",        "name": "heroImage",        "type": "image",        "isPreviewImage": true      }    ]  }]
```

### Preview your articles in the editor

[Section titled “Preview your articles in the editor”](#preview-your-articles-in-the-editor)

From the **Front Matter CMS** panel, click on the **Start server** button. This action starts the Astro local dev server. Once running, you can open the content dashboard, select one of the articles and click on the **Open preview** button to open the article in the editor.

### Create new articles

[Section titled “Create new articles”](#create-new-articles)

Open the **Front Matter CMS Dashboard**; you can do this as follows:

*   Open the Front Matter CMS’ content dashboard
*   Click on the **Create content** button
*   Front Matter will ask you for the title of the article. Fill it in and press enter
*   Your new article will be created and opened in the editor. You can start writing your article.

### Using Markdoc with Front Matter CMS

[Section titled “Using Markdoc with Front Matter CMS”](#using-markdoc-with-front-matter-cms)

To use Markdoc with Front Matter CMS, you must configure this in the `frontMatter.content.supportedFileTypes`. This setting lets the CMS know which types of files it can progress.

You can configure the setting as follows:

```
"frontMatter.content.supportedFileTypes": [ "md", "markdown", "mdx", "mdoc" ]
```

To allow your content to be created as Markdoc, specify the `fileType` property on the content-type.

```
"frontMatter.taxonomy.contentTypes": [  {    "name": "default",    "pageBundle": false,    "previewPath": "'blog'",    "filePrefix": null,    "fileType": "mdoc",    "fields": [      {        "title": "Title",        "name": "title",        "type": "string",        "single": true      },      {        "title": "Description",        "name": "description",        "type": "string"      },      {        "title": "Publishing date",        "name": "pubDate",        "type": "datetime",        "default": "{{now}}",        "isPublishDate": true      },      {        "title": "Content preview",        "name": "heroImage",        "type": "image",        "isPreviewImage": true      }    ]  }]
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Front Matter CMS](https://frontmatter.codes/)
*   [Front Matter CMS - Documentation](https://frontmatter.codes/docs/)
*   [Getting started with Astro and Front Matter CMS](https://youtu.be/xb6pZiier_E)

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
