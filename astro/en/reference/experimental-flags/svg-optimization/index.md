---
title: "Experimental SVG optimization"
source: "https://docs.astro.build/en/reference/experimental-flags/svg-optimization/"
canonical_url: "https://docs.astro.build/en/reference/experimental-flags/svg-optimization/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:14.089Z"
content_hash: "f57c6f76dd7b49ef9a315552caa78d413008a41c16c6e806dc95afa70eb16164"
menu_path: ["Experimental SVG optimization"]
section_path: []
nav_prev: {"path": "../chrome-devtools-workspace/index.md", "title": "Experimental Chrome DevTools workspace"}
nav_next: {"path": "../queued-rendering/index.md", "title": "Experimental queued rendering"}
---

# Experimental SVG optimization

**Type:** `boolean | object`  
**Default:** `false`  

**Added in:** `astro@5.16.0`

This experimental feature enables automatic optimization of your [SVG components](/en/guides/images/#svg-components) using [SVGO](https://svgo.dev/) during build time.

When enabled, your imported SVG files used as components will be optimized for smaller file sizes and better performance while maintaining visual quality. This can significantly reduce the size of your SVG assets by removing unnecessary metadata, comments, and redundant code.

To enable this feature with default settings, set it to `true` in your Astro config:

```
import { defineConfig } from "astro/config"
export default defineConfig({  experimental: {    svgo: true  }})
```

## Usage

[Section titled “Usage”](#usage)

No change to using SVG components is required to take advantage of this feature. With experimental `svgo` enabled, all your SVG component import files will be automatically optimized:

```
---import Logo from '../assets/logo.svg';---
<Logo />
```

The SVG will be optimized during the build process, resulting in smaller file sizes in your production build.

Note that this optimization applies to every SVG component import in your project. It is not possible to opt out on a per-component basis.

## Configuration

[Section titled “Configuration”](#configuration)

You can pass an [SVGO configuration object](https://github.com/svg/svgo#configuration) to customize optimization behavior:

```
export default defineConfig({  experimental: {    svgo: {      multipass: true,      floatPrecision: 2,      plugins: [        'preset-default',        'removeXMLNS',        {          name: "removeXlink",          params: {            includeLegacy: true          }        }      ]    }  }})
```

### `plugins`

[Section titled “plugins”](#plugins)

**Type:** `Array<string | PluginConfig>`  
**Default:** `[]`

An array of [SVGO plugins](https://svgo.dev/docs/plugins/) that will be used to optimize your SVG component imports.

This can include SVGO’s [`preset-default`](https://svgo.dev/docs/preset-default/) plugin collection, individual built-in plugins, or [custom plugins](https://svgo.dev/docs/plugins-api/).

To use a plugin’s default configuration, add its name to the array. If you need more control, use the `overrides` parameter to customize specific plugins within `preset-default`, or pass an object with a plugin’s `name` to override its individual parameters.

```
export default defineConfig({  experimental: {    svgo: {      plugins: [        {          name: 'preset-default',          params: {            overrides: {              convertPathData: false,              convertTransform: {                degPrecision: 1,                transformPrecision: 3              },              inlineStyles: false            },          },        },        'removeXMLNS',        {          name: "removeXlink",          params: {            includeLegacy: true          }        }      ]    }  }})
```

### Other configuration options

[Section titled “Other configuration options”](#other-configuration-options)

There are a few [SVGO configuration options](https://github.com/svg/svgo/blob/66d503a48c6c95661726262a3068053c429b06a9/lib/types.ts#L335), especially `floatPrecision` and `multipass`, that can be passed directly to your config object:

```
export default defineConfig({  experimental: {    svgo: {      multipass: true,      floatPrecision: 2    }  }})
```

The `multipass` option sets whether to run the optimization engine multiple times until no further optimizations are found. The `floatPrecision` option sets the number of decimal places to preserve globally, but can be overridden for a specific plugin by specifying a custom value in its `params` property.

## Common use cases

[Section titled “Common use cases”](#common-use-cases)

SVGO provides an extensive [default plugin list](https://svgo.dev/docs/preset-default/) with opinionated optimizations. While using this preset is more convenient than adding each plugin individually, you may need to customize it further. For example, it may remove items or clean up too aggressively for your situation, especially when using animations.

### Preserve specific attributes

[Section titled “Preserve specific attributes”](#preserve-specific-attributes)

You may want to preserve certain SVG attributes and elements, such as `<style>`, that SVGO inlines or removes by default:

```
export default defineConfig({  experimental: {    svgo: {      plugins: [        {          name: 'preset-default',          params: {            overrides: {              inlineStyles: false, // Preserve style elements for CSP hashing              removeDesc: false // Keep element regardless of contents            }          }        }      ]    }  }})
```

### Remove specific elements

[Section titled “Remove specific elements”](#remove-specific-elements)

You can configure plugins to remove specific unwanted elements like metadata or hidden layers. Note that many plugins are already included in `preset-default`, so you typically only need to configure their behavior:

```
export default defineConfig({  experimental: {    svgo: {      plugins: [        {          name: 'preset-default',          params: {            overrides: {              removeHiddenElems: {                isHidden: false,                displayNone: false              }            },          },        },        'removeRasterImages'      ]    }  }})
```

### Optimize for inlining in modern HTML5

[Section titled “Optimize for inlining in modern HTML5”](#optimize-for-inlining-in-modern-html5)

Inline SVG does not require the `xmlns` attribute and can be safely converted to the SVG 2 specification. The `removeXMLNS` and `removeXlink` plugins are recommended for this purpose:

```
export default defineConfig({  experimental: {    svgo: {      plugins: [        'preset-default',        'removeXMLNS',        {          name: "removeXlink",          params: {            includeLegacy: true          }        }      ]    }  }})
```

## How it works

[Section titled “How it works”](#how-it-works)

SVG optimization happens during the build process, not at runtime:

*   In **development mode**, SVG files are not optimized to ensure faster rebuild times and a smoother development experience.
*   In **production builds**, all imported SVG files are optimized once during the build process, resulting in smaller file sizes.
*   There is **no runtime overhead** - optimized SVGs are served as pre-processed static assets.

While the optimization process may slightly increase your build times, the result is smaller file sizes and faster page loads for your users.

## Further reading

[Section titled “Further reading”](#further-reading)

*   [SVGO documentation](https://svgo.dev/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
