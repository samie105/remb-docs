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
---
# Deploy your Astro Site to Cloudflare

You can deploy full-stack applications, including front-end static assets and back-end APIs, as well as on-demand rendered sites, to [Cloudflare Workers](https://developers.cloudflare.com/workers/static-assets/).

Read more about [using the Cloudflare runtime](/en/guides/integrations-guide/cloudflare/) in your Astro project.

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
    
2.  If your site uses on-demand rendering, install the [`@astrojs/cloudflare` adapter](/en/guides/integrations-guide/cloudflare/).
    
    This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.
    
    *   [npm](#tab-panel-1547)
    *   [pnpm](#tab-panel-1548)
    *   [Yarn](#tab-panel-1549)
    
    ```
    npx astro add cloudflare
    ```
    
    Read more about [on-demand rendering in Astro](/en/guides/on-demand-rendering/).
    
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

Read more about using [Cloudflare runtime APIs](/en/guides/integrations-guide/cloudflare/) such as bindings.

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

If you are building a project that is using on-demand rendering with [the Cloudflare adapter](/en/guides/integrations-guide/cloudflare/) and the server fails to build with an error message such as `[Error] Could not resolve "XXXX. The package "XXXX" wasn't found on the file system but is built into node.`:

*   This means that a package or import you are using in the server-side environment is not compatible with the [Cloudflare runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/).
    
*   If you are directly importing a Node.js runtime API, please refer to the Astro documentation on Cloudflare’s [Node.js compatibility](/en/guides/integrations-guide/cloudflare/#nodejs-compatibility) for further steps on how to resolve this.
    
*   If you are importing a package that imports a Node.js runtime API, check with the author of the package to see if they support the `node:*` import syntax. If they do not, you may need to find an alternative package.
    

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
