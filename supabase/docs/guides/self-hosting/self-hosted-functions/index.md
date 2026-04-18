---
title: "Self-Hosted Functions"
source: "https://supabase.com/docs/guides/self-hosting/self-hosted-functions"
canonical_url: "https://supabase.com/docs/guides/self-hosting/self-hosted-functions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:42.250Z"
content_hash: "8a01609d8cc51c08ffb675ad0d47e6563a298ad706ee414423509c2eb4070b7a"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Self-Hosted Functions","Self-Hosted Functions"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Self-Hosted Functions","Self-Hosted Functions"]
nav_prev: {"path": "supabase/docs/guides/self-hosting/self-hosted-auth-keys/index.md", "title": "New API Keys and Asymmetric Authentication"}
nav_next: {"path": "supabase/docs/guides/self-hosting/self-hosted-oauth/index.md", "title": "Configure Social Login (OAuth) Providers"}
---

# 

Self-Hosted Functions

## 

Run and manage Edge Functions in your self-hosted Supabase instance.

* * *

Edge Functions work out of the box in a self-hosted Supabase setup. The `functions` service, API gateway routing, and a `hello` example function are all [pre-configured](https://github.com/supabase/supabase/tree/master/docker).

On managed Supabase platform, Edge Functions are deployed across multiple regions. Self-hosted standalone instance configuration resembles a standard serverless setup.

## Invoke the default function[#](#invoke-the-default-function)

The default `hello` function is located at `volumes/functions/hello/index.ts`. You can invoke it immediately after starting your stack:

```
1curl http://<your-domain>:8000/functions/v1/hello
```

This returns `"Hello from Edge Functions!"`.

## Create a new function[#](#create-a-new-function)

### Step 1: Add a new function directory and the function code[#](#step-1-add-a-new-function-directory-and-the-function-code)

```
1mkdir -p volumes/functions/my-function &&2touch volumes/functions/my-function/index.ts
```

add the following code to `index.ts`:

```
1Deno.serve(async (req: Request) => {2  const { name } = await req.json()3  const message = `Hello, ${name}!`45  return new Response(JSON.stringify({ message }), {6    headers: { 'Content-Type': 'application/json' },7  })8})
```

### Step 2: Restart the functions service to pick up the new function[#](#step-2-restart-the-functions-service-to-pick-up-the-new-function)

```
1docker compose restart functions --no-deps
```

### Step 3: Invoke your function[#](#step-3-invoke-your-function)

```
1curl -X POST http://<your-domain>:8000/functions/v1/my-function \2  -H 'Content-Type: application/json' \3  -d '{"name": "World"}'
```

You should be able to see the response from `my-function`:

```
1{"message":"Hello, World!"}
```

## Custom environment variables[#](#custom-environment-variables)

### Using an env file (recommended)[#](#using-an-env-file-recommended)

For multiple variables or secrets, create a separate env file, e.g., `.env.functions` in your `docker/` directory:

```
1MY_CUSTOM_VAR=some-value
```

Add `env_file` to the `functions` service in `docker-compose.yml` (variables in `env_file` load first, then `environment` values take precedence):

```
1functions:2  env_file:3    - .env.functions4  environment:5    JWT_SECRET: ${JWT_SECRET}6    SUPABASE_URL: http://kong:8000
```

Don't commit `.env.functions` to version control if it contains secrets. Add it to your `.gitignore`.

Restart the functions service:

```
1docker compose up -d --force-recreate --no-deps functions
```

### Using inline environment variables[#](#using-inline-environment-variables)

For one or two variables, you can add them directly under `environment` in `docker-compose.yml`:

```
1functions:2  environment:3    # Custom variables4    MY_CUSTOM_VAR: ${MY_CUSTOM_VAR}5    # Required variables6    JWT_SECRET: ${JWT_SECRET}7    SUPABASE_URL: http://kong:8000
```

Then define `MY_CUSTOM_VAR` in your main `.env` file, or specify the value directly.

### Accessing variables in functions[#](#accessing-variables-in-functions)

All container environment variables are forwarded to function workers by `main/index.ts`. Access them with:

```
1const customVar = Deno.env.get('MY_CUSTOM_VAR')
```

## Calling Supabase services from functions[#](#calling-supabase-services-from-functions)

The functions service is pre-configured with the following environment variables:

Variable

Value

Purpose

`SUPABASE_URL`

`http://kong:8000`

Internal API gateway URL

`SUPABASE_PUBLIC_URL`

`http://<your-domain>:8000`

Base URL for accessing Supabase from the Internet

`JWT_SECRET`

Your secret key

Legacy symmetric encryption key used to sign and verify JWTs

`SUPABASE_ANON_KEY`

Your anon key

Client-side API key with limited permissions (`anon` role).

`SUPABASE_SERVICE_ROLE_KEY`

Your service role key

Server-side API key with full database access (`service_role` role)

`SUPABASE_DB_URL`

Postgres connection string

Can be used for direct database access

Here's an example function that queries a table using `@supabase/supabase-js`:

```
1import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'23Deno.serve(async () => {4  const supabase = createClient(5    Deno.env.get('SUPABASE_URL')!,6    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!7  )89  const { data, error } = await supabase.from('todos').select('*')1011  return new Response(JSON.stringify({ data, error }), {12    headers: { 'Content-Type': 'application/json' },13  })14})
```

### Internal vs external URLs[#](#internal-vs-external-urls)

This is a key distinction that affects how you build URLs in your functions:

*   **`SUPABASE_URL`** contains an internal Docker network hostname. Use it for server-side calls from your functions to other Supabase services (Auth, Storage, database via PostgREST). This is what the Supabase JS client should use inside functions.
    
*   **`SUPABASE_PUBLIC_URL`** is the externally-reachable URL of your Supabase instance (e.g., `<your-domain>:8000`). Use it if your function needs to build URLs that HTTP clients can reach from the outside.
    

## Managing functions via dashboard[#](#managing-functions-via-dashboard)

Self-hosted Studio [mounts](https://github.com/supabase/supabase/blob/df8729a82b1847e2989c14ede27965612761d503/docker/docker-compose.yml#L66) the same `volumes/functions` directory as the functions service. You can check what functions are available using **Edge Functions** > **Functions** UI.

## Deploying functions to a remote server[#](#deploying-functions-to-a-remote-server)

To deploy a function to a remote server running self-hosted Supabase, copy the function directory with `scp`:

```
1scp -r ./my-function user@<your-domain>:/path/to/self-hosted/volumes/functions/
```

Then restart the functions service on the remote host:

```
1ssh user@<your-domain> 'cd /path/to/self-hosted && docker compose restart functions --no-deps'
```

## Copying functions from Supabase platform[#](#copying-functions-from-supabase-platform)

If you have existing functions on Supabase platform, you can download them and run them on your self-hosted instance. There are two ways to get the function source code:

*   **Dashboard** - open the function details in Dashboard and click **Download**.
*   **Local development & CLI** - run `supabase functions download <function-name> --project-ref <ref>` to download the source.

Use `scp` to copy the function into `volumes/functions/<function-name>/` on your self-hosted instance, then restart the functions service.

For more details, see:

*   [Quick start - Download edge functions](/docs/guides/functions/quickstart-dashboard#download-edge-functions)
*   [CLI commands - Download a function](/docs/reference/cli/supabase-functions-download)

## Troubleshooting[#](#troubleshooting)

### 400 "missing function name in request"[#](#400-missing-function-name-in-request)

The request URL must include the function name after `/functions/v1/`. For example, `/functions/v1/hello` — not just `/functions/v1/`.

### 500 error on invocation[#](#500-error-on-invocation)

Check the functions service logs:

```
1docker compose logs functions
```

Common causes: syntax errors in your function code, invalid imports, or missing dependencies.

### 401 "invalid JWT"[#](#401-invalid-jwt)

*   Check that `FUNCTIONS_VERIFY_JWT` matches your intent (`true` or `false`) in `.env`
*   If verification is enabled, ensure you're passing a valid token: `Authorization: Bearer <anon_key or service_role_key>`

### Changes to function code not reflected after editing[#](#changes-to-function-code-not-reflected-after-editing)

Restart the functions service:

```
1docker compose restart functions --no-deps
```

### Custom env vars not available in functions[#](#custom-env-vars-not-available-in-functions)

*   Verify the variable is defined in `docker-compose.yml` (under `env_file` or `environment`)
*   Recreate the functions container after changing configuration
*   Check that the variable name matches exactly (case-sensitive)

Use the following command to recreate the container, not just `restart`:

```
1docker compose up -d --force-recreate --no-deps functions
```

### Memory or timeout errors[#](#memory-or-timeout-errors)

The default limits are 150 MB memory and 60 seconds timeout per function invocation. These are set in `volumes/functions/main/index.ts`. To adjust them, edit the `memoryLimitMb` and `workerTimeoutMs` values and restart the functions service.
