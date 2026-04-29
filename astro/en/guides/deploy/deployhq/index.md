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
nav_prev: {"path": "astro/en/guides/deploy/deno/index.md", "title": "Deploy your Astro Site with Deno"}
nav_next: {"path": "astro/en/guides/deploy/edgeone-pages/index.md", "title": "Deploy your Astro Site to EdgeOne Pages"}
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
    
    ### [DeployHQ](index.md)
    
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
