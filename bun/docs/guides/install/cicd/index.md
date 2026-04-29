---
title: "Install dependencies with Bun in GitHub Actions"
source: "https://bun.com/docs/guides/install/cicd"
canonical_url: "https://bun.com/docs/guides/install/cicd"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:43.415Z"
content_hash: "1cf69e1f494367b109e845af46e2b661a18e4536a9cfbdbfc7e36a7978999a93"
menu_path: ["Install dependencies with Bun in GitHub Actions"]
section_path: []
nav_prev: {"path": "bun/docs/guides/install/azure-artifacts/index.md", "title": "Using bun install with an Azure Artifacts npm registry"}
nav_next: {"path": "bun/docs/guides/install/custom-registry/index.md", "title": "Override the default npm registry for bun install"}
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

Use the official [`setup-bun`](https://github.com/oven-sh/setup-bun) GitHub Action to install `bun` in your GitHub Actions runner.

workflow.yml

```
title: my-workflow
jobs:
  my-job:
    title: my-job
    runs-on: ubuntu-latest
    steps:
      # ...
      - uses: actions/checkout@v4
      - uses: oven-sh/setup-bun@v2 // [!code ++]

      # run any `bun` or `bunx` command
      - run: bun install // [!code ++]
```

* * *

To specify a version of Bun to install:

workflow.yml

```
title: my-workflow
jobs:
  my-job:
    title: my-job
    runs-on: ubuntu-latest
    steps:
      # ...
      - uses: oven-sh/setup-bun@v2
         with:
          version: "latest" # or "canary" #
```

* * *

Refer to the [README.md](https://github.com/oven-sh/setup-bun) for complete documentation of the `setup-bun` GitHub Action.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/cicd.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/cicd>)

[

Configure git to diff Bun's lockb lockfile

Previous

](../git-diff-bun-lockfile/index.md)[

Run your tests with the Bun test runner

Next

](../../test/run-tests/index.md)
