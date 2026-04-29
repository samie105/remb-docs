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
nav_prev: {"path": "astro/en/guides/cms/flotiq/index.md", "title": "Flotiq & Astro"}
nav_next: {"path": "astro/en/guides/cms/ghost/index.md", "title": "Ghost & Astro"}
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
    
    ### [Front Matter CMS](index.md)
    
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
