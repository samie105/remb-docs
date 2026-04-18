---
title: "Deploy your Astro Site to Fly.io"
source: "https://docs.astro.build/en/guides/deploy/flyio/"
canonical_url: "https://docs.astro.build/en/guides/deploy/flyio/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:05.883Z"
content_hash: "20854a16a03259fc0a6191932922e014f4a15ffbda160438a008c12e5bb387db"
menu_path: ["Deploy your Astro Site to Fly.io"]
section_path: []
---
# Deploy your Astro Site to Fly.io

You can deploy your Astro project to [Fly.io](https://fly.io/), a platform for running full stack apps and databases close to your users.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Fly.io as a static site, or as a server-side rendered site (SSR).

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Fly.io.

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable on-demand rendering in your Astro project and deploy on Fly.io, add [the Node.js adapter](/en/guides/integrations-guide/node/).

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1.  [Sign up for Fly.io](https://fly.io/docs/getting-started/log-in-to-fly/#first-time-or-no-fly-account-sign-up-for-fly) if you haven’t already.
    
2.  [Install `flyctl`](https://fly.io/docs/hands-on/install-flyctl/), your Fly.io app command center.
    
3.  Run the following command in your terminal.
    
    ```
    fly launch
    ```
    
    `flyctl` will automatically detect Astro, configure the correct settings, build your image, and deploy it to the Fly.io platform.
    

## Generating your Astro Dockerfile

[Section titled “Generating your Astro Dockerfile”](#generating-your-astro-dockerfile)

If you don’t already have a Dockerfile, `fly launch` will generate one for you, as well as prepare a `fly.toml` file. For pages rendered on demand, this Dockerfile will include the appropriate start command and environment variables.

You can instead create your own Dockerfile using [Dockerfile generator](https://www.npmjs.com/package/@flydotio/dockerfile) and then run using the command `npx dockerfile` for Node applications or `bunx dockerfile` for Bun applications.

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   Check out [the official Fly.io docs](https://fly.io/docs/js/frameworks/astro/)

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
