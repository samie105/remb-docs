---
title: "Upgrade to Astro v6"
source: "https://docs.astro.build/en/guides/upgrade-to/v6/"
canonical_url: "https://docs.astro.build/en/guides/upgrade-to/v6/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:19.932Z"
content_hash: "1616814db89b15c867994495d796e968284c4072c74314cea08333d303a4ff17"
menu_path: ["Upgrade to Astro v6"]
section_path: []
nav_prev: {"path": "astro/en/upgrade-astro/index.md", "title": "Upgrade Astro"}
nav_next: {"path": "astro/en/guides/upgrade-to/v5/index.md", "title": "Upgrade to Astro v5"}
---

# Upgrade to Astro v6

This guide will help you migrate from Astro v5 to Astro v6.

Need to upgrade an older project to v5 first? See our [older migration guide](/en/guides/upgrade-to/v5/).

Need to see the v5 docs? Visit this [older version of the docs site (unmaintained v5.18.0 snapshot)](https://v5.docs.astro.build/).

## Upgrade Astro

[Section titled “Upgrade Astro”](#upgrade-astro)

Update your project’s version of Astro to the latest version using your package manager:

*   [npm](#tab-panel-1894)
*   [pnpm](#tab-panel-1895)
*   [Yarn](#tab-panel-1896)

```
# Upgrade Astro and official integrations togethernpx @astrojs/upgrade
```

You can also [upgrade your Astro integrations manually](/en/guides/integrations/#manual-upgrading) if needed, and you may also need to upgrade other dependencies in your project.

Astro v6.0 includes [potentially breaking changes](#breaking-changes), as well as the removal and deprecation of some features.

If your project doesn’t work as expected after upgrading to v6.0, check this guide for an overview of all breaking changes and instructions on how to update your codebase.

See [the Astro changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) for full release notes.

## Dependency Upgrades

[Section titled “Dependency Upgrades”](#dependency-upgrades)

Any major upgrades to Astro’s dependencies may cause breaking changes in your project.

### Node 22

[Section titled “Node 22”](#node-22)

[Implementation PR: feat!: drop node 18 and 20 (#14427)](https://github.com/withastro/astro/pull/14427)

Node 18 reached its End of Life in March 2025 and Node 20 is scheduled to reach its End of Life in April 2026.

Astro v6.0 drops Node 18 and Node 20 support entirely so that all Astro users can take advantage of Node’s more modern features.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do)

Check that both your development environment and your deployment environment are using **Node `22.12.0` or higher**.

1.  Check your local version of Node using:
    
    ```
    node -v
    ```
    
2.  Check your [deployment environment’s](/en/guides/deploy/) own documentation to verify that they support Node 22.
    
    You can specify Node `22.12.0` for your Astro project either in a dashboard configuration setting or a `.nvmrc` file.
    
    ```
    22.12.0
    ```
    

### Vite 7.0

[Section titled “Vite 7.0”](#vite-70)

[Implementation PR: feat: update vite (#14445)](https://github.com/withastro/astro/pull/14445)

Astro v6.0 upgrades to Vite v7.0 as the development server and production bundler.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-1)

If you are using Vite-specific plugins, configuration, or APIs, check the [Vite migration guide](https://vite.dev/guide/migration) for their breaking changes and upgrade your project as needed.

Using [Astro’s `getViteConfig()` helper](/en/guides/testing/#vitest) requires at least Vitest v3.2 or v4.1 beta 5.

### Vite Environment API

[Section titled “Vite Environment API”](#vite-environment-api)

[Implementation PR: feat: integrate vite environments (#14306)](https://github.com/withastro/astro/pull/14306)

Astro v6.0 introduces significant changes to how Astro manages different runtime environments (client, server, and prerender) after an internal refactor to use [Vite’s new Environments API](https://vite.dev/guide/api-environment).

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-2)

Integration and adapter maintainers should pay special attention to changes affecting these parts of the Integration API and Adapter API (full details included below with other breaking changes to these APIs):

*   [Rollup output file name config path](#changed-rollup-output-file-name-config-path-vite-config)
*   [integration hooks and HMR access patterns](#changed-integration-hooks-and-hmr-access-patterns-integration-api)
*   [`SSRManifest` structure](#changed-ssrmanifest-interface-structure-adapter-api)
*   [generating routes with `RouteData`](#removed-routedatagenerate-adapter-api)
*   [routes with percent-encoded percent signs (e.g. `%25`)](#removed-percent-encoding-in-routes)
*   [`astro:ssr-manifest` virtual module](#removed-astrossr-manifest-virtual-module-integration-api)
*   [`NodeApp` from `astro/app/node`](#deprecated-nodeapp-from-astroappnode-adapter-api)
*   [`loadManifest()` and `loadApp()` from `astro/app/node`](#deprecated-loadmanifest-and-loadapp-from-astroappnode-adapter-api)
*   [`createExports()` and `start()`](#deprecated-createexports-and-start-adapter-api)

### Zod 4

[Section titled “Zod 4”](#zod-4)

Astro v6.0 upgrades to Zod 4, a major dependency update that may require changes to custom Zod schemas in your project.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-3)

If you have custom Zod schemas in your `content.config.ts` or other configuration files, you’ll need to update them for Zod 4. Refer to the [Zod migration guide](https://zod.dev/v4/changelog) for detailed changes in the Zod API.

Notably, [many `string()` formats have been deprecated](https://zod.dev/v4/changelog#deprecates-email-etc) (e.g. `z.string().email()`, `z.string.url()`), and their APIs have been moved to the top-level `z` namespace. You may need to update how you validate form input for your Astro Actions:

```
email: z.string().email(),email: z.email(),
```

Additionally, Zod has made some [changes to handling error messages](https://zod.dev/v4/changelog#error-customization) and has dropped support for a custom `errorsMap` which was useful to redefine or translate your error messages. You may need to update any custom error messages:

```
z.string().min(5, { message: "Too short." });z.string().min(5, { error: "Too short." });
```

Also, if you use [`.default()` with transforms](https://zod.dev/v4/changelog#default-updates), you may need to update your schemas. In Zod 4, default values must match the output type (after transforms), not the input type. The default value short-circuits parsing when the input is `undefined`:

```
import { z } from 'astro/zod';
const blog = defineCollection({  schema: z.object({    // Zod 3: default matched input type (string)    views: z.string().transform(Number).default("0"),    // Zod 4: default must match output type (number)    views: z.string().transform(Number).default(0),  })});
```

For the old behavior where defaults are parsed, use the new `.prefault()` method.

These are only some of the many changes upgrading from Zod 3 to Zod 4. If you encounter any issues with your Zod schemas after upgrading to Astro 6, please consult the [Zod 4 changelog](https://zod.dev/v4/changelog) for complete upgrade guidance.

Additionally, a [community codemod](https://github.com/nicoespeon/zod-v3-to-v4), which can potentially automate some of these changes when migrating from Zod 3 to Zod 4, is also available.

You can ensure you’re the same version of Zod that Astro uses internally by [importing Zod from `astro/zod`](#deprecated-astroschema-and-z-from-astrocontent).

```
import { z } from 'astro/zod';
```

See more about [the `astro/zod` module](/en/reference/modules/astro-zod/).

### Shiki 4.0

[Section titled “Shiki 4.0”](#shiki-40)

[Implementation PR: chore(deps): update shiki to v4 (#15726)](https://github.com/withastro/astro/pull/15726)

Astro v6.0 upgrades to Shiki v4.0 for syntax highlighting.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-4)

If you are using Shiki-specific APIs, check the [Shiki migration guide](https://shiki.style/blog/v4) for their breaking changes and upgrade your project as needed.

### Official Astro integrations

[Section titled “Official Astro integrations”](#official-astro-integrations)

All of [Astro’s official server adapters](/en/guides/on-demand-rendering/#server-adapters) have also updated to a new major version to accompany the upgrade to Vite v7.0 with Vite’s Environment API as the development server and production bundler.

In particular, Astro’s Cloudflare adapter has undergone significant changes, and breaking changes to your existing Cloudflare setup are expected.

See the [Cloudflare adapter upgrade instructions](/en/guides/integrations-guide/cloudflare/#upgrading-to-v13-and-astro-6) for detailed migration guidance.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-5)

If you are using an Astro adapter for on-demand rendering or other platform-specific features, please check your specific adapter’s changelog for upgrade guidance:

*   [`@astrojs/cloudflare` CHANGELOG](https://github.com/withastro/astro/blob/next/packages/integrations/cloudflare/CHANGELOG.md)
*   [`@astrojs/netlify` CHANGELOG](https://github.com/withastro/astro/blob/next/packages/integrations/netlify/CHANGELOG.md)
*   [`@astrojs/node` CHANGELOG](https://github.com/withastro/astro/blob/next/packages/integrations/node/CHANGELOG.md)
*   [`@astrojs/vercel` CHANGELOG](https://github.com/withastro/astro/blob/next/packages/integrations/vercel/CHANGELOG.md)

## Legacy

[Section titled “Legacy”](#legacy)

The following features are now considered legacy features. They should function normally but are no longer recommended and are in maintenance mode. They will see no future improvements and documentation will not be updated. These features will eventually be deprecated, and then removed entirely.

### Legacy: content collections backwards compatibility

[Section titled “Legacy: content collections backwards compatibility”](#legacy-content-collections-backwards-compatibility)

In Astro 5.x, projects could delay upgrading to the new Content Layer API introduced for content collections because of some existing automatic backwards compatibility that was not previously behind a flag. This meant that it was possible to upgrade from Astro 4 to Astro 5 without updating your content collections, even if you had not enabled the `legacy.collections` flag. Projects would continue to build, and no errors or warnings would be displayed.

Astro v6.0 removes this automatic legacy content collections support, along with [the `legacy.collections` flag](#removed-legacy-content-collections). All content collections must now use [the Content Layer API introduced in Astro v5.0](https://astro.build/blog/content-layer-deep-dive/) that powers all content collections.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-6)

If you experience content collections errors after updating to v6, [check your project for any removed legacy features](#if-you-have) that may need updating to the Content Layer API.

See [the Astro v5 upgrade guide](/en/guides/upgrade-to/v5/#legacy-v20-content-collections-api) for detailed instructions on upgrading legacy collections to the new Content Layer API.

If you are unable to update immediately, you can enable [the `legacy.collectionsBackwardsCompat` flag](/en/reference/legacy-flags/#collectionsbackwardscompat) as a temporary migration helper:

```
export default defineConfig({  legacy: {    collectionsBackwardsCompat: true,  },});
```

This flag preserves some legacy v4 content collections features:

*   Supports the legacy configuration file `src/content/config.ts`
*   Supports `type: 'content'` and `type: 'data'` without loaders
*   Preserves legacy entry API: `entry.slug` and `entry.render()`
*   Uses path-based entry IDs instead of slug-based IDs

**This is a temporary migration helper.** Migrate your collections to the Content Layer API as soon as possible, then disable this flag.

## Deprecated

[Section titled “Deprecated”](#deprecated)

The following deprecated features are no longer supported and are no longer documented. Please update your project accordingly.

Some deprecated features may temporarily continue to function until they are completely removed. Others may silently have no effect, or throw an error prompting you to update your code.

### Deprecated: `Astro` in `getStaticPaths()`

[Section titled “Deprecated: Astro in getStaticPaths()”](#deprecated-astro-in-getstaticpaths)

[Implementation PR: feat: deprecate Astro in getStaticPaths (#14432)](https://github.com/withastro/astro/pull/14432)

In Astro 5.x, it was possible to access an `Astro` object inside `getStaticPaths()`. However, despite being typed the same as the `Astro` object accessible in the frontmatter, this object only had `site` and `generator` properties. This could lead to confusion about which `Astro` object properties were available inside `getStaticPaths()`.

Astro 6.0 deprecates this object for `getStaticPaths()` to avoid confusion and improves error handling when attempting to access `Astro` values that are unavailable. Using `Astro.site` or `Astro.generator` within `getStaticPaths()` will now log a deprecation warning, and accessing any other property will throw a specific error with a helpful message. In a future major version, this object will be removed entirely, and accessing `Astro.site` or `Astro.generator` will also throw an error.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-7)

Update your `getStaticPaths()` function if you were attempting to access any `Astro` properties inside its scope. Remove `Astro.generator` entirely, and replace all occurrences of `Astro.site` with `import.meta.env.SITE`:

```
---import { getPages } from "../../../utils/data";
export async function getStaticPaths() {  console.log(Astro.generator);  return getPages(Astro.site);  return getPages(import.meta.env.SITE);}---
```

Read more about [built-in environment variables such as `import.meta.env.SITE`](/en/guides/environment-variables/#default-environment-variables) that are accessible when [using `getStaticPaths()` to dynamically generate static routes](/en/guides/routing/#static-ssg-mode).

### Deprecated: `import.meta.env.ASSETS_PREFIX`

[Section titled “Deprecated: import.meta.env.ASSETS\_PREFIX”](#deprecated-importmetaenvassets_prefix)

[Implementation PR: feat: deprecate import.meta.env.ASSETS\_PREFIX (#14461)](https://github.com/withastro/astro/pull/14461)

In Astro 5.x, it was possible to access `build.assetsPrefix` in your Astro config via the built-in environment variable `import.meta.env.ASSETS_PREFIX`. However, Astro v5.7.0 introduced the `astro:config` virtual module to expose a non-exhaustive, serializable, type-safe version of the Astro configuration which included access to `build.assetsPrefix` directly. This became the preferred way to access the prefix for Astro-generated asset links when set, although the environment variable still existed.

Astro 6.0 deprecates this variable in favor of `build.assetsPrefix` from the `astro:config/server` module.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-8)

Replace any occurrences of `import.meta.env.ASSETS_PREFIX` with the `build.assetsPrefix` import from `astro:config/server`. This is a drop-in replacement to provide the existing value, and no other changes to your code should be necessary:

```
import { someLogic } from "./utils"import { build } from "astro:config/server"
someLogic(import.meta.env.ASSETS_PREFIX)someLogic(build.assetsPrefix)
```

Read more about the [`astro:config` virtual module](/en/reference/modules/astro-config/).

### Deprecated: `astro:schema` and `z` from `astro:content`

[Section titled “Deprecated: astro:schema and z from astro:content”](#deprecated-astroschema-and-z-from-astrocontent)

[Implementation PR: feat!: consolidate zod export (#14923)](https://github.com/withastro/astro/pull/14923)

In Astro 5.x, `astro:schema` was introduced as an alias of `astro/zod`. `z` was also exported from `astro:content` for convenience. However this occasionally created confusion for users who were unsure about where they should be importing from.

Astro 6.0 deprecates `astro:schema` and `z` from `astro:content` in favor of `astro/zod`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-9)

Replace any occurrences of `astro:schema` with `astro/zod`:

```
import { z } from "astro:schema"import { z } from "astro/zod"
```

Remove `z` from your `astro:content` imports and import `z` separately from `astro/zod` instead:

```
import { defineCollection, z } from "astro:content"import { defineCollection } from "astro:content"import { z } from "astro/zod"
```

See more about [defining collection schemas with Zod](/en/guides/content-collections/#defining-datatypes-with-zod).

### Deprecated: exposed `astro:transitions` internals

[Section titled “Deprecated: exposed astro:transitions internals”](#deprecated-exposed-astrotransitions-internals)

[Implementation PR: feat!: deprecate transitions exports (#14989)](https://github.com/withastro/astro/pull/14989)

In Astro 5.x, some internals were exported from `astro:transitions` and `astro:transitions/client` that were not meant to be exposed for public use.

Astro 6.0 removes the following functions and types as exports from the `astro:transitions` and `astro:transitions/client` virtual modules. These can no longer be imported in your project files:

*   `createAnimationScope()`
*   `isTransitionBeforePreparationEvent()`
*   `isTransitionBeforeSwapEvent()`
*   `TRANSITION_BEFORE_PREPARATION`
*   `TRANSITION_AFTER_PREPARATION`
*   `TRANSITION_BEFORE_SWAP`
*   `TRANSITION_AFTER_SWAP`
*   `TRANSITION_PAGE_LOAD`

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-10)

Remove any occurrences of `createAnimationScope()`:

```
import { createAnimationScope } from 'astro:transitions';
```

Update any occurrences of the other deprecated exports:

```
import {  isTransitionBeforePreparationEvent,  TRANSITION_AFTER_SWAP,} from 'astro:transitions/client';
console.log(isTransitionBeforePreparationEvent(event));console.log(event.type === 'astro:before-preparation');
console.log(TRANSITION_AFTER_SWAP);console.log('astro:after-swap');
```

Learn more about all utilities available in the [View Transitions Router API Reference](/en/reference/modules/astro-transitions/).

### Deprecated: session driver string signature

[Section titled “Deprecated: session driver string signature”](#deprecated-session-driver-string-signature)

[Implementation PR: feat(sessions): drivers (#15006)](https://github.com/withastro/astro/pull/15006)

In Astro 5.x, any [unstorage provider](https://unstorage.unjs.io/drivers) name or a custom entrypoint could be provided to define a session driver, and options were also provided directly to the `session` configuration. However, we felt that this API was limited and inconsistent with other parts of the Astro config.

Astro 6.0 deprecates the driver string signature and options in favor of a new object shape.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-11)

Update your session config to use the newly exported `sessionDrivers`:

```
import { defineConfig } from 'astro/config'import { defineConfig, sessionDrivers } from 'astro/config'
export default defineConfig({  session: {    driver: 'redis',    options: {      url: process.env.REDIS_URL    },    driver: sessionDrivers.redis({      url: process.env.REDIS_URL    }),    cookie: {      secure: true    },    ttl: 3600  }})
```

Learn more about [available session drivers](/en/reference/session-driver-reference/#building-a-session-driver).

### Deprecated: `NodeApp` from `astro/app/node` (Adapter API)

[Section titled “Deprecated: NodeApp from astro/app/node (Adapter API)”](#deprecated-nodeapp-from-astroappnode-adapter-api)

[Implementation PR: feat: deprecate NodeApp (#15535)](https://github.com/withastro/astro/pull/15535)

In Astro 5.x, adapters could implement their server entrypoint using `App` for standard web requests/responses, or `NodeApp` for node requests/responses.

Astro 6.0 deprecates `NodeApp` in favor of `createApp()` and new utilities: `createRequest()` and `writeResponse()`. This allows a more consistent API while preserving the same features as before. It also deprecates the `NodeAppHeadersJson` type.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-12)

If you have built an adapter, update any usage of `NodeApp` with `createApp()`:

```
import { NodeApp } from 'astro/app/node';
export function createExports(manifest) {  const app = new NodeApp(manifest);
  const handler = async (req, res) => {    const response = await app.render(req);    await NodeApp.writeResponse(response, res);  };
  return { handler };}import { createApp } from 'astro/app/entrypoint';import { createRequest, writeResponse } from 'astro/app/node';
const app = createApp();
export const handler = async (req, res) => {  const request = createRequest(req);  const response = await app.render(request);  await writeResponse(response, res);}
```

Learn more about [the `astro/app/node` module](/en/reference/modules/astro-app/#imports-from-astroappnode).

### Deprecated: `loadManifest()` and `loadApp()` from `astro/app/node` (Adapter API)

[Section titled “Deprecated: loadManifest() and loadApp() from astro/app/node (Adapter API)”](#deprecated-loadmanifest-and-loadapp-from-astroappnode-adapter-api)

[Implementation PR: feat: deprecate NodeApp (#15535)](https://github.com/withastro/astro/pull/15535)

In Astro 5.x, the `astro/app/node` exposed `loadManifest()` and `loadApp()` utilities to allow loading the SSR manifest or a `NodeApp` instance from a `URL` instance. However, these were not documented and are no longer recommended usage with the v6 Adapter API.

Astro 6.0 deprecates both functions.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-13)

If you have built an adapter, remove `loadManifest()` and replace `loadApp()` by `createApp()`:

```
import { loadManifest, loadApp, NodeApp } from 'astro/app/node';
const manifest = await loadManifest(new URL(import.meta.url));const app1 = new NodeApp(loadManifest);const app2 = await loadApp(new URL(import.meta.url));import { createApp } from 'astro/app/entrypoint';
const app = createApp();
```

Learn more about [the `astro/app/entrypoint` module](/en/reference/modules/astro-app/#imports-from-astroappentrypoint).

### Deprecated: `createExports()` and `start()` (Adapter API)

[Section titled “Deprecated: createExports() and start() (Adapter API)”](#deprecated-createexports-and-start-adapter-api)

[Implementation PR: feat: improve naming of new adapter api (#15461)](https://github.com/withastro/astro/pull/15461)

In Astro 5.x, adapters had to provide the exports required by the host in their server entrypoint using a `createExports()` function before passing them to `setAdapter()` as an `exports` list.

Astro 6.0 introduces a simpler yet more powerful way of making server entrypoints. This relies on passing a new option `entrypointResolution: "auto"` to `setAdapter()`.

However, for backwards compatibility with existing adapters, the default value of `entrypointResolution` (`"explicit"`) mimics Astro 5.x API behavior. This means that your adapters can continue to function until you can fully migrate your adapter to the `auto` value, as shown below.

Note that `entrypointResolution: "explicit"` (maintaining v5 API behavior) is considered deprecated usage, but the option has been provided so that no immediate change to your adapter is required and to allow adapter authors time to update. This option will be removed in a future major version in favor of all adapters using `entrypointResolution: "auto"`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-14)

If you are an adapter author with a public repository and [include the `astro-adapter` keyword in your `package.json`](/en/guides/integrations/#categories), the Astro core team will attempt to make a PR to your repository directly to help you migrate your code if you have not yet followed the steps below.

If you are seeing warnings because you are using a community adapter that is not yet updated, please reach out to the adapter author directly to let them know. It is ultimately their responsibility to update their adapters. You can also let the Astro core team know in the [`#integrations` channel of our Discord](https://astro.build/chat) and we will attempt to help the adapter author upgrade.

If you have built an adapter, follow these steps to remove the legacy v5 behavior:

1.  Update your `setAdapter()`: set `entrypointResolution: "auto"`, remove `exports` and `args`
    
    ```
    setAdapter({  // ...  entrypointResolution: 'auto',  exports: ['handler'],  args: { assets: config.build.assets }})
    ```
    
2.  Update your server entrypoint to provide any required exports without `createExports()`:
    
    ```
    import { App } from 'astro/app';
    export function createExports(manifest) {  const app = new App(manifest);
      const handler = (event, context) => {    // ...  };
      return { handler };}import { createApp } from 'astro/app/entrypoint';
    const app = createApp();
    export const handler = (event, context) => {  // ...}
    ```
    
3.  If your adapter provides a `start()` function, update your server entrypoint to call the code directly:
    
    ```
    import { App } from 'astro/app';
    export function start(manifest) {  const app = new App(manifest);
      addEventListener('fetch', event => {    // ...  });}import { createApp } from 'astro/app/entrypoint';
    const app = createApp();
    addEventListener('fetch', event => {  // ...});
    ```
    
4.  If you were relying on `args`, [create a virtual module to pass the build time configuration](/en/reference/adapter-reference/#passing-build-time-configuration) and import them from the virtual module instead:
    
    ```
    export function createExports(manifest, { assets }) {  // ...}import { assets } from 'virtual:@example/my-adapter:config';
    ```
    

Learn more about [the Adapter API](/en/reference/adapter-reference/).

## Removed

[Section titled “Removed”](#removed)

The following features have now been entirely removed from the code base and can no longer be used. Some of these features may have continued to work in your project even after deprecation. Others may have silently had no effect.

Projects now containing these removed features will be unable to build, and there will no longer be any supporting documentation prompting you to remove these features.

### Removed: legacy content collections

[Section titled “Removed: legacy content collections”](#removed-legacy-content-collections)

[Implementation PR: fix: remove legacy content collections (#14407)](https://github.com/withastro/astro/pull/14407)

In Astro 5.x, it was still possible to use [the original Content Collections API first introduced in Astro v2.0](https://astro.build/blog/introducing-content-collections/), **either through a `legacy` configuration flag or via built-in backwards compatibility**. These methods allowed you to upgrade to Astro v5 even if you were not yet ready or able to update your existing content collections to those powered by the new Content Layer API.

Astro v6.0 removes this previously deprecated Content Collections API support entirely, including the `legacy.collections` flag **and some existing backwards compatibility that was not previously behind a flag**. All content collections must now use [the Content Layer API introduced in Astro v5.0](https://astro.build/blog/content-layer-deep-dive/) that powers all content collections. **No backwards compatibility support is available.**

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-15)

If you had previously enabled the legacy flag, you must remove it.

```
import { defineConfig } from 'astro/config';
export default defineConfig({  legacy: {    collections: true,  }})
```

Additionally, if you did not upgrade your collections for Astro v5.0, ensure that your content collections are **fully updated** for the new API.

Astro v5.x included some automatic backwards compatibility to allow content collections to continue to work even if they had not been updated to use the new API. Therefore, your v5 collections may contain one or more legacy features that need updating to the newer API for v6, even if your project was previously error-free.

If you have [content collections errors](/en/reference/error-reference/#content-collection-errors) or warnings after upgrading to v6, use the following list to help you identify and upgrade any legacy features that may exist in your code.

##### If you have…

[Section titled “If you have…”](#if-you-have)

no content collections configuration file Create `src/content.config.ts` and [define your collections](/en/guides/content-collections/#defining-build-time-content-collections) in it.

a configuration file located at `src/content/config.ts` / ([`LegacyContentConfigError`](/en/reference/errors/legacy-content-config-error/)) Rename and move this file to `src/content.config.ts`

a collection that does not define a `loader` / ([`ContentCollectionMissingALoaderError`](/en/reference/errors/content-collection-missing-loader/))

Import [Astro’s built-in `glob()` loader](/en/guides/content-collections/#the-glob-loader) and define the `pattern` and `base` for your collection entries:

```
import { defineCollection } from 'astro:content';import { z } from 'astro/zod';import { glob } from 'astro/loaders';
const blog = defineCollection({  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/data/blog" }),  schema: z.object({    title: z.string(),    description: z.string(),    pubDate: z.coerce.date(),    updatedDate: z.coerce.date().optional(),  }),});
```

a collection that defines a collection type (`type: 'content'` or `type: 'data'`) / ([`ContentCollectionInvalidTypeError`](/en/reference/errors/content-collection-invalid-type/)) There are no longer different types of collections. This must be deleted from your collection definition.

```
import { defineCollection } from 'astro:content';import { z } from 'astro/zod';import { glob } from 'astro/loaders';
const blog = defineCollection({  // For content layer you no longer define a `type`  type: 'content',  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/data/blog" }),  schema: z.object({    title: z.string(),    description: z.string(),    pubDate: z.coerce.date(),    updatedDate: z.coerce.date().optional(),  }),});
```

legacy collection querying methods `getDataEntryById()` and `getEntryBySlug()` / ([`GetEntryDeprecationError`](/en/reference/errors/get-entry-deprecation-error/)) Replace both methods with [`getEntry()`](/en/reference/modules/astro-content/#getentry).

legacy collection querying and rendering methods that depend on a `slug` property / ([`ContentSchemaContainsSlugError`](/en/reference/errors/content-schema-contains-slug-error/)) Previously, the `id` was based on the filename, and there was a `slug` property that could be used in a URL. Now the [`CollectionEntry`](/en/reference/modules/astro-content/#collectionentry) `id` is a slug. If you need access to the filename (previously available as the `id`), use the `filePath` property. Replace instances of `slug` with `id`:

```
---export async function getStaticPaths() {  const posts = await getCollection('blog');  return posts.map((post) => ({    params: { slug: post.slug },    params: { slug: post.id },    props: post,  }));}---
```

content rendered using `entry.render()` Collection entries no longer have a `render()` method. Instead, import the `render()` function from `astro:content` and use `render(entry)`:

```
---import { getEntry, render } from 'astro:content';
const post = await getEntry('pages', 'homepage');
const { Content, headings } = await post.render();const { Content, headings } = await render(post);---<Content />
```

See [the Astro v5 upgrade guide](/en/guides/upgrade-to/v5/#legacy-v20-content-collections-api) for previous guidance about backwards compatibility of legacy collections in Astro v5 and full step-by-step instructions for upgrading legacy collections to the new Content Layer API.

### Removed: `<ViewTransitions />` component

[Section titled “Removed: <ViewTransitions /> component”](#removed-viewtransitions--component)

[Implementation PR: Remove deprecated ViewTransitions component (#14400)](https://github.com/withastro/astro/pull/14400)

In Astro 5.0, the `<ViewTransitions />` component was renamed to `<ClientRouter />` to clarify the role of the component. The new name makes it more clear that the features you get from Astro’s `<ClientRouter />` routing component are slightly different from the native CSS-based MPA router. However, a deprecated version of the `<ViewTransitions />` component still existed and may have functioned in Astro 5.x.

Astro 6.0 removes the `<ViewTransitions />` component entirely and it can no longer be used in your project. Update to the `<ClientRouter />` component to continue to use these features.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-16)

Replace all occurrences of the `ViewTransitions` import and component with `ClientRouter`:

```
import { ViewTransitions } from 'astro:transitions';import { ClientRouter } from 'astro:transitions';
<html>  <head>    ...    <ViewTransitions />    <ClientRouter />  </head></html>
```

Read more about [view transitions and client-side routing in Astro](/en/guides/view-transitions/).

### Removed: `emitESMImage()`

[Section titled “Removed: emitESMImage()”](#removed-emitesmimage)

[Implementation PR: feat!: remove emitESMImage() (#14426)](https://github.com/withastro/astro/pull/14426)

In Astro 5.6.2, the `emitESMImage()` function was deprecated in favor of `emitImageMetadata()`, which removes two deprecated arguments that were not meant to be exposed for public use: `_watchMode` and `experimentalSvgEnabled`.

Astro 6.0 removes `emitESMImage()` entirely. Update to `emitImageMetadata()` to keep your current behavior.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-17)

Replace all occurrences of the `emitESMImage()` with `emitImageMetadata()` and remove unused arguments:

```
import { emitESMImage } from 'astro/assets/utils';import { emitImageMetadata } from 'astro/assets/utils';
const imageId = '/images/photo.jpg';const result = await emitESMImage(imageId, false, false);const result = await emitImageMetadata(imageId);
```

Read more about [`emitImageMetadata()`](/en/reference/modules/astro-assets/#emitimagemetadata).

### Removed: `Astro.glob()`

[Section titled “Removed: Astro.glob()”](#removed-astroglob)

[Implementation PR: feat!: remove Astro.glob (#14421)](https://github.com/withastro/astro/pull/14421)

In Astro 5.0, `Astro.glob()` was deprecated in favor of using `getCollection()` to query your collections, and `import.meta.glob()` to query other source files in your project.

Astro 6.0 removes `Astro.glob()` entirely. Update to `import.meta.glob()` to keep your current behavior.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-18)

Replace all use of `Astro.glob()` with `import.meta.glob()`. Note that `import.meta.glob()` no longer returns a `Promise`, so you may have to update your code accordingly. You should not require any updates to your [glob patterns](/en/guides/imports/#glob-patterns).

```
---const posts = await Astro.glob('./posts/*.md');const posts = Object.values(import.meta.glob('./posts/*.md', { eager: true }));---
{posts.map((post) => <li><a href={post.url}>{post.frontmatter.title}</a></li>)}
```

Where appropriate, consider using [content collections](/en/guides/content-collections/) to organize your content, which has its own newer, more performant querying functions.

You may also wish to consider using glob packages from NPM, such as [`fast-glob`](https://www.npmjs.com/package/fast-glob).

Learn more about [importing files with `import.meta.glob`](/en/guides/imports/#importmetaglob).

### Removed: exposed `astro:actions` internals

[Section titled “Removed: exposed astro:actions internals”](#removed-exposed-astroactions-internals)

[Implementation PR: refactor: cleanup public actions API (#14844)](https://github.com/withastro/astro/pull/14844)

In Astro 5.x, some internals were exported from `astro:actions` that were not meant to be exposed for public use.

Astro 6.0 removes the following functions, classes and types as exports from the `astro:actions` virtual module. These can no longer be imported in your project files:

*   `ACTION_ERROR_CODES`
*   `ActionInputError`
*   `appendForwardSlash`
*   `astroCalledServerError`
*   `callSafely`
*   `deserializeActionResult`
*   `formDataToObject`
*   `getActionQueryString`
*   `serializeActionResult`
*   `type Actions`
*   `type ActionAccept`
*   `type AstroActionContext`
*   `type SerializedActionResult`

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-19)

Replace all imports of `serializeActionResult()` and `deserializeActionResult()` with `getActionContext()`. These two methods are now available through `getActionContext()`:

```
import { defineMiddleware } from 'astro:middleware';import { serializeActionResult, deserializeActionResult } from 'astro:actions';import { getActionContext } from 'astro:actions';
export const onRequest = defineMiddleware(async (context, next) => {  const { serializeActionResult, deserializeActionResult } = getActionContext(context);  // ...});
```

Remove any occurrences of the other removed exports:

```
import {  ACTION_ERROR_CODES,  ActionInputError,  appendForwardSlash,  astroCalledServerError,  callSafely,  formDataToObject,  getActionQueryString,  type Actions,  type ActionAccept,  type AstroActionContext,  type SerializedActionResult,} from 'astro:actions';
```

Learn more about all utilities available in the [Actions API Reference](/en/reference/modules/astro-actions/).

### Removed: Percent-Encoding in routes

[Section titled “Removed: Percent-Encoding in routes”](#removed-percent-encoding-in-routes)

[Implementation PR: feat: integrate vite environments (#14306)](https://github.com/withastro/astro/pull/14306)

In Astro 5.x, it was possible to include a percent-encoded percent sign (`%25`) in filenames.

Astro 6.0 removes support for the characters `%25` in filenames for security reasons. This restriction prevents encoding-based security bypasses where `%25` decodes to `%`, potentially leading to ambiguous or invalid encoding sequences.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-20)

If you have route files with `%25` in the filename, rename them to use a different character:

```
src/pages/test%25file.astrosrc/pages/test-file.astro
```

### Removed: `astro:ssr-manifest` virtual module (Integration API)

[Section titled “Removed: astro:ssr-manifest virtual module (Integration API)”](#removed-astrossr-manifest-virtual-module-integration-api)

[Implementation PR: feat: integrate vite environments (#14306)](https://github.com/withastro/astro/pull/14306)

In Astro 5.x, the deprecated `astro:ssr-manifest` virtual module could still be used to access configuration values.

Astro 6.0 removes the `astro:ssr-manifest` virtual module entirely. It is no longer used by integrations or internally by Astro. The manifest is now passed directly through integration hooks and adapter APIs rather than through a virtual module. For build-specific manifest data, use the `astro:build:ssr` integration hook, which receives the manifest as a parameter.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-21)

If your integration or code imports from `astro:ssr-manifest`, use `astro:config/server` instead to access configuration values:

```
import { manifest } from 'astro:ssr-manifest';import { srcDir, outDir, root } from 'astro:config/server';// Use srcDir, outDir, root, etc. for configuration values
```

Learn more about [the `astro:config` virtual module](/en/reference/modules/astro-config/).

### Removed: `RouteData.generate()` (Adapter API)

[Section titled “Removed: RouteData.generate() (Adapter API)”](#removed-routedatagenerate-adapter-api)

[Implementation PR: feat: integrate vite environments (#14306)](https://github.com/withastro/astro/pull/14306)

In Astro 5.x, routes could be generated using the `generate()` method on `RouteData`.

Astro 6.0 removes `RouteData.generate()` because route generation is now handled internally by Astro.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-22)

Remove any calls to `route.generate()` in your code. This method is no longer needed:

```
const generated = route.generate(params);
```

Learn more about [the Adapter API](/en/reference/adapter-reference/).

### Removed: `routes` on `astro:build:done` hook (Integration API)

[Section titled “Removed: routes on astro:build:done hook (Integration API)”](#removed-routes-on-astrobuilddone-hook-integration-api)

[Implementation PR: feat: cleanup integration api (#14446)](https://github.com/withastro/astro/pull/14446)

In Astro 5.0, accessing `routes` on the `astro:build:done` hook was deprecated.

Astro 6.0 removes the `routes` array passed to this hook entirely. Instead, the `astro:routes:resolved` hook should be used.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-23)

Remove any instance of `routes` passed to `astro:build:done` and replace it with the new `astro:routes:resolved` hook. Access `distURL` on the newly exposed `assets` map:

```
const integration = () => {    let routes    return {        name: 'my-integration',        hooks: {            'astro:routes:resolved': (params) => {                routes = params.routes            },            'astro:build:done': ({                routes                assets            }) => {                for (const route of routes) {                    const distURL = assets.get(route.pattern)                    if (distURL) {                        Object.assign(route, { distURL })                    }                }                console.log(routes)            }        }    }}
```

Learn more about [the Integration API `astro:routes:resolved` hook](/en/reference/integrations-reference/#astroroutesresolved) for building integrations.

### Removed: `entryPoints` on `astro:build:ssr` hook (Integration API)

[Section titled “Removed: entryPoints on astro:build:ssr hook (Integration API)”](#removed-entrypoints-on-astrobuildssr-hook-integration-api)

[Implementation PR: feat: cleanup integration api (#14446)](https://github.com/withastro/astro/pull/14446)

In Astro 5.0, [`functionPerRoute` was deprecated](/en/guides/upgrade-to/v5/#deprecated-functionperroute-adapter-api). That meant that `entryPoints` on the `astro:build:ssr` hook was always empty.

Astro 6.0 removes the `entryPoints` map passed to this hook entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-24)

Remove any instance of `entryPoints` passed to `astro:build:ssr`:

```
const integration = () => {    return {        name: 'my-integration',        hooks: {            'astro:build:ssr': (params) => {                someLogic(params.entryPoints)            },        }    }}
```

### Removed: old `app.render()` signature (Adapter API)

[Section titled “Removed: old app.render() signature (Adapter API)”](#removed-old-apprender-signature-adapter-api)

[Implementation PR: feat: clean deprecated APIs (#14462)](https://github.com/withastro/astro/pull/14462)

In Astro 4.0, the `app.render()` signature that allowed passing `routeData` and `locals` as optional arguments was deprecated in favor of a single optional `renderOptions` argument.

Astro 6.0 removes this signature entirely. Attempting to pass these separate arguments will now cause an error in your project.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-25)

Review your `app.render()` calls and pass `routeData` and `locals` as properties of an object instead of as multiple independent arguments:

```
app.render(request, routeData, locals)app.render(request, { routeData, locals })
```

Learn more about the [Adapter API](/en/reference/adapter-reference/).

### Removed: `app.setManifestData()` (Adapter API)

[Section titled “Removed: app.setManifestData() (Adapter API)”](#removed-appsetmanifestdata-adapter-api)

[Implementation PR: chore(astro)!: remove app.setManifestData() (#14758)](https://github.com/withastro/astro/pull/14758)

In Astro 5.0, the `app.setManifestData()` method was available on `App` and `NodeApp`, but is no longer used nor needed.

Astro 6.0 removes this method entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-26)

Remove any call to `app.setManifestData()`. If you need to update the manifest, create a new `App` instance.

Learn more about the [Adapter API](/en/reference/adapter-reference/).

### Removed: `handleForms` prop for the `<ClientRouter />` component

[Section titled “Removed: handleForms prop for the <ClientRouter /> component”](#removed-handleforms-prop-for-the-clientrouter--component)

[Implementation PR: feat: clean deprecated APIs (#14462)](https://github.com/withastro/astro/pull/14462)

In Astro 4.0, the `handleForms` prop of the `<ClientRouter />` component was deprecated, as it was no longer necessary to opt in to handling `submit` events for `form` elements. This functionality has been built in by default and the property, if still included in your project, silently had no impact on form submission.

Astro 6.0 removes this prop entirely and it now must be removed to avoid errors in your project.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-27)

Remove the `handleForms` property from your `<ClientRouter />` component if it exists. It has provided no additional functionality, and so removing it should not change any behavior in your project:

```
---import { ClientRouter } from "astro:transitions";---<html>  <head>    <ClientRouter handleForms />  </head>  <body>    <!-- stuff here -->  </body></html>
```

Learn more about [transitions with forms](/en/guides/view-transitions/#transitions-with-forms).

### Removed: `prefetch()` `with` option

[Section titled “Removed: prefetch() with option”](#removed-prefetch-with-option)

[Implementation PR: feat: clean deprecated APIs (#14462)](https://github.com/withastro/astro/pull/14462)

In Astro 4.8.4, the `with` option of the programmatic `prefetch()` function was deprecated in favor of a more sensible default behavior that no longer required specifying the priority of prefetching for each page.

Astro 6.0 removes this option entirely and it is no longer possible to configure the priority of prefetching by passing the `with` option. Attempting to do so will now cause errors.

By default, Astro’s prefetching now uses an automatic approach that will always try to use `<link rel="prefetch>` if supported, or will fall back to `fetch()`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-28)

Review your `prefetch()` calls and remove the `with` option if it still exists:

```
prefetch('/about', { with: 'fetch' });prefetch('/about');
```

Learn more about [prefetching](/en/guides/prefetch/).

### Removed: `rewrite()` from Actions context

[Section titled “Removed: rewrite() from Actions context”](#removed-rewrite-from-actions-context)

[Implementation PR: feat!: remove rewrite from action context (#14477)](https://github.com/withastro/astro/pull/14477)

In Astro 5.5.6, the `ActionAPIContext.rewrite()` method was deprecated because custom endpoints should be used instead of rewrites.

Astro 6.0 removes the `rewrite()` method from `ActionAPIContext` entirely and it may no longer be used.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-29)

Review your Actions handlers and remove any call to `rewrite()`:

```
import { defineAction } from 'astro:actions';import { z } from 'astro/zod';
export const server = {  getGreeting: defineAction({    input: z.object({      // ...    }),    handler: async (input, context) => {      context.rewrite('/')      // ...    }  })}
```

Learn more about [rewrites](/en/guides/routing/#rewrites).

### Removed: schema function signature (Content Loader API)

[Section titled “Removed: schema function signature (Content Loader API)”](#removed-schema-function-signature-content-loader-api)

[Implementation PR: feat: loader.createSchema() (#14759)](https://github.com/withastro/astro/pull/14759)

In Astro 5.x, a content loader could choose to define a schema as a function instead of defining a Zod schema object for validation. This is useful to dynamically generate the schema based on the configuration options or by introspecting an API.

Astro 6.0 removes this signature and introduces a new `createSchema()` property as a replacement for those who still want to dynamically define a schema in their content loader.

Providing a schema function in the old way will log a warning message that the loader’s schema is being ignored, but otherwise the loader will continue to work as if no schema had been provided. In a future major version, loaders that provide a schema function will throw an error and cannot be used.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-30)

If you are building a content loader and using a function to dynamically return a collection `schema` property, you must remove your existing function and use the new `createSchema()` property to define your schema instead.

For example, you can reproduce Astro’s previous behavior by using `zod-to-ts` directly with `createSchema()` and any previous function logic:

```
import type { Loader } from 'astro/loaders'import { createTypeAlias, zodToTs } from 'zod-to-ts'import { getSchemaFromApi } from './utils'
function myLoader() {  return {    name: 'my-loader',    load: async (context) => {      // ...    },    schema: async () => await getSchemaFromApi(),    createSchema: async () => {      const schema = await getSchemaFromApi()      const identifier = 'Entry'      const { node } = zodToTs(schema, identifier)      const typeAlias = createTypeAlias(node, identifier)
      return {        schema,        types: `export ${typeAlias}`      }    }  } satisfies Loader}
```

Learn more about [`createSchema()`](/en/reference/content-loader-reference/#loadercreateschema) in the Content Loader API reference.

### Removed: session `test` driver

[Section titled “Removed: session test driver”](#removed-session-test-driver)

[Implementation PR: feat(sessions): drivers (#15006)](https://github.com/withastro/astro/pull/15006)

In Astro 5.x, the internal session `test` driver was exported in the Astro config types, but it was not meant to be exposed for public use.

Astro 6.0 removes the session `test` driver as it is no longer used internally to test `context.session`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-31)

It is unlikely that you are using this internal API. If you do, you must remove any usage of the session `test` driver:

```
import { defineConfig } from 'astro/config'import { createMockStorage } from './utils'
export default defineConfig({  session: {    driver: 'test',    options: {      mockStorage: createMockStorage()    }  }})
```

Learn more about the [Session Driver API](/en/reference/session-driver-reference/).

### Removed: support for CommonJS config files

[Section titled “Removed: support for CommonJS config files”](#removed-support-for-commonjs-config-files)

[Implementation PR: Drop cjs config support (#15192)](https://github.com/withastro/astro/pull/15192)

In Astro 5.x, the Astro config file could use any of the following extensions: `.mjs`, `.js`, `.ts`, `.mts`, `.cjs` and `.cts`.

Astro 6.0 removes `.cjs` and `.cts` extensions.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-32)

If you have a `astro.config.cjs` or `astro.config.cts` file, update it to use of the supported extensions: `.mjs`, `.js`, `.ts` or `.mts`.

Learn more about the [Astro config file](/en/guides/configuring-astro/#the-astro-config-file).

### Experimental Flags

[Section titled “Experimental Flags”](#experimental-flags)

Experimental flags allow you to opt in to features while they are in early development. Astro may also use experimental flags to test breaking changes to default behavior. The following experimental flags have been removed in Astro 6.0 and are now stable, or the new default behavior.

Remove these experimental flags from your Astro config if you were previously using them:

```
import { defineConfig } from 'astro/config';
export default defineConfig({  experimental: {    csp: true,    fonts: true,    liveContentCollections: true,    preserveScriptOrder: true,    staticImportMetaEnv: true,    headingIdCompat: true,    failOnPrerenderConflict: true  },})
```

#### Experimental features now stable:

[Section titled “Experimental features now stable:”](#experimental-features-now-stable)

*   `csp` (See the [`security.csp` configuration reference](/en/reference/configuration-reference/#securitycsp) to learn more about Content Security Policy.)
*   `fonts` (See the updated [fonts guide](/en/guides/fonts/) to learn more about adding custom fonts to your project.)
*   `liveContentCollections` (See the updated [content collections docs](/en/guides/content-collections/) to learn more about live collections.)
*   `failOnPrerenderConflict` (See the new [`prerenderConflictBehavior`](/en/reference/configuration-reference/#prerenderconflictbehavior) configuration option.)

#### New default or recommended behavior:

[Section titled “New default or recommended behavior:”](#new-default-or-recommended-behavior)

*   `preserveScriptOrder` (See below for breaking changes to [default `<script>` and `<style>` behavior](#changed-script-and-style-tags-are-rendered-in-the-order-they-are-defined).)
*   `staticImportMetaEnv` (See below for breaking changes to [`import.meta.env`](#changed-importmetaenv-values-are-always-inlined).)
*   `headingIdCompat` (See below for breaking changes to [Markdown heading ID generation](#changed-markdown-heading-id-generation).)

Read about exciting new features and more in [the v6.0 Blog post](https://astro.build/blog/astro-6/).

## Changed Defaults

[Section titled “Changed Defaults”](#changed-defaults)

Some default behavior has changed in Astro v6.0 and your project code may need updating to account for these changes.

In most cases, the only action needed is to review your existing project’s deployment and ensure that it continues to function as you expect, making updates to your code as necessary. In some cases, there may be a configuration setting to allow you to continue to use the previous default behavior.

### Changed: `i18n.routing.redirectToDefaultLocale` default value

[Section titled “Changed: i18n.routing.redirectToDefaultLocale default value”](#changed-i18nroutingredirecttodefaultlocale-default-value)

[Implementation PR: feat(astro)!: update i18n.redirectToDefaultLocale default (#14406)](https://github.com/withastro/astro/pull/14406)

In Astro v5.0, the `i18n.routing.redirectToDefaultLocale` default value was `true`. When combined with the `i18n.routing.prefixDefaultLocale` default value of `false`, the resulting redirects could cause infinite loops.

In Astro v6.0, `i18n.routing.redirectToDefaultLocale` now defaults to `false`. Additionally, it can now only be used if `i18n.routing.prefixDefaultLocale` is set to `true`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-33)

Review your Astro `i18n` config as you may now need to explicitly set values for `redirectToDefaultLocale` and `prefixDefaultLocale` to recreate your project’s previous behavior.

```
import { defineConfig } from 'astro/config';
export default defineConfig({  i18n: {    routing: {      prefixDefaultLocale: true,      redirectToDefaultLocale: true    }  }})
```

If you are using manual routing, you may also need to update your middleware configuration:

```
import { middleware } from "astro:i18n"; // Astro's own i18n routing config
export const onRequest = middleware({  prefixDefaultLocale: false,  prefixDefaultLocale: true,  redirectToDefaultLocale: true,})
```

Learn more about [Internationalization routing](/en/guides/internationalization/#routing).

### Changed: `<script>` and `<style>` tags are rendered in the order they are defined

[Section titled “Changed: <script> and <style> tags are rendered in the order they are defined”](#changed-script-and-style-tags-are-rendered-in-the-order-they-are-defined)

[Implementation PR: feat: stabilize experimental preserveScriptOrder option (#14480)](https://github.com/withastro/astro/pull/14480)

In Astro v5.5, the `experimental.preserveScriptOrder` flag was introduced to render multiple `<style>` and `<script>` tags in the same order as they were declared in the source code. Astro 5.x reversed their order in your generated HTML output. This could give unexpected results, for example, CSS styles being overridden by earlier defined style tags when your site was built.

Astro 6.0 removes this experimental flag and makes this the new default behavior in Astro: scripts and styles are now rendered in the order defined in your code.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-34)

If you were previously using this experimental feature, you must [remove this experimental flag from your configuration](#experimental-flags) as it no longer exists.

Review your `<script>` and `<style>` tags to make sure they behave as desired. You may need to reverse their order:

```
<p>I am a component</p><style>  body {    background: red;    background: yellow;  }</style><style>  body {    background: yellow;    background: red;  }</style><script>    console.log("hello")    console.log("world")</script><script>    console.log("world!")    console.log("hello!")</script>
```

Read more about [using `script`](/en/guides/client-side-scripts/) and [`style`](/en/guides/styling/) tags.

### Changed: how responsive image styles are emitted

[Section titled “Changed: how responsive image styles are emitted”](#changed-how-responsive-image-styles-are-emitted)

[Implementation PR: support responsive images (#15407)](https://github.com/withastro/astro/pull/15407)

In Astro 5.x, images were computed at runtime and the `fit` and `pos` responsive image styles were injected in a `style` attribute. This did not allow compatibility with Astro’s Content Security Policy (CSP) for many reasons.

Astro 6 generates image styles inside a virtual module at build time based on project configuration, resulting in a hash class and `data-*` attributes to apply responsive styling to your images.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-35)

Visually inspect your images to ensure that they are rendering as expected. This is an implementation detail that should not affect the expected use of responsive images.

However, if you were relying on the inline styles previously generated for your images:

```
<img style="--fit: <value>; --pos: <value>" >
```

then you will need to update your project code to account for the new `data-*` attributes instead:

```
<img class="__a_HaSh350" data-astro-fit="value" data-astro-pos="value" >
```

## Breaking Changes

[Section titled “Breaking Changes”](#breaking-changes)

The following changes are considered breaking changes in Astro v6.0. Breaking changes may or may not provide temporary backwards compatibility. If you were using these features, you may have to update your code as recommended in each entry.

### Changed: endpoints with a file extension cannot be accessed with a trailing slash

[Section titled “Changed: endpoints with a file extension cannot be accessed with a trailing slash”](#changed-endpoints-with-a-file-extension-cannot-be-accessed-with-a-trailing-slash)

[Implementation PR: feat!: trailing slash never for endpoints with file extension (#14457)](https://github.com/withastro/astro/pull/14457)

In Astro v5.0, custom endpoints whose URL ended in a file extension (e.g. `/src/pages/sitemap.xml.ts` ) could be accessed with a trailing slash (`/sitemap.xml/`) or without (`/sitemap.xml`), regardless of the value configured for `build.trailingSlash`.

In Astro v6.0, these endpoints can only be accessed without a trailing slash. This is true regardless of your `build.trailingSlash` configuration.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-36)

Review your links to your custom endpoints that include a file extension in the URL and remove any trailing slashes:

```
<a href="/sitemap.xml/">Sitemap</a><a href="/sitemap.xml">Sitemap</a>
```

Learn more about [custom endpoints](/en/guides/endpoints/).

### Changed: `import.meta.env` values are always inlined

[Section titled “Changed: import.meta.env values are always inlined”](#changed-importmetaenv-values-are-always-inlined)

[Implementation PR: feat: stabilize static import meta env (#14485)](https://github.com/withastro/astro/pull/14485)

In Astro 5.13, the `experimental.staticImportMetaEnv` flag was introduced to update the behavior when accessing `import.meta.env` directly to align with [Vite’s handling of environment variables](https://vite.dev/guide/env-and-mode.html#env-variables) and ensures that `import.meta.env` values are always inlined.

In Astro 5.x, non-public environment variables were replaced by a reference to `process.env`. Additionally, Astro could also convert the value type of your environment variables used through `import.meta.env`, which could prevent access to some values such as the strings `"true"` (which was converted to a boolean value), and `"1"` (which was converted to a number).

Astro 6 removes this experimental flag and makes this the new default behavior in Astro: `import.meta.env` values are always inlined and never coerced.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-37)

If you were previously using this experimental feature, you must [remove this experimental flag from your configuration](#experimental-flags) as it no longer exists.

If you were relying on coercion, you may need to update your project code to apply it manually:

```
const enabled: boolean = import.meta.env.ENABLED;const enabled: boolean = import.meta.env.ENABLED === "true";
```

If you were relying on the transformation into `process.env`, you may need to update your project code to apply it manually:

```
const enabled: boolean = import.meta.env.DB_PASSWORD;const enabled: boolean = process.env.DB_PASSWORD;
```

You may also need to update types:

```
interface ImportMetaEnv {  readonly PUBLIC_POKEAPI: string;  readonly DB_PASSWORD: string;  readonly ENABLED: boolean;  readonly ENABLED: string;}
interface ImportMeta {  readonly env: ImportMetaEnv;}
namespace NodeJS {  interface ProcessEnv {    DB_PASSWORD: string;  }}
```

If you need more control over environment variables in Astro, we recommend you use `astro:env`.

Learn more about [environment variables](/en/guides/environment-variables/) in Astro, including `astro:env`.

### Changed: Cropping by default in default image service

[Section titled “Changed: Cropping by default in default image service”](#changed-cropping-by-default-in-default-image-service)

[Implementation PR: feat(assets): Always allow cropping and never upscale (#14629)](https://github.com/withastro/astro/pull/14629)

In Astro 5.0, the default image service would only apply cropping when the `fit` option was provided.

Astro 6.0 applies cropping by default without requiring setting the `fit` option.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-38)

No changes are needed to your existing cropped images as the `fit` property is still valid. However, if you were previously setting `fit` to `contain` (its default value) in order to crop your images, you may now remove this option and still achieve the same cropping behavior by specifying `width` and `height` alone:

```
---import { Image } from 'astro:assets';import myImage from '../assets/photo.jpg';---<Image src={myImage} width={400} height={300} fit="contain" /><Image src={myImage} width={400} height={300} />
```

### Changed: Never upscale images in default image service

[Section titled “Changed: Never upscale images in default image service”](#changed-never-upscale-images-in-default-image-service)

[Implementation PR: feat(assets): Always allow cropping and never upscale (#14629)](https://github.com/withastro/astro/pull/14629)

In Astro 5.x, the default image service would upscale images when the requested dimensions were larger than the source image.

Astro 6.0 removes this behavior: the default image service never upscales images.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-39)

Review your images and update dimensions as needed. If you do need to upscale images, you may consider upscaling the images manually or using a custom image service that supports upscaling.

### Changed: SVG rasterization

[Section titled “Changed: SVG rasterization”](#changed-svg-rasterization)

[Implementation PR: add support for SVG rasterization (#15180)](https://github.com/withastro/astro/pull/15180)

In Astro v5.x, Astro’s default Sharp image service was unable to convert SVG files to raster files (e.g. PNG, WebP). This meant that the `<Image />` component would ignore any value set for `format` when optimizing and transforming SVG files.

Astro 6.0 now supports SVG rasterization. This is subject to [many limitations](https://github.com/lovell/sharp/issues?q=is%3Aissue%20state%3Aopen%20svg), for instance, SVGs with embedded fonts might not be converted properly. However, when the `format` property is set, the image service will now attempt to convert SVG images.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-40)

If you were previously relying on the fact that the image service would automatically skip converting SVGs, you must now check the format of your images beforehand to avoid converting SVGs to raster images:

```
<Image src={imageThatMightBeAnSvg} format="avif" alt="example" />
<Image  src={imageThatMightBeAnSvg}  format={imageThatMightBeAnSvg.format === "svg" ? "svg" : "avif"}  alt="example"/>
```

Learn more about [the `format` image property](/en/reference/modules/astro-assets/#format).

### Changed: `getImage()` throws when called on the client

[Section titled “Changed: getImage() throws when called on the client”](#changed-getimage-throws-when-called-on-the-client)

[Implementation PR: feat: disallow getImage on the client (#15800)](https://github.com/withastro/astro/pull/15800)

In Astro 5.x, calling `getImage()` from `astro:assets` on the client would silently fail or produce incorrect results.

Astro 6.0 throws a runtime error when `getImage()` is called on the client.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-41)

Call `getImage()` on the server and pass the resulting `src` to the client instead:

```
---import { getImage } from "astro:assets";import myBackground from "../background.png";
const optimizedBackground = await getImage({ src: myBackground, format: "avif" });---
<div id="background" data-src={optimizedBackground.src}></div>
<script>  const src = document.getElementById("background").dataset.src;  // use src client-side as needed</script>
```

See [generating images with `getImage()`](/en/guides/images/#generating-images-with-getimage) for a full example.

### Changed: Markdown heading ID generation

[Section titled “Changed: Markdown heading ID generation”](#changed-markdown-heading-id-generation)

[Implementation PR: feat!: stabilize experimental.headingIdCompat (#14494)](https://github.com/withastro/astro/pull/14494)

In Astro 5.x, an additional default processing step to Markdown stripped trailing hyphens from the end of IDs for section headings ending in special characters. This provided a cleaner `id` value, but could lead to incompatibilities rendering your Markdown across platforms.

In Astro 5.5, the `experimental.headingIdCompat` flag was introduced to allow you to make the IDs generated by Astro for Markdown headings compatible with common platforms like GitHub and npm, using the popular [`github-slugger`](https://github.com/Flet/github-slugger) package.

Astro 6.0 removes this experimental flag and makes this the new default behavior in Astro: trailing hyphens from the end of IDs for headings ending in special characters are no longer removed.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-42)

If you have manual links to headings, you may need to update the anchor link value with a new trailing hyphen. For example, the following Markdown heading:

```
## `<Picture />`
```

will now generate the following HTML with a trailing hyphen in the heading `id`:

```
<h2 id="picture-"><code>&lt;Picture /&gt;</code></h2>
```

and must now be linked to as:

```
See [the Picture component](/en/guides/images/#picture-) for more details.
```

If you were previously using the experimental feature to enforce trailing hyphens, you must [remove this experimental flag from your configuration](#experimental-flags) as it no longer exists.

If you were previously using the `rehypeHeadingIds` plugin directly to enforce compatibility, remove the `headingIdCompat` option as it no longer exists:

```
import { defineConfig } from 'astro/config';import { rehypeHeadingIds } from '@astrojs/markdown-remark';import { otherPluginThatReliesOnHeadingIDs } from 'some/plugin/source';
export default defineConfig({  markdown: {    rehypePlugins: [      [rehypeHeadingIds, { headingIdCompat: true }],      [rehypeHeadingIds],      otherPluginThatReliesOnHeadingIDs,    ],  },});
```

If you want to keep the old ID generation for backward compatibility reasons, you can create a custom rehype plugin that will generate headings IDs like Astro 5.x. This will allow you to continue to use your existing anchor links without adding trailing hyphens.

Create a custom rehype plugin to strip trailing hyphens

1.  Install required dependencies:
    
    *   [npm](#tab-panel-1897)
    *   [pnpm](#tab-panel-1898)
    *   [Yarn](#tab-panel-1899)
    
    ```
    npm i github-slugger hast-util-heading-rank unist-util-visit hast-util-to-string
    ```
    
2.  Create a custom rehype plugin that will generate headings IDs like Astro v5:
    
    ```
    import GithubSlugger from 'github-slugger';import { headingRank } from 'hast-util-heading-rank';import { visit } from 'unist-util-visit';import { toString } from 'hast-util-to-string';
    const slugs = new GithubSlugger();
    export function rehypeSlug() {  /**   * @param {import('hast').Root} tree   */  return (tree) => {    slugs.reset();    visit(tree, 'element', (node) => {      if (headingRank(node) && !node.properties.id) {        let slug = slugs.slug(toString(node));        // Strip trailing hyphens like in Astro v5 and below:        if (slug.endsWith('-')) slug = slug.slice(0, -1);        node.properties.id = slug;      }    });  };}
    ```
    
3.  Add the custom plugin to your Markdown configuration in `astro.config.mjs`:
    
    ```
    import { defineConfig } from 'astro/config';import { rehypeSlug } from './plugins/rehype-slug';
    export default defineConfig({  markdown: {    rehypePlugins: [rehypeSlug],  },});
    ```
    

Learn more about [Heading IDs](/en/guides/markdown-content/#heading-ids).

### Changed: `getStaticPaths()` cannot return `params` of type number

[Section titled “Changed: getStaticPaths() cannot return params of type number”](#changed-getstaticpaths-cannot-return-params-of-type-number)

[Implementation PR: fix!: disallow number in getStaticPaths params (#14586)](https://github.com/withastro/astro/pull/14586)

In Astro 5.x, `getStaticPaths()` could return `params` of type number, which would always be stringified by Astro. However, that could be confusing because it conflicted with `Astro.params` types.

Astro 6.0 removes this behavior: `getStaticPaths()` must now return string or undefined `params` values.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-43)

Review your dynamic routes using `getStaticPaths()` and convert any number params to strings:

```
---export function getStaticPaths() {  return [    {      params: {        id: 1,        id: "1",        label: "foo",      }    },    {      params: {        id: 2,        id: "2",        label: "bar",      }    },  ]}---
```

Learn more about [dynamic SSG routes with `getStaticPaths()`](/en/guides/routing/#static-ssg-mode).

### Changed: Astro components cannot be rendered in Vitest client environments (Container API)

[Section titled “Changed: Astro components cannot be rendered in Vitest client environments (Container API)”](#changed-astro-components-cannot-be-rendered-in-vitest-client-environments-container-api)

[Implementation PR: feat: remove Vitest workaround for client environment (#14895)](https://github.com/withastro/astro/pull/14895)

In Astro 5.x, rendering an Astro component on the client was forbidden. However we temporarily allowed this behavior in Vitest client environments such as `jsdom` or `happy-dom` using the [experimental Container API](/en/reference/container-reference/).

Astro 6.0 removes the ability to render Astro components in Vitest client environments: tests that render Astro components must now run in a server environment like `node`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-44)

If you use Vitest to run tests that render Astro components in client environments like `jsdom` or `happy-dom`, update your Vitest config to use the `node` environment for these:

```
import { defineConfig } from 'vitest/config';
export default defineConfig({  test: {    environment: 'jsdom',    environment: 'node',  },});
```

Learn more about [testing Astro components](/en/guides/testing/).

### Changed: Rollup output file name config path (Vite config)

[Section titled “Changed: Rollup output file name config path (Vite config)”](#changed-rollup-output-file-name-config-path-vite-config)

[Implementation PR: feat: integrate vite environments (#14306)](https://github.com/withastro/astro/pull/14306)

In Astro 5.x, custom Rollup output file name options for client assets could be configured at `vite.build.rollupOptions.output`.

Astro 6.0 scopes client build output configuration to Vite’s client environment. If you customize `entryFileNames`, `chunkFileNames`, or `assetFileNames` for client assets, use `vite.environments.client.build.rollupOptions.output`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-45)

Move your config from `vite.build.rollupOptions.output` to `vite.environments.client.build.rollupOptions.output`:

```
export default defineConfig({  vite: {    environments: {      client: {        build: {          rollupOptions: {            output: {              entryFileNames: 'js/[name]-[hash].js',            },          },        },      },    },  },});
```

### Changed: Integration hooks and HMR access patterns (Integration API)

[Section titled “Changed: Integration hooks and HMR access patterns (Integration API)”](#changed-integration-hooks-and-hmr-access-patterns-integration-api)

[Implementation PR: feat: integrate vite environments (#14306)](https://github.com/withastro/astro/pull/14306)

In Astro 5.x, Astro relied on certain patterns for integration hooks and HMR access that were incompatible with or could be improved by integrating Vite’s Environment API.

Astro 6.0 uses Vite’s new Environment API for build configuration and dev server interactions. This primarily enables dev mode in runtimes like workerd, but means that some integration hooks and HMR access patterns have changed.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-46)

**For integrations using `astro:build:setup`:**

The hook is now called once with all environments configured (`ssr`, `client`, `prerender`), instead of being called separately for each build target. Remove the `target` parameter and use `vite.environments` to configure specific environments:

```
{  hooks: {    'astro:build:setup': ({ target, vite }) => {      if (target === 'client') {        vite.build.minify = false;      }    }    'astro:build:setup': ({ vite }) => {      vite.environments.client.build.minify = false;    }  }}
```

**For dev toolbar and integration code accessing HMR:**

Replace `server.hot.send()` with `server.environments.client.hot.send()`:

```
server.hot.send(event)server.environments.client.hot.send(event)
```

Learn more about the [Vite Environment API](https://vite.dev/guide/api-environment) and Astro [integration hooks](/en/reference/integrations-reference/#astrobuildsetup).

### Changed: `SSRManifest` interface structure (Adapter API)

[Section titled “Changed: SSRManifest interface structure (Adapter API)”](#changed-ssrmanifest-interface-structure-adapter-api)

[Implementation PR: feat: integrate vite environments (#14306)](https://github.com/withastro/astro/pull/14306)

In Astro 5.x, path properties of the `SSRManifest` interface like `srcDir`, `outDir`, `cacheDir`, `publicDir`, `buildClientDir`, and `buildServerDir` were URL strings.

Astro 6.0 changes the form of these path properties to `URL` objects instead of URL strings. With this change, several new properties are now available on the manifest, and others have been updated or removed.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-47)

If you were treating these path properties as strings, you will now need to handle the `URL` object. For example, you will now need to access the `href` property of the `URL` object:

```
// To retrieve the same format (e.g., "file:///path/to/src"), make the following change:const srcPath = manifest.srcDir;const srcPath = manifest.srcDir.href;
```

If you were accessing the `hrefRoot` property, you will need to remove it, as it is no longer available on the manifest.

Update any use of `serverIslandMappings` and `sessionDriver`. These are now async methods:

```
const mappings = manifest.serverIslandMappings;const driver = manifest.sessionDriver;const mappings = await manifest.serverIslandMappings?.();const driver = await manifest.sessionDriver?.();
```

Learn more about [the Adapter API](/en/reference/adapter-reference/).

### Changed: schema types are inferred instead of generated (Content Loader API)

[Section titled “Changed: schema types are inferred instead of generated (Content Loader API)”](#changed-schema-types-are-inferred-instead-of-generated-content-loader-api)

[Implementation PR: feat: loader.createSchema() (#14759)](https://github.com/withastro/astro/pull/14759)

In Astro 5.x, the types for content collections were generated using `zod-to-ts` when provided by a content loader and not defined by a user-provided schema.

Astro 6.0 removes this behavior: types are no longer generated using `zod-to-ts`. Instead, types are inferred.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-48)

If you are providing a `schema` in a content loader, you must use the [TypeScript’ `satisfies` operator](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator):

```
import type { Loader } from 'astro/loaders'
function myLoader(): Loader {function myLoader() {  return {    name: 'my-loader',    load: async (context) => {      // ...    },    schema: z.object({/* ... */})  }  } satisfies Loader}
```

Learn more about [defining loader schema types](/en/reference/content-loader-reference/#the-loader-object).

## Known Issues

[Section titled “Known Issues”](#known-issues)

Please check [Astro’s issues on GitHub](https://github.com/withastro/astro/issues/) for any reported issues, or to file an issue yourself.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


