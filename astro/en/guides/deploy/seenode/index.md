---
title: "Deploy your Astro Site to Seenode"
source: "https://docs.astro.build/en/guides/deploy/seenode/"
canonical_url: "https://docs.astro.build/en/guides/deploy/seenode/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:46.448Z"
content_hash: "4ea00d5f01e60f666985e61a98bccb65fc2d31839908fde6f2d9816d0799a0d6"
menu_path: ["Deploy your Astro Site to Seenode"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/render/index.md", "title": "Deploy your Astro Site to Render"}
nav_next: {"path": "astro/en/guides/deploy/sevalla/index.md", "title": "Deploy your Astro Site to Sevalla"}
---

# Deploy your Astro Site to Seenode

[Seenode](https://seenode.com) is a deployment platform for building and deploying web applications with databases, built-in observability, and auto-scaling. Astro sites can be deployed to Seenode using server-side rendering (SSR).

This guide includes instructions for deploying to Seenode through the web interface.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable on-demand rendering in your Astro project and deploy to Seenode, add [the Node.js adapter](../../integrations-guide/node/index.md) with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

*   [npm](#tab-panel-1594)
*   [pnpm](#tab-panel-1595)
*   [Yarn](#tab-panel-1596)

```
npx astro add node
```

After installing the adapter, update your `astro.config.mjs` to configure the server for Seenode’s requirements:

```
import { defineConfig } from 'astro/config';import node from '@astrojs/node';
export default defineConfig({  output: 'server',  adapter: node({    mode: 'standalone'  }),  server: {    port: process.env.NODE_ENV === 'production' ? (Number(process.env.PORT) || 80) : 4321,    host: true  }});
```

Update your `package.json` to include a start script that runs the built server:

```
{  "scripts": {    "dev": "astro dev",    "build": "astro build",    "preview": "astro preview",    "start": "NODE_ENV=production node ./dist/server/entry.mjs"  }}
```

See [Seenode’s Astro deployment guide](https://seenode.com/docs/frameworks/javascript/astro/) for more configuration options and troubleshooting.

## How to Deploy

[Section titled “How to Deploy”](#how-to-deploy)

You can deploy to Seenode through the web interface by connecting your Git repository.

### Web Interface Deployment

[Section titled “Web Interface Deployment”](#web-interface-deployment)

1.  Create a [Seenode account](https://cloud.seenode.com) and sign in.
    
2.  Push your code to your Git repository (GitHub or GitLab).
    
3.  From the [Seenode Dashboard](https://cloud.seenode.com/dashboard/applications/web/create), create a new **Web Service** and connect your repository.
    
4.  Seenode will automatically detect your Astro project. Configure the deployment settings:
    
    *   **Build Command:** `npm ci && npm run build` (or use `pnpm` / `yarn` equivalents)
    *   **Start Command:** `npm start`
    *   **Port:** `80` (required for web services)
5.  Select your preferred instance size and click **Create Web Service**.
    
6.  Your application will be built and deployed. Once complete, you’ll receive a URL to access your live Astro site after which you can link your domain.
    

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Seenode Cloud](https://cloud.seenode.com) — Seenode dashboard
*   [Seenode Documentation](https://seenode.com/docs) — complete platform documentation
*   [Seenode Astro Guide](https://seenode.com/docs/frameworks/javascript/astro/) — detailed deployment guide and troubleshooting
*   [Seenode Astro Template](https://github.com/seenode/example-astro) — pre-configured starter template

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
    
    ### [Seenode](index.md)
    
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
