---
title: "Google Cloud Run ​"
source: "https://hono.dev/docs/getting-started/google-cloud-run"
canonical_url: "https://hono.dev/docs/getting-started/google-cloud-run"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:59.904Z"
content_hash: "b88e82066dabba270a62ebd3ab6b3460980281d185daf5b882e8acf75c23e843"
menu_path: ["Google Cloud Run ​"]
section_path: []
---
[Google Cloud Run](https://cloud.google.com/run) is a serverless platform built by Google Cloud. You can run your code in response to events and Google automatically manages the underlying compute resources for you.

Google Cloud Run uses containers to run your service. This means you can use any runtime you like (E.g., Deno or Bun) by providing a Dockerfile. If no Dockerfile is provided Google Cloud Run will use the default Node.js buildpack.

This guide assumes you already have a Google Cloud account and a billing account.

## 1\. Install the CLI [​](#_1-install-the-cli)

When working with Google Cloud Platform, it is easiest to work with the [gcloud CLI](https://cloud.google.com/sdk/docs/install).

For example, on MacOS using Homebrew:

sh

```
brew install --cask gcloud-cli
```

Authenticate with the CLI.

sh

```
gcloud auth login
```

## 2\. Project setup [​](#_2-project-setup)

Create a project. Accept the auto-generated project ID at the prompt.

sh

```
gcloud projects create --set-as-default --name="my app"
```

Create environment variables for your project ID and project number for easy reuse. It may take ~30 seconds before the project successfully returns with the `gcloud projects list` command.

sh

```
PROJECT_ID=$(gcloud projects list \
    --format='value(projectId)' \
    --filter='name="my app"')

PROJECT_NUMBER=$(gcloud projects list \
    --format='value(projectNumber)' \
    --filter='name="my app"')

echo $PROJECT_ID $PROJECT_NUMBER
```

Find your billing account ID.

sh

```
gcloud billing accounts list
```

Add your billing account from the prior command to the project.

sh

```
gcloud billing projects link $PROJECT_ID \
    --billing-account=[billing_account_id]
```

Enable the required APIs.

sh

```
gcloud services enable run.googleapis.com \
    cloudbuild.googleapis.com
```

Update the service account permissions to have access to Cloud Build.

sh

```
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com \
    --role=roles/run.builder
```

## 3\. Hello World [​](#_3-hello-world)

Start your project with "create-hono" command. Select `nodejs`.

sh

```
npm create hono@latest my-app
```

Move to `my-app` and install the dependencies.

sh

```
cd my-app
npm i
```

Update the port in `src/index.ts` to be `8080`.

ts

```
import { serve } from '@hono/node-server'
import { Hono } from 'hono'

const app = new Hono()

app.get('/', (c) => {
  return c.text('Hello Hono!')
})

serve({
  fetch: app.fetch,
  port: 3000
  port: 8080
}, (info) => {
  console.log(`Server is running on http://localhost:${info.port}`)
})
```

Run the development server locally. Then, access [http://localhost:8080](http://localhost:8080/) in your Web browser.

sh

```
npm run dev
```

## 4\. Deploy [​](#_4-deploy)

Start the deployment and follow the interactive prompts (E.g., select a region).

sh

```
gcloud run deploy my-app --source . --allow-unauthenticated
```

## Changing runtimes [​](#changing-runtimes)

If you want to deploy using Deno or Bun runtimes (or a customised Nodejs container), add a `Dockerfile` (and optionally `.dockerignore`) with your desired environment.

For information on containerizing, please refer to:

*   [Node.js](https://hono.dev/docs/getting-started/nodejs#building-deployment)
*   [Bun](https://bun.com/guides/ecosystem/docker)
*   [Deno](https://docs.deno.com/examples/google_cloud_run_tutorial)
