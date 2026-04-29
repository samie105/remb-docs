---
title: "Add a peer dependency"
source: "https://bun.com/docs/guides/install/add-peer"
canonical_url: "https://bun.com/docs/guides/install/add-peer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:27.809Z"
content_hash: "8a2cd13353601069ac3d12345321e10e73b47a00198fa9bb151a7686935f7d51"
menu_path: ["Add a peer dependency"]
section_path: []
nav_prev: {"path": "bun/docs/guides/install/add-optional/index.md", "title": "Add an optional dependency"}
nav_next: {"path": "bun/docs/guides/install/add-tarball/index.md", "title": "Add a tarball dependency"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](../../../index.md)[Package Manager

](../../../pm/cli/install/index.md)[Bundler

](../../../bundler/index.md)[Test Runner

](../../../test/index.md)[Guides

](../../index.md)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](../../../feedback/index.md)

To add an npm package as a peer dependency, use the `--peer` flag.

terminal

```
bun add @types/bun --peer
```

* * *

This will add the package to `peerDependencies` in `package.json`.

package.json

```
{
  "peerDependencies": {
    "@types/bun": "^1.3.3"
  }
}
```

* * *

Running `bun install` will install peer dependencies by default, unless marked optional in `peerDependenciesMeta`.

package.json

```
{
  "peerDependencies": {
    "@types/bun": "^1.3.3"
  },
  "peerDependenciesMeta": {
    "@types/bun": { 
      "optional": true
    } 
  }
}
```

* * *

See [Docs > Package manager](../../../pm/cli/install/index.md) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/add-peer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/add-peer>)

[

Add an optional dependency

Previous

](../add-optional/index.md)[

Add a Git dependency

Next

](../add-git/index.md)
