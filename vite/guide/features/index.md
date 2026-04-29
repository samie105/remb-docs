---
title: "Features ​"
source: "https://vite.dev/guide/features"
canonical_url: "https://vite.dev/guide/features"
docset: "vite"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:38.964Z"
content_hash: "9344cd9bba71a44460873e2c6440c42483921edc49187d4aa1b7122efcd75ef0"
menu_path: ["Features ​"]
section_path: []
nav_prev: {"path": "vite/guide/why/index.md", "title": "Why Vite \u200b"}
nav_next: {"path": "vite/guide/cli/index.md", "title": "Command Line Interface \u200b"}
---

# .scss and .sass
npm add -D sass-embedded # or sass

# .less
npm add -D less

# .styl and .stylus
npm add -D stylus
```

If using Vue single file components, this also automatically enables `<style lang="sass">` et al.

Vite improves `@import` resolving for Sass and Less so that Vite aliases are also respected. In addition, relative `url()` references inside imported Sass/Less files that are in different directories from the root file are also automatically rebased to ensure correctness. Rebasing `url()` references that start with a variable or a interpolation are not supported due to its API constraints.

`@import` alias and url rebasing are not supported for Stylus due to its API constraints.

You can also use CSS modules combined with pre-processors by prepending `.module` to the file extension, for example `style.module.scss`.

### Disabling CSS injection into the page [​](#disabling-css-injection-into-the-page)

The automatic injection of CSS contents can be turned off via the `?inline` query parameter. In this case, the processed CSS string is returned as the module's default export as usual, but the styles aren't injected to the page.

js

```
import './foo.css' // will be injected into the page
import otherStyles from './bar.css?inline' // will not be injected
```

NOTE

Default and named imports from CSS files (e.g `import style from './foo.css'`) are removed since Vite 5. Use the `?inline` query instead.

### Lightning CSS [​](#lightning-css)

Vite uses [Lightning CSS](https://lightningcss.dev/) to minify CSS in production builds by default. However, PostCSS is still used for other CSS processing.

There is experimental support for using Lightning CSS for CSS processing entirely. You can opt into it by adding [`css.transformer: 'lightningcss'`](../../config/shared-options/index.md#css-transformer).

To configure it, you can pass Lightning CSS options to the [`css.lightningcss`](../../config/shared-options/index.md#css-lightningcss) config option. To configure CSS Modules, you should use [`css.lightningcss.cssModules`](https://lightningcss.dev/css-modules.html) instead of [`css.modules`](../../config/shared-options/index.md#css-modules) (which configures the way PostCSS handles CSS modules).

## Static Assets [​](#static-assets)

Importing a static asset will return the resolved public URL when it is served:

js

```
import imgUrl from './img.png'
document.getElementById('hero-img').src = imgUrl
```

Special queries can modify how assets are loaded:

js

```
// Explicitly load assets as URL (automatically inlined depending on the file size)
import assetAsURL from './asset.js?url'
```

js

```
// Load assets as strings
import assetAsString from './shader.glsl?raw'
```

js

```
// Load Web Workers
import Worker from './worker.js?worker'
```

js

```
// Web Workers inlined as base64 strings at build time
import InlineWorker from './worker.js?worker&inline'
```

More details in [Static Asset Handling](../assets/index.md).

## JSON [​](#json)

JSON files can be directly imported - named imports are also supported:

js

```
// import the entire object
import json from './example.json'
// import a root field as named exports - helps with tree-shaking!
import { field } from './example.json'
```

## Glob Import [​](#glob-import)

Vite supports importing multiple modules from the file system via the special `import.meta.glob` function:

js

```
const modules = import.meta.glob('./dir/*.js')
```

The above will be transformed into the following:

js

```
// code produced by vite
const modules = {
  './dir/bar.js': () => import('./dir/bar.js'),
  './dir/foo.js': () => import('./dir/foo.js'),
}
```

You can then iterate over the keys of the `modules` object to access the corresponding modules:

js

```
for (const path in modules) {
  modules[path]().then((mod) => {
    console.log(path, mod)
  })
}
```

Matched files are by default lazy-loaded via dynamic import and will be split into separate chunks during build. If you'd rather import all the modules directly (e.g. relying on side-effects in these modules to be applied first), you can pass `{ eager: true }` as the second argument:

js

```
const modules = import.meta.glob('./dir/*.js', { eager: true })
```

The above will be transformed into the following:

js

```
// code produced by vite
import * as __vite_glob_0_0 from './dir/bar.js'
import * as __vite_glob_0_1 from './dir/foo.js'
const modules = {
  './dir/bar.js': __vite_glob_0_0,
  './dir/foo.js': __vite_glob_0_1,
}
```

### Multiple Patterns [​](#multiple-patterns)

The first argument can be an array of globs, for example

js

```
const modules = import.meta.glob(['./dir/*.js', './another/*.js'])
```

### Negative Patterns [​](#negative-patterns)

Negative glob patterns are also supported (prefixed with `!`). To ignore some files from the result, you can add exclude glob patterns to the first argument:

js

```
const modules = import.meta.glob(['./dir/*.js', '!**/bar.js'])
```

js

```
// code produced by vite
const modules = {
  './dir/foo.js': () => import('./dir/foo.js'),
}
```

#### Named Imports [​](#named-imports)

It's possible to only import parts of the modules with the `import` options.

ts

```
const modules = import.meta.glob('./dir/*.js', { import: 'setup' })
```

ts

```
// code produced by vite
const modules = {
  './dir/bar.js': () => import('./dir/bar.js').then((m) => m.setup),
  './dir/foo.js': () => import('./dir/foo.js').then((m) => m.setup),
}
```

When combined with `eager` it's even possible to have tree-shaking enabled for those modules.

ts

```
const modules = import.meta.glob('./dir/*.js', {
  import: 'setup',
  eager: true,
})
```

ts

```
// code produced by vite:
import { setup as __vite_glob_0_0 } from './dir/bar.js'
import { setup as __vite_glob_0_1 } from './dir/foo.js'
const modules = {
  './dir/bar.js': __vite_glob_0_0,
  './dir/foo.js': __vite_glob_0_1,
}
```

Set `import` to `default` to import the default export.

ts

```
const modules = import.meta.glob('./dir/*.js', {
  import: 'default',
  eager: true,
})
```

ts

```
// code produced by vite:
import { default as __vite_glob_0_0 } from './dir/bar.js'
import { default as __vite_glob_0_1 } from './dir/foo.js'
const modules = {
  './dir/bar.js': __vite_glob_0_0,
  './dir/foo.js': __vite_glob_0_1,
}
```

#### Custom Queries [​](#custom-queries)

You can also use the `query` option to provide queries to imports, for example, to import assets [as a string](../assets/index.md#importing-asset-as-string) or [as a url](../assets/index.md#importing-asset-as-url):

ts

```
const moduleStrings = import.meta.glob('./dir/*.svg', {
  query: '?raw',
  import: 'default',
})
const moduleUrls = import.meta.glob('./dir/*.svg', {
  query: '?url',
  import: 'default',
})
```

ts

```
// code produced by vite:
const moduleStrings = {
  './dir/bar.svg': () => import('./dir/bar.svg?raw').then((m) => m['default']),
  './dir/foo.svg': () => import('./dir/foo.svg?raw').then((m) => m['default']),
}
const moduleUrls = {
  './dir/bar.svg': () => import('./dir/bar.svg?url').then((m) => m['default']),
  './dir/foo.svg': () => import('./dir/foo.svg?url').then((m) => m['default']),
}
```

You can also provide custom queries for other plugins to consume:

ts

```
const modules = import.meta.glob('./dir/*.js', {
  query: { foo: 'bar', bar: true },
})
```

#### Base Path [​](#base-path)

You can also use the `base` option to provide base path for the imports:

ts

```
const modulesWithBase = import.meta.glob('./**/*.js', {
  base: './base',
})
```

ts

```
// code produced by vite:
const modulesWithBase = {
  './dir/foo.js': () => import('./base/dir/foo.js'),
  './dir/bar.js': () => import('./base/dir/bar.js'),
}
```

The base option can only be a directory path relative to the importer file or absolute against the project root. Aliases and virtual modules aren't supported.

Only the globs that are relative paths are interpreted as relative to the resolved base.

All the resulting module keys are modified to be relative to the base if provided.

### Glob Import Caveats [​](#glob-import-caveats)

Note that:

*   This is a Vite-only feature and is not a web or ES standard.
*   The glob patterns are treated like import specifiers: they must be either relative (start with `./`) or absolute (start with `/`, resolved relative to project root) or an alias path (see [`resolve.alias` option](../../config/shared-options/index.md#resolve-alias)).
*   The glob matching is done via [`tinyglobby`](https://github.com/SuperchupuDev/tinyglobby) - check out its documentation for [supported glob patterns](https://superchupu.dev/tinyglobby/comparison).
*   You should also be aware that all the arguments in the `import.meta.glob` must be **passed as literals**. You can NOT use variables or expressions in them.

## Dynamic Import [​](#dynamic-import)

Similar to [glob import](#glob-import), Vite also supports dynamic import with variables.

ts

```
const module = await import(`./dir/${file}.js`)
```

Note that variables only represent file names one level deep. If `file` is `'foo/bar'`, the import would fail. For more advanced usage, you can use the [glob import](#glob-import) feature.

Also note that the dynamic import must match the following rules to be bundled:

*   Imports must start with `./` or `../`: ``import(`./dir/${foo}.js`)`` is valid, but ``import(`${foo}.js`)`` is not.
*   Imports must end with a file extension: ``import(`./dir/${foo}.js`)`` is valid, but ``import(`./dir/${foo}`)`` is not.
*   Imports to the own directory must specify a file name pattern: ``import(`./prefix-${foo}.js`)`` is valid, but ``import(`./${foo}.js`)`` is not.

These rules are enforced to prevent accidentally importing files that are not intended to be bundled. For example, without these rules, `import(foo)` would bundle everything in the file system.

## WebAssembly [​](#webassembly)

Pre-compiled `.wasm` files can be imported with `?init`. The default export will be an initialization function that returns a Promise of the [`WebAssembly.Instance`](https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/Instance):

js

```
import init from './example.wasm?init'

init().then((instance) => {
  instance.exports.test()
})
```

The init function can also take an importObject which is passed along to [`WebAssembly.instantiate`](https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/instantiate) as its second argument:

js

```
init({
  imports: {
    someFunc: () => {
      /* ... */
    },
  },
}).then(() => {
  /* ... */
})
```

In the production build, `.wasm` files smaller than `assetInlineLimit` will be inlined as base64 strings. Otherwise, they will be treated as a [static asset](../assets/index.md) and fetched on-demand.

For SSR build, Node.js compatible runtimes are only supported

Due to the lack of a universal way to load a file, the internal implementation for `.wasm?init` relies on `node:fs` module. This means that this feature will only work in Node.js compatible runtimes for SSR builds.

### Accessing the WebAssembly Module [​](#accessing-the-webassembly-module)

If you need access to the `Module` object, e.g. to instantiate it multiple times, use an [explicit URL import](../assets/index.md#explicit-url-imports) to resolve the asset, and then perform the instantiation:

js

```
import wasmUrl from 'foo.wasm?url'

const main = async () => {
  const responsePromise = fetch(wasmUrl)
  const { module, instance } =
    await WebAssembly.instantiateStreaming(responsePromise)
  /* ... */
}

main()
```

## Web Workers [​](#web-workers)

### Import with Constructors [​](#import-with-constructors)

A web worker script can be imported using [`new Worker()`](https://developer.mozilla.org/en-US/docs/Web/API/Worker/Worker) and [`new SharedWorker()`](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker/SharedWorker). Compared to the worker suffixes, this syntax leans closer to the standards and is the **recommended** way to create workers.

ts

```
const worker = new Worker(new URL('./worker.js', import.meta.url))
```

The worker constructor also accepts options, which can be used to create "module" workers:

ts

```
const worker = new Worker(new URL('./worker.js', import.meta.url), {
  type: 'module',
})
```

The worker detection will only work if the `new URL()` constructor is used directly inside the `new Worker()` declaration. Additionally, all options parameters must be static values (i.e. string literals).

### Import with Query Suffixes [​](#import-with-query-suffixes)

A web worker script can be directly imported by appending `?worker` or `?sharedworker` to the import request. The default export will be a custom worker constructor:

js

```
import MyWorker from './worker?worker'

const worker = new MyWorker()
```

The worker script can also use ESM `import` statements instead of `importScripts()`. **Note**: During development this relies on [browser native support](https://caniuse.com/?search=module%20worker), but for the production build it is compiled away.

By default, the worker script will be emitted as a separate chunk in the production build. If you wish to inline the worker as base64 strings, add the `inline` query:

js

```
import MyWorker from './worker?worker&inline'
```

If you wish to retrieve the worker as a URL, add the `url` query:

js

```
import MyWorker from './worker?worker&url'
```

See [Worker Options](../../config/worker-options/index.md) for details on configuring the bundling of all workers.

## Content Security Policy (CSP) [​](#content-security-policy-csp)

To deploy CSP, certain directives or configs must be set due to Vite's internals.

### [`'nonce-{RANDOM}'`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/Sources#nonce-base64-value) [​](#nonce-random)

When [`html.cspNonce`](../../config/shared-options/index.md#html-cspnonce) is set, Vite adds a nonce attribute with the specified value to any `<script>` and `<style>` tags, as well as `<link>` tags for stylesheets and module preloading. Additionally, when this option is set, Vite will inject a meta tag (`<meta property="csp-nonce" nonce="PLACEHOLDER" />`).

The nonce value of a meta tag with `property="csp-nonce"` will be used by Vite whenever necessary during both dev and after build.

WARNING

Ensure that you replace the placeholder with a unique value for each request. This is important to prevent bypassing a resource's policy, which can otherwise be easily done.

### [`data:`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/Sources#scheme-source:~:text=schemes%20\(not%20recommended\).-,data%3A,-Allows%20data%3A) [​](#data)

By default, during build, Vite inlines small assets as data URIs. Allowing `data:` for related directives (e.g. [`img-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/img-src), [`font-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/font-src)), or, disabling it by setting [`build.assetsInlineLimit: 0`](../../config/build-options/index.md#build-assetsinlinelimit) is necessary.

WARNING

Do not allow `data:` for [`script-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src). It will allow injection of arbitrary scripts.

## License [​](#license)

Vite can generate a file of all the dependencies' licenses used in the build with the [`build.license`](../../config/build-options/index.md#build-license) option. It can be hosted to display and acknowledge the dependencies used by the app.

vite.config.js

js

```
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    license: true,
  },
})
```

This will generate a `.vite/license.md` file with an output that may look like this:

md

```
# Licenses

The app bundles dependencies which contain the following licenses:

## dep-1 - 1.2.3 (CC0-1.0)

CC0 1.0 Universal

...

## dep-2 - 4.5.6 (MIT)

MIT License

...
```

To serve the file at a different path, you can pass `{ fileName: 'license.md' }` for example, so that it's served at `https://example.com/license.md`. See the [`build.license`](../../config/build-options/index.md#build-license) docs for more information.

## Build Optimizations [​](#build-optimizations)

> Features listed below are automatically applied as part of the build process and there is no need for explicit configuration unless you want to disable them.

### CSS Code Splitting [​](#css-code-splitting)

Vite automatically extracts the CSS used by modules in an async chunk and generates a separate file for it. The CSS file is automatically loaded via a `<link>` tag when the associated async chunk is loaded, and the async chunk is guaranteed to only be evaluated after the CSS is loaded to avoid [FOUC](https://en.wikipedia.org/wiki/Flash_of_unstyled_content#:~:text=A%20flash%20of%20unstyled%20content,before%20all%20information%20is%20retrieved.).

If you'd rather have all the CSS extracted into a single file, you can disable CSS code splitting by setting [`build.cssCodeSplit`](../../config/build-options/index.md#build-csscodesplit) to `false`.

### Preload Directives Generation [​](#preload-directives-generation)

Vite automatically generates `<link rel="modulepreload">` directives for entry chunks and their direct imports in the built HTML.

### Async Chunk Loading Optimization [​](#async-chunk-loading-optimization)

In real world applications, Rollup often generates "common" chunks - code that is shared between two or more other chunks. Combined with dynamic imports, it is quite common to have the following scenario:

In the non-optimized scenarios, when async chunk `A` is imported, the browser will have to request and parse `A` before it can figure out that it also needs the common chunk `C`. This results in an extra network roundtrip:

```
Entry ---> A ---> C
```

Vite automatically rewrites code-split dynamic import calls with a preload step so that when `A` is requested, `C` is fetched **in parallel**:

```
Entry ---> (A + C)
```

It is possible for `C` to have further imports, which will result in even more roundtrips in the un-optimized scenario. Vite's optimization will trace all the direct imports to completely eliminate the roundtrips regardless of import depth.
