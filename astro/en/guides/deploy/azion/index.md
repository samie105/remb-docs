---
title: "Deploy your Astro Site to Azion"
source: "https://docs.astro.build/en/guides/deploy/azion/"
canonical_url: "https://docs.astro.build/en/guides/deploy/azion/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:24.150Z"
content_hash: "2e3729c8060a57ba111568a6b7495c1240d46f6941923afa3bb7cfd0a530f4f5"
menu_path: ["Deploy your Astro Site to Azion"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/aws-via-sst/index.md", "title": "Deploy your Astro Site to AWS with SST"}
nav_next: {"path": "astro/en/guides/deploy/buddy/index.md", "title": "Deploy your Astro Site with Buddy"}
---

# Deploy your Astro Site to Azion

You can deploy your Astro project on [Azion](https://console.azion.com/), a platform for frontend developers to collaborate and deploy static (JAMstack) and SSR websites.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

*   An [Azion account](https://www.azion.com/). If you don’t have one, you can sign up for a free account.
*   Your app code stored in a [GitHub](https://github.com/) repository.
*   [Azion CLI](https://www.azion.com/en/documentation/products/azion-cli/overview/) installed for faster project setup and deployment.

## How to Deploy through Azion Console Dashboard

[Section titled “How to Deploy through Azion Console Dashboard”](#how-to-deploy-through-azion-console-dashboard)

To start building, follow these steps:

1.  Access [Azion Console](https://console.azion.com).
2.  On the homepage, click the **\+ Create** button.
    *   This opens a modal with the options to create new applications and resources.
3.  Select the **Import from GitHub** option and click the card.
    *   This action opens the settings page.
4.  Connect your Azion account with GitHub.
    *   A pop-up window will appear asking for authorization.
5.  Select the repository you want to import from GitHub.
6.  Configure the build settings:
    *   **Framework preset:** Select the appropriate framework (e.g., `Astro`).
    *   **Root Directory:** This refers to the directory in which your code is located. Your code must be located at the root directory, not a subdirectory. A ./ symbol appears in this field, indicating it’s a root directory.
    *   **Install Command:** the command that compiles your settings to build for production. Build commands are executed through scripts. For example: npm run build or npm install for an NPM package.
7.  Click **Save and Deploy**.
8.  Monitor the deployment using **Azion Real-Time Metrics** and verify your site is live on the edge.

## How to Deploy a Static Site Using the Azion CLI

[Section titled “How to Deploy a Static Site Using the Azion CLI”](#how-to-deploy-a-static-site-using-the-azion-cli)

1.  **Install the Azion CLI:**
    
    *   Download and install the [Azion CLI](https://www.azion.com/en/documentation/products/azion-cli/overview/) for easier management and deployment.
2.  **Authenticate the CLI:**
    
    *   Run the following command to authenticate your CLI with your Azion account.
    
    ```
    azion login
    ```
    
3.  **Set Up Your Application:**
    
    *   Use the following commands to initialize and configure your project:
    
    ```
    azion init
    ```
    
4.  **Build Your Astro Project:**
    
    *   Run your build command locally:
    
    ```
    azion build
    ```
    
5.  **Deploy Your Static Files:**
    
    *   Deploy your static files using the Azion CLI:
    
    ```
    azion deploy
    ```
    

This guide provides an overview of deploying static applications.

## Enabling Local Development Using Azion CLI

[Section titled “Enabling Local Development Using Azion CLI”](#enabling-local-development-using-azion-cli)

For the preview to work, you must execute the following command:

```
azion dev
```

Once you’ve initialized the local development server, the application goes through the `build` process.

```
Building your Edge Application. This process may take a few minutesRunning build step command:...
```

Then, when the build is complete, the access to the application is prompted:

```
[Azion Bundler] [Server] › ✔  success   Function running on port http://localhost:3000
```

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Node.js runtime APIs

[Section titled “Node.js runtime APIs”](#nodejs-runtime-apis)

A project using an NPM package fails to build with an error message such as `[Error] Could not resolve "XXXX. The package "XXXX" wasn't found on the file system but is built into node.`:

This means that a package or import you are using is not compatible with Azion’s runtime APIs.

If you are directly importing a Node.js runtime API, please refer to the [Azion Node.js compatibility](https://www.azion.com/en/documentation/products/azion-edge-runtime/compatibility/node/) for further steps on how to resolve this.

If you are importing a package that imports a Node.js runtime API, check with the author of the package to see if they support the `node:*` import syntax. If they do not, you may need to find an alternative package.

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


