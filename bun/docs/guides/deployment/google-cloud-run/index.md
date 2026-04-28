---
title: "Deploy a Bun application on Google Cloud Run"
source: "https://bun.com/docs/guides/deployment/google-cloud-run"
canonical_url: "https://bun.com/docs/guides/deployment/google-cloud-run"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:57.146Z"
content_hash: "8576f408aa37eaf1f05646fa7b6e61e12edc6c7d9f8d4be5d4c27bd2f24a8946"
menu_path: ["Deploy a Bun application on Google Cloud Run"]
section_path: []
nav_prev: {"path": "bun/docs/guides/deployment/digital-ocean/index.md", "title": "Deploy a Bun application on DigitalOcean"}
nav_next: {"path": "bun/docs/guides/deployment/railway/index.md", "title": "Deploy a Bun application on Railway"}
---

# Use the official Bun image to run the application
FROM oven/bun:latest

# Copy the package.json and bun.lock into the container
COPY package.json bun.lock ./

# Install the dependencies
RUN bun install --production --frozen-lockfile

# Copy the rest of the application into the container
COPY . .

# Run the application
CMD ["bun", "index.ts"]
```

Make sure that the start command corresponds to your application’s entry point. This can also be `CMD ["bun", "run", "start"]` if you have a start script in your `package.json`.This image installs dependencies and runs your app with Bun inside a container. If your app doesn’t have dependencies, you can omit the `RUN bun install --production --frozen-lockfile` line.

Create a new `.dockerignore` file in the root of your project. This file contains the files and directories that should be _excluded_ from the container image, such as `node_modules`. This makes your builds faster and smaller:

.dockerignore

```
node_modules
Dockerfile*
.dockerignore
.git
.gitignore
README.md
LICENSE
.vscode
.env
# Any other files or directories you want to exclude
```

6

Deploy your service

Make sure you’re in the directory containing your `Dockerfile`, then deploy directly from your local source:

Update the `--region` flag to your preferred region. You can also omit this flag to get an interactive prompt to select a region.

terminal

```
gcloud run deploy my-bun-app --source . --region=us-west1 --allow-unauthenticated
```

```
Deploying from source requires an Artifact Registry Docker repository to store built containers. A repository named
[cloud-run-source-deploy] in region [us-west1] will be created.

Do you want to continue (Y/n)? Y

Building using Dockerfile and deploying container to Cloud Run service [my-bun-app] in project [my-bun-app-...] region [us-west1]
✓ Building and deploying... Done.
  ✓ Validating Service...
  ✓ Uploading sources...
  ✓ Building Container... Logs are available at [https://console.cloud.google.com/cloud-build/builds...].
  ✓ Creating Revision...
  ✓ Routing traffic...
  ✓ Setting IAM Policy...
Done.
Service [my-bun-app] revision [my-bun-app-...] has been deployed and is serving 100 percent of traffic.
Service URL: https://my-bun-app-....us-west1.run.app
```

7

Visit your live application

🎉 Your Bun application is now live!Visit the Service URL (`https://my-bun-app-....us-west1.run.app`) to confirm everything works as expected.
