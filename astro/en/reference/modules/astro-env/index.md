---
title: "Environment Variables API Reference"
source: "https://docs.astro.build/en/reference/modules/astro-env/"
canonical_url: "https://docs.astro.build/en/reference/modules/astro-env/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:40.920Z"
content_hash: "98dc5b486f98e8ba6d99055ead2a83967458344588796266a5dfa5c502efed6c"
menu_path: ["Environment Variables API Reference"]
section_path: []
---
# Environment Variables API Reference

**Added in:** `astro@5.0.0`

The `astro:env` API lets you configure a type-safe schema for environment variables you have set. This allows you to indicate whether they should be available on the server or the client, and define their data type and additional properties. For examples and usage instructions, [see the `astro:env` guide](/en/guides/environment-variables/#type-safe-environment-variables).

## Imports from `astro:env`

[Section titled “Imports from astro:env”](#imports-from-astroenv)

```
import {  getSecret, } from 'astro:env/server';
```

### `getSecret()`

[Section titled “getSecret()”](#getsecret)

**Added in:** `astro@5.0.0`

The `getSecret()` helper function allows retrieving the raw value of an environment variable by its key.

For example, you can retrieve a boolean value as a string:

```
import {  FEATURE_FLAG, // boolean  getSecret} from 'astro:env/server'
getSecret('FEATURE_FLAG') // string | undefined
```

This can also be useful to get a secret not defined in your schema, for example one that depends on dynamic data from a database or API.

If you need to retrieve environment variables programmatically, we recommend using `getSecret()` instead of `process.env` (or equivalent). Because its implementation is provided by your adapter, you won’t need to update all your calls if you switch adapters. It defaults to `process.env` in dev and build.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
