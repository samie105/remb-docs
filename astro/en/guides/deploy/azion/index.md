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
    
    ### [AWS](../aws/index.md)
    
*   ![](/logos/flightcontrol.svg)
    
    ### [AWS via Flightcontrol](../aws-via-flightcontrol/index.md)
    
*   ![](/logos/sst.svg)
    
    ### [AWS via SST](../aws-via-sst/index.md)
    
*   ![](/logos/azion.svg)
    
    ### [Azion](index.md)
    
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
    
    ### [Zephyr Cloud](../zephyr/index.md)
    
*   ![](/logos/zerops.svg)
    
    ### [Zerops](../zerops/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
