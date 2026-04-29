---
title: "Deploy your Astro Site to Sevalla"
source: "https://docs.astro.build/en/guides/deploy/sevalla/"
canonical_url: "https://docs.astro.build/en/guides/deploy/sevalla/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:48.542Z"
content_hash: "2616dbf32395b66abab7dcf6b4d7ee25b12b6271927520cbf07d75cd2db3064e"
menu_path: ["Deploy your Astro Site to Sevalla"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/seenode/index.md", "title": "Deploy your Astro Site to Seenode"}
nav_next: {"path": "astro/en/guides/deploy/stormkit/index.md", "title": "Deploy your Astro Site to Stormkit"}
---

# Deploy your Astro Site to Sevalla

[Sevalla](https://sevalla.com/) is an all-in-one hosting and management platform for static sites, applications, and databases.

This guide details how to deploy your Astro project to Sevalla.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

*   A [**Sevalla** account](https://sevalla.com/signup/).
*   Your Astro project pushed to a [public or supported private Git repository](https://docs.sevalla.com/applications/git/overview) (GitHub, GitLab, or Bitbucket).

## Static Site Deployment

[Section titled “Static Site Deployment”](#static-site-deployment)

Sevalla’s Static Site Hosting deploys your site directly to a global edge network.

1.  Create a new [**Static Site**](https://docs.sevalla.com/static-sites/get-started/add-a-static-site) in the Sevalla dashboard.
    
2.  Connect your Git repository (GitHub, GitLab, or Bitbucket).
    
3.  Select your repository and branch (e.g., `main`).
    
4.  Configure the build settings:
    
    *   **Build command:** `npm run build`
    *   **Publish directory:** `dist`
5.  Click **Create Static Site** to deploy.
    

## SSR Deployment

[Section titled “SSR Deployment”](#ssr-deployment)

Sevalla’s Application Hosting supports full-stack applications. You can deploy Astro projects using [on-demand rendering](../../on-demand-rendering/index.md) (server-side rendering) via the Node.js adapter.

1.  Add the [`@astrojs/node` adapter](../../integrations-guide/node/index.md) to your Astro project.
    
    ```
    npx astro add node
    ```
    
2.  Configure the adapter in `astro.config.mjs`. Set `mode: 'standalone'` and ensure `host: true` is set so the server listens on all addresses (required for containerized environments).
    
    ```
    import { defineConfig } from 'astro/config';import node from '@astrojs/node';
    export default defineConfig({  output: 'server',  adapter: node({    mode: 'standalone'  }),  server: {    host: true  }});
    ```
    
3.  Ensure your `package.json` has a `start` script that runs the built server:
    
    ```
    "scripts": {  "start": "node ./dist/server/entry.mjs"}
    ```
    
4.  Create a new [**Application**](https://docs.sevalla.com/applications/get-started/add-an-application) in the Sevalla dashboard.
    
5.  Connect your Git repository.
    
6.  Configure the build settings:
    
    *   **Build Method:** Sevalla automatically detects Node.js projects (via Nixpacks).
    *   **Build command:** `npm run build`
    *   **Start command:** `npm run start`
7.  Click **Create Application** to deploy.
    

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Build Failures

[Section titled “Build Failures”](#build-failures)

Check the [**Build Logs**](https://docs.sevalla.com/applications/runtime-logs) in the Sevalla dashboard for error messages. Ensure all dependencies are in `dependencies` (not `devDependencies` if needed at runtime).

### Node Version

[Section titled “Node Version”](#node-version)

Ensure the Node.js version selected in Sevalla matches your local development version (check `node -v`).

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
    
    ### [Sevalla](index.md)
    
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
