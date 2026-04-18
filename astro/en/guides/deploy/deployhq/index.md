---
title: "Deploy your Astro Site with DeployHQ"
source: "https://docs.astro.build/en/guides/deploy/deployhq/"
canonical_url: "https://docs.astro.build/en/guides/deploy/deployhq/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:51.635Z"
content_hash: "9d8b0bff61f965805811cadd5208baa8fdad3f4d9c4aa65acc90d5607f06ba40"
menu_path: ["Deploy your Astro Site with DeployHQ"]
section_path: []
---
# Deploy your Astro Site with DeployHQ

You can deploy your Astro project to your own servers using [DeployHQ](https://www.deployhq.com/), a deployment automation platform that builds your code and pushes it to SSH/SFTP servers, FTP servers, cloud storage (e.g. Amazon S3, Cloudflare R2), and modern hosting platforms (e.g. Netlify, Heroku).

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1.  If you do not already have one, sign up for a [DeployHQ account](https://www.deployhq.com/).
    
2.  From the DeployHQ web interface, create a new project and connect the Git repository for your Astro project (GitHub, GitLab, Bitbucket, or any private repository). You will also need to authorize DeployHQ to access your repository.
    
3.  Add a server and enter your server details:
    
    *   Give your server a name.
    *   Select your protocol (SSH/SFTP, FTP, or cloud platform).
    *   Enter your server hostname, username, and password/SSH key.
    *   Set **Deployment Path** to your web root (e.g. `public_html/`).
4.  In your project settings, navigate to **Build Pipeline** and add your build commands:
    
    ```
    npm installnpm run build
    ```
    
5.  Click **Deploy Project**, then select your server and click **Deploy** to start your first deployment.
    

Your Astro site will be built and deployed to your server. You can enable automatic deployments to deploy on every Git push, or schedule deployments for specific times.

See [DeployHQ’s documentation](https://www.deployhq.com/support) for more info on advanced deployment features.

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
