---
title: "Deploy your Astro Site with Deno"
source: "https://docs.astro.build/en/guides/deploy/deno/"
canonical_url: "https://docs.astro.build/en/guides/deploy/deno/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:48.679Z"
content_hash: "98c0ab28e007582385c5727a907f18324f5926c10d6e9fa6afab0b22a6ca43c9"
menu_path: ["Deploy your Astro Site with Deno"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/cloudray/index.md", "title": "Deploy your Astro Site with CloudRay"}
nav_next: {"path": "astro/en/guides/deploy/deployhq/index.md", "title": "Deploy your Astro Site with DeployHQ"}
---

# Deploy your Astro Site with Deno

You can deploy a static or on-demand rendered Astro site using Deno, either on your own server, or to [Deno Deploy](https://deno.com/deploy), a distributed system that runs JavaScript, TypeScript, and WebAssembly at the edge, worldwide.

This guide includes instructions for running your Astro site on your own server with Deno, and deploying to Deno Deploy through GitHub Actions or the Deno Deploy CLI.

## Requirements

[Section titled “Requirements”](#requirements)

This guide assumes you already have [Deno](https://deno.com/) installed.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed as a static site, or as an on-demand rendered site.

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site with Deno, or to Deno Deploy.

### Adapter for on-demand rendering

[Section titled “Adapter for on-demand rendering”](#adapter-for-on-demand-rendering)

To enable on-demand rendering in your Astro project using Deno, and to deploy on Deno Deploy:

1.  Install [the `@deno/astro-adapter` adapter](https://github.com/denoland/deno-astro-adapter) to your project’s dependencies using your preferred package manager:
    
    *   [npm](#tab-panel-1558)
    *   [pnpm](#tab-panel-1559)
    *   [Yarn](#tab-panel-1560)
    
    ```
    npm install @deno/astro-adapter
    ```
    
2.  Update your `astro.config.mjs` project configuration file with the changes below.
    
    ```
    import { defineConfig } from 'astro/config';import deno from '@deno/astro-adapter';
    export default defineConfig({  output: 'server',  adapter: deno(),});
    ```
    
3.  Update your `preview` script in `package.json` with the change below.
    
    ```
    {  // ...  "scripts": {    "dev": "astro dev",    "start": "astro dev",    "build": "astro build",    "preview": "astro preview"    "preview": "deno run --allow-net --allow-read --allow-env ./dist/server/entry.mjs"  }}
    ```
    
    You can now use this command to preview your production Astro site locally with Deno.
    
    *   [npm](#tab-panel-1561)
    *   [pnpm](#tab-panel-1562)
    *   [Yarn](#tab-panel-1563)
    
    ```
    npm run preview
    ```
    

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can run your Astro site on your own server, or deploy to Deno Deploy through GitHub Actions or using Deno Deploy’s CLI (command line interface).

### On your own server

[Section titled “On your own server”](#on-your-own-server)

1.  Copy your project onto your server.
    
2.  Install the project dependencies using your preferred package manager:
    
    *   [npm](#tab-panel-1564)
    *   [pnpm](#tab-panel-1565)
    *   [Yarn](#tab-panel-1566)
    
    ```
    npm install
    ```
    
3.  Build your Astro site with your preferred package manager:
    
    *   [npm](#tab-panel-1567)
    *   [pnpm](#tab-panel-1568)
    *   [Yarn](#tab-panel-1569)
    
    ```
    npm run build
    ```
    
4.  Start your application with the following command:
    
    *   [Static](#tab-panel-1550)
    *   [On demand](#tab-panel-1551)
    
    ```
    deno run -A jsr:@std/http/file-server dist
    ```
    

### GitHub Actions Deployment

[Section titled “GitHub Actions Deployment”](#github-actions-deployment)

If your project is stored on GitHub, the [Deno Deploy website](https://dash.deno.com/) will guide you through setting up GitHub Actions to deploy your Astro site.

1.  Push your code to a public or private GitHub repository.
    
2.  Sign in on [Deno Deploy](https://dash.deno.com/) with your GitHub account, and click on [New Project](https://dash.deno.com).
    
3.  Select your repository, the branch you want to deploy from, and select **GitHub Action** mode. (Your Astro site requires a build step, and cannot use Automatic mode.)
    
4.  In your Astro project, create a new file at `.github/workflows/deploy.yml` and paste in the YAML below. This is similar to the YAML given by Deno Deploy, with the additional steps needed for your Astro site.
    
    *   [Static](#tab-panel-1552)
    *   [On demand](#tab-panel-1553)
    
    ```
    name: Deployon: [push]
    jobs:  deploy:    name: Deploy    runs-on: ubuntu-latest    permissions:      id-token: write # Needed for auth with Deno Deploy      contents: read # Needed to clone the repository
        steps:      - name: Clone repository        uses: actions/checkout@v6
          # Not using npm? Change `npm ci` to `yarn install` or `pnpm i`      - name: Install dependencies        run: npm ci
          # Not using npm? Change `npm run build` to `yarn build` or `pnpm run build`      - name: Build Astro        run: npm run build
          - name: Upload to Deno Deploy        uses: denoland/deployctl@v1        with:          project: my-deno-project # TODO: replace with Deno Deploy project name          entrypoint: jsr:@std/http/file-server          root: dist
    ```
    
5.  After committing this YAML file, and pushing to GitHub on your configured deploy branch, the deploy should begin automatically!
    
    You can track the progress using the “Actions” tab on your GitHub repository page, or on [Deno Deploy](https://dash.deno.com).
    

### CLI Deployment

[Section titled “CLI Deployment”](#cli-deployment)

1.  Install the [Deno Deploy CLI](https://docs.deno.com/deploy/manual/deployctl).
    
    ```
    deno install -gArf jsr:@deno/deployctl
    ```
    
2.  Build your Astro site with your preferred package manager:
    
    *   [npm](#tab-panel-1570)
    *   [pnpm](#tab-panel-1571)
    *   [Yarn](#tab-panel-1572)
    
    ```
    npm run build
    ```
    
3.  Run `deployctl` to deploy!
    
    *   [Static](#tab-panel-1554)
    *   [On demand](#tab-panel-1555)
    
    ```
    cd dist && deployctl deploy jsr:@std/http/file-server
    ```
    
    You can track all your deploys on [Deno Deploy](https://dash.deno.com).
    
4.  (Optional) To simplify the build and deploy into one command, add a `deploy-deno` script in `package.json`.
    
    *   [Static](#tab-panel-1556)
    *   [On demand](#tab-panel-1557)
    
    ```
    {  // ...  "scripts": {  "dev": "astro dev",  "start": "astro dev",  "build": "astro build",  "preview": "astro preview",  "deno-deploy": "npm run build && cd dist && deployctl deploy jsr:@std/http/file-server"  }}
    ```
    
    Then you can use this command to build and deploy your Astro site in one step.
    
    ```
    npm run deno-deploy
    ```
    

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
