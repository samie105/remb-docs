---
title: "Deploy your Astro Site to Zerops"
source: "https://docs.astro.build/en/guides/deploy/zerops/"
canonical_url: "https://docs.astro.build/en/guides/deploy/zerops/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:05.221Z"
content_hash: "9f8888982b5be8ea14ea85b7020d854bdd330ee2e81ab9b1bbb06c66673aede6"
menu_path: ["Deploy your Astro Site to Zerops"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/zephyr/index.md", "title": "Deploy your Astro Site to Zephyr Cloud"}
nav_next: {"path": "astro/en/guides/cms/index.md", "title": "Use a CMS with Astro"}
---

# Deploy your Astro Site to Zerops

[Zerops](https://zerops.io/) is a dev-first cloud platform that can be used to deploy both Static and SSR Astro site.

This guide will walk you through setting up and deploying both Static and SSR Astro sites on Zerops.

Running apps on Zerops requires two steps:

1.  Creating a project
2.  Triggering build & deploy pipeline

## Astro Static site on Zerops

[Section titled “Astro Static site on Zerops”](#astro-static-site-on-zerops)

### Creating a project and a service for Astro Static

[Section titled “Creating a project and a service for Astro Static”](#creating-a-project-and-a-service-for-astro-static)

Projects and services can be added either through a [`Project add`](https://app.zerops.io/dashboard/project-add) wizard or imported using a yaml structure:

```
# see https://docs.zerops.io/references/import for full referenceproject:  name: recipe-astroservices:  - hostname: app    type: static
```

This will create a project called `recipe-astro` with a Zerops Static service called `app`.

### Deploying your Astro Static site

[Section titled “Deploying your Astro Static site”](#deploying-your-astro-static-site)

To tell Zerops how to build and run your site, add a `zerops.yml` to your repository:

*   [npm](#tab-panel-1615)
*   [pnpm](#tab-panel-1616)
*   [Yarn](#tab-panel-1617)

```
# see https://docs.zerops.io/zerops-yml/specification for full referencezerops:  - setup: app    build:      base: nodejs@20      buildCommands:        - npm i        - npm build      deployFiles:        - dist/~    run:      base: static
```

Now you can [trigger the build & deploy pipeline using the Zerops CLI](#trigger-the-pipeline-using-zerops-cli-zcli) or by connecting the `app` service with your [GitHub](https://docs.zerops.io/references/github-integration/) / [GitLab](https://docs.zerops.io/references/gitlab-integration) repository from inside the service detail.

## Astro SSR site on Zerops

[Section titled “Astro SSR site on Zerops”](#astro-ssr-site-on-zerops)

### Update scripts

[Section titled “Update scripts”](#update-scripts)

Update your `start` script to run the server output from the Node adapter.

```
"scripts": {  "start": "node ./dist/server/entry.mjs",}
```

### Creating a project and a service for Astro SSR (Node.js)

[Section titled “Creating a project and a service for Astro SSR (Node.js)”](#creating-a-project-and-a-service-for-astro-ssr-nodejs)

Projects and services can be added either through a [`Project add`](https://app.zerops.io/dashboard/project-add) wizard or imported using a yaml structure:

```
# see https://docs.zerops.io/references/import for full referenceproject:  name: recipe-astroservices:  - hostname: app    type: nodejs@20
```

This will create a project called `recipe-astro` with Zerops Node.js service called `app`.

### Deploying your Astro SSR site

[Section titled “Deploying your Astro SSR site”](#deploying-your-astro-ssr-site)

To tell Zerops how to build and run your site using the official [Astro Node.js adapter](../../integrations-guide/node/index.md) in `standalone` mode, add a `zerops.yml` file to your repository:

*   [npm](#tab-panel-1618)
*   [pnpm](#tab-panel-1619)
*   [Yarn](#tab-panel-1620)

```
# see https://docs.zerops.io/zerops-yml/specification for full referencezerops:  - setup: app    build:      base: nodejs@20      buildCommands:        - npm i        - npm run build      deployFiles:        - dist        - package.json        - node_modules    run:      base: nodejs@20      ports:        - port: 3000          httpSupport: true      envVariables:        PORT: 3000        HOST: 0.0.0.0      start: npm start
```

Now you can [trigger the build & deploy pipeline using the Zerops CLI](#trigger-the-pipeline-using-zerops-cli-zcli) or by connecting the `app` service with your [GitHub](https://docs.zerops.io/references/github-integration/) / [GitLab](https://docs.zerops.io/references/gitlab-integration) repository from inside the service detail.

## Trigger the pipeline using Zerops CLI (zcli)

[Section titled “Trigger the pipeline using Zerops CLI (zcli)”](#trigger-the-pipeline-using-zerops-cli-zcli)

1.  Install the Zerops CLI.
    
    ```
    # To download the zcli binary directly,# use https://github.com/zeropsio/zcli/releasesnpm i -g @zerops/zcli
    ```
    
2.  Open [`Settings > Access Token Management`](https://app.zerops.io/settings/token-management) in the Zerops app and generate a new access token.
    
3.  Log in using your access token with the following command:
    
    ```
    zcli login <token>
    ```
    
4.  Navigate to the root of your app (where `zerops.yml` is located) and run the following command to trigger the deploy:
    
    ```
    zcli push
    ```
    

## Resources

[Section titled “Resources”](#resources)

### Official

[Section titled “Official”](#official)

*   [Create Zerops account](https://app.zerops.io/registration)
*   [Zerops Documentation](https://docs.zerops.io)
*   [Zerops Astro recipe](https://app.zerops.io/recipe/astro)

### Community

[Section titled “Community”](#community)

*   [Deploying Astro to Zerops in 3 mins](https://medium.com/@arjunaditya/how-to-deploy-astro-to-zerops-4230816a62b4)
*   [Deploying Astro SSG with Node.js on Zerops with One Click Deploy](https://youtu.be/-4KTa4VWtBE)
*   [Deploying Astro SSR with Node.js on Zerops with One Click Deploy](https://youtu.be/eR6b_JnDH6g)

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
    
    ### [Zerops](index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
