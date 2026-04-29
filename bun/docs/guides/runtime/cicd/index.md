---
title: "Install and run Bun in GitHub Actions"
source: "https://bun.com/docs/guides/runtime/cicd"
canonical_url: "https://bun.com/docs/guides/runtime/cicd"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:14.723Z"
content_hash: "013552059976b962fb36ab42d9540cc77fe925363478a8e7d09c23375d38b933"
menu_path: ["Install and run Bun in GitHub Actions"]
section_path: []
nav_prev: {"path": "../build-time-constants/index.md", "title": "Build-time constants with --define"}
nav_next: {"path": "../codesign-macos-executable/index.md", "title": "Codesign a single-file JavaScript executable on macOS"}
---

Use the official [`setup-bun`](https://github.com/oven-sh/setup-bun) GitHub Action to install `bun` in your GitHub Actions runner.

workflow.yml

```
name: my-workflow
jobs:
  my-job:
    name: my-job
    runs-on: ubuntu-latest
    steps:
      # ...
      - uses: actions/checkout@v4
      - uses: oven-sh/setup-bun@v2

      # run any `bun` or `bunx` command
      - run: bun install
      - run: bun index.ts
      - run: bun run build
```

* * *

To specify a version of Bun to install:

workflow.yml

```
name: my-workflow
jobs:
  my-job:
    name: my-job
    runs-on: ubuntu-latest
    steps:
      # ...
      - uses: oven-sh/setup-bun@v2
        with:
          bun-version: 1.3.3 # or "latest", "canary", <sha> #
```

* * *

Refer to the [README.md](https://github.com/oven-sh/setup-bun) for complete documentation of the `setup-bun` GitHub Action.

Was this page helpful?
