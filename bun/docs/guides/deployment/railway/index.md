---
title: "Deploy a Bun application on Railway"
source: "https://bun.com/docs/guides/deployment/railway"
canonical_url: "https://bun.com/docs/guides/deployment/railway"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:00.577Z"
content_hash: "d7f01363185b3f82ba6d0362719fa259564a6ffab2be8029c1e75e59a2674cc4"
menu_path: ["Deploy a Bun application on Railway"]
section_path: []
---
[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

Railway is an infrastructure platform where you can provision infrastructure, develop with that infrastructure locally, and then deploy to the cloud. It enables instant deployments from GitHub with zero configuration, automatic SSL, and built-in database provisioning. This guide walks through deploying a Bun application with a PostgreSQL database (optional), which is exactly what the template below provides. You can either follow this guide step-by-step or deploy the pre-configured template with one click: [![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/bun-react-postgres?referralCode=Bun&utm_medium=integration&utm_source=template&utm_campaign=bun)

* * *

**Prerequisites**:

*   A Bun application ready for deployment
*   A [Railway account](https://railway.app/)
*   Railway CLI (for CLI deployment method)
*   A GitHub account (for Dashboard deployment method)

* * *

## 

[​

](#method-1-deploy-via-cli)

Method 1: Deploy via CLI

1

[

](#)

Step 1

Ensure sure you have the Railway CLI installed.

terminal

```
bun install -g @railway/cli
```

2

[

](#)

Step 2

Log into your Railway account.

terminal

```
railway login
```

3

[

](#)

Step 3

After successfully authenticating, initialize a new project.

terminal

```
railway init
```

4

[

](#)

Step 4

After initializing the project, add a new database and service.

Step 4 is only necessary if your application uses a database. If you don’t need PostgreSQL, skip to Step 5.

terminal

```
# Add PostgreSQL database. Make sure to add this first!
railway add --database postgres

# Add your application service.
railway add --service bun-react-db --variables DATABASE_URL=\${{Postgres.DATABASE_URL}}
```

5

[

](#)

Step 5

After the services have been created and connected, deploy the application to Railway. By default, services are only accessible within Railway’s private network. To make your app publicly accessible, you need to generate a public domain.

terminal

```
# Deploy your application
railway up

# Generate public domain
railway domain
```

Your app is now live! Railway auto-deploys on every GitHub push.

* * *

## 

[​

](#method-2-deploy-via-dashboard)

Method 2: Deploy via Dashboard

1

[

](#)

Step 1

Create a new project

1.  Go to [Railway Dashboard](http://railway.com/dashboard?utm_medium=integration&utm_source=docs&utm_campaign=bun)
2.  Click **”+ New”** → **“GitHub repo”**
3.  Choose your repository

2

[

](#)

Step 2

Add a PostgreSQL database, and connect this database to the service

Step 2 is only necessary if your application uses a database. If you don’t need PostgreSQL, skip to Step 3.

1.  Click **”+ New”** → **“Database”** → **“Add PostgreSQL”**
2.  After the database has been created, select your service (not the database)
3.  Go to **“Variables”** tab
4.  Click **”+ New Variable”** → **“Add Reference”**
5.  Select `DATABASE_URL` from postgres

3

[

](#)

Step 3

Generate a public domain

1.  Select your service
2.  Go to **“Settings”** tab
3.  Under **“Networking”**, click **“Generate Domain”**

Your app is now live! Railway auto-deploys on every GitHub push.

* * *

## 

[​

](#configuration-optional)

Configuration (Optional)

By default, Railway uses [Nixpacks](https://docs.railway.com/guides/build-configuration#nixpacks-options) to automatically detect and build your Bun application with zero configuration. However, using the [Railpack](https://docs.railway.com/guides/build-configuration#railpack) application builder provides better Bun support, and will always support the latest version of Bun. The pre-configured templates use Railpack by default. To enable Railpack in a custom project, add the following to your `railway.json`:

railway.json

```
{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "builder": "RAILPACK"
  }
}
```

For more build configuration settings, check out the [Railway documentation](https://docs.railway.com/guides/build-configuration).

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/deployment/railway.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/deployment/railway>)

[

Deploy a Bun application on Vercel

Previous

](/docs/guides/deployment/vercel)[

Deploy a Bun application on Render

Next

](/docs/guides/deployment/render)
