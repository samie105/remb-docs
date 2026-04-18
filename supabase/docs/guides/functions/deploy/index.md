---
title: "Deploy to Production"
source: "https://supabase.com/docs/guides/functions/deploy"
canonical_url: "https://supabase.com/docs/guides/functions/deploy"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:23.731Z"
content_hash: "f2b978d5fd28def49293a96584cd87343a4d2f97cbe8ebb93186df02c14b16a4"
menu_path: ["Edge Functions","Edge Functions","Development","Development","Deploy to Production","Deploy to Production"]
section_path: ["Edge Functions","Edge Functions","Development","Development","Deploy to Production","Deploy to Production"]
nav_prev: {"path": "supabase/docs/guides/functions/dependencies/index.md", "title": "Managing dependencies"}
nav_next: {"path": "supabase/docs/guides/functions/development-environment/index.md", "title": "Development Environment"}
---

# 

Deploy to Production

## 

Deploy your Edge Functions to your remote Supabase Project.

* * *

Once you have developed your Edge Functions locally, you can deploy them to your Supabase project.

Before getting started, make sure you have the Supabase CLI installed. Check out the CLI installation guide for installation methods and troubleshooting.

* * *

## Step 1: Authenticate[#](#step-1-authenticate)

Log in to the Supabase CLI if you haven't already:

```
1supabase login
```

* * *

## Step 2: Connect your project[#](#step-2-connect-your-project)

Get the project ID associated with your function:

```
1supabase projects list
```

##### Need a new project?

If you haven't yet created a Supabase project, you can do so by visiting [database.new](https://database.new).

[Link](/docs/reference/cli/usage#supabase-link) your local project to your remote Supabase project using the ID you just retrieved:

```
1supabase link --project-ref your-project-id
```

Now you should have your local development environment connected to your production project.

* * *

## Step 3: Deploy Functions[#](#step-3-deploy-functions)

You can deploy all edge functions within the `functions` folder with a single command:

```
1supabase functions deploy
```

Or deploy individual Edge Functions by specifying the function name:

```
1supabase functions deploy hello-world
```

### Deploying public functions[#](#deploying-public-functions)

By default, Edge Functions require a valid JWT in the authorization header. If you want to deploy Edge Functions without Authorization checks (commonly used for Stripe webhooks), you can pass the `--no-verify-jwt` flag:

```
1supabase functions deploy hello-world --no-verify-jwt
```

Be careful when using this flag, as it will allow anyone to invoke your Edge Function without a valid JWT. The Supabase client libraries automatically handle authorization.

## Step 4: Verify successful deployment[#](#step-4-verify-successful-deployment)

🎉 Your function is now live!

When the deployment is successful, your function is automatically distributed to edge locations worldwide. Your edge functions is now running globally at `https://[YOUR_PROJECT_ID].supabase.co/functions/v1/hello-world.`

* * *

## Step 5: Test your live function[#](#step-5-test-your-live-function)

You can now invoke your Edge Function using the project's `ANON_KEY`, which can be found in the [API settings](/dashboard/project/_/settings/api) of the Supabase Dashboard. You can invoke it from within your app:

```
1curl --request POST 'https://<project_id>.supabase.co/functions/v1/hello-world' \2  --header 'Authorization: Bearer ANON_KEY' \3  --header 'Content-Type: application/json' \4  --data '{ "name":"Functions" }'
```

Note that the `SUPABASE_PUBLISHABLE_KEY` is different in development and production. To get your production anon key, you can find it in your Supabase dashboard under Settings > API.

You should now see the expected response:

```
1{ "message": "Hello Production!" }
```

You can also test the function through the Dashboard. To see how that works, check out the [Dashboard Quickstart guide](/docs/guides/dashboard/quickstart).

* * *

## CI/CD deployment[#](#cicd-deployment)

You can use popular CI / CD tools like GitHub Actions, Bitbucket, and GitLab CI to automate Edge Function deployments.

### GitHub Actions[#](#github-actions)

You can use the official [`setup-cli` GitHub Action](https://github.com/marketplace/actions/supabase-cli-action) to run Supabase CLI commands in your GitHub Actions.

The following GitHub Action deploys all Edge Functions any time code is merged into the `main` branch:

```
1name: Deploy Function23on:4  push:5    branches:6      - main7  workflow_dispatch:89jobs:10  deploy:11    runs-on: ubuntu-latest1213    env:14      SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}15      PROJECT_ID: your-project-id1617    steps:18      - uses: actions/checkout@v41920      - uses: supabase/setup-cli@v121        with:22          version: latest2324      - run: supabase functions deploy --project-ref $PROJECT_ID
```

* * *

### GitLab CI[#](#gitlab-ci)

Here is the sample pipeline configuration to deploy via GitLab CI.

```
1image: node:2023# List of stages for jobs, and their order of execution4stages:5  - setup6  - deploy78# This job runs in the setup stage, which runs first.9setup-npm:10  stage: setup11  script:12    - npm i supabase13  cache:14    paths:15      - node_modules/16  artifacts:17    paths:18      - node_modules/1920# This job runs in the deploy stage, which only starts when the job in the build stage completes successfully.21deploy-function:22  stage: deploy23  script:24    - npx supabase init25    - npx supabase functions deploy --debug26  services:27    - docker:dind28  variables:29    DOCKER_HOST: tcp://docker:2375
```

* * *

### Bitbucket Pipelines[#](#bitbucket-pipelines)

Here is the sample pipeline configuration to deploy via Bitbucket.

```
1image: node:2023pipelines:4  default:5    - step:6        name: Setup7        caches:8          - node9        script:10          - npm i supabase11    - parallel:12        - step:13            name: Functions Deploy14            script:15              - npx supabase init16              - npx supabase functions deploy --debug17            services:18              - docker
```

* * *

### Function configuration[#](#function-configuration)

Individual function configuration like [JWT verification](/docs/guides/cli/config#functions.function_name.verify_jwt) and [import map location](/docs/guides/cli/config#functions.function_name.import_map) can be set via the `config.toml` file.

```
1[functions.hello-world]2verify_jwt = false
```

This ensures your function configurations are consistent across all environments and deployments.

* * *

### Example[#](#example)

This example shows a GitHub Actions workflow that deploys all Edge Functions when code is merged into the `main` branch.

```
1name: Deploy Function23on:4  push:5    branches:6      - main7  workflow_dispatch:89jobs:10  deploy:11    runs-on: ubuntu-latest1213    env:14      SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}15      SUPABASE_PROJECT_ID: ${{ secrets.SUPABASE_PROJECT_ID }}1617    steps:18      - uses: actions/checkout@v31920      - uses: supabase/setup-cli@v121        with:22          version: latest2324      - run: supabase functions deploy --project-ref $SUPABASE_PROJECT_ID
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/.github/workflows/deploy.yaml)
