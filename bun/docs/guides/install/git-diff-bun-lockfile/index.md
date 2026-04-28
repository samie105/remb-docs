---
title: "Configure git to diff Bun's lockb lockfile"
source: "https://bun.com/docs/guides/install/git-diff-bun-lockfile"
canonical_url: "https://bun.com/docs/guides/install/git-diff-bun-lockfile"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:59.516Z"
content_hash: "909f6c17e540dc62c9ea8b675912817bf2fccc46cd9d21f835b7287717413a5a"
menu_path: ["Configure git to diff Bun's lockb lockfile"]
section_path: []
nav_prev: {"path": "bun/docs/guides/install/from-npm-install-to-bun-install/index.md", "title": "Migrate from npm install to bun install"}
nav_next: {"path": "bun/docs/guides/install/jfrog-artifactory/index.md", "title": "Using bun install with Artifactory"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

Bun v1.1.39 introduced `bun.lock`, a JSONC formatted lockfile. `bun.lock` is human-readable and git-diffable without configuration, at no cost to performance. In 1.2.0+ it is the default format used for new projects. [**Learn more.**](/docs/pm/lockfile#text-based-lockfile)

* * *

To teach `git` how to generate a human-readable diff of Bun’s binary lockfile format (`.lockb`), add the following to your local or global `.gitattributes` file:

gitattributes

```
*.lockb binary diff=lockb
```

* * *

Then add the following to you local git config with:

terminal

```
git config diff.lockb.textconv bun
git config diff.lockb.binary true
```

* * *

To globally configure git to diff Bun’s lockfile, add the following to your global git config with:

terminal

```
git config --global diff.lockb.textconv bun
git config --global diff.lockb.binary true
```

* * *

## 

[​

](#how-this-works)

How this works

Why this works:

*   `textconv` tells git to run bun on the file before diffing
*   `binary` tells git to treat the file as binary (so it doesn’t try to diff it line-by-line)

In Bun, you can execute Bun’s lockfile (`bun ./bun.lockb`) to generate a human-readable version of the lockfile and `git diff` can then use that to generate a human-readable diff.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/git-diff-bun-lockfile.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/git-diff-bun-lockfile>)

[

Migrate from npm install to bun install

Previous

](/docs/guides/install/from-npm-install-to-bun-install)[

Install dependencies with Bun in GitHub Actions

Next

](/docs/guides/install/cicd)
