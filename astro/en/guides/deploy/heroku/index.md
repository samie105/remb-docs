---
title: "Deploy your Astro Site to Heroku"
source: "https://docs.astro.build/en/guides/deploy/heroku/"
canonical_url: "https://docs.astro.build/en/guides/deploy/heroku/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:24.502Z"
content_hash: "3aa5a03452ee8797fd4957f5178809bb9d8e27df8466ee080c589610122dd0cf"
menu_path: ["Deploy your Astro Site to Heroku"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/google-cloud/index.md", "title": "Deploy your Astro Site to Google Cloud"}
nav_next: {"path": "astro/en/guides/deploy/juno/index.md", "title": "Deploy your Astro Site to Juno"}
---

# Deploy your Astro Site to Heroku

[Heroku](https://www.heroku.com/) is a platform-as-a-service for building, running, and managing modern apps in the cloud. You can deploy an Astro site to Heroku using this guide.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1.  Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
    
2.  Create a Heroku account by [signing up](https://signup.heroku.com/).
    
3.  Run `heroku login` and fill in your Heroku credentials:
    
    ```
    $ heroku login
    ```
    
4.  Create a file called `static.json` in the root of your project with the below content:
    
    ```
    {  "root": "./dist"}
    ```
    
    This is the configuration of your site; read more at [heroku-buildpack-static](https://github.com/heroku/heroku-buildpack-static).
    
5.  Set up your Heroku git remote:
    
    ```
    # version change$ git init$ git add .$ git commit -m "My site ready for deployment."
    # creates a new app with a specified name$ heroku apps:create example
    # set buildpack for static sites$ heroku buildpacks:set https://github.com/heroku/heroku-buildpack-static.git
    ```
    
6.  Deploy your site:
    
    ```
    # publish site$ git push heroku master
    # opens a browser to view the Dashboard version of Heroku CI$ heroku open
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
    
    ### [Heroku](index.md)
    
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
