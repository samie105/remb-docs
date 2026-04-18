---
title: "Cannot set both densities and widths"
source: "https://docs.astro.build/en/reference/errors/incompatible-descriptor-options/"
canonical_url: "https://docs.astro.build/en/reference/errors/incompatible-descriptor-options/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:03.197Z"
content_hash: "cc05400f46ab96a83c2b522c23106e83f7ffb1d03e82f2522fe3f00b6e960f6b"
menu_path: ["Cannot set both densities and widths"]
section_path: []
---
# Cannot set both densities and widths

> **IncompatibleDescriptorOptions**: Only one of `densities` or `widths` can be specified. In most cases, you’ll probably want to use only `widths` if you require specific widths.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Only one of `densities` or `widths` can be specified. Those attributes are used to construct a `srcset` attribute, which cannot have both `x` and `w` descriptors.

**See Also:**

*   [Images](/en/guides/images/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
