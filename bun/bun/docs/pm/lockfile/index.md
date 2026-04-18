---
title: "Lockfile"
source: "https://bun.com/docs/pm/lockfile"
canonical_url: "https://bun.com/docs/pm/lockfile"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:57.417Z"
content_hash: "140b7712571d1f7beeeebaacd89c1330a935acbb00878fd93dc1b7aa4ad9b848"
menu_path: ["Lockfile"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/lifecycle/index.md", "title": "Lifecycle scripts"}
nav_next: {"path": "bun/bun/docs/pm/overrides/index.md", "title": "Overrides and resolutions"}
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

Running `bun install` will create a lockfile called `bun.lock`.

#### 

[​

](#should-it-be-committed-to-git)

Should it be committed to git?

Yes

#### 

[​

](#generate-a-lockfile-without-installing)

Generate a lockfile without installing?

To generate a lockfile without installing to `node_modules` you can use the `--lockfile-only` flag. The lockfile will always be saved to disk, even if it is up-to-date with the `package.json`(s) for your project.

terminal

```
bun install --lockfile-only
```

Using `--lockfile-only` will still populate the global install cache with registry metadata and git/tarball dependencies.

#### 

[​

](#can-i-opt-out)

Can I opt out?

To install without creating a lockfile:

terminal

```
bun install --no-save
```

To install a Yarn lockfile _in addition_ to `bun.lock`.

```
bun install --yarn
```

#### 

[​

](#text-based-lockfile)

Text-based lockfile

Bun v1.2 changed the default lockfile format to the text-based `bun.lock`. Existing binary `bun.lockb` lockfiles can be migrated to the new format by running `bun install --save-text-lockfile --frozen-lockfile --lockfile-only` and deleting `bun.lockb`. More information about the new lockfile format can be found on [our blogpost](https://bun.com/blog/bun-lock-text-lockfile).

#### 

[​

](#automatic-lockfile-migration)

Automatic lockfile migration

When running `bun install` in a project without a `bun.lock`, Bun automatically migrates existing lockfiles:

*   `yarn.lock` (v1)
*   `package-lock.json` (npm)
*   `pnpm-lock.yaml` (pnpm)

The original lockfile is preserved and can be removed manually after verification.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/lockfile.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/lockfile>)

[

Isolated installs

Previous

](/docs/pm/isolated-installs)[

Lifecycle scripts

Next

](/docs/pm/lifecycle)


