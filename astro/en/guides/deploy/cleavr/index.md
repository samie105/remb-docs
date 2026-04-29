---
title: "Deploy your Astro Site with Cleavr"
source: "https://docs.astro.build/en/guides/deploy/cleavr/"
canonical_url: "https://docs.astro.build/en/guides/deploy/cleavr/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:32.905Z"
content_hash: "507ea5a587ec4accd183d6b754f946074fd64aa6fb5abd82558fbb0493ac1230"
menu_path: ["Deploy your Astro Site with Cleavr"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/buddy/index.md", "title": "Deploy your Astro Site with Buddy"}
nav_next: {"path": "astro/en/guides/deploy/clever-cloud/index.md", "title": "Deploy your Astro Site to Clever Cloud"}
---

# Deploy your Astro Site with Cleavr

You can deploy your Astro project to your own Virtual Private Server (VPS) using [Cleavr](https://cleavr.io/), a server and app deployment management tool.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

*   A Cleavr account
*   A server on your VPS provider using Cleavr

## Add your site

[Section titled “Add your site”](#add-your-site)

1.  In Cleavr, navigate to the server you want to add your Astro project to.
    
2.  Select **Add Site** and fill in the details for your application, such as domain name.
    
3.  For **App Type**, select ‘NodeJS Static’ or ‘NodeJS SSR’ according to how you are setting up your Astro app.
    
4.  For Static apps, set **Artifact Folder** to `dist`.
    
5.  For SSR apps:
    
    *   Set **Entry Point** to `entry.mjs`.
    *   Set **Artifact Folder** to `dist/server`.
6.  Select **Add** to add the site to your server.
    

## Setup and deploy

[Section titled “Setup and deploy”](#setup-and-deploy)

1.  Once your new site is added, click **Setup and deploy**.
    
2.  Select the **VC Profile**, **Repo**, and **Branch** for your Astro Project.
    
3.  Make any additional configurations necessary for your project.
    
4.  Click on the **Deployments** tab and then click on **Deploy**.
    

Congratulations, you’ve just deployed your Astro app!

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
    
    ### [Cleavr](index.md)
    
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
    
    ### [Fleek](../fleek/index.md)
    
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
