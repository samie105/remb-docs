---
title: "Config imports API Reference"
source: "https://docs.astro.build/en/reference/modules/astro-config/"
canonical_url: "https://docs.astro.build/en/reference/modules/astro-config/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:35.923Z"
content_hash: "620ea03b36e0f9a32461559c35b6224bfd11d8174c85814235370f4094b9c5da"
menu_path: ["Config imports API Reference"]
section_path: []
nav_prev: {"path": "astro/en/reference/modules/astro-assets/index.md", "title": "Image and Assets API Reference"}
nav_next: {"path": "astro/en/reference/modules/astro-content/index.md", "title": "Content Collections API Reference"}
---

# Config imports API Reference

**Added in:** `astro@5.7.0`

This virtual module `astro:config` exposes a non-exhaustive, serializable, type-safe version of the Astro configuration. There are two submodules for accessing different subsets of your configuration values: [`/client`](#imports-from-astroconfigclient) and [`/server`](#imports-from-astroconfigserver).

All available config values can be accessed from `astro:config/server`. However, for code executed on the client, only those values exposed by `astro:config/client` will be available. This protects your information by only making some data available to the client.

## Imports from `astro:config/client`

[Section titled “Imports from astro:config/client”](#imports-from-astroconfigclient)

The following helpers are imported from the `client` directory of the virtual config module.

```
import {  i18n,  trailingSlash,  base,  build,  site,  compressHTML,} from "astro:config/client";
```

Use this submodule for client-side code:

```
import { trailingSlash } from "astro:config/client";
function addForwardSlash(path) {  if (trailingSlash === "always") {    return path.endsWith("/") ? path : path + "/"  } else {    return path  }}
```

See more about the configuration imports available from `astro:config/client`:

*   [`i18n`](../../configuration-reference/index.md#i18n)
*   [`trailingSlash`](../../configuration-reference/index.md#trailingslash)
*   [`base`](../../configuration-reference/index.md#base)
*   [`build.format`](../../configuration-reference/index.md#buildformat)
*   [`site`](../../configuration-reference/index.md#site)
*   [`compressHTML`](../../configuration-reference/index.md#compresshtml)

## Imports from `astro:config/server`

[Section titled “Imports from astro:config/server”](#imports-from-astroconfigserver)

The following helpers are imported from the `server` directory of the virtual config module.

```
import {  i18n,  trailingSlash,  base,  build,  site,  srcDir,  cacheDir,  outDir,  publicDir,  root,  compressHTML,} from "astro:config/server";
```

These imports include everything available from `astro:config/client` as well as additional sensitive information about your file system configuration that is not safe to expose to the client.

Use this submodule for server side code:

```
import { integration } from "./integration.mjs";
export default defineConfig({    integrations: [      integration(),    ]});
```

```
import { outDir } from "astro:config/server";import { writeFileSync } from "node:fs";import { fileURLToPath } from "node:url";
export default function() {  return {    name: "internal-integration",    hooks: {      "astro:build:done": () => {        let file = new URL("result.json", outDir);        // generate data from some operation        let data = JSON.stringify([]);        writeFileSync(fileURLToPath(file), data, "utf-8");      }    }  }}
```

See more about the configuration imports available from `astro:config/server`:

*   [`i18n`](../../configuration-reference/index.md#i18n)
*   [`trailingSlash`](../../configuration-reference/index.md#trailingslash)
*   [`base`](../../configuration-reference/index.md#base)
*   [`build.format`](../../configuration-reference/index.md#buildformat)
*   [`build.client`](../../configuration-reference/index.md#buildclient)
*   [`build.server`](../../configuration-reference/index.md#buildserver)
*   [`site`](../../configuration-reference/index.md#site)
*   [`srcDir`](../../configuration-reference/index.md#srcdir)
*   [`cacheDir`](../../configuration-reference/index.md#cachedir)
*   [`outDir`](../../configuration-reference/index.md#outdir)
*   [`publicDir`](../../configuration-reference/index.md#publicdir)
*   [`root`](../../configuration-reference/index.md#root)
*   [`compressHTML`](../../configuration-reference/index.md#compresshtml)

## Imports from `astro/config`

[Section titled “Imports from astro/config”](#imports-from-astroconfig)

The following helpers are imported from the regular config module:

```
import {  defineConfig,  envField,  fontProviders,  getViteConfig,  mergeConfig,  passthroughImageService,  sessionDrivers,  sharpImageService,  validateConfig,} from "astro/config";
```

### `defineConfig()`

[Section titled “defineConfig()”](#defineconfig)

**Type:** `(config: [AstroUserConfig](../../configuration-reference/index.md)) => AstroUserConfig`

Configures your project with type safety [in a supported Astro configuration file](../../../guides/configuring-astro/index.md#the-astro-config-file).

### `envField`

[Section titled “envField”](#envfield)

**Type:** `object`  

**Added in:** `astro@5.0.0`

Describes the supported data types when [defining environment variables](../../configuration-reference/index.md#envschema).

Each data type must define the [variable type](../../../guides/environment-variables/index.md#variable-types) with `context` (`"client"` or `"server"`) and `access` (`"secret"` or `"public"`). In addition, you can define a `default` value, specify whether the variable is `optional` (default `false`), and some data types provide optional validation methods.

Learn more about [using type safe environment variables](../../../guides/environment-variables/index.md#type-safe-environment-variables) in your Astro project.

#### `envField.string()`

[Section titled “envField.string()”](#envfieldstring)

**Type:** `(options: StringFieldInput) => StringField`

Defines an environment variable of string type. You can perform [string validation with Zod](https://zod.dev/api#strings) using the following properties: `max`, `min`, `length`, `url`, `includes`, `startsWith`, and `endsWith`.

The following example defines the expected shape for an environment variable storing an API URL:

```
import { defineConfig, envField } from "astro/config";
export default defineConfig({  env: {    schema: {      API_URL: envField.string({        context: "client",        access: "public",        optional: false,        default: "",        min: 12,        url: true,        includes: "astro",        startsWith: "https",      }),    }  }})
```

#### `envField.number()`

[Section titled “envField.number()”](#envfieldnumber)

**Type:** `(options: NumberFieldInput) => NumberField`

Defines an environment variable of number type. You can perform [number validation with Zod](https://zod.dev/api#numbers) using the following properties: `gt`, `lt`, `min`, `max`, and `int`.

The following example defines the expected shape for an environment variable storing an API port:

```
import { defineConfig, envField } from "astro/config";
export default defineConfig({  env: {    schema: {      API_PORT: envField.number({        context: "server",        access: "public",        optional: true,        default: 4321,        min: 2,        int: true,      }),    }  }})
```

#### `envField.boolean()`

[Section titled “envField.boolean()”](#envfieldboolean)

**Type:** `(options: BooleanFieldInput) => BooleanField`

Defines an environment variable of boolean type.

The following example defines the expected shape for an environment variable storing whether analytics are enabled:

```
import { defineConfig, envField } from "astro/config";
export default defineConfig({  env: {    schema: {      ANALYTICS_ENABLED: envField.boolean({        context: "client",        access: "public",        optional: true,        default: true,      }),    }  }})
```

#### `envField.enum()`

[Section titled “envField.enum()”](#envfieldenum)

**Type:** `(options: EnumFieldInput<T>) => EnumField`

Defines an environment variable of enum type by providing the allowed `values` as an array.

The following example defines the expected shape for an environment variable storing the configured debug mode:

```
import { defineConfig, envField } from "astro/config";
export default defineConfig({  env: {    schema: {      DEBUG_MODE: envField.enum({        context: "server",        access: "public",        values: ['info', 'warnings', 'errors'], // required        optional: true,        default: 'errors',      }),    }  }})
```

### `fontProviders`

[Section titled “fontProviders”](#fontproviders)

**Type:** `object`  

**Added in:** `astro@6.0.0`

Describes the [built-in provider](../../font-provider-reference/index.md#built-in-providers) used [to retrieve the configured font](../../configuration-reference/index.md#fontprovider).

### `getViteConfig()`

[Section titled “getViteConfig()”](#getviteconfig)

**Type:** `(userViteConfig: [ViteUserConfig](../../configuration-reference/index.md#vite), inlineAstroConfig?: [AstroInlineConfig](../../configuration-reference/index.md)) => ViteUserConfigFn`

Retrieves the Vite configuration to use by merging a custom Vite configuration object and an optional Astro configuration object. This is useful [to set up Vitest for testing](../../../guides/testing/index.md#vitest).

### `mergeConfig()`

[Section titled “mergeConfig()”](#mergeconfig)

See [`mergeConfig()` in the Programmatic API reference](../../programmatic-reference/index.md#mergeconfig).

### `passthroughImageService()`

[Section titled “passthroughImageService()”](#passthroughimageservice)

**Type:** `() => [ImageServiceConfig](../astro-assets/index.md#imageserviceconfig)`

Retrieves a no-op image service. This is useful when your adapter does not support Astro’s built-in Sharp image optimization and you want to [use the `<Image />` and `<Picture />` components](../../../guides/images/index.md#astro-components-for-images).

The following example defines `passthroughImageService()` as image service in the Astro configuration file to avoid Sharp image processing:

```
import { defineConfig, passthroughImageService } from "astro/config";
export default defineConfig({  image: {    service: passthroughImageService()  }});
```

Learn more about [configuring a no-op passthrough service](../../../guides/images/index.md#configure-no-op-passthrough-service).

### `sessionDrivers`

[Section titled “sessionDrivers”](#sessiondrivers)

**Type:** `object`  

**Added in:** `astro@5.7.0`

Describes the [built-in driver](../../session-driver-reference/index.md#built-in-drivers) used [for session storage](../../configuration-reference/index.md#session-options).

The following example configures the Redis driver to enable sessions:

```
import { defineConfig, sessionDrivers } from "astro/config";
export default defineConfig({  session: {    driver: sessionDrivers.redis({      url: process.env.REDIS_URL    }),  }})
```

Learn more about [using sessions](../../../guides/sessions/index.md) in your Astro project.

### `sharpImageService()`

[Section titled “sharpImageService()”](#sharpimageservice)

**Type:** `(config?: SharpImageServiceConfig) => [ImageServiceConfig](../astro-assets/index.md#imageserviceconfig)`  

**Added in:** `astro@2.4.1`

Retrieves the Sharp service used to process Astro’s image assets. This takes an optional object describing the [configuration options for Sharp](../../configuration-reference/index.md#imageservice).

### `validateConfig()`

[Section titled “validateConfig()”](#validateconfig)

See [`validateConfig()` in the Programmatic API reference](../../programmatic-reference/index.md#validateconfig).

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
