---
title: "Deploy your Astro Site to Juno"
source: "https://docs.astro.build/en/guides/deploy/juno/"
canonical_url: "https://docs.astro.build/en/guides/deploy/juno/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:30.561Z"
content_hash: "daba77141eb368fd85aa95da49651b0c1c41f832ecf2c47f4c33199a653db703"
menu_path: ["Deploy your Astro Site to Juno"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/heroku/index.md", "title": "Deploy your Astro Site to Heroku"}
nav_next: {"path": "astro/en/guides/deploy/microsoft-azure/index.md", "title": "Deploy your Astro Site to Microsoft Azure"}
---

# Deploy your Astro Site to Juno

[Juno](https://juno.build) is an open-source serverless platform for hosting static websites, building web applications, and running serverless functions with the privacy and control of self-hosting.

## Create your container

[Section titled “Create your container”](#create-your-container)

1.  Log in to the [Juno Console](https://console.juno.build).
    
2.  Click the **Launch a new satellite** button (the container for your project) from the launchpad
    
3.  Enter a **name** and select **Website**
    
4.  Confirm with **Create a Satellite**
    
5.  The platform will then provision its resources.
    
6.  Once the process is complete, click Continue to access the overview page.
    

## Configure your project

[Section titled “Configure your project”](#configure-your-project)

Your Astro project can be deployed to Juno as a static site.

Create a `juno.config.mjs` file at the root of your project, and replace the `PROD_SATELLITE_ID` with the ID of the Satellite you created earlier.

```
import { defineConfig } from '@junobuild/config';
/** @type {import('@junobuild/config').JunoConfig} */export default defineConfig({  satellite: {    ids: {      production: '<PROD_SATELLITE_ID>'    },    source: 'dist',    predeploy: ['npm run build']  }});
```

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy using either GitHub Actions or CLI (command line interface).

### GitHub Actions deployment

[Section titled “GitHub Actions deployment”](#github-actions-deployment)

1.  From your Satellite’s overview, navigate to the **Setup** tab.
    
2.  Click on **Add an access key**.
    
3.  Generate a new key with the default option. Click **Submit**.
    
4.  Upon successful creation, a **Secret token** will be displayed. Copy the value and save it as an [encrypted secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets) in your GitHub repository or organization, using the key `JUNO_TOKEN`.
    
5.  Create a `deploy.yml` file in the `.github/workflows` subfolder of your repo.
    
6.  Add the following workflow configuration:
    
    ```
    name: Deploy to Juno
    on:  workflow_dispatch:  push:    branches: [main]
    jobs:  deploy:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v6
          - uses: actions/setup-node@v6        with:          node-version: 24          registry-url: "https://registry.npmjs.org"
          - name: Install Dependencies        run: npm ci
          - name: Deploy to Juno        uses: junobuild/juno-action@main        with:          args: hosting deploy        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
    ```
    

### CLI deployment

[Section titled “CLI deployment”](#cli-deployment)

1.  Install the CLI
    
    *   [npm](#tab-panel-1588)
    *   [pnpm](#tab-panel-1589)
    *   [Yarn](#tab-panel-1590)
    
    ```
    npm i -g @junobuild/cli
    ```
    
2.  Authenticate the CLI. This will open the Juno Console.
    
    ```
    juno login
    ```
    
3.  In the browser window, click **Authorize** to grant permission.
    
4.  Deploy your site:
    
    ```
    juno hosting deploy
    ```
    

## Guides

[Section titled “Guides”](#guides)

*   [Use Juno with Astro](https://juno.build/docs/guides/astro)
*   [Deployment with GitHub Actions](https://juno.build/docs/category/deployment)
*   [Manual Deployment](https://juno.build/docs/guides/manual-deployment)

## Examples

[Section titled “Examples”](#examples)

Quickly scaffold a website with a ready-made Astro template.

*   [npm](#tab-panel-1591)
*   [pnpm](#tab-panel-1592)
*   [Yarn](#tab-panel-1593)

```
npm create juno@latest -- --template astro-starter
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

