---
title: "Using Plugins ​"
source: "https://vite.dev/guide/using-plugins"
canonical_url: "https://vite.dev/guide/using-plugins"
docset: "vite"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:46.033Z"
content_hash: "64ec5d4dc5b59f264a4f8cd9ed1230169dff0b5b49c969126afe951606f024fa"
menu_path: ["Using Plugins ​"]
section_path: []
nav_prev: {"path": "vite/guide/cli/index.md", "title": "Command Line Interface \u200b"}
nav_next: {"path": "vite/guide/dep-pre-bundling/index.md", "title": "Dependency Pre-Bundling \u200b"}
---

Vite can be extended using plugins, which are based on Rollup's well-designed plugin interface with a few extra Vite-specific options. This means that Vite users can rely on the mature ecosystem of Rollup plugins, while also being able to extend the dev server and SSR functionality as needed.

## Adding a Plugin [​](#adding-a-plugin)

To use a plugin, it needs to be added to the `devDependencies` of the project and included in the `plugins` array in the `vite.config.js` config file. For example, to provide support for legacy browsers, the official [@vitejs/plugin-legacy](https://github.com/vitejs/vite/tree/main/packages/plugin-legacy) can be used:

```
$ npm add -D @vitejs/plugin-legacy
```

vite.config.js

js

```
import legacy from '@vitejs/plugin-legacy'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    legacy({
      targets: ['defaults', 'not IE 11'],
    }),
  ],
})
```

`plugins` also accepts presets including several plugins as a single element. This is useful for complex features (like framework integration) that are implemented using several plugins. The array will be flattened internally.

Falsy plugins will be ignored, which can be used to easily activate or deactivate plugins.

## Finding Plugins [​](#finding-plugins)

NOTE

Vite aims to provide out-of-the-box support for common web development patterns. Before searching for a Vite or compatible Rollup plugin, check out the [Features Guide](../features/index.md). A lot of the cases where a plugin would be needed in a Rollup project are already covered in Vite.

Check out the [Plugins section](../../plugins/index.md) for information about official plugins. Community plugins that are published to npm are listed in [Vite Plugin Registry](../../plugins/index.md).

## Enforcing Plugin Ordering [​](#enforcing-plugin-ordering)

For compatibility with some Rollup plugins, it may be needed to enforce the order of the plugin or only apply at build time. This should be an implementation detail for Vite plugins. You can enforce the position of a plugin with the `enforce` modifier:

*   `pre`: invoke plugin before Vite core plugins
*   default: invoke plugin after Vite core plugins
*   `post`: invoke plugin after Vite build plugins

vite.config.js

js

```
import image from '@rollup/plugin-image'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    {
      ...image(),
      enforce: 'pre',
    },
  ],
})
```

Check out [Plugins API Guide](../api-plugin/index.md#plugin-ordering) for detailed information.

## Conditional Application [​](#conditional-application)

By default, plugins are invoked for both serve and build. In cases where a plugin needs to be conditionally applied only during serve or build, use the `apply` property to only invoke them during `'build'` or `'serve'`:

vite.config.js

js

```
import typescript2 from 'rollup-plugin-typescript2'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    {
      ...typescript2(),
      apply: 'build',
    },
  ],
})
```

## Building Plugins [​](#building-plugins)

Check out the [Plugins API Guide](../api-plugin/index.md) for documentation about creating plugins.
