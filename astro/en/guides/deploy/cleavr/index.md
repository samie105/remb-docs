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


