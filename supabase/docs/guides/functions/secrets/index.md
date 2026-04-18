---
title: "Environment Variables"
source: "https://supabase.com/docs/guides/functions/secrets"
canonical_url: "https://supabase.com/docs/guides/functions/secrets"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:28.114Z"
content_hash: "8faadecfa4244d2843d3854bd0286d116ff338f2cb4459ed3b50e5f5995a8b45"
menu_path: ["Edge Functions","Edge Functions","Configuration","Configuration","Environment Variables","Environment Variables"]
section_path: ["Edge Functions","Edge Functions","Configuration","Configuration","Environment Variables","Environment Variables"]
nav_prev: {"path": "supabase/docs/guides/functions/routing/index.md", "title": "Handling Routing in Functions"}
nav_next: {"path": "supabase/docs/guides/functions/schedule-functions/index.md", "title": "Scheduling Edge Functions"}
---

# 

Environment Variables

## 

Manage sensitive data securely across environments.

* * *

## Default secrets[#](#default-secrets)

Edge Functions have access to these secrets by default:

*   `SUPABASE_URL`: The API gateway for your Supabase project
*   `SUPABASE_ANON_KEY`: The `anon` key for your Supabase API. This is safe to use in a browser when you have Row Level Security enabled
*   `SUPABASE_SERVICE_ROLE_KEY`: The `service_role` key for your Supabase API. This is safe to use in Edge Functions, but it should NEVER be used in a browser. This key will bypass Row Level Security
*   `SUPABASE_DB_URL`: The URL for your Postgres database. You can use this to connect directly to your database

In a hosted environment, functions have access to the following environment variables:

*   `SB_REGION`: The region function was invoked
*   `SB_EXECUTION_ID`: A UUID of function instance ([isolate](/docs/guides/functions/architecture#4-execution-mechanics-fast-and-isolated))
*   `DENO_DEPLOYMENT_ID`: Version of the function code (`{project_ref}_{function_id}_{version}`)

* * *

## Accessing environment variables[#](#accessing-environment-variables)

You can access environment variables using Deno's built-in handler, and passing it the name of the environment variable you’d like to access.

```
1Deno.env.get('NAME_OF_SECRET')
```

For example, in a function:

```
1import { createClient } from 'npm:@supabase/supabase-js@2'23// For user-facing operations (respects RLS)4const supabase = createClient(5  Deno.env.get('SUPABASE_URL')!,6  Deno.env.get('SUPABASE_ANON_KEY')!7)89// For admin operations (bypasses RLS)10const supabaseAdmin = createClient(11  Deno.env.get('SUPABASE_URL')!,12  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!13)
```

* * *

### Local secrets[#](#local-secrets)

In development, you can load environment variables in two ways:

1.  Through an `.env` file placed at `supabase/functions/.env`, which is automatically loaded on `supabase start`
2.  Through the `--env-file` option for `supabase functions serve`. This allows you to use custom file names like `.env.local` to distinguish between different environments.

```
1supabase functions serve --env-file .env.local
```

Never check your `.env` files into Git! Instead, add the path to this file to your `.gitignore`.

We can automatically access the secrets in our Edge Functions through Deno’s handler

```
1const secretKey = Deno.env.get('STRIPE_SECRET_KEY')
```

Now we can invoke our function locally. If you're using the default `.env` file at `supabase/functions/.env`, it's automatically loaded:

```
1supabase functions serve hello-world
```

Or you can specify a custom `.env` file with the `--env-file` flag:

```
1supabase functions serve hello-world --env-file .env.local
```

This is useful for managing different environments (development, staging, etc.).

* * *

### Production secrets[#](#production-secrets)

You will also need to set secrets for your production Edge Functions. You can do this via the Dashboard or using the CLI.

**Using the Dashboard**:

1.  Visit [Edge Function Secrets Management](/dashboard/project/_/functions/secrets) page in your Dashboard.
2.  Add the Key and Value for your secret and press Save

![Edge Functions Secrets Management](/docs/img/edge-functions-secrets--light.jpg)

Note that you can paste multiple secrets at a time.

**Using the CLI**

You can create a `.env` file to help deploy your secrets to production

```
1# .env2STRIPE_SECRET_KEY=sk_live_...
```

Never check your `.env` files into Git! Instead, add the path to this file to your `.gitignore`.

You can push all the secrets from the `.env` file to your remote project using `supabase secrets set`. This makes the environment visible in the dashboard as well.

```
1supabase secrets set --env-file .env
```

Alternatively, this command also allows you to set production secrets individually rather than storing them in a `.env` file.

```
1supabase secrets set STRIPE_SECRET_KEY=sk_live_...
```

To see all the secrets which you have set remotely, you can use `supabase secrets list`

```
1supabase secrets list
```

You don't need to re-deploy after setting your secrets. They're available immediately in your functions.
