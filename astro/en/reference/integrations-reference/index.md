---
title: "Astro Integration API"
source: "https://docs.astro.build/en/reference/integrations-reference/"
canonical_url: "https://docs.astro.build/en/reference/integrations-reference/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:34.761Z"
content_hash: "5185462849e86022ac939f4bd7b9881e1fd9505d172dbcaf347cb21b21b73a90"
menu_path: ["Astro Integration API"]
section_path: []
nav_prev: {"path": "astro/en/reference/modules/astro-zod/index.md", "title": "Zod API Reference"}
nav_next: {"path": "astro/en/reference/adapter-reference/index.md", "title": "Astro Adapter API"}
---

# Astro Integration API

**Astro Integrations** add new functionality and behaviors for your project with only a few lines of code.

This reference page is for anyone writing their own integration. To learn how to use an integration in your project, check out our [Using Integrations](/en/guides/integrations/) guide instead.

## Examples

[Section titled “Examples”](#examples)

The official Astro integrations can act as reference for you as you go to build your own integrations.

*   **Renderers:** [`svelte`](/en/guides/integrations-guide/svelte/), [`react`](/en/guides/integrations-guide/react/), [`preact`](/en/guides/integrations-guide/preact/), [`vue`](/en/guides/integrations-guide/vue/), [`solid`](/en/guides/integrations-guide/solid-js/)
*   **Libraries:** [`partytown`](/en/guides/integrations-guide/partytown/)
*   **Features:** [`sitemap`](/en/guides/integrations-guide/sitemap/)

## Quick API Reference

[Section titled “Quick API Reference”](#quick-api-reference)

```
interface AstroIntegration {  name: string;  hooks: {    'astro:config:setup'?: (options: {      config: AstroConfig;      command: 'dev' | 'build' | 'preview' | 'sync';      isRestart: boolean;      updateConfig: (newConfig: DeepPartial<AstroConfig>) => AstroConfig;      addRenderer: (renderer: AstroRenderer) => void;      addWatchFile: (path: URL | string) => void;      addClientDirective: (directive: ClientDirectiveConfig) => void;      addMiddleware: (middleware: AstroIntegrationMiddleware) => void;      addDevToolbarApp: (entrypoint: DevToolbarAppEntry) => void;      injectScript: (stage: InjectedScriptStage, content: string) => void;      injectRoute: (injectedRoute: InjectedRoute) => void;      createCodegenDir: () => URL;      logger: AstroIntegrationLogger;    }) => void | Promise<void>;    'astro:route:setup'?: (options: {      route: RouteOptions;      logger: AstroIntegrationLogger;    }) => void | Promise<void>;    'astro:routes:resolved'?: (options: {      routes: IntegrationResolvedRoute[];      logger: AstroIntegrationLogger;    }) => void | Promise<void>;    'astro:config:done'?: (options: {      config: AstroConfig;      setAdapter: (adapter: AstroAdapter) => void;      injectTypes: (injectedType: InjectedType) => URL;      logger: AstroIntegrationLogger;      buildOutput: 'static' | 'server';    }) => void | Promise<void>;    'astro:server:setup'?: (options: {      server: vite.ViteDevServer;      logger: AstroIntegrationLogger;      toolbar: ReturnType<typeof getToolbarServerCommunicationHelpers>;      refreshContent?: (options: RefreshContentOptions) => Promise<void>;    }) => void | Promise<void>;    'astro:server:start'?: (options: {      address: AddressInfo;      logger: AstroIntegrationLogger;    }) => void | Promise<void>;    'astro:server:done'?: (options: {      logger: AstroIntegrationLogger;    }) => void | Promise<void>;    'astro:build:start'?: (options: {      logger: AstroIntegrationLogger;      setPrerenderer: (prerenderer: AstroPrerenderer | ((defaultPrerenderer: AstroPrerenderer) => AstroPrerenderer)) => void;    }) => void | Promise<void>;    'astro:build:setup'?: (options: {      vite: vite.InlineConfig;      pages: Map<string, PageBuildData>;      updateConfig: (newConfig: vite.InlineConfig) => void;      logger: AstroIntegrationLogger;    }) => void | Promise<void>;    'astro:build:ssr'?: (options: {      manifest: SerializedSSRManifest;      middlewareEntryPoint: URL | undefined;      logger: AstroIntegrationLogger;    }) => void | Promise<void>;    'astro:build:generated'?: (options: {      dir: URL;      logger: AstroIntegrationLogger;    }) => void | Promise<void>;    'astro:build:done'?: (options: {      pages: { pathname: string }[];      dir: URL;      assets: Map<string, URL[]>;      logger: AstroIntegrationLogger;    }) => void | Promise<void>;
    // ... any custom hooks from integrations  };}
```

## Hooks

[Section titled “Hooks”](#hooks)

Astro provides hooks that integrations can implement to execute during certain parts of Astro’s lifecycle. Astro hooks are defined in the `IntegrationHooks` interface, which is part of the global `Astro` namespace. Each hook has a [`logger` option](#astrointegrationlogger) that allows you to use the Astro logger to write logs.

The following hooks are built in to Astro:

### `astro:config:setup`

[Section titled “astro:config:setup”](#astroconfigsetup)

**Next hook:** [`astro:route:setup`](#astroroutesetup)

**When:** On initialization, before either the [Vite](https://vite.dev/config/) or [Astro config](/en/reference/configuration-reference/) have resolved.

**Why:** To extend the project config. This includes updating the [Astro config](/en/reference/configuration-reference/), applying [Vite plugins](https://vite.dev/guide/api-plugin.html), adding component renderers, and injecting scripts onto the page.

```
'astro:config:setup'?: (options: {  config: AstroConfig;  command: 'dev' | 'build' | 'preview' | 'sync';  isRestart: boolean;  updateConfig: (newConfig: DeepPartial<AstroConfig>) => AstroConfig;  addRenderer: (renderer: AstroRenderer) => void;  addClientDirective: (directive: ClientDirectiveConfig) => void;  addMiddleware: (middleware: AstroIntegrationMiddleware) => void;  addDevToolbarApp: (entrypoint: DevToolbarAppEntry) => void;  addWatchFile: (path: URL | string) => void;  injectScript: (stage: InjectedScriptStage, content: string) => void;  injectRoute: (injectedRoute: InjectedRoute) => void;  createCodegenDir: () => URL;  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

#### `config` option

[Section titled “config option”](#config-option)

**Type:** `AstroConfig`

A read-only copy of the user-supplied [Astro config](/en/reference/configuration-reference/). This is resolved _before_ any other integrations have run. If you need a copy of the config after all integrations have completed their config updates, [see the `astro:config:done` hook](#astroconfigdone).

#### `command` option

[Section titled “command option”](#command-option)

**Type:** `'dev' | 'build' | 'preview' | 'sync'`

*   `dev` - Project is executed with `astro dev`
*   `build` - Project is executed with `astro build`
*   `preview` - Project is executed with `astro preview`
*   `sync` - Project is executed with `astro sync`

#### `isRestart` option

[Section titled “isRestart option”](#isrestart-option)

**Type:** `boolean`  

**Added in:** `astro@1.5.0`

`false` when the dev server starts, `true` when a reload is triggered. Useful to detect when this function is called more than once.

#### `updateConfig()` option

[Section titled “updateConfig() option”](#updateconfig-option)

**Type:** `(newConfig: DeepPartial<AstroConfig>) => AstroConfig;`

A callback function to update the user-supplied [Astro config](/en/reference/configuration-reference/). Any config you provide **will be merged with the user config + other integration config updates,** so you are free to omit keys!

For example, say you need to supply a [Vite](https://vite.dev/) plugin to the user’s project:

```
import bananaCSS from '@vitejs/official-banana-css-plugin';
export default {  name: 'banana-css-integration',  hooks: {    'astro:config:setup': ({ updateConfig }) => {      updateConfig({        vite: {          plugins: [bananaCSS()],        }      })    }  }}
```

#### `addRenderer()` option

[Section titled “addRenderer() option”](#addrenderer-option)

**Type:** `(renderer: [AstroRenderer](/en/reference/renderer-reference/#astrorenderer)) => void;`  
**Examples:** [`svelte`](https://github.com/withastro/astro/blob/main/packages/integrations/svelte/src/index.ts), [`react`](https://github.com/withastro/astro/blob/main/packages/integrations/react/src/index.ts), [`preact`](https://github.com/withastro/astro/blob/main/packages/integrations/preact/src/index.ts), [`vue`](https://github.com/withastro/astro/blob/main/packages/integrations/vue/src/index.ts), [`solid`](https://github.com/withastro/astro/blob/main/packages/integrations/solid/src/index.ts)

A callback function to [add a component framework renderer](/en/reference/renderer-reference/) (i.e. React, Vue, Svelte, etc).

#### `addWatchFile()` option

[Section titled “addWatchFile() option”](#addwatchfile-option)

**Type:** `(path: URL | string) => void`  

**Added in:** `astro@1.5.0`

If your integration depends on some configuration file that Vite doesn’t watch and/or needs a full dev server restart to take effect, add it with `addWatchFile()`. Whenever that file changes, the Astro dev server will be reloaded (you can check when a reload happens with [`isRestart`](#isrestart-option)).

Example usage:

```
// Must be an absolute path!addWatchFile('/home/user/.../my-config.json');addWatchFile(new URL('./ec.config.mjs', config.root));
```

#### `addClientDirective()` option

[Section titled “addClientDirective() option”](#addclientdirective-option)

**Type:** `(directive: [ClientDirectiveConfig](#clientdirectiveconfig)) => void;`  

**Added in:** `astro@2.6.0`

Adds a [custom client directive](/en/reference/directives-reference/#custom-client-directives) to be used in `.astro` files.

Note that directive entrypoints are only bundled through esbuild and should be kept small so they don’t slow down component hydration.

Example usage:

```
import { defineConfig } from 'astro/config';import clickDirective from './astro-click-directive/register.js'
// https://astro.build/configexport default defineConfig({  integrations: [    clickDirective()  ],});
```

```
/** * @type {() => import('astro').AstroIntegration} */export default () => ({  name: "client:click",  hooks: {    "astro:config:setup": ({ addClientDirective }) => {      addClientDirective({        name: "click",        entrypoint: "./astro-click-directive/click.js",      });    },  },});
```

```
/** * Hydrate on first click on the window * @type {import('astro').ClientDirective} */export default (load, opts, el) => {  window.addEventListener('click', async () => {    const hydrate = await load()    await hydrate()  }, { once: true })}
```

You can also add types for the directives in your library’s type definition file:

```
import 'astro'declare module 'astro' {  interface AstroClientDirectives {    'client:click'?: boolean  }}
```

#### `addDevToolbarApp()` option

[Section titled “addDevToolbarApp() option”](#adddevtoolbarapp-option)

**Type:** `(entrypoint: DevToolbarAppEntry) => void;`  

**Added in:** `astro@3.4.0`

Adds a [custom dev toolbar app](/en/reference/dev-toolbar-app-reference/).

Example usage:

```
import { defineConfig } from 'astro/config';import devToolbarIntegration from './astro-dev-toolbar-app/integration.js'
// https://astro.build/configexport default defineConfig({  integrations: [    devToolbarIntegration()  ],});
```

```
/** * @type {() => import('astro').AstroIntegration} */export default () => ({  name: "dev-toolbar-app",  hooks: {    "astro:config:setup": ({ addDevToolbarApp }) => {      addDevToolbarApp({        entrypoint: "./astro-dev-toolbar-app/plugin.js",        id: "my-plugin",        name: "My Plugin"      });    },  },});
```

```
/** * @type {import('astro').DevToolbarApp} */export default {  id: "my-plugin",  name: "My Plugin",  icon: "<svg>...</svg>",  init() {    console.log("I'm a dev toolbar app!")  },};
```

#### `addMiddleware()` option

[Section titled “addMiddleware() option”](#addmiddleware-option)

**Type:** `(middleware: [AstroIntegrationMiddleware](#astrointegrationmiddleware)) => void;`  

**Added in:** `astro@3.5.0`

Adds [middleware](/en/guides/middleware/) to run on each request. Takes the `entrypoint` module that contains the middleware, and an `order` to specify whether it should run before (`pre`) other middleware or after (`post`).

```
/** * @type {() => import('astro').AstroIntegration} */export default () => ({  name: "my-middleware-package",  hooks: {    "astro:config:setup": ({ addMiddleware }) => {      addMiddleware({        entrypoint: '@my-package/middleware',        order: 'pre'      });    },  },});
```

Middleware is defined in a package with an [`onRequest()` function](/en/reference/modules/astro-middleware/#onrequest), as with user-defined middleware.

```
import { defineMiddleware } from 'astro:middleware';
export const onRequest = defineMiddleware(async (context, next) => {  if(context.url.pathname === '/some-test-path') {    return Response.json({      ok: true    });  }
  return next();});
```

**Added in:** `astro@5.0.0`

The function also accepts a `URL` for `entrypoint`:

```
/** * @type {() => import('astro').AstroIntegration} */export default () => ({  name: "my-middleware-package",  hooks: {    "astro:config:setup": ({ addMiddleware }) => {      addMiddleware({        entrypoint: new URL('./middleware.js', import.meta.url),        order: 'pre'      });    },  },});
```

#### `injectRoute()` option

[Section titled “injectRoute() option”](#injectroute-option)

**Type:** `({ pattern: string; entrypoint: string | URL; prerender?: boolean }) => void;`

A callback function to inject routes into an Astro project. Injected routes can be [`.astro` pages](/en/basics/astro-pages/) or [`.js` and `.ts` route handlers](/en/guides/endpoints/#static-file-endpoints).

`injectRoute()` takes an object with a `pattern` and an `entrypoint`.

*   `pattern` - where the route should be output in the browser, for example `/foo/bar`. A `pattern` can use Astro’s filepath syntax for denoting dynamic routes, for example `/foo/[bar]` or `/foo/[...bar]`. Note that a file extension is **not** needed in the `pattern`.
*   `entrypoint` - a bare module specifier pointing towards the `.astro` page or `.js`/`.ts` route handler that handles the route denoted in the `pattern`.
*   `prerender` - a boolean to set if Astro can’t detect your `prerender` export.

##### Example usage

[Section titled “Example usage”](#example-usage)

```
injectRoute({  // Use Astro’s pattern syntax for dynamic routes.  pattern: '/subfolder/[dynamic]',  // Use relative path syntax for a local route.  entrypoint: './src/dynamic-page.astro',  // Use only if Astro can't detect your prerender export  prerender: false});
```

For an integration designed to be installed in other projects, use its package name to refer to the route entrypoint. The following example shows a package published to npm as `@fancy/dashboard` injecting a dashboard route:

```
injectRoute({  pattern: '/fancy-dashboard',  entrypoint: '@fancy/dashboard/dashboard.astro'});
```

When publishing your package (`@fancy/dashboard`, in this case) to npm, you must export `dashboard.astro` in your `package.json`:

```
{  "name": "@fancy/dashboard",  // ...  "exports": { "./dashboard.astro": "./dashboard.astro" }}
```

**Added in:** `astro@5.0.0`

The function also accepts a `URL` for `entrypoint`:

```
injectRoute({  pattern: '/fancy-dashboard',  entrypoint: new URL('./dashboard.astro', import.meta.url)});
```

#### `injectScript()` option

[Section titled “injectScript() option”](#injectscript-option)

**Type:** `(stage: InjectedScriptStage, content: string) => void;`

A callback function to inject a string of JavaScript content onto every page.

The **`stage`** denotes how this script (the `content`) should be inserted. Some stages allow inserting scripts without modification, while others allow optimization during [Vite’s bundling step](https://vite.dev/guide/build.html):

*   `"head-inline"`: Injected into a script tag in the `<head>` of every page. **Not** optimized or resolved by Vite.
    
*   `"before-hydration"`: Imported client-side, before the hydration script runs. Optimized and resolved by Vite.
    
*   `"page"`: Similar to `head-inline`, except that the injected snippet is handled by Vite and bundled with any other `<script>` tags defined inside of Astro components on the page. The script will be loaded with a `<script type="module">` in the final page output, optimized and resolved by Vite.
    
*   `"page-ssr"`: Imported as a separate module in the frontmatter of every Astro page component. Because this stage imports your script, the `Astro` global is not available and your script will only be run once when the `import` is first evaluated.
    
    The main use for the `page-ssr` stage is injecting a CSS `import` into every page to be optimized and resolved by Vite:
    
    ```
    injectScript('page-ssr', 'import "global-styles.css";');
    ```
    

#### `createCodegenDir()`

[Section titled “createCodegenDir()”](#createcodegendir)

**Type:** `() => URL;`  

**Added in:** `astro@5.0.0`

A function that creates the `<root>/.astro/integrations/<normalized_integration_name>` folder and returns its path.

It allows you to have a dedicated folder, avoiding conflicts with another integration or Astro itself. This directory is created by calling this function so it’s safe to write files to it directly:

```
import { writeFileSync } from 'node:fs'
const integration = {  name: 'my-integration',  hooks: {    'astro:config:setup': ({ createCodegenDir }) => {      const codegenDir = createCodegenDir()      writeFileSync(new URL('cache.json', codegenDir), '{}', 'utf-8')    }  }}
```

### `astro:route:setup`

[Section titled “astro:route:setup”](#astroroutesetup)

**Added in:** `astro@4.14.0`

**Previous hook:** [`astro:config:setup`](#astroconfigsetup)

**Next hook:** [`astro:routes:resolved`](#astroroutesresolved)

**When:** In `astro build`, before bundling starts. In `astro dev`, while building the module graph and on every change to a file based route (added/removed/updated).

**Why:** To set options for a route at build or request time, such as enabling [on-demand server rendering](/en/guides/on-demand-rendering/#enabling-on-demand-rendering).

```
'astro:route:setup'?: (options: {  route: RouteOptions;  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

#### `route` option

[Section titled “route option”](#route-option)

**Type:** `{ readonly component: string; prerender?: boolean; }`

An object with a `component` property to identify the route and the following additional values to allow you to configure the generated route: `prerender`.

##### `route.component`

[Section titled “route.component”](#routecomponent)

**Type:** `string`  

**Added in:** `astro@4.14.0`

The `component` property indicates the entrypoint that will be rendered on the route. You can access this value before the routes are built to configure on-demand server rendering for that page.

##### `route.prerender`

[Section titled “route.prerender”](#routeprerender)

**Type:** `boolean`  
**Default:** `undefined`  

**Added in:** `astro@4.14.0`

The `prerender` property is used to configure [on-demand server rendering](/en/guides/on-demand-rendering/#enabling-on-demand-rendering) for a route. If the route file contains an explicit `export const prerender` value, the value will be used as the default instead of `undefined`.

```
import { defineConfig } from 'astro/config';
export default defineConfig({  integrations: [setPrerender()],});
function setPrerender() {  return {    name: 'set-prerender',    hooks: {      'astro:route:setup': ({ route }) => {        if (route.component.endsWith('/blog/[slug].astro')) {          route.prerender = true;        }      },    },  };}
```

If the final value after running all the hooks is `undefined`, the route will fall back to a prerender default based on the [`output` option](/en/reference/configuration-reference/#output): prerendered for `static` mode, and on-demand rendered for `server` mode.

### `astro:routes:resolved`

[Section titled “astro:routes:resolved”](#astroroutesresolved)

**Added in:** `astro@5.0.0`

**Previous hook:** [`astro:route:setup`](#astroroutesetup)

**Next hook:** [`astro:config:done`](#astroconfigdone) (only during setup)

**When:** In `astro dev`, it also runs on every change to a file based route (added/removed/updated).

**Why:** To access routes and their metadata

```
'astro:routes:resolved'?: (options: {  routes: IntegrationResolvedRoute[];  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

#### `routes` option

[Section titled “routes option”](#routes-option)

**Type:** [`IntegrationResolvedRoute[]`](#integrationresolvedroute)

A list of all routes with their associated metadata.

Example use:

```
const integration = () => {  return {    name: 'my-integration',    hooks: {      'astro:routes:resolved': ({ routes }) => {        const projectRoutes = routes.filter(r => r.origin === 'project').map(r => r.pattern)
        console.log(projectRoutes)      },    }  }}
```

### `astro:config:done`

[Section titled “astro:config:done”](#astroconfigdone)

**Previous hook:** [`astro:routes:resolved`](#astroroutesresolved)

**Next hook:** [`astro:server:setup`](#astroserversetup) when running in “dev” mode, or [`astro:build:start`](#astrobuildstart) during production builds

**When:** After the Astro config has resolved and other integrations have run their `astro:config:setup` hooks.

**Why:** To retrieve the final config for use in other hooks.

```
'astro:config:done'?: (options: {  config: AstroConfig;  setAdapter: (adapter: AstroAdapter) => void;  injectTypes: (injectedType: InjectedType) => URL;  logger: AstroIntegrationLogger;  buildOutput: 'static' | 'server';}) => void | Promise<void>;
```

#### `config` option

[Section titled “config option”](#config-option-1)

**Type:** `AstroConfig`

A read-only copy of the user-supplied [Astro config](/en/reference/configuration-reference/). This is resolved _after_ other integrations have run.

#### `setAdapter()` option

[Section titled “setAdapter() option”](#setadapter-option)

**Type:** `(adapter: AstroAdapter) => void;`

Makes the integration an adapter. Read more in the [adapter API](/en/reference/adapter-reference/).

#### `injectTypes()` option

[Section titled “injectTypes() option”](#injecttypes-option)

**Type:** `(injectedType: { filename: string; content: string }) => URL`  

**Added in:** `astro@4.14.0`

Allows you to inject types into your user’s project by adding a new `*.d.ts` file.

The `filename` property will be used to generate a file at `/.astro/integrations/<normalized_integration_name>/<normalized_filename>.d.ts` and must end with `".d.ts"`.

The `content` property will create the body of the file and must be valid TypeScript.

Additionally, `injectTypes()` returns a URL to the normalized path so you can overwrite its content later on, or manipulate it in any way you want.

```
const path = injectTypes({  filename: "types.d.ts",  content: "declare module 'virtual:integration' {}"})console.log(path) // URL
```

#### `buildOutput` option

[Section titled “buildOutput option”](#buildoutput-option)

**Type:** `'static' | 'server'`  

**Added in:** `astro@5.0.0`

Allows you to adapt the logic of your integration depending on the user’s project output.

### `astro:server:setup`

[Section titled “astro:server:setup”](#astroserversetup)

**Previous hook:** [`astro:config:done`](#astroconfigdone)

**Next hook:** [`astro:server:start`](#astroserverstart)

**When:** Just after the Vite server is created in “dev” mode, but before the `listen()` event is fired. [See Vite’s createServer API](https://vite.dev/guide/api-javascript.html#createserver) for more.

**Why:** To update Vite server options and middleware, or enable support for refreshing the content layer.

```
'astro:server:setup'?: (options: {  server: vite.ViteDevServer;  logger: AstroIntegrationLogger;  toolbar: ReturnType<typeof getToolbarServerCommunicationHelpers>;  refreshContent: (options: {    loaders?: Array<string>;    context?: Record<string, any>;  }) => Promise<void>;}) => void | Promise<void>;
```

#### `server` option

[Section titled “server option”](#server-option)

**Type:** [`ViteDevServer`](https://vite.dev/guide/api-javascript.html#vitedevserver)

A mutable instance of the Vite server used in “dev” mode. For instance, this is [used by our Partytown integration](/en/guides/integrations-guide/partytown/) to inject the Partytown server as middleware:

```
export default {  name: 'partytown',  hooks: {    'astro:server:setup': ({ server }) => {      server.middlewares.use(        function middleware(req, res, next) {          // handle requests        }      );    }  }}
```

#### `toolbar` option

[Section titled “toolbar option”](#toolbar-option)

**Type:** `ReturnType<typeof getToolbarServerCommunicationHelpers>`  

**Added in:** `astro@4.7.0`

An object providing callback functions to interact with the [dev toolbar](/en/reference/dev-toolbar-app-reference/):

##### `toolbar.on()`

[Section titled “toolbar.on()”](#toolbaron)

**Type:** `<T>(event: string, callback: (data: T) => void) => void`  

A function that takes an event name as first argument and a callback function as second argument. This allows you to receive a message from a dev toolbar app with data associated to that event.

##### `toolbar.onAppInitialized()`

[Section titled “toolbar.onAppInitialized()”](#toolbaronappinitialized)

**Type:** `(appId: string, callback: (data: Record<string, never>) => void) => void`  

A function fired when a dev toolbar app is initialized. The first argument is the id of the app that was initialized. The second argument is a callback function to run when the app is initialized.

##### `toolbar.onAppToggled()`

[Section titled “toolbar.onAppToggled()”](#toolbaronapptoggled)

**Type:** `(appId: string, callback: (data: { state: boolean; }) => void) => void`  

A function fired when a dev toolbar app is toggled on or off. The first argument is the id of the app that was toggled. The second argument is a callback function providing the state to execute when the application is toggled.

##### `toolbar.send()`

[Section titled “toolbar.send()”](#toolbarsend)

**Type:** `<T>(event: string, payload: T) => void`  

A function that sends a message to the dev toolbar that an app can listen for. This takes an event name as the first argument and a payload as the second argument which can be any serializable data.

#### `refreshContent()` option

[Section titled “refreshContent() option”](#refreshcontent-option)

**Type:** `(options: { loaders?: Array<string>; context?: Record<string, any>; }) => Promise<void>`  

**Added in:** `astro@5.0.0`

A function for integrations to trigger an update to the content layer during `astro dev`. This can be used, for example, to register a webhook endpoint during dev, or to open a socket to a CMS to listen for changes.

By default, `refreshContent()` will refresh all collections. You can optionally pass a `loaders` property, which is an array of loader names. If provided, only collections that use those loaders will be refreshed. For example, A CMS integration could use this property to only refresh its own collections.

You can also pass a `context` object to the loaders. This can be used to pass arbitrary data such as the webhook body, or an event from the websocket.

```
{  name: 'my-integration',  hooks: {    'astro:server:setup': async ({ server, refreshContent }) => {      // Register a dev server webhook endpoint      server.middlewares.use('/_refresh', async (req, res) => {        if(req.method !== 'POST') {          res.statusCode = 405          res.end('Method Not Allowed');          return        }        let body = '';        req.on('data', chunk => {          body += chunk.toString();        });        req.on('end', async () => {          try {            const webhookBody = JSON.parse(body);            await refreshContent({              context: { webhookBody },              loaders: ['my-loader']            });            res.writeHead(200, { 'Content-Type': 'application/json' });            res.end(JSON.stringify({ message: 'Content refreshed successfully' }));          } catch (error) {            res.writeHead(500, { 'Content-Type': 'application/json' });            res.end(JSON.stringify({ error: 'Failed to refresh content: ' + error.message }));          }        });      });    }  }}
```

The loader can then access the `refreshContextData` property to get the webhook body. See the [`refreshContextData`](/en/reference/content-loader-reference/#loadercontextrefreshcontextdata) property for more information.

### `astro:server:start`

[Section titled “astro:server:start”](#astroserverstart)

**Previous hook:** [`astro:server:setup`](#astroserversetup)

**Next hook:** [`astro:server:done`](#astroserverdone)

**When:** Just after the server’s `listen()` event has fired.

**Why:** To intercept network requests at the specified address. If you intend to use this address for middleware, consider using `astro:server:setup` instead.

```
'astro:server:start'?: (options: {  address: AddressInfo;  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

#### `address` option

[Section titled “address option”](#address-option)

**Type:** `AddressInfo`

The address, family and port number supplied by the [`server.address()` method of the Node.js Net module](https://nodejs.org/api/net.html#serveraddress).

### `astro:server:done`

[Section titled “astro:server:done”](#astroserverdone)

**Previous hook:** [`astro:server:start`](#astroserverstart)

**When:** Just after the dev server is closed.

**Why:** To run any cleanup events you may trigger during the `astro:server:setup` or `astro:server:start` hooks.

```
'astro:server:done'?: (options: {  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

### `astro:build:start`

[Section titled “astro:build:start”](#astrobuildstart)

**Previous hook:** [`astro:config:done`](#astroconfigdone)

**Next hook:** [`astro:build:setup`](#astrobuildsetup)

**When:** After the `astro:config:done` event, but before the production build begins.

**Why:** To set up any global objects or clients needed during a production build. This can also extend the build configuration options in the [adapter API](/en/reference/adapter-reference/).

```
'astro:build:start'?: (options: {  logger: AstroIntegrationLogger;  setPrerenderer: (prerenderer: AstroPrerenderer | ((defaultPrerenderer: AstroPrerenderer) => AstroPrerenderer)) => void;}) => void | Promise<void>;
```

#### `setPrerenderer()` option

[Section titled “setPrerenderer() option”](#setprerenderer-option)

**Type:** `(prerenderer: [AstroPrerenderer](#astroprerenderer) | ((defaultPrerenderer: AstroPrerenderer) => AstroPrerenderer)) => void`  

**Added in:** `astro@6.0.0`

A callback function to set a custom prerenderer for the build. This allows adapters to provide their own prerendering logic.

The function accepts either an [`AstroPrerenderer` object](#astroprerenderer) directly, or a factory function that receives the default prerenderer and returns a custom one. This is useful when you want to wrap or extend the default behavior.

```
'astro:build:start': ({ setPrerenderer }) => {  setPrerenderer((defaultPrerenderer) => ({    name: 'my-prerenderer',    async setup() {      // Optional: called once before prerendering starts    },    async getStaticPaths() {      // Returns array of { pathname: string, route: RouteData }      return defaultPrerenderer.getStaticPaths();    },    async render(request, { routeData }) {      // request: Request, options: { routeData: RouteData }      // Returns: Response    },    async teardown() {      // Optional: called after all pages are prerendered    }  }));}
```

See the [adapter reference](/en/reference/adapter-reference/#custom-prerenderer) for more details on implementing a custom prerenderer.

### `astro:build:setup`

[Section titled “astro:build:setup”](#astrobuildsetup)

**Previous hook:** [`astro:build:start`](#astrobuildstart)

**Next hook:** [`astro:build:ssr`](#astrobuildssr)

**When:** After the `astro:build:start` hook, runs immediately before the build.

**Why:** At this point, the Vite config for the build has been completely constructed, this is your final chance to modify it. This can be useful for example to overwrite some defaults. If you’re not sure whether you should use this hook or `astro:build:start`, use `astro:build:start` instead.

```
'astro:build:setup'?: (options: {  vite: vite.InlineConfig;  pages: Map<string, PageBuildData>;  updateConfig: (newConfig: vite.InlineConfig) => void;  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

#### `vite` option

[Section titled “vite option”](#vite-option)

**Type:** [`InlineConfig`](https://vite.dev/guide/api-javascript.html#inlineconfig)

An object that allows you to access the Vite configuration used in the build.

This can be useful if you need to access configuration options in your integration:

```
export default {  name: 'my-integration',  hooks: {    'astro:build:setup': ({ vite }) => {      const { publicDir, root } = vite;    },  }}
```

#### `pages` option

[Section titled “pages option”](#pages-option)

**Type:** `Map<string, [PageBuildData](#the-pagebuilddata-object)>`

A `Map` with a list of pages as key and [their build data](#the-pagebuilddata-object) as value.

This can be used to perform an action if a route matches a criteria:

```
export default {  name: 'my-integration',  hooks: {    'astro:build:setup': ({ pages }) => {      pages.forEach((data) => {        if (data.route.pattern.test("/blog")) {          console.log(data.route.type);        }      });    },  }}
```

##### The `PageBuildData` object

[Section titled “The PageBuildData object”](#the-pagebuilddata-object)

Describes how to build a page.

###### `PageBuildData.key`

[Section titled “PageBuildData.key”](#pagebuilddatakey)

**Type:** `string`  

**Added in:** `astro@4.8.0`

Specifies a unique identifier for the page.

###### `PageBuildData.component`

[Section titled “PageBuildData.component”](#pagebuilddatacomponent)

**Type:** `string`

Specifies the source component URL.

###### `PageBuildData.route`

[Section titled “PageBuildData.route”](#pagebuilddataroute)

**Type:** [`RouteData`](#routedata)

Describes the information about the page route.

###### `PageBuildData.moduleSpecifier`

[Section titled “PageBuildData.moduleSpecifier”](#pagebuilddatamodulespecifier)

**Type:** `string`

Defines a string that can be resolved into a file path for the module.

###### `PageBuildData.styles`

[Section titled “PageBuildData.styles”](#pagebuilddatastyles)

**Type:** `Array<{ depth: number; order: number; sheet: { type: 'inline'; content: string } | { type: 'external'; src: string } }>`  

**Added in:** `astro@2.4.0`

A list of styles to render on the page. Each style contains its `depth` in the components tree and its display `order` on the page, as well as an indication of whether this should be applied as an inline or external style.

#### `updateConfig()` option

[Section titled “updateConfig() option”](#updateconfig-option-1)

**Type:** `(newConfig: [InlineConfig](https://vite.dev/guide/api-javascript.html#inlineconfig)) => void`

A callback function to update the [Vite](https://vite.dev/) options used in the build. Any config you provide **will be merged with the user config + other integration config updates**, so you are free to omit keys!

For example, this can be used to supply a plugin to the user’s project:

```
import awesomeCssPlugin from 'awesome-css-vite-plugin';
export default {  name: 'my-integration',  hooks: {    'astro:build:setup': ({ updateConfig }) => {      updateConfig({        plugins: [awesomeCssPlugin()],      })    }  }}
```

### `astro:build:ssr`

[Section titled “astro:build:ssr”](#astrobuildssr)

**Previous hook:** [`astro:build:setup`](#astrobuildsetup)

**Next hook:** [`astro:build:generated`](#astrobuildgenerated)

**When:** After a production SSR build has completed.

**Why:** To access the SSR manifest and map of the emitted entry points. This is useful when creating custom SSR builds in plugins or integrations.

*   `middlewareEntryPoint` is the file system path of the middleware file;

```
'astro:build:ssr'?: (options: {  manifest: SerializedSSRManifest;  middlewareEntryPoint: URL | undefined;  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

#### `manifest` option

[Section titled “manifest option”](#manifest-option)

**Type:** `SerializedSSRManifest`

Allows you to create a custom build by accessing a serialized version of the [`SSRManifest`](#ssrmanifest). This contains the same information as `SSRManifest`, with some properties converted to serializable formats.

The following example checks the [`i18n.strategy`](#ssrmanifesti18nstrategy) configuration stored in the `manifest`:

```
export default {  name: 'my-integration',  hooks: {    'astro:build:ssr': ({ manifest }) => {      const { i18n } = manifest;      if (i18n?.strategy === "domains-prefix-always") {        // do something      }    },  },}
```

##### `manifest.rootDir`

[Section titled “manifest.rootDir”](#manifestrootdir)

**Type:** `string`

Specifies a serialized version of the [`SSRManifest.rootDir`](#ssrmanifestrootdir).

##### `manifest.srcDir`

[Section titled “manifest.srcDir”](#manifestsrcdir)

**Type:** `string`

Specifies a serialized version of the [`SSRManifest.srcDir`](#ssrmanifestsrcdir).

##### `manifest.cacheDir`

[Section titled “manifest.cacheDir”](#manifestcachedir)

**Type:** `string`

Specifies a serialized version of the [`SSRManifest.cacheDir`](#ssrmanifestcachedir).

##### `manifest.outDir`

[Section titled “manifest.outDir”](#manifestoutdir)

**Type:** `string`

Specifies a serialized version of the [`SSRManifest.outDir`](#ssrmanifestoutdir).

##### `manifest.publicDir`

[Section titled “manifest.publicDir”](#manifestpublicdir)

**Type:** `string`

Specifies a serialized version of the [`SSRManifest.publicDir`](#ssrmanifestpublicdir).

##### `manifest.buildClientDir`

[Section titled “manifest.buildClientDir”](#manifestbuildclientdir)

**Type:** `string`

Specifies a serialized version of the [`SSRManifest.buildClientDir`](#ssrmanifestbuildclientdir).

##### `manifest.buildServerDir`

[Section titled “manifest.buildServerDir”](#manifestbuildserverdir)

**Type:** `string`

Specifies a serialized version of the [`SSRManifest.buildServerDir`](#ssrmanifestbuildserverdir).

##### `manifest.routes`

[Section titled “manifest.routes”](#manifestroutes)

**Type:** `SerializedRouteInfo[]`

Defines a list of serialized route information. Each route contains the same properties as [`SSRManifest.routes`](#ssrmanifestroutes), with `routeData` converted to a JSON-serializable format.

##### `manifest.assets`

[Section titled “manifest.assets”](#manifestassets)

**Type:** `string[]`

Defines a list of serialized asset file paths.

##### `manifest.componentMetadata`

[Section titled “manifest.componentMetadata”](#manifestcomponentmetadata)

**Type:** `[string, [SSRComponentMetadata](#ssrcomponentmetadata)][]`  

**Added in:** `astro@2.1.7`

Defines an array of key-value pairs where the first element is the component identifier and the second is an object describing the build metadata.

##### `manifest.inlinedScripts`

[Section titled “manifest.inlinedScripts”](#manifestinlinedscripts)

**Type:** `[string, string][]`

Defines an array of key-value pairs where each entry is a tuple. The first element is the script identifier and the second is the script content.

##### `manifest.clientDirectives`

[Section titled “manifest.clientDirectives”](#manifestclientdirectives)

**Type:** `[string, string][]`  

**Added in:** `astro@2.5.0`

Defines an array of key-value pairs where the first element is the directive name (e.g. `load`, `visible`) and the second is the directive’s implementation code.

##### `manifest.key`

[Section titled “manifest.key”](#manifestkey)

**Type:** `string`  

**Added in:** `astro@4.13.4`

Specifies the cryptographic key, serialized as a string, used for encrypting server island props.

#### `middlewareEntryPoint` option

[Section titled “middlewareEntryPoint option”](#middlewareentrypoint-option)

**Type:** `URL | undefined`  

**Added in:** `astro@2.8.0`

Exposes the [middleware](/en/guides/middleware/) file path.

```
export default {  name: 'my-integration',  hooks: {    'astro:build:ssr': ({ middlewareEntryPoint }) => {      if (middlewareEntryPoint) {        // do some operations if a middleware exist      }    },  },}
```

### `astro:build:generated`

[Section titled “astro:build:generated”](#astrobuildgenerated)

**Added in:** `astro@1.3.0`

**Previous hook:** [`astro:build:ssr`](#astrobuildssr)

**Next hook:** [`astro:build:done`](#astrobuilddone)

**When:** After a static production build has finished generating routes and assets.

**Why:** To access generated routes and assets **before** build artifacts are cleaned up. This is a very uncommon use case. We recommend using [`astro:build:done`](#astrobuilddone) unless you really need to access the generated files before cleanup.

```
'astro:build:generated'?: (options: {  dir: URL;  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

#### `dir` option

[Section titled “dir option”](#dir-option)

**Type:** [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL)

A URL path to the build output directory.

The following example uses Node’s built-in [`fileURLToPath()`](https://nodejs.org/api/url.html#urlfileurltopathurl-options) utility to compute a valid absolute path string for a file provided by the integration:

```
import { fileURLToPath } from 'node:url';
export default {  name: 'my-integration',  hooks: {    'astro:build:generated': ({ dir }) => {      const outFile = fileURLToPath(new URL('./my-integration.json', dir));    }  }}
```

### `astro:build:done`

[Section titled “astro:build:done”](#astrobuilddone)

**Previous hook:** [`astro:build:generated`](#astrobuildgenerated)

**When:** After a production build (SSG or SSR) has completed.

**Why:** To access generated routes and assets for extension (ex. copy content into the generated `/assets` directory). If you plan to transform generated assets, we recommend exploring the [Vite Plugin API](https://vite.dev/guide/api-plugin.html) and [configuring via `astro:config:setup`](#updateconfig-option) instead.

```
'astro:build:done'?: (options: {  pages: { pathname: string }[];  dir: URL;  assets: Map<string, URL[]>;  logger: AstroIntegrationLogger;}) => void | Promise<void>;
```

#### `dir` option

[Section titled “dir option”](#dir-option-1)

**Type:** [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL)

A URL path to the build output directory.

The following example uses Node’s built-in [`fileURLToPath()`](https://nodejs.org/api/url.html#urlfileurltopathurl-options) utility to compute a valid absolute path string for a file provided by the integration before writing to it:

```
import { writeFile } from 'node:fs/promises';import { fileURLToPath } from 'node:url';
export default function myIntegration() {  return {    hooks: {      'astro:build:done': async ({ dir }) => {        const metadata = await getIntegrationMetadata();        // Use fileURLToPath to get a valid, cross-platform absolute path string        const outFile = fileURLToPath(new URL('./my-integration.json', dir));        await writeFile(outFile, JSON.stringify(metadata));      }    }  }}
```

#### `assets` option

[Section titled “assets option”](#assets-option)

**Type:** `Map<string, URL[]>`  

**Added in:** `astro@5.0.0`

Contains URLs to output files paths, grouped by [`IntegrationResolvedRoute`](#integrationresolvedroute) `pattern` property.

#### `pages` option

[Section titled “pages option”](#pages-option-1)

**Type:** `{ pathname: string }[]`

A list of all generated pages. Each entry is an object with one property:

*   `pathname` - the finalized path of the page.

### Custom hooks

[Section titled “Custom hooks”](#custom-hooks)

Custom hooks can be added to integrations by extending the `IntegrationHooks` interface through [global augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#global-augmentation).

```
declare global {  namespace Astro {    export interface IntegrationHook {      'your:hook': (params: YourHookParameters) => Promise<void>    }  }}
```

Astro reserves the `astro:` prefix for future built-in hooks. Please choose a different prefix when naming your custom hook.

## Astro vite environments

[Section titled “Astro vite environments”](#astro-vite-environments)

Astro inherits the environments Vite provides by default, `ssr` and `client`.

Additionally there are two other environments that Astro creates:

*   `prerender` is an environment used during the `build` and it’s used to build static pages.
*   `astro` is an environment used during the development, and it’s used as a “secondary” SSR environment when the Vite `ssr` environment [isn’t a runnable dev environment](https://vite.dev/guide/api-environment-frameworks#runnabledevenvironment).

Astro’s [Vite environments](https://vite.dev/guide/api-environment) allow you to optimize your integration’s Vite plugins for different environments. One of the main uses of Vite environments is the ability to run and configure your integration’s Vite plugins conditionally:

```
resolveId(id) {  if (id === '\0virtual:foo') {    if (this.environment.name === 'client') {      throw new Error('This is a server-only module');    }    return 'export const foo = "bar"';  }}
```

## Integration types reference

[Section titled “Integration types reference”](#integration-types-reference)

The following types can be imported from the `astro` module:

```
import type {  AstroIntegrationLogger,  AstroIntegrationMiddleware,  AstroMiddlewareInstance,  AstroPrerenderer,  ClientDirectiveConfig,  HookParameters,  IntegrationResolvedRoute,  RedirectConfig,  RouteData,  RoutePart,  RouteType,  SSRComponentMetadata,  SSRManifest,  ValidRedirectStatus,} from "astro";
```

### `AstroIntegrationLogger`

[Section titled “AstroIntegrationLogger”](#astrointegrationlogger)

An instance of the Astro logger, useful to write logs. This logger uses the same [log level](/en/reference/cli-reference/#--verbose) configured via CLI.

**Methods available** to write to terminal:

*   `logger.info("Message")`;
*   `logger.warn("Message")`;
*   `logger.error("Message")`;
*   `logger.debug("Message")`;

All the messages are prepended with a label that has the same value as the name of the integration.

```
import type { AstroIntegration } from "astro";export function formatIntegration(): AstroIntegration {  return {    name: "astro-format",    hooks: {      "astro:build:done": ({ logger }) => {        // do something        logger.info("Integration ready.");      }    }  }}
```

The example above will log a message that includes the provided `info` message:

```
[astro-format] Integration ready.
```

To log some messages with a different label, use the `.fork` method to specify an alternative to the default `name`:

```
import type { AstroIntegration } from "astro";export function formatIntegration(): AstroIntegration {  return {    name: "astro-format",    hooks: {      "astro:config:done": ({ logger }) => {        // do something        logger.info("Integration ready.");      },      "astro:build:done": ({ logger }) => {        const buildLogger = logger.fork("astro-format/build");        // do something        buildLogger.info("Build finished.")      }    }  }}
```

The example above will produce logs with `[astro-format]` by default, and `[astro-format/build]` when specified:

```
[astro-format] Integration ready.[astro-format/build] Build finished.
```

### `AstroIntegrationMiddleware`

[Section titled “AstroIntegrationMiddleware”](#astrointegrationmiddleware)

**Type:** `{ order: "pre" | "post"; entrypoint: string | URL; }`

Describes a [middleware added by an integration](#addmiddleware-option).

#### `AstroIntegrationMiddleware.order`

[Section titled “AstroIntegrationMiddleware.order”](#astrointegrationmiddlewareorder)

**Type:** `"pre" | "post"`

Specifies whether the middleware should run before (`pre`) or after (`post`) other middleware.

#### `AstroIntegrationMiddleware.entrypoint`

[Section titled “AstroIntegrationMiddleware.entrypoint”](#astrointegrationmiddlewareentrypoint)

**Type:** `string | URL`

Defines the import path of the middleware.

### `AstroMiddlewareInstance`

[Section titled “AstroMiddlewareInstance”](#astromiddlewareinstance)

**Type:** `{ onRequest?: [MiddlewareHandler](/en/reference/modules/astro-middleware/#middlewarehandler); }`

An object containing an [`onRequest()`](/en/reference/modules/astro-middleware/#onrequest) property defined with the project’s middleware function when it exists.

### `AstroPrerenderer`

[Section titled “AstroPrerenderer”](#astroprerenderer)

**Type:** `string`  

**Added in:** `astro@6.0.0`

Describes a [custom prerender](/en/reference/adapter-reference/#custom-prerenderer) that adapters can provide to control page prerendering.

#### `AstroPrerenderer.name`

[Section titled “AstroPrerenderer.name”](#astroprerenderername)

**Type:** `string`

Specifies a unique name for the prerender.

#### `AstroPrerenderer.setup()`

[Section titled “AstroPrerenderer.setup()”](#astroprerenderersetup)

**Type:** `() => Promise<void>`

Defines an optional method that will be called once before the prerendering starts. This is useful for starting a preview server.

#### `AstroPrerenderer.getStaticPaths()`

[Section titled “AstroPrerenderer.getStaticPaths()”](#astroprerenderergetstaticpaths)

**Type:** `() => Promise<Array<{ pathname: string; route: [RouteData](#routedata); }>>`

Returns a list of objects describing the prerendered route path and its associated data.

#### `AstroPrerenderer.render()`

[Section titled “AstroPrerenderer.render()”](#astroprerendererrender)

**Type:** `(request: Request, options: { routeData: [RouteData](#routedata) }) => Promise<Response>`

Defines an optional method describing how to render a page. This will be called by Astro for each path returned by [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths).

#### `AstroPrerenderer.teardown()`

[Section titled “AstroPrerenderer.teardown()”](#astroprerendererteardown)

**Type:** `() => Promise<void>`

Defines an optional method called once all pages are pre-rendered. This is useful for performing cleanup tasks such as stopping a preview server.

### `ClientDirectiveConfig`

[Section titled “ClientDirectiveConfig”](#clientdirectiveconfig)

**Type:** `{ name: string; entrypoint: string | URL; }`

Describes a [custom client directive added by an integration](#addclientdirective-option).

#### `ClientDirectiveConfig.name`

[Section titled “ClientDirectiveConfig.name”](#clientdirectiveconfigname)

**Type:** `string`

A custom name for the event triggered by the directive.

#### `ClientDirectiveConfig.entrypoint`

[Section titled “ClientDirectiveConfig.entrypoint”](#clientdirectiveconfigentrypoint)

**Type:** `string | URL`

Defines the import path of the code executed whenever the directive is used.

### `HookParameters`

[Section titled “HookParameters”](#hookparameters)

You can get the type of a hook’s arguments by passing the hook’s name to the `HookParameters` utility type.

In the following example, a function’s `options` argument is typed to match the parameters of the [`astro:config:setup` hook](#astroconfigsetup):

```
import type { HookParameters } from 'astro';
function mySetup(options: HookParameters<'astro:config:setup'>) {  options.updateConfig({ /* ... */ });}
```

### `IntegrationResolvedRoute`

[Section titled “IntegrationResolvedRoute”](#integrationresolvedroute)

A subset of [`RouteData`](#routedata) with remapped properties.

```
interface IntegrationResolvedRoute extends Pick<    RouteData,    'params' | 'pathname' | 'segments' | 'type' | 'redirect' | 'origin'  > & {  pattern: RouteData['route'];  patternRegex: RouteData['pattern'];  entrypoint: RouteData['component'];  isPrerendered: RouteData['prerender'];  redirectRoute?: IntegrationResolvedRoute;  fallbackRoutes: IntegrationResolvedRoute[];  generate: (data?: any) => string;}
```

#### `IntegrationResolvedRoute.pattern`

[Section titled “IntegrationResolvedRoute.pattern”](#integrationresolvedroutepattern)

**Type:** [`RouteData['route']`](#routedataroute)

Allows you to identify the type of route based on its path. Here are some examples of paths associated with their pattern:

*   `src/pages/index.astro` will be `/`
*   `src/pages/blog/[...slug].astro` will be `/blog/[...slug]`
*   `src/pages/site/[blog]/[...slug].astro` will be `/site/[blog]/[...slug]`

#### `IntegrationResolvedRoute.patternRegex`

[Section titled “IntegrationResolvedRoute.patternRegex”](#integrationresolvedroutepatternregex)

**Type:** [`RouteData['pattern']`](#routedatapattern)

Allows you to access a regex used for matching an input URL against a requested route.

For example, given a `[fruit]/about.astro` path, the regex will be `/^\/([^/]+?)\/about\/?$/`. Using `pattern.test("banana/about")` will return `true`.

#### `IntegrationResolvedRoute.entrypoint`

[Section titled “IntegrationResolvedRoute.entrypoint”](#integrationresolvedrouteentrypoint)

**Type:** [`RouteData['component']`](#routedatacomponent)

The URL pathname of the source component.

#### `IntegrationResolvedRoute.isPrerendered`

[Section titled “IntegrationResolvedRoute.isPrerendered”](#integrationresolvedrouteisprerendered)

**Type:** [`RouteData['prerender']`](#routedataprerender)

Determines whether the route use [on demand rendering](/en/guides/on-demand-rendering/). The value will be `true` for projects configured with:

*   `output: 'static'` when the route does not export `const prerender = true`
*   `output: 'server'` when the route exports `const prerender = false`

#### `IntegrationResolvedRoute.redirectRoute`

[Section titled “IntegrationResolvedRoute.redirectRoute”](#integrationresolvedrouteredirectroute)

**Type:** `IntegrationResolvedRoute | undefined`

When the value of `IntegrationResolvedRoute.type` is `redirect`, the value will be the `IntegrationResolvedRoute` to redirect to. Otherwise, the value will be undefined.

#### `IntegrationResolvedRoute.fallbackRoutes`

[Section titled “IntegrationResolvedRoute.fallbackRoutes”](#integrationresolvedroutefallbackroutes)

**Type:** `IntegrationResolvedRoute[]`  

**Added in:** `astro@6.1.0` New

When the project uses [i18n with fallback routes](/en/guides/internationalization/#fallback), the value will be a list of the routes this route falls back to when the requested locale isn’t available. The fallback content may be served as a redirect or rewrite depending on `i18n.routing.fallbackType`. Otherwise, the value will be an empty array.

#### `IntegrationResolvedRoute.generate()`

[Section titled “IntegrationResolvedRoute.generate()”](#integrationresolvedroutegenerate)

**Type:** `(data?: any) => string`  

**Added in:** `astro@6.0.0`

A function that provides the optional parameters of the route, interpolates them with the route pattern, and returns the path name of the route.

For example, with a route such as `/blog/[...id].astro`, the `generate()` function could return:

```
generate({ id: 'presentation' }) // will output `/blog/presentation`
```

### `RedirectConfig`

[Section titled “RedirectConfig”](#redirectconfig)

**Type:** `string | { status: [ValidRedirectStatus](#validredirectstatus); destination: string; }`

Describes the destination of a redirect. This can be a string or an object containing information about the status code and its destination.

### `RouteData`

[Section titled “RouteData”](#routedata)

Describes the information about a route.

#### `RouteData.route`

[Section titled “RouteData.route”](#routedataroute)

**Type:** `string`

Defines the current route pattern. Here are some examples of paths associated with their pattern:

*   `src/pages/index.astro` will be `/`
*   `src/pages/blog/[...slug].astro` will be `/blog/[...slug]`
*   `src/pages/site/[blog]/[...slug].astro` will be `/site/[blog]/[...slug]`

#### `RouteData.component`

[Section titled “RouteData.component”](#routedatacomponent)

**Type:** `string`

Specifies the source component URL.

#### `RouteData.params`

[Section titled “RouteData.params”](#routedataparams)

**Type:** `string[]`

Allows you to access the route `params`. For example, when a project uses the following [dynamic routes](/en/guides/routing/#dynamic-routes) `/pages/[lang]/[...slug].astro`, the value will be `['lang', '...slug']`.

#### `RouteData.pathname`

[Section titled “RouteData.pathname”](#routedatapathname)

**Type:** `string | undefined`

For regular routes, the value will be the URL pathname where this route will be served. When the project uses [dynamic routes](/en/guides/routing/#dynamic-routes) (ie. `[dynamic]` or `[...spread]`), the pathname will be undefined.

#### `RouteData.distURL`

[Section titled “RouteData.distURL”](#routedatadisturl)

**Type:** `URL[]`  

**Added in:** `astro@5.0.0`

Defines the paths of the physical files emitted by this route. When a route isn’t prerendered, the value is an empty array.

#### `RouteData.pattern`

[Section titled “RouteData.pattern”](#routedatapattern)

**Type:** `RegExp`

Specifies a regex to use for matching an input URL against a requested route.

For example, given a `[fruit]/about.astro` path, the regex will be `/^\/([^/]+?)\/about\/?$/`. Using `pattern.test("banana/about")` will return `true`.

#### `RouteData.segments`

[Section titled “RouteData.segments”](#routedatasegments)

**Type:** `[RoutePart](#routepart)[][]`

Allows you to access the route [`params`](#routedataparams) with additional metadata. Each object contains the following properties:

*   `content`: the `param` name,
*   `dynamic`: whether the route is dynamic or not,
*   `spread`: whether the dynamic route uses the spread syntax or not.

For example, the following route `/pages/[blog]/[...slug].astro` will output the segments:

```
[  [ { content: 'pages', dynamic: false, spread: false } ],  [ { content: 'blog', dynamic: true, spread: false } ],  [ { content: '...slug', dynamic: true, spread: true } ]]
```

#### `RouteData.type`

[Section titled “RouteData.type”](#routedatatype)

**Type:** [`RouteType`](#routetype)

Allows you to identify the [type of route](#routetype).

#### `RouteData.prerender`

[Section titled “RouteData.prerender”](#routedataprerender)

**Type:** `boolean`

Determines whether a route uses [on demand rendering](/en/guides/on-demand-rendering/) or is statically prerendered at build time.

See also [`prerendered`](/en/reference/routing-reference/#prerender) in the routing reference.

#### `RouteData.redirect`

[Section titled “RouteData.redirect”](#routedataredirect)

**Type:** `[RedirectConfig](#redirectconfig) | undefined`

Allows you to access the route to redirect to.

#### `RouteData.redirectRoute`

[Section titled “RouteData.redirectRoute”](#routedataredirectroute)

**Type:** `RouteData | undefined`

Specifies the `RouteData` to redirect to when [`RouteData.type`](#routedatatype) is `redirect`.

#### `RouteData.fallbackRoutes`

[Section titled “RouteData.fallbackRoutes”](#routedatafallbackroutes)

**Type:** `RouteData[]`  

**Added in:** `astro@3.5.6`

Defines a list of `RouteData` to fallback to when [`i18n.fallback`](/en/reference/configuration-reference/#i18nfallback) has a list of locales.

#### `RouteData.isIndex`

[Section titled “RouteData.isIndex”](#routedataisindex)

**Type:** `boolean`

Specifies if the route is a directory index (e.g. `src/pages/index.astro`, `src/pages/blog/index.astro`).

#### `RouteData.origin`

[Section titled “RouteData.origin”](#routedataorigin)

**Type:** `'internal' | 'external' | 'project'`  

**Added in:** `astro@5.0.0`

Determines if a route comes from Astro core (`internal`), an integration (`external`) or the user’s project (`project`).

### `RoutePart`

[Section titled “RoutePart”](#routepart)

**Type:** `{ content: string; dynamic: boolean; spread: boolean; }`

Describes a route segment.

#### `RoutePart.content`

[Section titled “RoutePart.content”](#routepartcontent)

**Type:** `string`

Specifies the parameter name for the route. For example:

*   `about.astro` has the name `about`
*   `[slug].astro` has the name `slug`
*   `[...id].astro` has the name `id`

#### `RoutePart.dynamic`

[Section titled “RoutePart.dynamic”](#routepartdynamic)

**Type:** `boolean`

Whether the route is dynamic or not.

#### `RoutePart.spread`

[Section titled “RoutePart.spread”](#routepartspread)

**Type:** `boolean`

Whether the dynamic route uses the spread syntax or not.

### `RouteType`

[Section titled “RouteType”](#routetype)

**Type:** `'page' | 'endpoint' | 'redirect' | 'fallback'`

A union of supported route types:

*   `page`: a route that lives in the file system, usually an Astro component
*   `endpoint`: a route that lives in the file system, usually a JS file that exposes endpoints methods
*   `redirect`: a route points to another route that lives in the file system
*   `fallback`: a route that doesn’t exist in the file system that needs to be handled with other means, usually a middleware

### `SSRComponentMetadata`

[Section titled “SSRComponentMetadata”](#ssrcomponentmetadata)

**Type:** `{ propagation: PropagationHint; containsHead: boolean; }`

Describes the build metadata of a component rendered by the server.

#### `SSRComponentMetadata.propagation`

[Section titled “SSRComponentMetadata.propagation”](#ssrcomponentmetadatapropagation)

**Type:** `'none' | 'self' | 'in-tree'`

A description of how to render head content from this component, including whether the Astro runtime needs to wait for a component:

*   `none`: The component does not propagate the head content.
*   `self`: The component appends the head content.
*   `in-tree`: Another component within this component’s dependency tree appends the head content.

#### `SSRComponentMetadata.containsHead`

[Section titled “SSRComponentMetadata.containsHead”](#ssrcomponentmetadatacontainshead)

**Type:** `boolean`

Determines whether the component contains the head content.

### `SSRManifest`

[Section titled “SSRManifest”](#ssrmanifest)

An object containing build configuration and project metadata that the server adapters use at runtime to serve on-demand rendered pages.

#### `SSRManifest.adapterName`

[Section titled “SSRManifest.adapterName”](#ssrmanifestadaptername)

**Type:** `string`

Defines the name of the [server adapter](/en/guides/on-demand-rendering/#server-adapters) used for on-demand rendering.

#### `SSRManifest.routes`

[Section titled “SSRManifest.routes”](#ssrmanifestroutes)

**Type:** `RouteInfo[]`

A list of information about the routes available in this project. Each entry contains the following properties.

##### `RouteInfo.routeData`

[Section titled “RouteInfo.routeData”](#routeinforoutedata)

**Type:** [`RouteData`](#routedata)

An object describing known information about a route.

##### `RouteInfo.file`

[Section titled “RouteInfo.file”](#routeinfofile)

**Type:** `string`

Specifies the file path to the built route entrypoint.

##### `RouteInfo.links`

[Section titled “RouteInfo.links”](#routeinfolinks)

**Type:** `string[]`

Defines a list of [HTML `link` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link) required by this route.

##### `RouteInfo.scripts`

[Section titled “RouteInfo.scripts”](#routeinfoscripts)

**Type:** `Array<{ children: string; stage: string } | { type: 'inline' | 'external'; value: string }>`

Defines a list of scripts associated with this route. This includes both integration-injected scripts with `children` and `stage` properties and hoisted scripts with `type` and `value` properties.

##### `RouteInfo.styles`

[Section titled “RouteInfo.styles”](#routeinfostyles)

**Type:** `Array<{ type: "inline"; content: string; } | { type: "external"; src: string; }>`  

**Added in:** `astro@2.4.0`

Defines the list of stylesheets associated with this route. This includes both inline styles and stylesheet URLs.

#### `SSRManifest.site`

[Section titled “SSRManifest.site”](#ssrmanifestsite)

**Type:** `string`

Specifies the [configured `site`](/en/reference/configuration-reference/#site).

#### `SSRManifest.base`

[Section titled “SSRManifest.base”](#ssrmanifestbase)

**Type:** `string`

Specifies the [configured `base` path](/en/reference/configuration-reference/#base) to deploy to.

#### `SSRManifest.userAssetsBase`

[Section titled “SSRManifest.userAssetsBase”](#ssrmanifestuserassetsbase)

**Type:** `string | undefined`  

**Added in:** `astro@5.3.1`

Specifies the base path to use in development mode for user-generated assets, such as scripts and styles.

#### `SSRManifest.trailingSlash`

[Section titled “SSRManifest.trailingSlash”](#ssrmanifesttrailingslash)

**Type:** [`AstroConfig['trailingSlash']`](/en/reference/configuration-reference/#trailingslash)  

**Added in:** `astro@3.5.4`

Specifies the [configured behavior for trailing slashes](/en/reference/configuration-reference/#trailingslash) in development mode and for on-demand rendered pages.

#### `SSRManifest.buildFormat`

[Section titled “SSRManifest.buildFormat”](#ssrmanifestbuildformat)

**Type:** [`NonNullable<AstroConfig['build']>['format']`](/en/reference/configuration-reference/#buildformat)  

**Added in:** `astro@4.2.2`

Specifies the [configured output file format](/en/reference/configuration-reference/#buildformat).

#### `SSRManifest.compressHTML`

[Section titled “SSRManifest.compressHTML”](#ssrmanifestcompresshtml)

**Type:** `boolean`  

**Added in:** `astro@2.7.2`

Determines whether [HTML minification is enabled in the project configuration](/en/reference/configuration-reference/#compresshtml).

#### `SSRManifest.assetsPrefix`

[Section titled “SSRManifest.assetsPrefix”](#ssrmanifestassetsprefix)

**Type:** `string | ({ fallback: string; } & Record<string, string>) | undefined`  

**Added in:** `astro@2.3.1`

Specifies the [configured prefix for Astro-generated asset links](/en/reference/configuration-reference/#buildassetsprefix).

#### `SSRManifest.renderers`

[Section titled “SSRManifest.renderers”](#ssrmanifestrenderers)

**Type:** `[SSRLoadedRenderer](/en/reference/renderer-reference/#ssrloadedrenderer)[]`

A list of renderers (e.g. React, Vue, Svelte, MDX) available for the server to use.

#### `SSRManifest.serverLike`

[Section titled “SSRManifest.serverLike”](#ssrmanifestserverlike)

**Type:** `boolean`  

**Added in:** `astro@6.0.0`

Determines whether this application uses any on-demand rendered routes.

#### `SSRManifest.clientDirectives`

[Section titled “SSRManifest.clientDirectives”](#ssrmanifestclientdirectives)

**Type:** `Map<string, string>`  

**Added in:** `astro@2.5.0`

Defines a mapping of client directive names (e.g. `load`, `visible`) to their implementation code. This includes both [built-in client directives](/en/reference/directives-reference/#client-directives) and [custom client directives](/en/reference/directives-reference/#custom-client-directives).

#### `SSRManifest.entryModules`

[Section titled “SSRManifest.entryModules”](#ssrmanifestentrymodules)

**Type:** `Record<string, string>`

Defines a mapping of entrypoints to their output file paths.

#### `SSRManifest.inlinedScripts`

[Section titled “SSRManifest.inlinedScripts”](#ssrmanifestinlinedscripts)

**Type:** `Map<string, string>`  

**Added in:** `astro@4.5.0`

Defines a mapping of script identifiers to their content for scripts that will be inlined in the HTML output.

#### `SSRManifest.assets`

[Section titled “SSRManifest.assets”](#ssrmanifestassets)

**Type:** `Set<string>`

Defines a set of file paths for all assets that are part of the build.

#### `SSRManifest.componentMetadata`

[Section titled “SSRManifest.componentMetadata”](#ssrmanifestcomponentmetadata)

**Type:** `Map<string, [SSRComponentMetadata](#ssrcomponentmetadata)>`  

**Added in:** `astro@2.1.7`

Defines a mapping of component identifiers to their build metadata. Each entry contains information about the [`propagation`](#ssrcomponentmetadatapropagation) behavior and whether it contains head elements.

#### `SSRManifest.pageModule`

[Section titled “SSRManifest.pageModule”](#ssrmanifestpagemodule)

**Type:** `{ page: ImportComponentInstance; onRequest?: MiddlewareHandler; }`  

**Added in:** `astro@2.7.0`

Specifies information about a page module.

##### `SSRManifest.pageModule.page()`

[Section titled “SSRManifest.pageModule.page()”](#ssrmanifestpagemodulepage)

**Type:** `() => Promise<ComponentInstance>`

A function to retrieve an instance of the page component.

##### `SSRManifest.pageModule.onRequest()`

[Section titled “SSRManifest.pageModule.onRequest()”](#ssrmanifestpagemoduleonrequest)

**Type:** [`MiddlewareHandler`](/en/reference/modules/astro-middleware/#middlewarehandler)  

**Added in:** `astro@3.0.3`

An [Astro middleware function](/en/reference/modules/astro-middleware/#onrequest) when defined in the user project.

#### `SSRManifest.pageMap`

[Section titled “SSRManifest.pageMap”](#ssrmanifestpagemap)

**Type:** `Map<string, () => Promise<[typeof pageModule](#ssrmanifestpagemodule)>>`

Defines a mapping of component paths to their importable instances.

#### `SSRManifest.serverIslandMappings`

[Section titled “SSRManifest.serverIslandMappings”](#ssrmanifestserverislandmappings)

**Type:** `() => Promise<ServerIslandMappings> | ServerIslandMappings`  

**Added in:** `astro@6.0.0`

An object, or a function that returns an object, describing available server islands mapping.

##### `SSRManifest.serverIslandMappings.serverIslandMap`

[Section titled “SSRManifest.serverIslandMappings.serverIslandMap”](#ssrmanifestserverislandmappingsserverislandmap)

**Type:** `Map<string, () => Promise<ComponentInstance>>`  

**Added in:** `astro@4.12.0`

Defines a mapping of server island IDs to their component instances.

##### `SSRManifest.serverIslandMappings.serverIslandNameMap`

[Section titled “SSRManifest.serverIslandMappings.serverIslandNameMap”](#ssrmanifestserverislandmappingsserverislandnamemap)

**Type:** `Map<string, string>`  

**Added in:** `astro@4.12.0`

Defines a mapping of server island component paths to their assigned names.

#### `SSRManifest.key`

[Section titled “SSRManifest.key”](#ssrmanifestkey)

**Type:** `Promise<CryptoKey>`  

**Added in:** `astro@4.13.4`

Determines the [cryptographic key](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKey) used for encrypting server island props.

#### `SSRManifest.i18n`

[Section titled “SSRManifest.i18n”](#ssrmanifesti18n)

**Type:** `SSRManifestI18n | undefined`  

**Added in:** `astro@3.5.0`

Specifies the resolved [`i18n` configuration](/en/reference/configuration-reference/#i18n) when enabled in the project.

##### `SSRManifest.i18n.strategy`

[Section titled “SSRManifest.i18n.strategy”](#ssrmanifesti18nstrategy)

**Type:** `"manual" | "pathname-prefix-always" | "pathname-prefix-other-locales" | "pathname-prefix-always-no-redirect" | "domains-prefix-always" | "domains-prefix-other-locales" | "domains-prefix-always-no-redirect"`

Defines the [i18n routing strategy](/en/reference/configuration-reference/#i18nrouting) configured. This determines how locales are handled in URLs and whether redirects occur.

##### `SSRManifest.i18n.locales`

[Section titled “SSRManifest.i18n.locales”](#ssrmanifesti18nlocales)

**Type:** `Locales`

Specifies a list of [supported locales configured in the project](/en/reference/configuration-reference/#i18nlocales).

##### `SSRManifest.i18n.defaultLocale`

[Section titled “SSRManifest.i18n.defaultLocale”](#ssrmanifesti18ndefaultlocale)

**Type:** `string`

Determines the [default locale configured in the project](/en/reference/configuration-reference/#i18ndefaultlocale).

##### `SSRManifest.i18n.fallback`

[Section titled “SSRManifest.i18n.fallback”](#ssrmanifesti18nfallback)

**Type:** `Record<string, string> | undefined`

Specifies a mapping of locales to their fallback locales as [configured in `i18n.fallback`](/en/reference/configuration-reference/#i18nfallback).

##### `SSRManifest.i18n.fallbackType`

[Section titled “SSRManifest.i18n.fallbackType”](#ssrmanifesti18nfallbacktype)

**Type:** `"redirect" | "rewrite"`

Determines the [configured fallback strategy for the project](/en/reference/configuration-reference/#i18nroutingfallbacktype).

##### `SSRManifest.i18n.domainLookupTable`

[Section titled “SSRManifest.i18n.domainLookupTable”](#ssrmanifesti18ndomainlookuptable)

**Type:** `Record<string, string>`

A mapping of [configured domains](/en/reference/configuration-reference/#i18ndomains) to their associated locales.

#### `SSRManifest.middleware`

[Section titled “SSRManifest.middleware”](#ssrmanifestmiddleware)

**Type:** `() => Promise<[AstroMiddlewareInstance](#astromiddlewareinstance)> | [AstroMiddlewareInstance](#astromiddlewareinstance)`  

**Added in:** `astro@4.2.5`

Defines an instance to load the middleware.

#### `SSRManifest.actions`

[Section titled “SSRManifest.actions”](#ssrmanifestactions)

**Type:** `() => Promise<{ server: Record<string, [ActionClient](/en/reference/modules/astro-actions/#actionclient)>; }> | { server: Record<string, [ActionClient](/en/reference/modules/astro-actions/#actionclient)>; }`  

**Added in:** `astro@5.4.2`

An object, or a function that returns an object, with a `server` property that maps action names to their callable functions.

#### `SSRManifest.sessionDriver()`

[Section titled “SSRManifest.sessionDriver()”](#ssrmanifestsessiondriver)

**Type:** `() => Promise<{ default: SessionDriverFactory | null }>`  

**Added in:** `astro@6.0.0`

Retrieves the [configured session driver](/en/reference/configuration-reference/#sessiondriver) when enabled.

#### `SSRManifest.checkOrigin`

[Section titled “SSRManifest.checkOrigin”](#ssrmanifestcheckorigin)

**Type:** `boolean`  

**Added in:** `astro@4.6.0`

Determines whether [origin checking is enabled in the security configuration](/en/reference/configuration-reference/#securitycheckorigin).

#### `SSRManifest.allowedDomains`

[Section titled “SSRManifest.allowedDomains”](#ssrmanifestalloweddomains)

**Type:** `Partial<[RemotePattern](/en/reference/modules/astro-assets/#remotepattern)>[]`

Specifies the [configured list of permitted host patterns](/en/reference/configuration-reference/#securityalloweddomains) for incoming requests when using on-demand rendering.

#### `SSRManifest.sessionConfig`

[Section titled “SSRManifest.sessionConfig”](#ssrmanifestsessionconfig)

**Type:** `[SessionConfig<TDriver>](/en/reference/configuration-reference/#session-options) & { driverModule?: () => Promise<{ default: () => unstorage.Driver }>; }`  

**Added in:** `astro@5.1.0`

An object containing the [resolved session configuration](/en/reference/configuration-reference/#session-options) and an additional property defining the driver in use.

#### `SSRManifest.cacheDir`

[Section titled “SSRManifest.cacheDir”](#ssrmanifestcachedir)

**Type:** `URL`  

**Added in:** `astro@5.2.0`

Specifies the [configured directory for caching build artifacts](/en/reference/configuration-reference/#cachedir).

#### `SSRManifest.srcDir`

[Section titled “SSRManifest.srcDir”](#ssrmanifestsrcdir)

**Type:** `URL`  

**Added in:** `astro@5.2.0`

Specifies the [configured directory that Astro will read the site from](/en/reference/configuration-reference/#srcdir).

#### `SSRManifest.outDir`

[Section titled “SSRManifest.outDir”](#ssrmanifestoutdir)

**Type:** `URL`  

**Added in:** `astro@5.2.0`

Specifies the [configured directory in which to write the final build](/en/reference/configuration-reference/#outdir).

#### `SSRManifest.rootDir`

[Section titled “SSRManifest.rootDir”](#ssrmanifestrootdir)

**Type:** `URL`  

**Added in:** `astro@6.0.0`

Specifies the resolved URL for the [directory configured as the project root](/en/reference/configuration-reference/#root).

#### `SSRManifest.publicDir`

[Section titled “SSRManifest.publicDir”](#ssrmanifestpublicdir)

**Type:** `URL`  

**Added in:** `astro@5.2.0`

Specifies the [configured directory for the static assets](/en/reference/configuration-reference/#publicdir).

#### `SSRManifest.assetsDir`

[Section titled “SSRManifest.assetsDir”](#ssrmanifestassetsdir)

**Type:** `string`  

**Added in:** `astro@6.0.0`

Specifies the [configured directory for generated assets](/en/reference/configuration-reference/#buildassets) in the build output.

#### `SSRManifest.buildClientDir`

[Section titled “SSRManifest.buildClientDir”](#ssrmanifestbuildclientdir)

**Type:** `URL`  

**Added in:** `astro@5.2.0`

Determines the path where client-side build artifacts (e.g. JavaScript, CSS) are output within the build directory.

#### `SSRManifest.buildServerDir`

[Section titled “SSRManifest.buildServerDir”](#ssrmanifestbuildserverdir)

**Type:** `URL`  

**Added in:** `astro@5.2.0`

Determines the path where server-side build artifacts are output within the build directory.

#### `SSRManifest.csp`

[Section titled “SSRManifest.csp”](#ssrmanifestcsp)

**Type:** `SSRManifestCSP | undefined`  

**Added in:** `astro@5.9.0`

Describes the [Content Security Policy configuration](/en/reference/configuration-reference/#securitycsp).

##### `SSRManifest.csp.cspDestination`

[Section titled “SSRManifest.csp.cspDestination”](#ssrmanifestcspcspdestination)

**Type:** `'adapter' | 'meta' | 'header' | undefined`

Specifies whether CSP directives should be injected as a `meta` element, as a response `header`, or by the [`adapter` when it supports setting response headers](/en/reference/adapter-reference/#staticheaders).

##### `SSRManifest.csp.algorithm`

[Section titled “SSRManifest.csp.algorithm”](#ssrmanifestcspalgorithm)

**Type:** `'SHA-256' | 'SHA-384' | 'SHA-512'`

Specifies the [configured hash function](/en/reference/configuration-reference/#securitycspalgorithm).

##### `SSRManifest.csp.scriptHashes`

[Section titled “SSRManifest.csp.scriptHashes”](#ssrmanifestcspscripthashes)

**Type:** `string[]`

Specifies a list of generated hashes for project scripts and [user-supplied hashes](/en/reference/configuration-reference/#securitycspscriptdirectivehashes) for external scripts.

##### `SSRManifest.csp.scriptResources`

[Section titled “SSRManifest.csp.scriptResources”](#ssrmanifestcspscriptresources)

**Type:** `string[]`

Specifies a list of valid sources combining the [configured script resources](/en/reference/configuration-reference/#securitycspscriptdirectiveresources) and the [injected script resources](/en/reference/api-reference/#cspinsertscriptresource).

##### `SSRManifest.csp.isStrictDynamic`

[Section titled “SSRManifest.csp.isStrictDynamic”](#ssrmanifestcspisstrictdynamic)

**Type:** `boolean`

Determines whether support for [dynamic script injection is enabled in the configuration](/en/reference/configuration-reference/#securitycspscriptdirectivestrictdynamic).

##### `SSRManifest.csp.styleHashes`

[Section titled “SSRManifest.csp.styleHashes”](#ssrmanifestcspstylehashes)

**Type:** `string[]`

Specifies a list of generated hashes for project styles and [user-supplied hashes](/en/reference/configuration-reference/#securitycspstyledirectivehashes) for external styles.

##### `SSRManifest.csp.styleResources`

[Section titled “SSRManifest.csp.styleResources”](#ssrmanifestcspstyleresources)

**Type:** `string[]`

Specifies a list of valid sources combining the [configured style resources](/en/reference/configuration-reference/#securitycspstyledirectiveresources) and the [injected style resources](/en/reference/api-reference/#cspinsertstyleresource).

##### `SSRManifest.csp.directives`

[Section titled “SSRManifest.csp.directives”](#ssrmanifestcspdirectives)

**Type:** `CspDirective[]`

Specifies the [configured list of valid sources](/en/reference/configuration-reference/#securitycspdirectives) for specific content types.

#### `SSRManifest.devToolbar`

[Section titled “SSRManifest.devToolbar”](#ssrmanifestdevtoolbar)

**Type:** `{ enabled: boolean; latestAstroVersion: string | undefined; debugInfoOutput: string | undefined; }`  

**Added in:** `astro@6.0.0`

Describes the resolved dev toolbar settings.

##### `SSRManifest.devToolbar.enabled`

[Section titled “SSRManifest.devToolbar.enabled”](#ssrmanifestdevtoolbarenabled)

**Type:** `boolean`  

**Added in:** `astro@6.0.0`

Determines [whether the dev toolbar is enabled](/en/reference/configuration-reference/#devtoolbarenabled).

##### `SSRManifest.devToolbar.latestAstroVersion`

[Section titled “SSRManifest.devToolbar.latestAstroVersion”](#ssrmanifestdevtoolbarlatestastroversion)

**Type:** `string | undefined`  

**Added in:** `astro@6.0.0`

Specifies the latest available version of Astro. This is used to notify the user in the dev toolbar of when an update is available. This will be `undefined` when one of the following conditions applies:

*   the check fails or has not been completed yet
*   the user has disabled the check
*   the user is already using the latest version

##### `SSRManifest.devToolbar.debugInfoOutput`

[Section titled “SSRManifest.devToolbar.debugInfoOutput”](#ssrmanifestdevtoolbardebuginfooutput)

**Type:** `string | undefined`  

**Added in:** `astro@6.0.0`

Defines the serialized [debug information](/en/reference/cli-reference/#astro-info) passed to the dev toolbar for display.

#### `SSRManifest.internalFetchHeaders`

[Section titled “SSRManifest.internalFetchHeaders”](#ssrmanifestinternalfetchheaders)

**Type:** `Record<string, string>`  

**Added in:** `astro@5.15.0`

Specifies the headers that are automatically added to internal fetch requests made during rendering.

#### `SSRManifest.logLevel`

[Section titled “SSRManifest.logLevel”](#ssrmanifestloglevel)

**Type:** `"error" | "warn" | "debug" | "info" | "silent"`  

**Added in:** `astro@6.0.0`

Specifies the [Vite logging level](https://vite.dev/config/shared-options#loglevel).

### `ValidRedirectStatus`

[Section titled “ValidRedirectStatus”](#validredirectstatus)

**Type:** `301 | 302 | 303 | 307 | 308 | 300 | 304`

A union of supported redirect status code.

## Allow installation with `astro add`

[Section titled “Allow installation with astro add”](#allow-installation-with-astro-add)

[The `astro add` command](/en/reference/cli-reference/#astro-add) allows users to easily add integrations and adapters to their project. If you want _your_ integration to be installable with this tool, **add `astro-integration` to the `keywords` field in your `package.json`**:

```
{  "name": "example",  "keywords": ["astro-integration"],}
```

Once you [publish your integration to npm](https://docs.npmjs.com/cli/v8/commands/npm-publish), running `astro add example` will install your package with any peer dependencies specified in your `package.json`. This will also apply your integration to the user’s `astro.config.*` like so:

```
import { defineConfig } from 'astro/config';import example from 'example';
export default defineConfig({  integrations: [example()],})
```

## Integration Ordering

[Section titled “Integration Ordering”](#integration-ordering)

All integrations are run in the order that they are configured. For instance, for the array `[react(), svelte()]` in a user’s `astro.config.*`, `react` will run before `svelte`.

Your integration should ideally run in any order. If this isn’t possible, we recommend documenting that your integration needs to come first or last in your user’s `integrations` configuration array.

## Combine integrations into presets

[Section titled “Combine integrations into presets”](#combine-integrations-into-presets)

An integration can also be written as a collection of multiple, smaller integrations. We call these collections **presets.** Instead of creating a factory function that returns a single integration object, a preset returns an _array_ of integration objects. This is useful for building complex features out of multiple integrations.

```
integrations: [  // Example: where examplePreset() returns: [integrationOne, integrationTwo, ...etc]  examplePreset()]
```

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [Build your own Astro Integrations](https://www.freecodecamp.org/news/how-to-use-the-astro-ui-framework/#chapter-8-build-your-own-astro-integrations-1) - by Emmanuel Ohans on FreeCodeCamp
*   [Astro Integration Template](https://github.com/florian-lefebvre/astro-integration-template) - by Florian Lefebvre on GitHub

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


