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

To tell Zerops how to build and run your site using the official [Astro Node.js adapter](/en/guides/integrations-guide/node/) in `standalone` mode, add a `zerops.yml` file to your repository:

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
