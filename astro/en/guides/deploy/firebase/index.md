---
title: "Deploy your Astro Site to Google’s Firebase Hosting"
source: "https://docs.astro.build/en/guides/deploy/firebase/"
canonical_url: "https://docs.astro.build/en/guides/deploy/firebase/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:02.358Z"
content_hash: "4b8dd75466af5d905efa90e211d12bcecf5906a8b850663953b80b9d47303a2b"
menu_path: ["Deploy your Astro Site to Google’s Firebase Hosting"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/edgeone-pages/index.md", "title": "Deploy your Astro Site to EdgeOne Pages"}
nav_next: {"path": "astro/en/guides/deploy/fleek/index.md", "title": "Deploy your Astro Site to Fleek"}
---

# Deploy your Astro Site to Google’s Firebase Hosting

[Firebase Hosting](https://firebase.google.com/products/hosting) is a service provided by Google’s [Firebase](https://firebase.google.com/) app development platform, which can be used to deploy an Astro site.

See our separate guide for [adding Firebase backend services](../../backend/firebase/index.md) such as databases, authentication, and storage.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Firebase as a static site, or as a server-side rendered site (SSR).

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Firebase.

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable SSR in your Astro project and deploy on Firebase add the [Node.js adapter](../../integrations-guide/node/index.md).

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1.  Install the [Firebase CLI](https://github.com/firebase/firebase-tools). This is a command-line tool that allows you to interact with Firebase from the terminal.
    
    *   [npm](#tab-panel-1573)
    *   [pnpm](#tab-panel-1574)
    *   [Yarn](#tab-panel-1575)
    
    ```
    npm install firebase-tools
    ```
    
2.  Authenticate the Firebase CLI with your Google account. This will open a browser window where you can log in to your Google account.
    
    *   [npm](#tab-panel-1576)
    *   [pnpm](#tab-panel-1577)
    *   [Yarn](#tab-panel-1578)
    
    ```
    npx firebase login
    ```
    
3.  Enable experimental web frameworks support. This is an experimental feature that allows the Firebase CLI to detect and configure your deployment settings for Astro.
    
    *   [npm](#tab-panel-1579)
    *   [pnpm](#tab-panel-1580)
    *   [Yarn](#tab-panel-1581)
    
    ```
    npx firebase experiments:enable webframeworks
    ```
    
4.  Initialize Firebase Hosting in your project. This will create a `firebase.json` and `.firebaserc` file in your project root.
    
    *   [npm](#tab-panel-1582)
    *   [pnpm](#tab-panel-1583)
    *   [Yarn](#tab-panel-1584)
    
    ```
    npx firebase init hosting
    ```
    
5.  Deploy your site to Firebase Hosting. This will build your Astro site and deploy it to Firebase.
    
    *   [npm](#tab-panel-1585)
    *   [pnpm](#tab-panel-1586)
    *   [Yarn](#tab-panel-1587)
    
    ```
    npx firebase deploy --only hosting
    ```
    

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
    
    ### [Firebase](index.md)
    
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
