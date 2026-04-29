---
title: "Deploy your Astro Site with Railway"
source: "https://docs.astro.build/en/guides/deploy/railway/"
canonical_url: "https://docs.astro.build/en/guides/deploy/railway/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:37.956Z"
content_hash: "e9e76516588201b071afc56c0eaed7a11f4153454d7e7f0c409c865e8e2bc020"
menu_path: ["Deploy your Astro Site with Railway"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/netlify/index.md", "title": "Deploy your Astro Site to Netlify"}
nav_next: {"path": "astro/en/guides/deploy/render/index.md", "title": "Deploy your Astro Site to Render"}
---

# Deploy your Astro Site with Railway

[Railway](https://railway.com?utm_medium=integration&utm_source=button&utm_campaign=astro) is a deployment platform built to simplify your infrastructure stack from servers to observability with a unified developer experience.

This guide is for deploying an Astro static site to Railway using either the web interface or Railway CLI tool.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Railway’s default build system, [Railpack](https://docs.railway.com/reference/railpack), automatically builds your Astro project as a static site.

## Deploy via a Railway template

[Section titled “Deploy via a Railway template”](#deploy-via-a-railway-template)

If you do not already have an Astro project, and are starting from scratch:

1.  Go to the Astro template on Railway: [railway.com/deploy/astro-starter](https://railway.com/deploy/astro-starter?utm_medium=integration&utm_source=docs&utm_campaign=astro).
    
2.  Click “Deploy Now” and sign in with your GitHub account to authorize Railway. This will deploy the Astro template into your new Railway account.
    
3.  Eject the service code into your own Github repository by following [this guide](https://docs.railway.com/guides/deploy#eject-from-template-repository?utm_medium=integration&utm_source=docs&utm_campaign=astro). This will allow you to keep the repo deployed but customize it with your own code.
    

## Deploy via the web interface

[Section titled “Deploy via the web interface”](#deploy-via-the-web-interface)

If you have an existing Astro project you would like to deploy but not a Railway account yet:

1.  Create a [Railway account](https://railway.com/dashboard) and sign in.
    
2.  From the Railway dashboard, create a new [project](https://docs.railway.com/guides/projects).
    
3.  Select the option to deploy from a GitHub repository, and select your Astro project.
    
4.  Generate or add a custom domain from your project’s [network settings](https://docs.railway.com/guides/public-networking#railway-provided-domain).
    

## Deploy via Railway CLI

[Section titled “Deploy via Railway CLI”](#deploy-via-railway-cli)

If you have an existing Astro project you would like to deploy and an existing Railway account:

1.  [Install](https://docs.railway.com/guides/cli#installing-the-cli) the Railway CLI tool.
    
2.  Login with the command `railway login`.
    
3.  From within your Astro project, run `railway init` and choose a workspace and project name.
    
4.  Run `railway up` to deploy your project on Railway.
    
5.  Run `railway domain` to generate a Railway provided service domain.
    

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Railway guide to deploying an Astro app](https://docs.railway.com/guides/astro?utm_medium=integration&utm_source=docs&utm_campaign=astro)
*   [Railway Astro starter template](https://railway.com/deploy/astro-starter?utm_medium=integration&utm_source=docs&utm_campaign=astro)

## Community Resources

[Section titled “Community Resources”](#community-resources)

[How to host an Astro site on Railway](https://jacksmith.xyz/blog/how-to-host-astro-site-on-railway)

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
    
    ### [Railway](index.md)
    
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
