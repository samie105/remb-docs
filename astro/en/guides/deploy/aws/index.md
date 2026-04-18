---
title: "Deploy your Astro Site to AWS"
source: "https://docs.astro.build/en/guides/deploy/aws/"
canonical_url: "https://docs.astro.build/en/guides/deploy/aws/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:27.968Z"
content_hash: "cd5ee1929c4f25f06e930b0bc7d65622cfdb20d3c06f409daa18fb05e649a894"
menu_path: ["Deploy your Astro Site to AWS"]
section_path: []
---
# Deploy your Astro Site to AWS

[AWS](https://aws.amazon.com/) is a full-featured web app hosting platform that can be used to deploy an Astro site.

Deploying your project to AWS requires using the [AWS console](https://aws.amazon.com/console/). (Most of these actions can also be done using the [AWS CLI](https://aws.amazon.com/cli/)). This guide will walk you through the steps to deploy your site to AWS using [AWS Amplify](https://aws.amazon.com/amplify/), [S3 static website hosting](https://aws.amazon.com/s3/), and [CloudFront](https://aws.amazon.com/cloudfront/).

## AWS Amplify

[Section titled “AWS Amplify”](#aws-amplify)

AWS Amplify is a set of purpose-built tools and features that lets frontend web and mobile developers quickly and easily build full-stack applications on AWS. You can either deploy your Astro project as a static site, or as a server-rendered site.

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default.

1.  Create a new Amplify Hosting project.
    
2.  Connect your repository to Amplify.
    
3.  Modify your build settings to match your project’s build process.
    
    *   [npm](#tab-panel-1530)
    *   [pnpm](#tab-panel-1531)
    *   [Yarn](#tab-panel-1532)
    
    ```
    version: 1frontend:  phases:    preBuild:      commands:        - npm ci    build:      commands:        - npm run build  artifacts:    baseDirectory: /dist    files:      - '**/*'  cache:    paths:      - node_modules/**/*
    ```
    

Amplify will automatically deploy your website and update it when you push a commit to your repository.

### Adapter for on-demand rendering

[Section titled “Adapter for on-demand rendering”](#adapter-for-on-demand-rendering)

In order to deploy your project as a server-rendered site, you will need to use the third-party, [community-maintained AWS Amplify adapter](https://github.com/alexnguyennz/astro-aws-amplify) and make some changes to your config.

First, install the Amplify adapter.

*   [npm](#tab-panel-1533)
*   [pnpm](#tab-panel-1534)
*   [Yarn](#tab-panel-1535)

```
npm install astro-aws-amplify
```

Then, in your `astro.config.*` file, add the adapter and set the output to `server`.

```
import { defineConfig } from 'astro/config';import awsAmplify from 'astro-aws-amplify';
export default defineConfig({  // ...  output: "server",  adapter: awsAmplify(),});
```

Once the adapter has been installed, you can set up your Amplify project.

1.  Create a new Amplify Hosting project.
    
2.  Connect your repository to Amplify.
    
3.  Modify your build settings to match the adapter’s build process by either editing the build settings in the AWS console, or by adding an `amplify.yaml` in the root of your project.
    
    *   [npm](#tab-panel-1536)
    *   [pnpm](#tab-panel-1537)
    *   [Yarn](#tab-panel-1538)
    
    ```
    version: 1frontend:  phases:    preBuild:      commands:        - npm ci --cache .npm --prefer-offline    build:      commands:        - npm run build        - mv node_modules ./.amplify-hosting/compute/default  artifacts:    baseDirectory: .amplify-hosting    files:      - '**/*'  cache:    paths:      - .npm/**/*
    ```
    

Amplify will automatically deploy your website and update it when you push a commit to your repository.

See [AWS’s Astro deployment guide](https://docs.aws.amazon.com/amplify/latest/userguide/get-started-astro.html) for more info.

## S3 static website hosting

[Section titled “S3 static website hosting”](#s3-static-website-hosting)

S3 is the starting point of any application. It is where your project files and other assets are stored. S3 charges for file storage and number of requests. You can find more information about S3 in the [AWS documentation](https://aws.amazon.com/s3/).

1.  Create an S3 bucket with your project’s name.
    
2.  Disable **“Block all public access”**. By default, AWS sets all buckets to be private. To make it public, you need to uncheck the “Block public access” checkbox in the bucket’s properties.
    
3.  Upload your built files located in `dist` to S3. You can do this manually in the console or use the AWS CLI. If you use the AWS CLI, use the following command after [authenticating with your AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html):
    
    ```
    aws s3 cp dist/ s3://<BUCKET_NAME>/ --recursive
    ```
    
4.  Update your bucket policy to allow public access. You can find this setting in the bucket’s **Permissions > Bucket policy**.
    
    ```
    {  "Version": "2012-10-17",  "Statement": [    {      "Sid": "PublicReadGetObject",      "Effect": "Allow",      "Principal": "*",      "Action": "s3:GetObject",      "Resource": "arn:aws:s3:::<BUCKET_NAME>/*"    }  ]}
    ```
    
5.  Enable website hosting for your bucket. You can find this setting in the bucket’s **Properties > Static website hosting**. Set your index document to `index.html` and your error document to `404.html`. Finally, you can find your new website URL in the bucket’s **Properties > Static website hosting**.
    

## S3 with CloudFront

[Section titled “S3 with CloudFront”](#s3-with-cloudfront)

CloudFront is a web service that provides content delivery network (CDN) capabilities. It is used to cache content of a web server and distribute it to end users. CloudFront charges for the amount of data transferred. Adding CloudFront to your S3 bucket is more cost-effective and provides a faster delivery.

To connect S3 with CloudFront, create a CloudFront distribution with the following values:

*   **Origin domain:** Your S3 bucket static website endpoint. You can find your endpoint in your S3 bucket’s **Properties > Static website hosting**. Alternative, you can select your s3 bucket and click on the callout to replace your bucket address with your bucket static endpoint.
*   **Viewer protocol policy:** “Redirect to HTTPS”

This configuration will serve your site using the CloudFront CDN network. You can find your CloudFront distribution URL in the bucket’s **Distributions > Domain name**.

## Continuous deployment with GitHub Actions

[Section titled “Continuous deployment with GitHub Actions”](#continuous-deployment-with-github-actions)

There are many ways to set up continuous deployment for AWS. One possibility for code hosted on GitHub is to use [GitHub Actions](https://github.com/features/actions) to deploy your website every time you push a commit.

1.  Create a new policy in your AWS account using [IAM](https://aws.amazon.com/iam/) with the following permissions. This policy will allow you to upload built files to your S3 bucket and invalidate the CloudFront distribution files when you push a commit.
    
    ```
    {  "Version": "2012-10-17",  "Statement": [      {          "Sid": "VisualEditor0",          "Effect": "Allow",          "Action": [              "s3:PutObject",              "s3:ListBucket",              "s3:DeleteObject",              "cloudfront:CreateInvalidation"          ],          "Resource": [              "<DISTRIBUTION_ARN>",              "arn:aws:s3:::<BUCKET_NAME>/*",              "arn:aws:s3:::<BUCKET_NAME>"          ]      }  ]}
    ```
    
2.  Create a new IAM user and attach the policy to the user. This will provide your `AWS_SECRET_ACCESS_KEY` and `AWS_ACCESS_KEY_ID`.
    
3.  Add this sample workflow to your repository at `.github/workflows/deploy.yml` and push it to GitHub. You will need to add `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `BUCKET_ID`, and `DISTRIBUTION_ID` as “secrets” to your repository on GitHub under **Settings** > **Secrets** > **Actions**. Click New repository secret to add each one.
    
    ```
    name: Deploy Website
    on:  push:    branches:      - main
    jobs:  deploy:    runs-on: ubuntu-latest    steps:      - name: Checkout        uses: actions/checkout@v6      - name: Configure AWS Credentials        uses: aws-actions/configure-aws-credentials@v1        with:          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}          aws-region: us-east-1      - name: Install modules        run: npm ci      - name: Build application        run: npm run build      - name: Deploy to S3        run: aws s3 sync --delete ./dist/ s3://${{ secrets.BUCKET_ID }}      - name: Create CloudFront invalidation        run: aws cloudfront create-invalidation --distribution-id ${{ secrets.DISTRIBUTION_ID }} --paths "/*"
    ```
    

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [Deploy Astro to AWS Amplify](https://www.launchfa.st/blog/deploy-astro-aws-amplify)
*   [Deploy Astro to AWS Elastic Beanstalk](https://www.launchfa.st/blog/deploy-astro-aws-elastic-beanstalk)
*   [Deploy Astro to Amazon ECS on AWS Fargate](https://www.launchfa.st/blog/deploy-astro-aws-fargate)
*   [Troubleshooting SSR Amplify Deployments](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-ssr-deployment.html)

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
