---
title: "Deploy your Astro Site to Fleek"
source: "https://docs.astro.build/en/guides/deploy/fleek/"
canonical_url: "https://docs.astro.build/en/guides/deploy/fleek/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:08.680Z"
content_hash: "e224334a2fd11c3eb3e0fa23d4829276637305953db323a4000358a1596adf72"
menu_path: ["Deploy your Astro Site to Fleek"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/firebase/index.md", "title": "Deploy your Astro Site to Google\u2019s Firebase Hosting"}
nav_next: {"path": "astro/en/guides/deploy/flyio/index.md", "title": "Deploy your Astro Site to Fly.io"}
---

# Deploy your Astro Site to Fleek

You can use [Fleek](http://fleek.xyz/) to deploy a static Astro site to their edge-optimized decentralized network.

This guide gives a complete walkthrough of deploying your Astro site to Fleek using the Fleek UI and CLI.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Fleek as a static site.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy to Fleek through the website UI or using Fleek’s CLI (command line interface).

### Platform UI Deployment

[Section titled “Platform UI Deployment”](#platform-ui-deployment)

1.  Create a [Fleek](https://app.fleek.xyz) account.
    
2.  Push your code to your online Git repository (GitHub).
    
3.  Import your project into Fleek.
    
4.  Fleek will automatically detect Astro and then you can configure the correct settings.
    
5.  Your application is deployed!
    

### Fleek CLI

[Section titled “Fleek CLI”](#fleek-cli)

1.  Install the Fleek CLI.
    
    ```
    # You need to have Nodejs >= 18.18.2npm install -g @fleek-platform/cli
    ```
    
2.  Log in to your Fleek account from your terminal.
    
    ```
    fleek login
    ```
    
3.  Run the build command to generate the static files. By default, these will be located in the `dist/` directory.
    
    ```
    npm run build
    ```
    
4.  Initialize your project. This will generate a configuration file.
    
    ```
    fleek sites init
    ```
    
5.  You will be prompted to either create a new Fleek Site or use an existing one. Give the site a name and select the directory where your project is located.
    
6.  Deploy your site.
    
    ```
    fleek sites deploy
    ```
    

## Learn more

[Section titled “Learn more”](#learn-more)

[Deploy site from Fleek UI](https://fleek.xyz/docs/platform/deployments/)

[Deploy site from Fleek CLI](https://fleek.xyz/docs/cli/hosting/)

## More Deployment Guides

*   ![](/logos/aws.svg)
    
    ### [AWS](../aws/index.md)
    
*   ![](/logos/flightcontrol.svg)
    
    ### [AWS via Flightcontrol](../aws-via-flightcontrol/index.md)
    
*   ![](/logos/sst.svg)
    
    ### [AWS via SST](../aws-via-sst/index.md)
    
*   ![](/logos/azion.svg)
    
    ### [Azion](../azion/index.md)
    
*   ![](/logos/buddy.svg)
    
    ### [Buddy](../buddy/index.md)
    
*   ![](/logos/cleavr.svg)
    
    ### [Cleavr](../cleavr/index.md)
    
*   ![](/logos/clever-cloud.svg)
    
    ### [Clever Cloud](../clever-cloud/index.md)
    
*   ![](/logos/cloudflare-pages.svg)
    
    ### [Cloudflare](../cloudflare/index.md)
    
*   ![](/logos/cloudray.svg)
    
    ### [CloudRay](../cloudray/index.md)
    
*   ![](/logos/deno.svg)
    
    ### [Deno Deploy](../deno/index.md)
    
*   ![](/logos/deployhq.svg)
    
    ### [DeployHQ](../deployhq/index.md)
    
*   ![](/logos/edgeone-pages.svg)
    
    ### [EdgeOne Pages](../edgeone-pages/index.md)
    
*   ![](/logos/firebase.svg)
    
    ### [Firebase](../firebase/index.md)
    
*   ![](/logos/fleek.svg)
    
    ### [Fleek](index.md)
    
*   ![](/logos/flyio.svg)
    
    ### [Fly.io](../flyio/index.md)
    
*   ![](/logos/github.svg)
    
    ### [GitHub Pages](../github/index.md)
    
*   ![](/logos/gitlab.svg)
    
    ### [GitLab Pages](../gitlab/index.md)
    
*   ![](/logos/google-cloud.svg)
    
    ### [Google Cloud](../google-cloud/index.md)
    
*   ![](/logos/heroku.svg)
    
    ### [Heroku](../heroku/index.md)
    
*   ![](/logos/juno.svg)
    
    ### [Juno](../juno/index.md)
    
*   ![](/logos/microsoft-azure.svg)
    
    ### [Microsoft Azure](../microsoft-azure/index.md)
    
*   ![](/logos/netlify.svg)
    
    ### [Netlify](../netlify/index.md)
    
*   ![](/logos/railway.svg)
    
    ### [Railway](../railway/index.md)
    
*   ![](/logos/render.svg)
    
    ### [Render](../render/index.md)
    
*   ![](/logos/seenode.svg)
    
    ### [Seenode](../seenode/index.md)
    
*   ![](/logos/sevalla.svg)
    
    ### [Sevalla](../sevalla/index.md)
    
*   ![](/logos/stormkit.svg)
    
    ### [Stormkit](../stormkit/index.md)
    
*   ![](/logos/surge.svg)
    
    ### [Surge](../surge/index.md)
    
*   ![](/logos/vercel.svg)
    
    ### [Vercel](../vercel/index.md)
    
*   ![](/logos/zeabur.svg)
    
    ### [Zeabur](../zeabur/index.md)
    
*   ![](/logos/zephyr.svg)
    
    ### [Zephyr Cloud](../zephyr/index.md)
    
*   ![](/logos/zerops.svg)
    
    ### [Zerops](../zerops/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
