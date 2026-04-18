---
title: "Getting Started with Edge Functions"
source: "https://supabase.com/docs/guides/functions/quickstart"
canonical_url: "https://supabase.com/docs/guides/functions/quickstart"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:07.804Z"
content_hash: "7a65f3272301e906e31e0740ce15690a96f90183bbc1c9fe5a9a800e3cc78456"
menu_path: ["Edge Functions","Edge Functions","Getting started","Getting started","Quickstart (CLI)","Quickstart (CLI)"]
section_path: ["Edge Functions","Edge Functions","Getting started","Getting started","Quickstart (CLI)","Quickstart (CLI)"]
nav_prev: {"path": "supabase/docs/guides/functions/quickstart-dashboard/index.md", "title": "Getting Started with Edge Functions (Dashboard)"}
nav_next: {"path": "supabase/docs/guides/functions/recursive-functions/index.md", "title": "Recursive / Nested Function Calls"}
---

# 

Getting Started with Edge Functions

## 

Learn how to create, test, and deploy your first Edge Function using the Supabase CLI.

* * *

Before getting started, make sure you have the **Supabase CLI installed**. Check out the [CLI installation guide](/docs/guides/cli) for installation methods and troubleshooting.

##### Prefer using the Supabase Dashboard?

You can also create and deploy functions directly from the Supabase Dashboard. Check out our [Dashboard Quickstart guide](/docs/guides/functions/quickstart-dashboard).

* * *

## Step 1: Create or configure your project[#](#step-1-create-or-configure-your-project)

If you don't have a project yet, initialize a new Supabase project in your current directory.

```
1supabase init my-edge-functions-project2cd my-edge-functions-project
```

Or, if you already have a project locally, navigate to your project directory. If your project hasn't been configured for Supabase yet, make sure to run the `supabase init` command.

```
1cd your-existing-project2supabase init # Initialize Supabase, if you haven't already
```

After this step, you should have a project directory with a `supabase` folder containing `config.toml` and an empty `functions` directory.

* * *

## Step 2: Create your first function[#](#step-2-create-your-first-function)

Within your project, generate a new Edge Function with a basic template:

```
1supabase functions new hello-world
```

This creates a new function at `supabase/functions/hello-world/index.ts` with this starter code:

```
1Deno.serve(async (req) => {2  const { name } = await req.json()3  const data = {4    message: `Hello ${name}!`,5  }67  return new Response(JSON.stringify(data), { headers: { 'Content-Type': 'application/json' } })8})
```

This function accepts a JSON payload with a `name` field and returns a greeting message.

After this step, you should have a new file at `supabase/functions/hello-world/index.ts` containing the starter Edge Function code.

* * *

## Step 3: Test your function locally[#](#step-3-test-your-function-locally)

Start the local development server to test your function:

```
1supabase start  # Start all Supabase services2supabase functions serve hello-world
```

##### First time running Supabase services?

The `supabase start` command downloads Docker images, which can take a few minutes initially.

**Function not starting locally?**

*   Make sure Docker is running
*   Run `supabase stop` then `supabase start` to restart services

**Port already in use?**

*   Check what's running with `supabase status`
*   Stop other Supabase instances with `supabase stop`

Your function is now running at [`http://localhost:54321/functions/v1/hello-world`](http://localhost:54321/functions/v1/hello-world). Hot reloading is enabled, which means that the server will automatically reload when you save changes to your function code.

After this step, you should have all Supabase services running locally, and your Edge Function serving at the local URL. Keep these terminal windows open.

* * *

## Step 4: Send a test request[#](#step-4-send-a-test-request)

Open a new terminal and test your function with curl:

**Need your `SUPABASE_PUBLISHABLE_KEY`?**

Run `supabase status` to see your local anon key and other credentials.

```
1curl -i --location --request POST 'http://localhost:54321/functions/v1/hello-world' \2  --header 'Authorization: Bearer SUPABASE_PUBLISHABLE_KEY' \3  --header 'Content-Type: application/json' \4  --data '{"name":"Functions"}'
```

After running this curl command, you should see:

```
1{ "message": "Hello Functions!" }
```

You can also try different inputs. Change `"Functions"` to `"World"` in the curl command and run it again to see the response change.

After this step, you should have successfully tested your Edge Function locally and received a JSON response with your greeting message.

* * *

## Step 5: Connect to your Supabase project[#](#step-5-connect-to-your-supabase-project)

To deploy your function globally, you need to connect your local project to a Supabase project.

##### Need to create new Supabase project?

Create one at [database.new](https://database.new/).

First, login to the CLI if you haven't already, and authenticate with Supabase. This opens your browser to authenticate with Supabase; complete the login process in your browser.

```
1supabase login
```

Next, list your Supabase projects to find your project ID:

```
1supabase projects list
```

Next, copy your project ID from the output, then connect your local project to your remote Supabase project. Replace `YOUR_PROJECT_ID` with the ID from the previous step.

```
1supabase link --project-ref [YOUR_PROJECT_ID]
```

After this step, you should have your local project authenticated and linked to your remote Supabase project. You can verify this by running `supabase status`.

* * *

## Step 6: Deploy to production[#](#step-6-deploy-to-production)

Deploy your function to Supabase's global edge network:

```
1supabase functions deploy hello-world23# If you want to deploy all functions, run the `deploy` command without specifying a function name:4supabase functions deploy
```

##### Docker not required

The CLI automatically falls back to API-based deployment if Docker isn't available. You can also explicitly use API deployment with the `--use-api` flag:

```
1supabase functions deploy hello-world --use-api
```

If you want to skip JWT verification, you can add the `--no-verify-jwt` flag for webhooks that don't need authentication:

```
1supabase functions deploy hello-world --no-verify-jwt
```

##### Security Warning

**Use `--no-verify-jwt` carefully.** It allows anyone to invoke your function without authentication!

When the deployment is successful, your function is automatically distributed to edge locations worldwide.

Now, you should have your Edge Function deployed and running globally at `https://[YOUR_PROJECT_ID].supabase.co/functions/v1/hello-world`.

* * *

## Step 7: Test your live function[#](#step-7-test-your-live-function)

🎉 Your function is now live! Test it with your project's anon key:

```
1curl --request POST 'https://[YOUR_PROJECT_ID].supabase.co/functions/v1/hello-world' \2  --header 'Authorization: Bearer SUPABASE_PUBLISHABLE_KEY' \3  --header 'Content-Type: application/json' \4  --data '{"name":"Production"}'
```

**Expected response:**

```
1{ "message": "Hello Production!" }
```

##### Production vs Development Keys

The `SUPABASE_PUBLISHABLE_KEY` is different in development and production. To get your production anon key, you can find it in your Supabase dashboard under **Settings > API**.

Finally, you should have a fully deployed Edge Function that you can call from anywhere in the world.

* * *

## Usage[#](#usage)

Now that your function is deployed, you can invoke it from within your app:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://[YOUR_PROJECT_ID].supabase.co', 'YOUR_ANON_KEY')45const { data, error } = await supabase.functions.invoke('hello-world', {6  body: { name: 'JavaScript' },7})89console.log(data) // { message: "Hello JavaScript!" }
```


