---
title: "Development tips"
source: "https://supabase.com/docs/guides/functions/development-tips"
canonical_url: "https://supabase.com/docs/guides/functions/development-tips"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:25.159Z"
content_hash: "53574aa62d3fc364fa30ed035449dbd41a0b54308fdcc96494403eeb85b2a8ff"
menu_path: ["Development tips"]
section_path: []
nav_prev: {"path": "supabase/docs/guides/functions/deploy/index.md", "title": "Deploy to Production"}
nav_next: {"path": "supabase/docs/guides/functions/ephemeral-storage/index.md", "title": "File Storage"}
---

# 

Development tips

## 

Tips for getting started with Edge Functions.

* * *

Here are a few recommendations when you first start developing Edge Functions.

### Skipping authorization checks[#](#skipping-authorization-checks)

By default, Edge Functions require a valid JWT in the authorization header. If you want to use Edge Functions without Authorization checks (commonly used for Stripe webhooks), you can pass the `--no-verify-jwt` flag when serving your Edge Functions locally.

```
1supabase functions serve hello-world --no-verify-jwt
```

Be careful when using this flag, as it will allow anyone to invoke your Edge Function without a valid JWT. The Supabase client libraries automatically handle authorization.

### Using HTTP methods[#](#using-http-methods)

Edge Functions support `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`. A Function can be designed to perform different actions based on a request's HTTP method. See the [example on building a RESTful service](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/restful-tasks) to learn how to handle different HTTP methods in your Function.

##### HTML not supported

HTML content is not supported. `GET` requests that return `text/html` will be rewritten to `text/plain`.

### Naming Edge Functions[#](#naming-edge-functions)

We recommend using hyphens to name functions because hyphens are the most URL-friendly of all the naming conventions (snake\_case, camelCase, PascalCase).

### Organizing your Edge Functions[#](#organizing-your-edge-functions)

We recommend developing "fat functions". This means that you should develop few large functions, rather than many small functions. One common pattern when developing Functions is that you need to share code between two or more Functions. To do this, you can store any shared code in a folder prefixed with an underscore (`_`). We also recommend a separate folder for [Unit Tests](/docs/guides/functions/unit-test) including the name of the function followed by a `-test` suffix. We recommend this folder structure:

```
1└── supabase2    ├── functions3    │   ├── import_map.json # A top-level import map to use across functions.4    │   ├── _shared5    │   │   ├── supabaseAdmin.ts # Supabase client with SERVICE_ROLE key.6    │   │   └── supabaseClient.ts # Supabase client with ANON key.7    │   │   └── cors.ts # Reusable CORS headers.8    │   ├── function-one # Use hyphens to name functions.9    │   │   └── index.ts10    │   └── function-two11    │   │   └── index.ts12    │   └── tests13    │       └── function-one-test.ts14    │       └── function-two-test.ts15    ├── migrations16    └── config.toml
```

### Using config.toml[#](#using-configtoml)

Individual function configuration like [JWT verification](/docs/guides/cli/config#functions.function_name.verify_jwt) and [import map location](/docs/guides/cli/config#functions.function_name.import_map) can be set via the `config.toml` file.

```
1[functions.hello-world]2verify_jwt = false3import_map = './import_map.json'
```

### Not using TypeScript[#](#not-using-typescript)

When you create a new Edge Function, it will use TypeScript by default. However, it is possible to write and deploy Edge Functions using pure JavaScript.

Save your Function as a JavaScript file (e.g. `index.js`) and then update the `supabase/config.toml` as follows:

`entrypoint` is available only in Supabase CLI version 1.215.0 or higher.

```
1[functions.hello-world]2# other entries3entrypoint = './functions/hello-world/index.js' # path must be relative to config.toml
```

You can use any `.ts`, `.js`, `.tsx`, `.jsx` or `.mjs` file as the `entrypoint` for a Function.

### Error handling[#](#error-handling)

The `supabase-js` library provides several error types that you can use to handle errors that might occur when invoking Edge Functions:

```
1import { FunctionsHttpError, FunctionsRelayError, FunctionsFetchError } from '@supabase/supabase-js'23const { data, error } = await supabase.functions.invoke('hello', {4  headers: { 'my-custom-header': 'my-custom-header-value' },5  body: { foo: 'bar' },6})78if (error instanceof FunctionsHttpError) {9  const errorMessage = await error.context.json()10  console.log('Function returned an error', errorMessage)11} else if (error instanceof FunctionsRelayError) {12  console.log('Relay error:', error.message)13} else if (error instanceof FunctionsFetchError) {14  console.log('Fetch error:', error.message)15}
```

### Database Functions vs Edge Functions[#](#database-functions-vs-edge-functions)

For data-intensive operations we recommend using [Database Functions](/docs/guides/database/functions), which are executed within your database and can be called remotely using the [REST and GraphQL API](/docs/guides/api).

For use-cases which require low-latency we recommend [Edge Functions](/docs/guides/functions), which are globally-distributed and can be written in TypeScript.

