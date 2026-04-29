---
title: "Deploy your Astro Site with CloudRay"
source: "https://docs.astro.build/en/guides/deploy/cloudray/"
canonical_url: "https://docs.astro.build/en/guides/deploy/cloudray/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:43.237Z"
content_hash: "4bd819dedbe98a48f930c62834fc3daa98fa5d7f5bd9f5e73645cd8c806762bc"
menu_path: ["Deploy your Astro Site with CloudRay"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/cloudflare/index.md", "title": "Deploy your Astro Site to Cloudflare"}
nav_next: {"path": "astro/en/guides/deploy/deno/index.md", "title": "Deploy your Astro Site with Deno"}
---

# Deploy your Astro Site with CloudRay

You can deploy your Astro project using [CloudRay](https://cloudray.io), a centralized platform that helps you manage your servers, organize Bash scripts, and automate deployment tasks across virtual machines and cloud servers.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

*   A [CloudRay Account](https://app.cloudray.io)
*   Your app code stored in a [GitHub](https://github.com/) repository

## How to Deploy through CloudRay Dashboard

[Section titled “How to Deploy through CloudRay Dashboard”](#how-to-deploy-through-cloudray-dashboard)

Deploying with CloudRay typically involves three main steps:

1.  Install the [CloudRay Agent](https://cloudray.io/docs/agent) on your server to securely register your machine and enable remote automation.
    
2.  In your CloudRay Dashboard, write a reusable Bash script that clones your Astro repo, installs dependencies, builds your site, and configures a web server. Define any repo-specific values using [CloudRay’s variable groups](https://cloudray.io/docs/variable-groups).
    
3.  Use CloudRay’s Runlog interface to execute your script on your connected server and monitor the deployment in real time.
    

## Official Resources

[Section titled “Official Resources”](#official-resources)

Check out [the Astro guide in CloudRay’s docs](https://cloudray.io/articles/how-to-deploy-your-astro-site).

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
    
    ### [CloudRay](index.md)
    
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
