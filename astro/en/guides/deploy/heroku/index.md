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
