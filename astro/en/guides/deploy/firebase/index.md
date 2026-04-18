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
---
# Deploy your Astro Site to Google’s Firebase Hosting

[Firebase Hosting](https://firebase.google.com/products/hosting) is a service provided by Google’s [Firebase](https://firebase.google.com/) app development platform, which can be used to deploy an Astro site.

See our separate guide for [adding Firebase backend services](/en/guides/backend/firebase/) such as databases, authentication, and storage.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Firebase as a static site, or as a server-side rendered site (SSR).

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Firebase.

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable SSR in your Astro project and deploy on Firebase add the [Node.js adapter](/en/guides/integrations-guide/node/).

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
