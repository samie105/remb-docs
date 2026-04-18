---
title: "Deploy your Astro Site to Microsoft Azure"
source: "https://docs.astro.build/en/guides/deploy/microsoft-azure/"
canonical_url: "https://docs.astro.build/en/guides/deploy/microsoft-azure/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:27.714Z"
content_hash: "b7498c3425ef22619eb7a0d5e3e1fb71129caa763a0d56e52c012843cda41fd5"
menu_path: ["Deploy your Astro Site to Microsoft Azure"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/juno/index.md", "title": "Deploy your Astro Site to Juno"}
nav_next: {"path": "astro/en/guides/deploy/netlify/index.md", "title": "Deploy your Astro Site to Netlify"}
---

# Deploy your Astro Site to Microsoft Azure

[Azure](https://azure.microsoft.com/) is a cloud platform from Microsoft. You can deploy your Astro site with Microsoft Azure’s [Static Web Apps](https://aka.ms/staticwebapps) service.

This guide takes you through deploying your Astro site stored in GitHub using Visual Studio Code. Please see Microsoft guides for using an [Azure Pipelines Task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-static-web-app-v0?view=azure-pipelines) for other setups.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To follow this guide, you will need:

*   An Azure account and a subscription key. You can create a [free Azure account here](https://azure.microsoft.com/free).
*   Your app code pushed to [GitHub](https://github.com/).
*   The [SWA Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps) in [Visual Studio Code](https://code.visualstudio.com/).

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1.  Open your project in VS Code.
    
2.  Open the Static Web Apps extension, sign in to Azure, and click the **+** button to create a new Static Web App. You will be prompted to designate which subscription key to use.
    
3.  Follow the wizard started by the extension to give your app a name, choose a framework preset, and designate the app root (usually `/`) and built file location (use `/dist`). Astro is not listed in the built-in templates in Azure so you will need to select `custom`. The wizard will run and will create a [GitHub Action](https://github.com/features/actions) in the `.github` folder of your repo. (This folder will be automatically created if it does not already exist.)
    

The GitHub Action will deploy your app (you can see its progress in your repo’s Actions tab on GitHub). When successfully completed, you can view your app at the address shown in the SWA Extension’s progress window by clicking the **Browse Website** button (this will appear after the GitHub Action has run).

## Known Issues

[Section titled “Known Issues”](#known-issues)

The GitHub action yaml that is created for you assumes the use of node 14. This means the Astro build fails. To resolve this update your projects package.json file with this snippet.

```
  "engines": {    "node": ">=22.12.0"  },
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Microsoft Azure Static Web Apps documentation](https://learn.microsoft.com/en-us/azure/static-web-apps/)

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [Deploying an Astro Website to Azure Static Web Apps](https://www.blueboxes.co.uk/deploying-an-astro-website-to-azure-static-web-apps)
*   [Deploying a Static Astro Site to Azure Static Web Apps using GitHub Actions](https://agramont.net/blog/create-static-site-astro-azure-ssg/#automate-deployment-with-github-actions)
*   [Astro site deployment to Azure Static Web Apps with the CLI from GitHub Actions](https://www.eliostruyf.com/deploy-astro-azure-static-web-apps-github-cli/)

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


