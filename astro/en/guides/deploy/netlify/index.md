---
title: "Deploy your Astro Site to Netlify"
source: "https://docs.astro.build/en/guides/deploy/netlify/"
canonical_url: "https://docs.astro.build/en/guides/deploy/netlify/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:35.159Z"
content_hash: "ecc3a8d67d5edc9d3a5466d96b1bcbf127c4b766c15095b06842d1365625c0c1"
menu_path: ["Deploy your Astro Site to Netlify"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/microsoft-azure/index.md", "title": "Deploy your Astro Site to Microsoft Azure"}
nav_next: {"path": "astro/en/guides/deploy/railway/index.md", "title": "Deploy your Astro Site with Railway"}
---

# Deploy your Astro Site to Netlify

[Netlify](https://netlify.com) offers hosting and serverless backend services for web applications and static websites. Any Astro site can be hosted on Netlify!

This guide includes instructions for deploying to Netlify through the website UI or Netlify’s CLI.

## Project configuration

[Section titled “Project configuration”](#project-configuration)

Your Astro project can be deployed to Netlify in three different ways: as a static site, a server-rendered site, or an edge-rendered site.

### Static site

[Section titled “Static site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Netlify.

### Adapter for on-demand rendering

[Section titled “Adapter for on-demand rendering”](#adapter-for-on-demand-rendering)

Add [the Netlify adapter](/en/guides/integrations-guide/netlify/) to enable on-demand rendering in your Astro project and deploy to Netlify with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

```
npx astro add netlify
```

See the [Netlify adapter guide](/en/guides/integrations-guide/netlify/) to install manually instead, or for more configuration options, such as deploying your project’s Astro middleware using Netlify’s Edge Functions.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy to Netlify through the website UI or using Netlify’s CLI (command line interface). The process is the same for both static and on-demand rendered Astro sites.

### Website UI deployment

[Section titled “Website UI deployment”](#website-ui-deployment)

If your project is stored in GitHub, GitLab, BitBucket, or Azure DevOps, you can use the Netlify website UI to deploy your Astro site.

1.  Click Add a new site in your [Netlify dashboard](https://app.netlify.com/)
    
2.  Choose Import an existing project
    
    When you import your Astro repository from your Git provider, Netlify should automatically detect and pre-fill the correct configuration settings for you.
    
3.  Make sure that the following settings are entered, then press the Deploy button:
    
    *   **Build Command:** `astro build` or `npm run build`
    *   **Publish directory:** `dist`
    
    After deploying, you will be redirected to the site overview page. There, you can edit the details of your site.
    

Any future changes to your source repository will trigger preview and production deploys based on your deployment configuration.

#### `netlify.toml` file

[Section titled “netlify.toml file”](#netlifytoml-file)

You can optionally create a new `netlify.toml` file at the top level of your project repository to configure your build command and publish directory, as well as other project settings including environment variables and redirects. Netlify will read this file and automatically configure your deployment.

To configure the default settings, create a `netlify.toml` file with the following contents:

```
[build]  command = "npm run build"  publish = "dist"
```

More info at [“Deploying an existing Astro Git repository”](https://www.netlify.com/blog/how-to-deploy-astro/#deploy-an-existing-git-repository-to-netlify) on Netlify’s blog

### CLI deployment

[Section titled “CLI deployment”](#cli-deployment)

You can also create a new site on Netlify and link up your Git repository by installing and using the [Netlify CLI](https://cli.netlify.com/).

1.  Install Netlify’s CLI globally
    
    ```
    npm install --global netlify-cli
    ```
    
2.  Run `netlify login` and follow the instructions to log in and authorize Netlify
    
3.  Run `netlify init` and follow the instructions
    
4.  Confirm your build command (`astro build`)
    
    The CLI will automatically detect the build settings (`astro build`) and deploy directory (`dist`), and will offer to automatically generate [a `netlify.toml` file](#netlifytoml-file) with those settings.
    
5.  Build and deploy by pushing to Git
    
    The CLI will add a deploy key to the repository, which means your site will be automatically rebuilt on Netlify every time you `git push`.
    

More details from Netlify on [Deploy an Astro site using the Netlify CLI](https://www.netlify.com/blog/how-to-deploy-astro/#link-your-astro-project-and-deploy-using-the-netlify-cli)

### Set a Node.js version

[Section titled “Set a Node.js version”](#set-a-nodejs-version)

If you are using a legacy [build image](https://docs.netlify.com/configure-builds/get-started/#build-image-selection) (Xenial) on Netlify, make sure that your Node.js version is set. Astro requires `v22.12.0` or higher.

You can [specify your Node.js version in Netlify](https://docs.netlify.com/configure-builds/manage-dependencies/#node-js-and-javascript) using:

*   a [`.nvmrc`](https://github.com/nvm-sh/nvm#nvmrc) file in your base directory.
*   a `NODE_VERSION` environment variable in your site’s settings using the Netlify project dashboard.

## Using Netlify Functions

[Section titled “Using Netlify Functions”](#using-netlify-functions)

No special configuration is required to use Netlify Functions with Astro. Add a `netlify/functions` directory to your project root and follow [the Netlify Functions documentation](https://docs.netlify.com/functions/overview/) to get started!

## Examples

[Section titled “Examples”](#examples)

*   [Deploy An Astro site with Forms, Serverless Functions, and Redirects](https://www.netlify.com/blog/deploy-an-astro-site-with-forms-serverless-functions-and-redirects/) — Netlify Blog
*   [Deployment Walkthrough Video](https://youtu.be/GrSLYq6ZTes) — Netlify YouTube channel

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
