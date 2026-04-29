---
title: "Deploy your Astro Site to Clever Cloud"
source: "https://docs.astro.build/en/guides/deploy/clever-cloud/"
canonical_url: "https://docs.astro.build/en/guides/deploy/clever-cloud/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:37.089Z"
content_hash: "834a277758ac77fb7f1a116aa334a3c3b3e477343ea2490628937de5a7433a06"
menu_path: ["Deploy your Astro Site to Clever Cloud"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/cleavr/index.md", "title": "Deploy your Astro Site with Cleavr"}
nav_next: {"path": "astro/en/guides/deploy/cloudflare/index.md", "title": "Deploy your Astro Site to Cloudflare"}
---

# Deploy your Astro Site to Clever Cloud

[Clever Cloud](https://clevercloud.com) is a European cloud platform that provides automated, scalable services.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

You can deploy both fully static and on-demand rendered Astro projects on Clever Cloud. Regardless of your `output` mode (pre-rendered or [on-demand](../../on-demand-rendering/index.md)), you can choose to deploy as a **static application** which runs using a post-build hook, or as a **Node.js** application, which requires some manual configuration in your `package.json`.

### Scripts

[Section titled “Scripts”](#scripts)

If you’re running an on-demand Node.js application, update your `start` script to run the Node server. Applications on Clever Cloud listen on port **8080**.

```
"scripts": {  "start": "node ./dist/server/entry.mjs --host 0.0.0.0 --port 8080",}
```

## Deploy Astro from the Console

[Section titled “Deploy Astro from the Console”](#deploy-astro-from-the-console)

To deploy your Astro project to Clever Cloud, you will need to **create a new application**. The application wizard will walk you through the necessary configuration steps.

1.  From the lateral menubar, click **Create** > **An application**
    
2.  Choose how to deploy:
    
    *   **Create a brand new app**: to deploy from a local repository with Git
    
    or
    
    *   **Select a GitHub repository**: to deploy from GitHub
3.  Select a **Node.js** application, or a **static** one.
    
4.  Set up the minimal size for your instance and scalability options. Astro sites can typically be deployed using the **Nano** instance. Depending on your project’s specifications and dependencies, you may need to adjust accordingly as you watch the metrics from the **Overview** page.
    
5.  Select a **region** to deploy your instance.
    
6.  Skip [connecting **Add-ons** to your Clever application](https://www.clevercloud.com/developers/doc/addons/) unless you’re using a database or Keycloak.
    
7.  Inject **environment variables**:
    
    *   For **Node.js**, set the following environment variables based on your package manager:
    
    *   [npm](#tab-panel-1539)
    *   [pnpm](#tab-panel-1540)
    *   [Yarn](#tab-panel-1541)
    
    ```
    CC_NODE_BUILD_TOOL="npm"CC_PRE_BUILD_HOOK="npm install && npm run astro telemetry disable && npm run build"
    ```
    
    *   For a **static** application, add these variables:
    
    *   [npm](#tab-panel-1542)
    *   [pnpm](#tab-panel-1543)
    *   [Yarn](#tab-panel-1544)
    
    ```
    CC_POST_BUILD_HOOK="npm run build"CC_PRE_BUILD_HOOK="npm install && npm run astro telemetry disable"CC_WEBROOT="/dist"
    ```
    
8.  **Deploy!** If you’re deploying from **GitHub**, your deployment should start automatically. If you’re using **Git**, copy the remote and push on the **master** branch.
    

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Clever Cloud documentation for deploying a Node.js application](https://www.clevercloud.com/developers/doc/applications/nodejs/)
*   [Clever Cloud documentation for deploying Astro as a static application](https://www.clevercloud.com/developers/guides/astro/)

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
    
    ### [Clever Cloud](index.md)
    
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
