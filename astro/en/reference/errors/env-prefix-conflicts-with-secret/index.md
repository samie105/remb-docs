---
title: "envPrefix conflicts with secret environment variables"
source: "https://docs.astro.build/en/reference/errors/env-prefix-conflicts-with-secret/"
canonical_url: "https://docs.astro.build/en/reference/errors/env-prefix-conflicts-with-secret/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:28.957Z"
content_hash: "58c5cbf748c4196b956e96621580dc8f043cf1a39a11f2d4bcd6b4216abb7642"
menu_path: ["envPrefix conflicts with secret environment variables"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/env-invalid-variables/index.md", "title": "Invalid Environment Variables"}
nav_next: {"path": "astro/en/reference/errors/expected-image-options/index.md", "title": "Expected image options."}
---

# envPrefix conflicts with secret environment variables

> **EnvPrefixConflictsWithSecret**: The following environment variables are declared with `access: "secret"` in `env.schema`, but their names match a prefix in `vite.envPrefix`, which would expose them in client-side bundles:  
>   
> CONFLICTS.MAP((C) =\\ >`- ${C`).join('  
> ')}  
>   
> Either remove the conflicting prefixes from `vite.envPrefix`, or rename these variables to use a prefix not in `vite.envPrefix`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The configured `vite.envPrefix` includes prefixes that match environment variables declared with `access: "secret"` in `env.schema`. This would cause Vite to expose those secret values in client-side JavaScript bundles, bypassing the `access: "secret"` protection.

To fix this, either:

*   Remove the conflicting prefixes from `vite.envPrefix`, or
*   Rename your secret environment variables to use a prefix that is not in `vite.envPrefix`.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
