---
title: "Workspaces"
source: "https://bun.com/docs/pm/workspaces"
canonical_url: "https://bun.com/docs/pm/workspaces"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:08.926Z"
content_hash: "6042c76b60b38511414ac848efd9a7b9790650dd59c575bf39483f75cc9416f9"
menu_path: ["Workspaces"]
section_path: []
---
Bun supports [`workspaces`](https://docs.npmjs.com/cli/v9/using-npm/workspaces?v=true#description) in `package.json`. Workspaces let you develop complex software as a _monorepo_ consisting of several independent packages. It’s common for a monorepo to have the following structure:

File Tree

```
<root>
├── README.md
├── bun.lock
├── package.json
├── tsconfig.json
└── packages
    ├── pkg-a
    │   ├── index.ts
    │   ├── package.json
    │   └── tsconfig.json
    ├── pkg-b
    │   ├── index.ts
    │   ├── package.json
    │   └── tsconfig.json
    └── pkg-c
        ├── index.ts
        ├── package.json
        └── tsconfig.json
```

In the root `package.json`, the `"workspaces"` key is used to indicate which subdirectories should be considered packages/workspaces within the monorepo. It’s conventional to place all the workspace in a directory called `packages`.

package.json

```
{
  "name": "my-project",
  "version": "1.0.0",
  "workspaces": ["packages/*"],
  "devDependencies": {
    "example-package-in-monorepo": "workspace:*"
  }
}
```

package.json

```
{
  "name": "my-project",
  "version": "1.0.0",
  "workspaces": ["packages/**", "!packages/**/test/**", "!packages/**/template/**"]
}
```

Each workspace has it’s own `package.json`. When referencing other packages in the monorepo, semver or workspace protocols (e.g. `workspace:*`) can be used as the version field in your `package.json`.

packages/pkg-a/package.json

```
{
  "name": "pkg-a",
  "version": "1.0.0",
  "dependencies": {
    "pkg-b": "workspace:*"
  }
}
```

`bun install` will install dependencies for all workspaces in the monorepo, de-duplicating packages if possible. If you only want to install dependencies for specific workspaces, you can use the `--filter` flag.

```
# Install dependencies for all workspaces starting with `pkg-` except for `pkg-c`
bun install --filter "pkg-*" --filter "!pkg-c"

# Paths can also be used. This is equivalent to the command above.
bun install --filter "./packages/pkg-*" --filter "!pkg-c" # or --filter "!./packages/pkg-c"
```

When publishing, `workspace:` versions are replaced by the package’s `package.json` version,

```
"workspace:*" -> "1.0.1"
"workspace:^" -> "^1.0.1"
"workspace:~" -> "~1.0.1"
```

Setting a specific version takes precedence over the package’s `package.json` version,

```
"workspace:1.0.2" -> "1.0.2" // Even if current version is 1.0.1
```

Workspaces have a couple major benefits.

*   **Code can be split into logical parts.** If one package relies on another, add it as a dependency in `package.json`. If package `b` depends on `a`, `bun install` will install your local `packages/a` directory into `node_modules` instead of downloading it from the npm registry.
*   **Dependencies can be de-duplicated.** If `a` and `b` share a common dependency, it will be _hoisted_ to the root `node_modules` directory. This reduces redundant disk usage and minimizes “dependency hell” issues associated with having multiple versions of a package installed simultaneously.
*   **Run scripts in multiple packages.** You can use the [`--filter` flag](https://bun.com/docs/pm/filter) to run `package.json` scripts in multiple packages in your workspace, or `--workspaces` to run scripts across all workspaces.

When many packages need the same dependency versions, catalogs let you define those versions once in the root `package.json` and reference them from your workspaces using the `catalog:` protocol. Updating the catalog automatically updates every package that references it. See [Catalogs](https://bun.com/docs/pm/catalogs) for details.
