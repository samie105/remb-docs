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

You can deploy both fully static and on-demand rendered Astro projects on Clever Cloud. Regardless of your `output` mode (pre-rendered or [on-demand](/en/guides/on-demand-rendering/)), you can choose to deploy as a **static application** which runs using a post-build hook, or as a **Node.js** application, which requires some manual configuration in your `package.json`.

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

