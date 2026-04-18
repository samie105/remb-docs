---
title: "bun --filter"
source: "https://bun.com/docs/pm/filter"
canonical_url: "https://bun.com/docs/pm/filter"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:48.479Z"
content_hash: "dfa4e53f280f8e38a568292fce272ca4358ab33620ce25edd445e6a1d3f81265"
menu_path: ["bun --filter"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/why/index.md", "title": "bun why"}
nav_next: {"path": "bun/bun/docs/pm/global-cache/index.md", "title": "Global cache"}
---

# Install dependencies for all workspaces except `pkg-c`
bun install --filter '!pkg-c'

# Install dependencies for packages in `./packages` (`pkg-a`, `pkg-b`, `pkg-c`)
bun install --filter './packages/*'

# Save as above, but exclude the root package.json
bun install --filter '!./' --filter './packages/*'
```

Similarly, `bun outdated` will display outdated dependencies for all packages in the monorepo, and `--filter` can be used to restrict the command to a subset of the packages:

terminal

```
# Display outdated dependencies for workspaces starting with `pkg-`
bun outdated --filter 'pkg-*'

# Display outdated dependencies for only the root package.json
bun outdated --filter './'
```

For more information on both these commands, see [`bun install`](bun/bun/docs/pm/cli/install/index.md) and [`bun outdated`](bun/bun/docs/pm/cli/outdated/index.md).

* * *

## Running scripts with `--filter`

Use the `--filter` flag to execute scripts in multiple packages at once:

terminal

```
bun --filter <pattern> <script>
```

Say you have a monorepo with two packages: `packages/api` and `packages/frontend`, both with a `dev` script that will start a local development server. Normally, you would have to open two separate terminal tabs, cd into each package directory, and run `bun dev`:

terminal

```
cd packages/api
bun dev

# in another terminal
cd packages/frontend
bun dev
```

Using `--filter`, you can run the `dev` script in both packages at once:

terminal

```
bun --filter '*' dev
```

Both commands will be run in parallel, and you will see a nice terminal UI showing their respective outputs:

### Running scripts in workspaces

Filters respect your [workspace configuration](bun/bun/docs/pm/workspaces/index.md): If you have a `package.json` file that specifies which packages are part of the workspace, `--filter` will be restricted to only these packages. Also, in a workspace you can use `--filter` to run scripts in packages that are located anywhere in the workspace:

terminal

```
# Packages
# src/foo
# src/bar

# in src/bar: runs myscript in src/foo, no need to cd!
bun run --filter foo myscript
```

### Parallel and sequential mode

Combine `--filter` or `--workspaces` with `--parallel` or `--sequential` to run scripts across workspace packages with Foreman-style prefixed output:

terminal

```
# Run "build" in all matching packages concurrently
bun run --parallel --filter '*' build

# Run "build" in all workspace packages sequentially
bun run --sequential --workspaces build

# Run glob-matched scripts across all packages
bun run --parallel --filter '*' "build:*"

# Continue running even if one package's script fails
bun run --parallel --no-exit-on-error --filter '*' test

# Run multiple scripts across all packages
bun run --parallel --filter '*' build lint
```

Each line of output is prefixed with the package and script name (e.g. `pkg-a:build | ...`). Without `--filter`/`--workspaces`, the prefix is just the script name (e.g. `build | ...`). When a package’s `package.json` has no `name` field, the relative path from the workspace root is used instead. Use `--if-present` with `--workspaces` to skip packages that don’t have the requested script instead of erroring.

### Dependency Order

Bun will respect package dependency order when running scripts. Say you have a package `foo` that depends on another package `bar` in your workspace, and both packages have a `build` script. When you run `bun --filter '*' build`, you will notice that `foo` will only start running once `bar` is done.

