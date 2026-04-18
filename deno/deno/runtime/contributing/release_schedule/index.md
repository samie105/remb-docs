---
title: "Release Schedule"
source: "https://docs.deno.com/runtime/contributing/release_schedule/"
canonical_url: "https://docs.deno.com/runtime/contributing/release_schedule/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:52.533Z"
content_hash: "9fa8c67ee22e2c72ab7e35932d186690800f8d984b72a18f9c64cfc888b11aea"
menu_path: ["Release Schedule"]
section_path: []
---
On this page

*   [Canary channel](#canary-channel)

A new minor release for the `deno` cli is scheduled for release every 12 weeks.

See [Milestones on Deno's GitHub](https://github.com/denoland/deno/milestones) for the upcoming releases.

There are usually several patch releases (done weekly) after a minor release; after that a merge window for new features opens for the upcoming minor release.

Stable releases can be found on the [GitHub releases page](https://github.com/denoland/deno/releases).

## Canary channel

In addition to the stable channel described above, canaries are released multiple times daily (for each commit on main). You can upgrade to the latest canary release by running:

```console
deno upgrade --canary
```

To update to a specific canary, pass the commit hash in the `--version` option:

```console
deno upgrade --canary --version=973af61d8bb03c1709f61e456581d58386ed4952
```

To switch back to the stable channel, run `deno upgrade`.

Canaries can be downloaded from [https://dl.deno.land](https://dl.deno.land).
