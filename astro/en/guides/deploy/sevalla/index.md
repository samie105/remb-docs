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

Sevalla’s Application Hosting supports full-stack applications. You can deploy Astro projects using [on-demand rendering](/en/guides/on-demand-rendering/) (server-side rendering) via the Node.js adapter.

1.  Add the [`@astrojs/node` adapter](/en/guides/integrations-guide/node/) to your Astro project.
    
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


