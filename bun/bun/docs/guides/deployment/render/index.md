---
title: "Deploy a Bun application on Render"
source: "https://bun.com/docs/guides/deployment/render"
canonical_url: "https://bun.com/docs/guides/deployment/render"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:17.295Z"
content_hash: "3148dfe698a1e7f83ffd985138861656c1b0bf9855d828cc510090e89b2e8628"
menu_path: ["Deploy a Bun application on Render"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/deployment/railway/index.md", "title": "Deploy a Bun application on Railway"}
nav_next: {"path": "bun/bun/docs/guides/deployment/vercel/index.md", "title": "Deploy a Bun application on Vercel"}
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

[Render](https://render.com/) is a cloud platform that lets you flexibly build, deploy, and scale your apps. It offers features like auto deploys from GitHub, a global CDN, private networks, automatic HTTPS setup, and managed PostgreSQL and Redis. Render supports Bun natively. You can deploy Bun apps as web services, background workers, cron jobs, and more.

* * *

As an example, let’s deploy an Express HTTP server to Render.

1

[

](#)

Step 1

Create a new GitHub repo named `myapp`. Git clone it locally.

```
git clone git@github.com:my-github-username/myapp.git
cd myapp
```

2

[

](#)

Step 2

Add the Express library.

```
bun add express
```

3

[

](#)

Step 3

Define a server with Express:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import express from "express";

const app = express();
const port = process.env.PORT || 3001;

app.get("/", (req, res) => {
	res.send("Hello World!");
});

app.listen(port, () => {
	console.log(`Listening on port ${port}...`);
});
```

4

[

](#)

Step 4

Commit your changes and push to GitHub.

terminal

```
git add app.ts bun.lock package.json
git commit -m "Create simple Express app"
git push origin main
```

5

[

](#)

Step 5

In your [Render Dashboard](https://dashboard.render.com/), click `New` > `Web Service` and connect your `myapp` repo.

6

[

](#)

Step 6

In the Render UI, provide the following values during web service creation:

**Runtime**

`Node`

**Build Command**

`bun install`

**Start Command**

`bun app.ts`

That’s it! Your web service will be live at its assigned `onrender.com` URL as soon as the build finishes. You can view the [deploy logs](https://docs.render.com/logging#logs-for-an-individual-deploy-or-job) for details. Refer to [Render’s documentation](https://docs.render.com/deploys) for a complete overview of deploying on Render.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/deployment/render.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/deployment/render>)

[

Deploy a Bun application on Railway

Previous

](/docs/guides/deployment/railway)[

Deploy a Bun application on AWS Lambda

Next

](/docs/guides/deployment/aws-lambda)

