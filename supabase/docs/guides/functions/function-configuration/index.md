---
title: "Function Configuration"
source: "https://supabase.com/docs/guides/functions/function-configuration"
canonical_url: "https://supabase.com/docs/guides/functions/function-configuration"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:35.750Z"
content_hash: "558f2216b1e073e49cb95688c70d8f978005fb705a986b37326aea7432cf8b3d"
menu_path: ["Edge Functions","Edge Functions","Configuration","Configuration","Function Configuration","Function Configuration"]
section_path: ["Edge Functions","Edge Functions","Configuration","Configuration","Function Configuration","Function Configuration"]
nav_prev: {"path": "supabase/docs/guides/functions/error-handling/index.md", "title": "Error Handling"}
nav_next: {"path": "supabase/docs/guides/functions/http-methods/index.md", "title": "Routing"}
---

# 

Function Configuration

## 

Configure individual function behavior. Customize authentication, dependencies, and other settings per function.

* * *

## Configuration[#](#configuration)

By default, all your Edge Functions have the same settings. In real applications, however, you might need different behaviors between functions.

For example:

*   **Stripe webhooks** need to be publicly accessible (Stripe doesn't have your user tokens)
*   **User profile APIs** should require authentication
*   **Some functions** might need special dependencies or different file types

To enable these per-function rules, create `supabase/config.toml` in your project root:

```
1# Disables authentication for the Stripe webhook.2[functions.stripe-webhook]3verify_jwt = false45# Custom dependencies for this specific function6[functions.image-processor]7import_map = './functions/image-processor/import_map.json'89# Custom entrypoint for legacy function using JavaScript10[functions.legacy-processor]11entrypoint = './functions/legacy-processor/index.js
```

This configuration tell Supabase that the `stripe-webhook` function doesn't require a valid JWT, the `image-processor` function uses a custom import map, and `legacy-processor` uses a custom entrypoint.

You set these rules once and never worry about them again. Deploy your functions knowing that the security and behavior is exactly what each endpoint needs.

To see more general `config.toml` options, check out [this guide](/docs/guides/local-development/managing-config).

* * *

## Skipping authorization checks[#](#skipping-authorization-checks)

By default, Edge Functions require a valid JWT in the authorization header. If you want to use Edge Functions without Authorization checks (commonly used for Stripe webhooks), you can configure this in your `config.toml`:

```
1[functions.stripe-webhook]2verify_jwt = false
```

You can also pass the `--no-verify-jwt` flag when serving your Edge Functions locally:

```
1supabase functions serve hello-world --no-verify-jwt
```

Be careful when using this flag, as it will allow anyone to invoke your Edge Function without a valid JWT. The Supabase client libraries automatically handle authorization.

* * *

## Custom entrypoints[#](#custom-entrypoints)

`entrypoint` is available only in Supabase CLI version 1.215.0 or higher.

When you create a new Edge Function, it will use TypeScript by default. However, it is possible to write and deploy Edge Functions using pure JavaScript.

Save your Function as a JavaScript file (e.g. `index.js`) update the `supabase/config.toml` :

```
1[functions.hello-world]2entrypoint = './index.js' # path must be relative to config.toml
```

You can use any `.ts`, `.js`, `.tsx`, `.jsx` or `.mjs` file as the entrypoint for a Function.
