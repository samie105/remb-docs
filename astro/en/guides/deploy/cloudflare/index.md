---
title: "Deploy your Astro Site to Cloudflare"
source: "https://docs.astro.build/en/guides/deploy/cloudflare/"
canonical_url: "https://docs.astro.build/en/guides/deploy/cloudflare/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:41.475Z"
content_hash: "e99cdff5ff1b345199b1bbc670b3579f0e95d33f37b43ae2b342cf175e7eaa99"
menu_path: ["Deploy your Astro Site to Cloudflare"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/clever-cloud/index.md", "title": "Deploy your Astro Site to Clever Cloud"}
nav_next: {"path": "astro/en/guides/deploy/cloudray/index.md", "title": "Deploy your Astro Site with CloudRay"}
---

# Deploy your Astro Site to Cloudflare

You can deploy full-stack applications, including front-end static assets and back-end APIs, as well as on-demand rendered sites, to [Cloudflare Workers](https://developers.cloudflare.com/workers/static-assets/).

Read more about [using the Cloudflare runtime](../../integrations-guide/cloudflare/index.md) in your Astro project.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

*   A Cloudflare account. If you don’t already have one, you can create a free Cloudflare account during the process.

## Cloudflare Workers

[Section titled “Cloudflare Workers”](#cloudflare-workers)

### How to deploy with Wrangler

[Section titled “How to deploy with Wrangler”](#how-to-deploy-with-wrangler)

1.  Install [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/get-started/).
    
    ```
    npm install wrangler@latest --save-dev
    ```
    
2.  If your site uses on-demand rendering, install the [`@astrojs/cloudflare` adapter](../../integrations-guide/cloudflare/index.md).
    
    This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.
    
    *   [npm](#tab-panel-1547)
    *   [pnpm](#tab-panel-1548)
    *   [Yarn](#tab-panel-1549)
    
    ```
    npx astro add cloudflare
    ```
    
    Read more about [on-demand rendering in Astro](../../on-demand-rendering/index.md).
    
3.  Create a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).
    
    Running `astro add cloudflare` will create this for you; if you are not using the adapter, you’ll need to create it yourself.
    
    *   [Static](#tab-panel-1545)
    *   [On demand](#tab-panel-1546)
    
    ```
    {  "name": "my-astro-app",  "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy  "assets": {    "directory": "./dist",  }}
    ```
    
4.  Preview your project locally with Wrangler.
    
    ```
    npx astro build && npx wrangler dev
    ```
    
5.  Deploy using `npx wrangler deploy`.
    
    ```
    npx astro build && npx wrangler deploy
    ```
    

After your assets are uploaded, Wrangler will give you a preview URL to inspect your site.

Read more about using [Cloudflare runtime APIs](../../integrations-guide/cloudflare/index.md) such as bindings.

### How to deploy with CI/CD

[Section titled “How to deploy with CI/CD”](#how-to-deploy-with-cicd)

You can also use a CI/CD system such as [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) to automatically build and deploy your site on push.

If you’re using Workers Builds:

1.  Follow Steps 1-3 from the Wrangler section above.
    
2.  Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/) and navigate to `Compute > Workers & Pages`. Select `Create application`.
    
3.  Under `Import a repository`, select a Git account and then the repository containing your Astro project.
    
4.  Configure your project with:
    
    *   Build command: `npx astro build`
    *   Deploy command: `npx wrangler deploy`
5.  Click `Save and Deploy`. You can now preview your Worker at its provided `workers.dev` subdomain.
    

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### 404 behavior

[Section titled “404 behavior”](#404-behavior)

For Workers projects, you will need to set `not_found_handling` if you want to serve a custom 404 page. You can read more about this in the [Routing behavior section](https://developers.cloudflare.com/workers/static-assets/#routing-behavior) of Cloudflare’s documentation.

```
{  "assets": {    "directory": "./dist",    "not_found_handling": "404-page"  }}
```

### Client-side hydration

[Section titled “Client-side hydration”](#client-side-hydration)

Client-side hydration may fail as a result of Cloudflare’s Auto Minify setting. If you see `Hydration completed but contains mismatches` in the console, make sure to disable Auto Minify under Cloudflare settings.

### Node.js runtime APIs

[Section titled “Node.js runtime APIs”](#nodejs-runtime-apis)

If you are building a project that is using on-demand rendering with [the Cloudflare adapter](../../integrations-guide/cloudflare/index.md) and the server fails to build with an error message such as `[Error] Could not resolve "XXXX. The package "XXXX" wasn't found on the file system but is built into node.`:

*   This means that a package or import you are using in the server-side environment is not compatible with the [Cloudflare runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/).
    
*   If you are directly importing a Node.js runtime API, please refer to the Astro documentation on Cloudflare’s [Node.js compatibility](../../integrations-guide/cloudflare/index.md#nodejs-compatibility) for further steps on how to resolve this.
    
*   If you are importing a package that imports a Node.js runtime API, check with the author of the package to see if they support the `node:*` import syntax. If they do not, you may need to find an alternative package.
    

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
    
    ### [Cloudflare](index.md)
    
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
