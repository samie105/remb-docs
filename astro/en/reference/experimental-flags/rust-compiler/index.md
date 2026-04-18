---
title: "Experimental Rust compiler"
source: "https://docs.astro.build/en/reference/experimental-flags/rust-compiler/"
canonical_url: "https://docs.astro.build/en/reference/experimental-flags/rust-compiler/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:08.842Z"
content_hash: "c9ab0c01b3bb0a8f4a87e291005ecc1628a85378203a9b9043fada8d9cfd26b3"
menu_path: ["Experimental Rust compiler"]
section_path: []
nav_prev: {"path": "astro/en/reference/experimental-flags/queued-rendering/index.md", "title": "Experimental queued rendering"}
nav_next: {"path": "astro/en/reference/legacy-flags/index.md", "title": "Legacy flags"}
---

# Experimental Rust compiler

**Type:** `boolean`  
**Default:** `false`  

**Added in:** `astro@6.0.0`

Enables using the new Rust-based compiler for Astro files. This compiler is faster, provides better error messages, and generally has better support for modern JavaScript, TypeScript, and CSS features.

In a future major version, Astro will use this new compiler by default, but you can opt in to the future behavior early using the `experimental.rustCompiler` flag.

To give feedback on the compiler, or to keep up with its development, see the [RFC for a new compiler for Astro](https://github.com/withastro/roadmap/discussions/1306) for more information and discussion.

## Usage

[Section titled “Usage”](#usage)

This experimental flag requires no specific usage and only affects which compiler Astro uses for your project.

To enable the Rust compiler, add the following to your `astro.config.mjs`:

```
import { defineConfig } from "astro/config";
export default defineConfig({  experimental: {    rustCompiler: true  }});
```

and then install the `@astrojs/compiler-rs` package into your project:

*   [npm](#tab-panel-2046)
*   [pnpm](#tab-panel-2047)
*   [Yarn](#tab-panel-2048)

```
npm install @astrojs/compiler-rs
```

### Expected differences

[Section titled “Expected differences”](#expected-differences)

Unlike Astro’s current Go compiler, this experimental Rust compiler will not correct invalid HTML structure. For example, the following notable patterns will be left as written, and no longer corrected:

*   `<p><div>Bad nesting</div></p>` (instead of removing the `div` from of the `p`)
*   `<p>My paragraph` (instead of adding the missing closing `</p>` tag)

This means that if your Astro files contain invalid HTML, you may see a different output from the Rust compiler than you did with the previous compiler, or may encounter errors while building.

## Limitations

[Section titled “Limitations”](#limitations)

At this time, the Rust compiler does not output the required metadata for the dev toolbar audits to work correctly.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

