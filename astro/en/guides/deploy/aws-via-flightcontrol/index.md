---
title: "Deploy your Astro Site to AWS with Flightcontrol"
source: "https://docs.astro.build/en/guides/deploy/aws-via-flightcontrol/"
canonical_url: "https://docs.astro.build/en/guides/deploy/aws-via-flightcontrol/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:17.344Z"
content_hash: "3a4245945c3d965e3b97c6a1aeb7355d4b8fc3f9a0cf0218a66c8a089de0b4d9"
menu_path: ["Deploy your Astro Site to AWS with Flightcontrol"]
section_path: []
nav_prev: {"path": "../aws/index.md", "title": "Deploy your Astro Site to AWS"}
nav_next: {"path": "../aws-via-sst/index.md", "title": "Deploy your Astro Site to AWS with SST"}
---

# Deploy your Astro Site to AWS with Flightcontrol

You can deploy an Astro site using [Flightcontrol](https://www.flightcontrol.dev?ref=astro), which provides fully-automated deployments to your AWS account.

Supports both static and SSR Astro sites.

## How to Deploy

[Section titled “How to Deploy”](#how-to-deploy)

1.  Create a Flightcontrol account at [app.flightcontrol.dev/signup](https://app.flightcontrol.dev/signup?ref=astro)
    
2.  Go to [app.flightcontrol.dev/projects/new/1](https://app.flightcontrol.dev/projects/new/1)
    
3.  Connect your GitHub account and select your repo
    
4.  Select your desired “Config Type”:
    
    *   `GUI` (all config managed through Flightcontrol dashboard) where you will select the `Astro Static` or `Astro SSR` preset
    *   `flightcontrol.json` (“infrastructure as code” option where all config is in your repo) where you will select an Astro example config, then add it to your codebase as `flightcontrol.json`
5.  Adjust any configuration as needed
    
6.  Click “Create Project” and complete any required steps (like linking your AWS account).
    

### SSR Setup

[Section titled “SSR Setup”](#ssr-setup)

To deploy with SSR support, make sure you first set up the [`@astrojs/node`](/en/guides/integrations-guide/node/) adapter. Then, follow the steps above, choosing the appropriate configurations for Astro SSR.

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
