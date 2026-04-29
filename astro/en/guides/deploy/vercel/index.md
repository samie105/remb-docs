---
title: "Deploy your Astro Site to Vercel"
source: "https://docs.astro.build/en/guides/deploy/vercel/"
canonical_url: "https://docs.astro.build/en/guides/deploy/vercel/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:57.053Z"
content_hash: "bdc69abff200524854fd53c8ee64b96ee95073f9ca836102902b7825e7b2d594"
menu_path: ["Deploy your Astro Site to Vercel"]
section_path: []
nav_prev: {"path": "../surge/index.md", "title": "Deploy your Astro Site to Surge"}
nav_next: {"path": "../zeabur/index.md", "title": "Deploy your Astro Site to Zeabur"}
---

# Deploy your Astro Site to Vercel

You can use [Vercel](http://vercel.com/) to deploy an Astro site to their global edge network with zero configuration.

This guide includes instructions for deploying to Vercel through the website UI or Vercel’s CLI.

## Project configuration

[Section titled “Project configuration”](#project-configuration)

Your Astro project can be deployed to Vercel as a static site, or a server-rendered site.

### Static site

[Section titled “Static site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Vercel.

### Adapter for on-demand rendering

[Section titled “Adapter for on-demand rendering”](#adapter-for-on-demand-rendering)

Add [the Vercel adapter](/en/guides/integrations-guide/vercel/) to enable [on-demand rendering](/en/guides/on-demand-rendering/) in your Astro project with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

*   [npm](#tab-panel-1597)
*   [pnpm](#tab-panel-1598)
*   [Yarn](#tab-panel-1599)

```
npx astro add vercel
```

See the [Vercel adapter guide](/en/guides/integrations-guide/vercel/) to install manually instead, or for more configuration options, such as deploying your project’s Astro middleware using Vercel Edge Functions.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy to Vercel through the website UI or using Vercel’s CLI (command line interface). The process is the same for both static and on-demand rendered Astro sites.

### Website UI deployment

[Section titled “Website UI deployment”](#website-ui-deployment)

1.  Push your code to your online Git repository (GitHub, GitLab, BitBucket).
    
2.  [Import your project](https://vercel.com/new) into Vercel.
    
3.  Vercel will automatically detect Astro and configure the right settings.
    
4.  Your application is deployed! (e.g. [astro.vercel.app](https://astro.vercel.app/))
    

After your project has been imported and deployed, all subsequent pushes to branches will generate [Preview Deployments](https://vercel.com/docs/concepts/deployments/preview-deployments), and all changes made to the Production Branch (commonly “main”) will result in a [Production Deployment](https://vercel.com/docs/concepts/deployments/environments#production).

Learn more about Vercel’s [Git Integration](https://vercel.com/docs/concepts/git).

### CLI deployment

[Section titled “CLI deployment”](#cli-deployment)

1.  Install the [Vercel CLI](https://vercel.com/cli) and run `vercel` to deploy.
    
    *   [npm](#tab-panel-1600)
    *   [pnpm](#tab-panel-1601)
    *   [Yarn](#tab-panel-1602)
    
    ```
    npm install -g vercelvercel
    ```
    
2.  Vercel will automatically detect Astro and configure the right settings.
    
3.  When asked `Want to override the settings? [y/N]`, choose `N`.
    
4.  Your application is deployed! (e.g. [astro.vercel.app](https://astro.vercel.app/))
    

### Project config with `vercel.json`

[Section titled “Project config with vercel.json”](#project-config-with-verceljson)

You can use `vercel.json` to override the default behavior of Vercel and to configure additional settings. For example, you may wish to attach headers to HTTP responses from your Deployments.

Learn more about [Vercel’s project configuration](https://vercel.com/docs/project-configuration).

## More Deployment Guides

*   ![](/logos/aws.svg)
    
    ### [AWS](/en/guides/deploy/aws/)
    
*   ![](/logos/flightcontrol.svg)
    
    ### [AWS via Flightcontrol](/en/guides/deploy/aws-via-flightcontrol/)
    
*   ![](/logos/sst.svg)
    
    ### [AWS via SST](/en/guides/deploy/aws-via-sst/)
    
*   ![](/logos/azion.svg)
    
    ### [Azion](/en/guides/deploy/azion/)
    
*   ![](/logos/buddy.svg)
    
    ### [Buddy](/en/guides/deploy/buddy/)
    
*   ![](/logos/cleavr.svg)
    
    ### [Cleavr](/en/guides/deploy/cleavr/)
    
*   ![](/logos/clever-cloud.svg)
    
    ### [Clever Cloud](/en/guides/deploy/clever-cloud/)
    
*   ![](/logos/cloudflare-pages.svg)
    
    ### [Cloudflare](/en/guides/deploy/cloudflare/)
    
*   ![](/logos/cloudray.svg)
    
    ### [CloudRay](/en/guides/deploy/cloudray/)
    
*   ![](/logos/deno.svg)
    
    ### [Deno Deploy](/en/guides/deploy/deno/)
    
*   ![](/logos/deployhq.svg)
    
    ### [DeployHQ](/en/guides/deploy/deployhq/)
    
*   ![](/logos/edgeone-pages.svg)
    
    ### [EdgeOne Pages](/en/guides/deploy/edgeone-pages/)
    
*   ![](/logos/firebase.svg)
    
    ### [Firebase](/en/guides/deploy/firebase/)
    
*   ![](/logos/fleek.svg)
    
    ### [Fleek](/en/guides/deploy/fleek/)
    
*   ![](/logos/flyio.svg)
    
    ### [Fly.io](/en/guides/deploy/flyio/)
    
*   ![](/logos/github.svg)
    
    ### [GitHub Pages](/en/guides/deploy/github/)
    
*   ![](/logos/gitlab.svg)
    
    ### [GitLab Pages](/en/guides/deploy/gitlab/)
    
*   ![](/logos/google-cloud.svg)
    
    ### [Google Cloud](/en/guides/deploy/google-cloud/)
    
*   ![](/logos/heroku.svg)
    
    ### [Heroku](/en/guides/deploy/heroku/)
    
*   ![](/logos/juno.svg)
    
    ### [Juno](/en/guides/deploy/juno/)
    
*   ![](/logos/microsoft-azure.svg)
    
    ### [Microsoft Azure](/en/guides/deploy/microsoft-azure/)
    
*   ![](/logos/netlify.svg)
    
    ### [Netlify](/en/guides/deploy/netlify/)
    
*   ![](/logos/railway.svg)
    
    ### [Railway](/en/guides/deploy/railway/)
    
*   ![](/logos/render.svg)
    
    ### [Render](/en/guides/deploy/render/)
    
*   ![](/logos/seenode.svg)
    
    ### [Seenode](/en/guides/deploy/seenode/)
    
*   ![](/logos/sevalla.svg)
    
    ### [Sevalla](/en/guides/deploy/sevalla/)
    
*   ![](/logos/stormkit.svg)
    
    ### [Stormkit](/en/guides/deploy/stormkit/)
    
*   ![](/logos/surge.svg)
    
    ### [Surge](/en/guides/deploy/surge/)
    
*   ![](/logos/vercel.svg)
    
    ### [Vercel](/en/guides/deploy/vercel/)
    
*   ![](/logos/zeabur.svg)
    
    ### [Zeabur](/en/guides/deploy/zeabur/)
    
*   ![](/logos/zephyr.svg)
    
    ### [Zephyr Cloud](/en/guides/deploy/zephyr/)
    
*   ![](/logos/zerops.svg)
    
    ### [Zerops](/en/guides/deploy/zerops/)
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
