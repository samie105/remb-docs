---
title: "Deploy your Astro Site"
source: "https://docs.astro.build/en/guides/deploy/"
canonical_url: "https://docs.astro.build/en/guides/deploy/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:14.360Z"
content_hash: "3daf0a0a09bf750d0d9cf5a7ae594820ffcf5eab4ebc2838780fde33ff40bf35"
menu_path: ["Deploy your Astro Site"]
section_path: []
nav_prev: {"path": "astro/en/guides/integrations-guide/sitemap/index.md", "title": "@astrojs/\n\t\t\t\t\tsitemap"}
nav_next: {"path": "astro/en/guides/deploy/aws/index.md", "title": "Deploy your Astro Site to AWS"}
---

# Deploy your Astro Site

**Ready to build and deploy your Astro site?** Follow one of our guides to different deployment services or scroll down for general guidance about deploying an Astro site.

## Deployment Guides

[Section titled “Deployment Guides”](#deployment-guides)

*   ![](/logos/aws.svg)
    
    ### [AWS](aws/index.md)
    
    On demandStatic
    
*   ![](/logos/flightcontrol.svg)
    
    ### [AWS via Flightcontrol](aws-via-flightcontrol/index.md)
    
    On demandStatic
    
*   ![](/logos/sst.svg)
    
    ### [AWS via SST](aws-via-sst/index.md)
    
    On demandStatic
    
*   ![](/logos/azion.svg)
    
    ### [Azion](azion/index.md)
    
    On demandStatic
    
*   ![](/logos/buddy.svg)
    
    ### [Buddy](buddy/index.md)
    
    Static
    
*   ![](/logos/cleavr.svg)
    
    ### [Cleavr](cleavr/index.md)
    
    On demandStatic
    
*   ![](/logos/clever-cloud.svg)
    
    ### [Clever Cloud](clever-cloud/index.md)
    
    StaticOn demand
    
*   ![](/logos/cloudflare-pages.svg)
    
    ### [Cloudflare](cloudflare/index.md)
    
    On demandStatic
    
*   ![](/logos/cloudray.svg)
    
    ### [CloudRay](cloudray/index.md)
    
    Static
    
*   ![](/logos/deno.svg)
    
    ### [Deno Deploy](deno/index.md)
    
    On demandStatic
    
*   ![](/logos/deployhq.svg)
    
    ### [DeployHQ](deployhq/index.md)
    
    Static
    
*   ![](/logos/edgeone-pages.svg)
    
    ### [EdgeOne Pages](edgeone-pages/index.md)
    
    On demandStatic
    
*   ![](/logos/firebase.svg)
    
    ### [Firebase](firebase/index.md)
    
    On demandStatic
    
*   ![](/logos/fleek.svg)
    
    ### [Fleek](fleek/index.md)
    
    Static
    
*   ![](/logos/flyio.svg)
    
    ### [Fly.io](flyio/index.md)
    
    On demandStatic
    
*   ![](/logos/github.svg)
    
    ### [GitHub Pages](github/index.md)
    
    Static
    
*   ![](/logos/gitlab.svg)
    
    ### [GitLab Pages](gitlab/index.md)
    
    Static
    
*   ![](/logos/google-cloud.svg)
    
    ### [Google Cloud](google-cloud/index.md)
    
    On demandStatic
    
*   ![](/logos/heroku.svg)
    
    ### [Heroku](heroku/index.md)
    
    Static
    
*   ![](/logos/juno.svg)
    
    ### [Juno](juno/index.md)
    
    Static
    
*   ![](/logos/microsoft-azure.svg)
    
    ### [Microsoft Azure](microsoft-azure/index.md)
    
    Static
    
*   ![](/logos/netlify.svg)
    
    ### [Netlify](netlify/index.md)
    
    On demandStatic
    
*   ![](/logos/railway.svg)
    
    ### [Railway](railway/index.md)
    
    On demandStatic
    
*   ![](/logos/render.svg)
    
    ### [Render](render/index.md)
    
    Static
    
*   ![](/logos/seenode.svg)
    
    ### [Seenode](seenode/index.md)
    
    On demand
    
*   ![](/logos/sevalla.svg)
    
    ### [Sevalla](sevalla/index.md)
    
    On demandStatic
    
*   ![](/logos/stormkit.svg)
    
    ### [Stormkit](stormkit/index.md)
    
    Static
    
*   ![](/logos/surge.svg)
    
    ### [Surge](surge/index.md)
    
    Static
    
*   ![](/logos/vercel.svg)
    
    ### [Vercel](vercel/index.md)
    
    On demandStatic
    
*   ![](/logos/zeabur.svg)
    
    ### [Zeabur](zeabur/index.md)
    
    On demandStatic
    
*   ![](/logos/zephyr.svg)
    
    ### [Zephyr Cloud](zephyr/index.md)
    
    Static
    
*   ![](/logos/zerops.svg)
    
    ### [Zerops](zerops/index.md)
    
    On demandStatic
    

## Quick Deploy Options

[Section titled “Quick Deploy Options”](#quick-deploy-options)

You can build and deploy an Astro site to a number of hosts quickly using either their website’s dashboard UI or a CLI.

### Website UI

[Section titled “Website UI”](#website-ui)

A quick way to deploy your website is to connect your Astro project’s online Git repository (e.g. GitHub, GitLab, Bitbucket) to a host provider and take advantage of continuous deployment using Git.

These host platforms automatically detect pushes to your Astro project’s source repository, build your site and deploy it to the web at a custom URL or your personal domain. Often, setting up a deployment on these platforms will follow steps something like the following:

1.  Add your repository to an online Git provider (e.g. in GitHub, GitLab, Bitbucket)
    
2.  Choose a host that supports **continuous deployment** (e.g. [Netlify](netlify/index.md) or [Vercel](vercel/index.md)) and import your Git repository as a new site/project.
    
    Many common hosts will recognize your project as an Astro site, and should choose the appropriate configuration settings to build and deploy your site as shown below. (If not, these settings can be changed.)
    
3.  Click “Deploy” and your new website will be created at a unique URL for that host (e.g. `new-astro-site.netlify.app`).
    

The host will be automatically configured to watch your Git provider’s main branch for changes, and to rebuild and republish your site at each new commit. These settings can typically be configured in your host provider’s dashboard UI.

### CLI Deployment

[Section titled “CLI Deployment”](#cli-deployment)

Some hosts will have their own command line interface (CLI) you can install globally to your machine using npm. Often, using a CLI to deploy looks something like the following:

1.  Install your host’s CLI globally, for example:
    
    *   [npm](#tab-panel-1524)
    *   [pnpm](#tab-panel-1525)
    *   [Yarn](#tab-panel-1526)
    
    ```
    npm install --global netlify-cli
    ```
    
2.  Run the CLI and follow any instructions for authorization, setup etc.
    
3.  Build your site and deploy to your host
    
    Many common hosts will build and deploy your site for you. They will usually recognize your project as an Astro site, and should choose the appropriate configuration settings to build and deploy as shown below. (If not, these settings can be changed.)
    
    Other hosts will require you to [build your site locally](#building-your-site-locally) and deploy using the command line.
    

## Building Your Site Locally

[Section titled “Building Your Site Locally”](#building-your-site-locally)

Many hosts like Netlify and Vercel will build your site for you and then publish that build output to the web. But, some sites will require you to build locally and then run a deploy command or upload your build output.

You may also wish to build locally to preview your site, or to catch any potential errors and warnings in your own environment.

Run the command `npm run build` to build your Astro site.

*   [npm](#tab-panel-1527)
*   [pnpm](#tab-panel-1528)
*   [Yarn](#tab-panel-1529)

```
npm run build
```

By default, the build output will be placed at `dist/`. This location can be changed using the [`outDir` configuration option](../../reference/configuration-reference/index.md#outdir).

## Adding an Adapter for on-demand rendering

[Section titled “Adding an Adapter for on-demand rendering”](#adding-an-adapter-for-on-demand-rendering)

[Contribute](../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
