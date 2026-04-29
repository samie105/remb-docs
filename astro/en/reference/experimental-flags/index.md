---
title: "Configuring experimental flags"
source: "https://docs.astro.build/en/reference/experimental-flags/"
canonical_url: "https://docs.astro.build/en/reference/experimental-flags/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:59.018Z"
content_hash: "ec15797969d55f72663aa0002787b389462e28a02f15bc16c33110a179079bec"
menu_path: ["Configuring experimental flags"]
section_path: []
nav_prev: {"path": "astro/en/reference/programmatic-reference/index.md", "title": "Programmatic Astro API (experimental)"}
nav_next: {"path": "astro/en/reference/experimental-flags/route-caching/index.md", "title": "Experimental route caching"}
---

# Configuring experimental flags

Experimental features are available only after enabling a flag in the Astro configuration file.

```
import { defineConfig } from 'astro/config';
export default defineConfig({    experimental: {        // enable experimental flags        // to try out new features    },});
```

Astro offers experimental flags to give users early access to new features for testing and feedback.

These flags allow you to participate in feature development by reporting issues and sharing your opinions. These features are not guaranteed to be stable and may include breaking changes even in small `patch` releases while the feature is actively developed.

We recommend [updating Astro](../../upgrade-astro/index.md#upgrade-to-the-latest-version) frequently, and keeping up with release notes in the [Astro changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) which will inform you of any changes needed to your project code. The experimental feature documentation will always be updated for the current released version only.

[Contribute](../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
