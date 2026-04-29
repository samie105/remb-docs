---
title: "Experimental queued rendering"
source: "https://docs.astro.build/en/reference/experimental-flags/queued-rendering/"
canonical_url: "https://docs.astro.build/en/reference/experimental-flags/queued-rendering/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:06.249Z"
content_hash: "0eb4d283c2212cdfc65eb5593145a3fbcecaeb574f4e772fad29de0a8c59155c"
menu_path: ["Experimental queued rendering"]
section_path: []
nav_prev: {"path": "astro/en/reference/experimental-flags/svg-optimization/index.md", "title": "Experimental SVG optimization"}
nav_next: {"path": "astro/en/reference/experimental-flags/rust-compiler/index.md", "title": "Experimental Rust compiler"}
---

# Experimental queued rendering

**Type:** `object`  
**Default:** `{ enabled: false }`  

**Added in:** `astro@6.0.0`

Enables an experimental, more performant rendering infrastructure that is based on a queue instead of recursion.

By default, Astro renders `.astro`, `.md`, and `.mdx` files using a recursion algorithm. It takes as input a series of components that are serialised in a tree-like structure, and for each node of the tree, Astro calls a render function.

When queued rendering is enabled, Astro traverses all nodes in the tree and emits a [depth-first](https://en.wikipedia.org/wiki/Depth-first_search) list of nodes. This list is then iterated and rendered, without the need of a recursion algorithm. This rendering is more memory efficient, and it should provide more benefits in big projects.

To enable this feature with default settings, set `queuedRendering.enabled` to `true` in your Astro config:

```
import { defineConfig } from "astro/config";
export default defineConfig({  experimental: {    queuedRendering: {      enabled: true    }  }});
```

In a future major version, Astro will use this new compiler by default, but you can opt in to the future behavior early using the `experimental.queuedRendering` flag.

## Configuration

[Section titled “Configuration”](#configuration)

The queued rendering engine comes with additional, low-level features, which allow you to experiment with other possible optimizations. These optimisations aren’t directly part of the queued engine, and may be removed if they are proven inefficient during this experimental phase of testing.

### Node pooling

[Section titled “Node pooling”](#node-pooling)

**Type:** `number`  
**Default:** `1000`  

**Added in:** `astro@6.0.0`

Node pooling is a caching system designed to reuse component nodes across renders. This feature is automatically enabled with a reasonable default according to our early testing. However, you can configure the size of the pool to increase or decrease the number of nodes combined in a single pool according to your project needs. To disable this feature entirely, set `poolSize` to `0`.

The node pooling is very effective when rendering static pages because it saves some memory when building websites with many pages that share the same components.

The node pooling is turned off for pages rendered on demand because these rendering requests do not share memory, and there are therefore no savings to be gained with this strategy.

```
import { defineConfig } from "astro/config";
export default defineConfig({  experimental: {    queuedRendering: {      enabled: true,      poolSize: 3000 // use a pool of 3000 nodes    }  }});
```

### Content caching

[Section titled “Content caching”](#content-caching)

**Type:** `boolean`  
**Default:** `false`  

**Added in:** `astro@6.0.0`

Content caching is another technique to reuse values (usually strings) during the rendering of a page. Currently, this feature can only be enabled or disabled with no further configuration. It’s disabled by default, but when enabled, the experimental queued engine will choose a reasonable default cache size for most large content collections:

```
import { defineConfig } from "astro/config";
export default defineConfig({  experimental: {    queuedRendering: {      enabled: true,      contentCache: true    }  }});
```

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
