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
    
    ### [Zephyr Cloud](index.md)
    
*   ![](/logos/zerops.svg)
    
    ### [Zerops](../zerops/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
