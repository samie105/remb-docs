---
title: "Managing dependencies"
source: "https://supabase.com/docs/guides/functions/dependencies"
canonical_url: "https://supabase.com/docs/guides/functions/dependencies"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:16.282Z"
content_hash: "19121556786c4a384770324444228a478e64d9b6e4f0ee204d8a38bff7556fd1"
menu_path: ["Edge Functions","Edge Functions","Configuration","Configuration","Managing Dependencies","Managing Dependencies"]
section_path: ["Edge Functions","Edge Functions","Configuration","Configuration","Managing Dependencies","Managing Dependencies"]
nav_prev: {"path": "supabase/docs/guides/functions/dart-edge/index.md", "title": "Dart Edge"}
nav_next: {"path": "supabase/docs/guides/functions/development-environment/index.md", "title": "Development Environment"}
---

# 

Managing dependencies

## 

Handle dependencies within Edge Functions.

* * *

## Importing dependencies[#](#importing-dependencies)

Supabase Edge Functions support several ways to import dependencies:

*   JavaScript modules from npm ([https://docs.deno.com/examples/npm/](https://docs.deno.com/examples/npm/))
*   Built-in [Node APIs](https://docs.deno.com/runtime/manual/node/compatibility)
*   Modules published to [JSR](https://jsr.io/) or [deno.land/x](https://deno.land/x)

```
1// NPM packages (recommended)2import { createClient } from 'npm:@supabase/supabase-js@2'34// Node.js built-ins5import process from 'node:process'67// JSR modules (Deno's registry)8import path from 'jsr:@std/path@1.0.8'
```

### Using `deno.json` (recommended)[#](#using-denojson-recommended)

Each function should have its own `deno.json` file to manage dependencies and configure Deno-specific settings. This ensures proper isolation between functions and is the recommended approach for deployment. When you update the dependencies for one function, it won't accidentally break another function that needs different versions.

```
1{2  "imports": {3    "supabase": "npm:@supabase/supabase-js@2",4    "lodash": "https://cdn.skypack.dev/lodash"5  }6}
```

You can add this file directly to the function’s own directory:

```
1└── supabase2    ├── functions3    │   ├── function-one4    │   │   ├── index.ts5    │   │   └── deno.json    # Function-specific Deno configuration6    │   └── function-two7    │       ├── index.ts8    │       └── deno.json    # Function-specific Deno configuration9    └── config.toml
```

It's possible to use a global `deno.json` in the `/supabase/functions` directory for local development, but this approach is not recommended for deployment. Each function should maintain its own configuration to ensure proper isolation and dependency management.

### Using import maps (legacy)[#](#using-import-maps-legacy)

Import Maps are a legacy way to manage dependencies, similar to a `package.json` file. While still supported, we recommend using `deno.json`. If both exist, `deno.json` takes precedence.

Each function should have its own `import_map.json` file for proper isolation:

```
1# /function-one/import_map.json2{3  "imports": {4    "lodash": "https://cdn.skypack.dev/lodash"5  }6}
```

This JSON file should be located within the function’s own directory:

```
1└── supabase2    ├── functions3    │   ├── function-one4    │   │   ├── index.ts5    │   │   └── import_map.json    # Function-specific import map
```

It's possible to use a global `import_map.json` in the `/supabase/functions` directory for local development, but this approach is not recommended for deployment. Each function should maintain its own configuration to ensure proper isolation and dependency management.

If you’re using import maps with VSCode, update your `.vscode/settings.json` to point to your function-specific import map:

```
1{2  "deno.enable": true,3  "deno.unstable": ["bare-node-builtins", "byonm"],4  "deno.importMap": "./supabase/functions/function-one/import_map.json"5}
```

You can override the default import map location using the `--import-map <string>` flag with serve and deploy commands, or by setting the `import_map` property in your `config.toml` file:

```
1[functions.my-function]2import_map = "./supabase/functions/function-one/import_map.json"
```

* * *

## Private NPM packages[#](#private-npm-packages)

To use private npm packages, create a `.npmrc` file within your function’s own directory.

This feature requires Supabase CLI version 1.207.9 or higher.

```
1└── supabase2    └── functions3        └── my-function4            ├── index.ts5            ├── deno.json6            └── .npmrc       # Function-specific npm configuration
```

It's possible to use a global `.npmrc` in the `/supabase/functions` directory for local development, but this approach is not recommended for deployment. Each function should maintain its own configuration to ensure proper isolation and dependency management.

Add your registry details in the `.npmrc` file. Follow [this guide](https://docs.npmjs.com/cli/v10/configuring-npm/npmrc) to learn more about the syntax of npmrc files.

```
1# /my-function/.npmrc2@myorg:registry=https://npm.registryhost.com3//npm.registryhost.com/:_authToken=VALID_AUTH_TOKEN
```

After configuring your `.npmrc`, you can import the private package in your function code:

```
1import package from 'npm:@myorg/private-package@v1.0.1'
```

* * *

## Using a custom NPM registry[#](#using-a-custom-npm-registry)

This feature requires Supabase CLI version 2.2.8 or higher.

Some organizations require a custom NPM registry for security and compliance purposes. In such cases, you can specify the custom NPM registry to use via `NPM_CONFIG_REGISTRY` environment variable.

You can define it in the project's `.env` file or directly specify it when running the deploy command:

```
1NPM_CONFIG_REGISTRY=https://custom-registry/ supabase functions deploy my-function
```

* * *

## Importing types[#](#importing-types)

If your [environment is set up properly](/docs/guides/functions/development-environment) and the module you're importing is exporting types, the import will have types and autocompletion support.

Some npm packages may not ship out of the box types and you may need to import them from a separate package. You can specify their types with a `@deno-types` directive:

```
1// @deno-types="npm:@types/express@^4.17"2import express from 'npm:express@^4.17'
```

To include types for built-in Node APIs, add the following line to the top of your imports:

```
1/// <reference types="npm:@types/node" />
```

