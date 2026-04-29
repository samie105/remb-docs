---
title: "Deploy your Astro Site to GitLab Pages"
source: "https://docs.astro.build/en/guides/deploy/gitlab/"
canonical_url: "https://docs.astro.build/en/guides/deploy/gitlab/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:20.715Z"
content_hash: "c2eb808ca20c318d26a0a0f952348a015d73e98fba732d28fab9986cd943cb32"
menu_path: ["Deploy your Astro Site to GitLab Pages"]
section_path: []
nav_prev: {"path": "astro/en/guides/deploy/github/index.md", "title": "Deploy your Astro Site to GitHub Pages"}
nav_next: {"path": "astro/en/guides/deploy/google-cloud/index.md", "title": "Deploy your Astro Site to Google Cloud"}
---

# Deploy your Astro Site to GitLab Pages

You can use [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/) to host an Astro site for your [GitLab](https://about.gitlab.com/) projects, groups, or user account.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy an Astro site to GitLab Pages by using GitLab CI/CD to automatically build and deploy your site. To do this, your source code must be hosted on GitLab and you need to make the following changes to your Astro project:

1.  Set up [`site`](../../../reference/configuration-reference/index.md#site) and [`base`](../../../reference/configuration-reference/index.md#base) options in `astro.config.mjs`.
    
    ```
    import { defineConfig } from 'astro/config';
    export default defineConfig({  site: 'https://<username>.gitlab.io',  base: '/<my-repo>',  outDir: 'public',  publicDir: 'static',});
    ```
    
    `site`
    
    The value for `site` must be one of the following:
    
    *   The following URL based on your username: `https://<username>.gitlab.io`
    *   The following URL based on your group name: `https://<groupname>.gitlab.io`
    *   Your custom domain if you have it configured in your GitLab project’s settings: `https://example.com`
    
    For GitLab self-managed instances, replace `gitlab.io` with your instance’s Pages domain.
    
    `base`
    
    A value for `base` may be required so that Astro will treat your repository name (e.g. `/my-repo`) as the root of your website.
    
    The value for `base` should be your repository’s name starting with a forward slash, for example `/my-blog`. This is so that Astro understands your website’s root is `/my-repo`, rather than the default `/`.
    
2.  Rename the `public/` directory to `static/`.
    
3.  Set `outDir: 'public'` in `astro.config.mjs`. This setting instructs Astro to put the static build output in a folder called `public`, which is the folder required by GitLab Pages for exposed files.
    
    If you were using the [`public/` directory](../../../basics/project-structure/index.md#public) as a source of static files in your Astro project, rename it and use that new folder name in `astro.config.mjs` for the value of `publicDir`.
    
    For example, here are the correct `astro.config.mjs` settings when the `public/` directory is renamed to `static/`:
    
    ```
    import { defineConfig } from 'astro/config';
    export default defineConfig({  outDir: 'public',  publicDir: 'static',});
    ```
    
4.  Change the build output in `.gitignore`. In our example we need to change `dist/` to `public/`:
    
    ```
    # build outputdist/public/
    ```
    
5.  Create a file called `.gitlab-ci.yml` in the root of your project with the content below. This will build and deploy your site whenever you make changes to your content:
    
    ```
    pages:  # The Docker image that will be used to build your app  image: node:lts
      before_script:    - npm ci
      script:    # Specify the steps involved to build your app here    - npm run build
      artifacts:    paths:      # The folder that contains the built files to be published.      # This must be called "public".      - public
      only:    # Trigger a new build and deploy only when there is a push to the    # branch(es) below    - main
    ```
    
6.  Commit your changes and push them to GitLab.
    
7.  On GitLab, go to your repository’s **Deploy** menu and select **Pages**. Here you will see the full URL of your GitLab Pages website. To make sure you are using the URL format `https://username.gitlab.io/my-repo`, uncheck the **Use unique domain** setting on this page.
    

Your site should now be published! When you push changes to your Astro project’s repository, the GitLab CI/CD pipeline will automatically deploy them for you.

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
    
    ### [GitLab Pages](index.md)
    
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
