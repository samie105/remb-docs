---
title: "Upgrading to Drizzle v1 RC"
source: "https://orm.drizzle.team/docs/upgrade-v1"
canonical_url: "https://orm.drizzle.team/docs/upgrade-v1"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:25:47.362Z"
content_hash: "081f6a3b2fa5d01c11bf211e8f7d043430db0db858c4a08b40968afe62974bfb"
menu_path: ["Upgrading to Drizzle v1 RC"]
section_path: []
nav_prev: {"path": "drizzle/docs/gotchas/index.md", "title": "Drizzle gotchas"}
nav_next: {"path": "drizzle/docs/relations-v1-v2/index.md", "title": "Migrating to Relational Queries version 2"}
---

## Upgrading to Drizzle v1 RC

This guide assumes familiarity with:

*   **beta.1** release notes - a set of changes between `latest` and `beta` versions - [read here](https://github.com/drizzle-team/drizzle-orm/blob/beta/changelogs/drizzle-orm/1.0.0-beta.1.md)
*   **beta.2** release notes - additional set of changes between `latest` and `beta` versions - [read here](https://github.com/drizzle-team/drizzle-orm/releases/tag/v1.0.0-beta.2)
*   Ideally read all other `beta.X` changes to be familiar with everything that was fixed and changed

Drizzle release candidate is living on [`beta` branch](https://github.com/drizzle-team/drizzle-orm/tree/beta) in drizzle repository and under the `beta` tag on npm. So to install it you would need to run:

npm

yarn

pnpm

bun

```
npm i drizzle-orm@beta
npm i -D drizzle-kit@beta
```

```
yarn add drizzle-orm@beta
yarn add -D drizzle-kit@beta
```

```
pnpm add drizzle-orm@beta
pnpm add -D drizzle-kit@beta
```

```
bun add drizzle-orm@beta
bun add -D drizzle-kit@beta
```

It follows the `1.0.0-beta.x` release pattern, so you’ll see versions such as `1.0.0-beta.7`, `1.0.0-beta.8`, and so on. Release notes for each beta update are available on [GitHub releases](https://github.com/drizzle-team/drizzle-orm/tags)

#### Step 1 - Run `drizzle-kit up`[](#step-1---run-drizzle-kit-up)

> Linked discussion: [https://github.com/drizzle-team/drizzle-orm/discussions/2832](https://github.com/drizzle-team/drizzle-orm/discussions/2832)

We’ve updated the migrations folder structure by:

*   removing `journal.json`
*   grouping SQL files and snapshots into separate migration folders
*   removing the `drizzle-kit drop` command

These changes eliminate potential Git conflicts with the journal file and simplify the process of dropping or fixing conflicted migrations

In upcoming `beta` releases, we’ll introduce commutativity checks to help guide you through team migration conflicts, detect possible collisions, and suggest ways to resolve them

> Commutativity discussion: [https://github.com/drizzle-team/drizzle-orm/discussions/5005](https://github.com/drizzle-team/drizzle-orm/discussions/5005)

To migrate previous folders to a new format you would need to run

npm

yarn

pnpm

bun

```
npx drizzle-kit up
```

```
yarn drizzle-kit up
```

```
pnpm drizzle-kit up
```

```
bunx drizzle-kit up
```

#### Step 2 - Update validator packages imports[](#step-2---update-validator-packages-imports)

We’ve stopped maintaining separate validator packages (e.g., `drizzle-zod`, `drizzle-valibot`) and moved them into the `drizzle-orm` repo. This consolidates everything into a single package and eliminates the need to manage separate peer dependencies and versioning.

All packages are now available via `drizzle-orm` imports:

*   `drizzle-zod` -> `drizzle-orm/zod`
*   `drizzle-valibot` -> `drizzle-orm/valibot`
*   `drizzle-typebox` -> `drizzle-orm/typebox-legacy` (using `@sinclair/typebox`)
*   `drizzle-typebox` -> `drizzle-orm/typebox` (using `typebox`)
*   `drizzle-arktype` -> `drizzle-orm/arktype`

#### Step 3 - Update Relational Queries to v2[](#step-3---update-relational-queries-to-v2)

We’ve explained all the RQBv2 changes in detail, along with options for updating your codebase:

*   [How to migrate relations definition from v1 to v2](drizzle/docs/relations-v1-v2/index.md#how-to-migrate-relations-schema-definition-from-v1-to-v2)
*   [How to migrate queries from v1 to v2](drizzle/docs/relations-v1-v2/index.md#how-to-migrate-queries-from-v1-to-v2)
*   [Partial upgrade, or how to stay on v1 even after an upgrade?](drizzle/docs/relations-v1-v2/index.md#partial-upgrade-or-how-to-stay-on-rqb-v1-even-after-an-upgrade)

#### Step 3 - Done ✅[](#step-3---done-)
