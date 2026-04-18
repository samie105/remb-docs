---
title: "Deploy your Astro Site to Zephyr Cloud"
source: "https://docs.astro.build/en/guides/deploy/zephyr/"
canonical_url: "https://docs.astro.build/en/guides/deploy/zephyr/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:09.373Z"
content_hash: "41b80c0dbfd0203e11037efcb204cc2f81f62c4b106c0516bbfcab299e20e33e"
menu_path: ["Deploy your Astro Site to Zephyr Cloud"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/zeabur/index.md", "title": "Deploy your Astro Site to Zeabur"}
nav_next: {"path": "astro/en/guides/deploy/zerops/index.md", "title": "Deploy your Astro Site to Zerops"}
---

# Deploy your Astro Site to Zephyr Cloud

You can use [Zephyr Cloud](https://zephyr-cloud.io) to deploy an Astro site with intelligent asset management, comprehensive build analytics, and first-class support for Module Federation architectures.

Zephyr operates on a **Bring Your Own Cloud (BYOC)** model, deploy to your choice of [supported clouds](https://docs.zephyr-cloud.io/cloud) through a unified interface without vendor lock-in. Switch providers anytime without changing your deployment workflow.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

### Automatic Installation

[Section titled “Automatic Installation”](#automatic-installation)

1.  Add the Zephyr integration to your Astro project with the following command. This will install the integration and update your `astro.config.mjs` file automatically:
    
    *   [npm](#tab-panel-1603)
    *   [pnpm](#tab-panel-1604)
    *   [Yarn](#tab-panel-1605)
    
    ```
    npx with-zephyr@latest
    ```
    
2.  Build and deploy your Astro site:
    
    *   [npm](#tab-panel-1606)
    *   [pnpm](#tab-panel-1607)
    *   [Yarn](#tab-panel-1608)
    
    ```
    npm run build
    ```
    
3.  Your application is deployed! Zephyr will provide a deployment URL and comprehensive build analytics.
    

### Manual Installation

[Section titled “Manual Installation”](#manual-installation)

1.  Install the Zephyr Astro integration:
    
    *   [npm](#tab-panel-1609)
    *   [pnpm](#tab-panel-1610)
    *   [Yarn](#tab-panel-1611)
    
    ```
    npm install zephyr-astro-integration
    ```
    
2.  Add the integration to your `astro.config.mjs`:
    
    ```
    import { defineConfig } from 'astro/config';import { withZephyr } from 'zephyr-astro-integration';
    export default defineConfig({  integrations: [    withZephyr(),  ],});
    ```
    
3.  Build and deploy your Astro site:
    
    *   [npm](#tab-panel-1612)
    *   [pnpm](#tab-panel-1613)
    *   [Yarn](#tab-panel-1614)
    
    ```
    npm run build
    ```
    
4.  Your application is deployed! Zephyr will provide a deployment URL and comprehensive build analytics.
    

### More details

[Section titled “More details”](#more-details)

For more detailed information refer to the [Zephyr Cloud documentation on deploying with Astro](https://docs.zephyr-cloud.io/meta-frameworks/astro).

## What happens during deployment

[Section titled “What happens during deployment”](#what-happens-during-deployment)

When you build your Astro site with the Zephyr integration, the following process occurs:

1.  **Build Context Extraction**: Zephyr captures Git information (commit, branch, author) and package metadata
2.  **Asset Hashing**: All build outputs are hashed using SHA-256 for content-addressable storage
3.  **Delta Detection**: Zephyr queries the CDN edge to identify which assets already exist
4.  **Optimized Upload**: Only new or modified assets are uploaded
5.  **Snapshot Creation**: An immutable deployment snapshot is created with all asset references
6.  **Analytics Upload**: Build statistics, module graphs, and dependency information are sent to the dashboard
7.  **CDN Deployment**: Assets are published to your configured CDN with permanent cache headers

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Zephyr Cloud Documentation](https://docs.zephyr-cloud.io)
*   [Zephyr Astro Integration on GitHub](https://github.com/ZephyrCloudIO/zephyr-packages/tree/main/libs/zephyr-astro-integration)
*   [Zephyr Cloud Platform](https://zephyr-cloud.io)

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
