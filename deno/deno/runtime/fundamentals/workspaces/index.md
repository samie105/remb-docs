---
title: "Workspaces and monorepos"
source: "https://docs.deno.com/runtime/fundamentals/workspaces/"
canonical_url: "https://docs.deno.com/runtime/fundamentals/workspaces/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:07.686Z"
content_hash: "47f6f4a646f75b307af94906445f7764cc1b84d6d141f1090b03dac5f2a5a8bf"
menu_path: ["Workspaces and monorepos"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/fundamentals/debugging/index.md", "title": "Debugging"}
nav_next: {"path": "deno/deno/runtime/fundamentals/linting_and_formatting/index.md", "title": "Linting and formatting"}
---

# Test a published package
deno add jsr:@scope/my-published-package
deno test integration-test.ts
```

When publishing packages that depend on other workspace members, Deno will automatically replace workspace references with proper registry references in the published code.

### Migrating from `npm` workspaces

Deno workspaces support using a Deno-first package from an existing npm package. In this example, we mix and match a Deno library called `@deno/hi`, with a Node.js library called `@deno/log` that we developed a couple years back.

We'll need to include a `deno.json` configuration file in the root:

deno.json

```json
{
  "workspace": {
    "members": ["hi"]
  }
}
```

Alongside our existing package.json workspace:

package.json

```json
{
  "workspaces": ["log"]
}
```

The workspace currently has a log npm package:

log/package.json

```json
{
  "name": "@deno/log",
  "version": "0.5.0",
  "type": "module",
  "main": "index.js"
}
```

log/index.js

```js
export function log(output) {
  console.log(output);
}
```

Let's create an `@deno/hi` Deno-first package that imports `@deno/log`:

hi/deno.json

```json
{
  "name": "@deno/hi",
  "version": "0.2.0",
  "exports": "./mod.ts",
  "imports": {
    "log": "npm:@deno/log@^0.5"
  }
}
```

hi/mod.ts

```ts
import { log } from "log";

export function sayHiTo(name: string) {
  log(`Hi, ${name}!`);
}
```

Now, we can write a `main.ts` file that imports and calls `hi`:

main.ts

```ts
import { sayHiTo } from "@deno/hi";

sayHiTo("friend");
```

\>\_

```sh
$ deno run main.ts
Hi, friend!
```

You can even have both `deno.json` and `package.json` in your existing Node.js package. Additionally, you could remove the package.json in the root and specify the npm package in the deno.json workspace members. That allows you to gradually migrate to Deno, without putting a lot of upfront work.

For example, you can add `log/deno.json` to configure Deno's linter and formatter:

```jsonc
{
  "fmt": {
    "semiColons": false
  },
  "lint": {
    "rules": {
      "exclude": ["no-unused-vars"]
    }
  }
}
```

Running `deno fmt` in the workspace, will format the `log` package to not have any semicolons, and `deno lint` won't complain if you leave an unused var in one of the source files.

## Configuring built-in Deno tools

Some configuration options only make sense at the root of the workspace, eg. specifying `nodeModulesDir` option in one of the members is not available and Deno will warn if an option needs to be applied at the workspace root.

Here's a full matrix of various `deno.json` options available at the workspace root and its members:

Option

Workspace

Package

Notes

compilerOptions

✅

✅

importMap

✅

❌

Exclusive with imports and scopes per config file. Additionally, it is not supported to have importMap in the workspace config, and imports in the package config.

imports

✅

✅

Exclusive with importMap per config file.

scopes

✅

❌

Exclusive with importMap per config file.

exclude

✅

✅

lint.include

✅

✅

lint.exclude

✅

✅

lint.files

⚠️

❌

Deprecated

lint.rules.tags

✅

✅

Tags are merged by appending package to workspace list. Duplicates are ignored.

lint.rules.include

lint.rules.exclude

✅

✅

Rules are merged per package, with package taking priority over workspace (package include is stronger than workspace exclude).

lint.report

✅

❌

Only one reporter can be active at a time, so allowing different reporters per workspace would not work in the case where you lint files spanning multiple packages.

fmt.include

✅

✅

fmt.exclude

✅

✅

fmt.files

⚠️

❌

Deprecated

fmt.useTabs

✅

✅

Package takes priority over workspace.

fmt.indentWidth

✅

✅

Package takes priority over workspace.

fmt.singleQuote

✅

✅

Package takes priority over workspace.

fmt.proseWrap

✅

✅

Package takes priority over workspace.

fmt.semiColons

✅

✅

Package takes priority over workspace.

fmt.options.\*

⚠️

❌

Deprecated

nodeModulesDir

✅

❌

Resolution behaviour must be the same in the entire workspace.

vendor

✅

❌

Resolution behaviour must be the same in the entire workspace.

tasks

✅

✅

Package tasks take priority over workspace. cwd used is the cwd of the config file that the task was inside of.

test.include

✅

✅

test.exclude

✅

✅

test.files

⚠️

❌

Deprecated

publish.include

✅

✅

publish.exclude

✅

✅

bench.include

✅

✅

bench.exclude

✅

✅

bench.files

⚠️

❌

Deprecated

lock

✅

❌

Only a single lock file may exist per resolver, and only resolver may exist per workspace, so conditional enablement of the lockfile per package does not make sense.

unstable

✅

❌

For simplicities sake, we do not allow unstable flags, because a lot of the CLI assumes that unstable flags are immutable and global to the entire process. Also weird interaction with DENO\_UNSTABLE\_\* flags.

name

❌

✅

version

❌

✅

exports

❌

✅

workspace

✅

❌

Nested workspaces are not supported.

## Running commands across workspaces

Deno provides several ways to run commands across all or specific workspace members:

### Type checking

Workspace members can have different sets of compiler options. They are also inherited between root and member, much like [TSConfig `extends`](https://www.typescriptlang.org/tsconfig/#extends). For example:

deno.json

```json
{
  "workspace": ["./web"],
  "compilerOptions": {
    "checkJs": true
  }
}
```

web/deno.json

```json
{
  "compilerOptions": {
    "lib": ["esnext", "dom"]
  }
}
```

Files in the `web` subdirectory will be configured with the following options:

```json
{
  "compilerOptions": {
    "checkJs": true,
    "lib": ["esnext", "dom"]
  }
}
```

Each member will be partitioned and checked separately from one another. Just run `deno check` from the workspace root:

\>\_

```sh
deno check
```

### Running tests

To run tests across all workspace members, simply execute `deno test` from the workspace root:

\>\_

```sh
deno test
```

This will run tests in all workspace members according to their individual test configurations.

To run tests for a specific workspace member, you can either:

1.  Change to that member's directory and run the test command:

\>\_

```sh
cd my-directory
deno test
```

2.  Or specify the path from the workspace root:

\>\_

```sh
deno test my-directory/
```

### Formatting and linting

Similar to testing, formatting and linting commands run across all workspace members by default:

\>\_

```sh
deno fmt
deno lint
```

Each workspace member follows its own formatting and linting rules as defined in its `deno.json` file, with some settings inherited from the root configuration as shown in the table above.

### Using workspace tasks

You can define tasks at both the workspace root and in individual workspace members:

deno.json

```json
{
  "workspace": ["./add", "./subtract"],
  "tasks": {
    "build": "echo 'Building all packages'",
    "test:all": "deno test"
  }
}
```

add/deno.json

```json
{
  "name": "@scope/add",
  "version": "0.1.0",
  "exports": "./mod.ts",
  "tasks": {
    "build": "echo 'Building add package'",
    "test": "deno test"
  }
}
```

To run a task defined in a specific package:

\>\_

```sh
deno task --cwd=add build
```

## Sharing and managing dependencies

Workspaces provide powerful ways to share and manage dependencies across projects:

### Sharing development dependencies

Common development dependencies like testing libraries can be defined at the workspace root:

deno.json

```json
{
  "workspace": ["./add", "./subtract"],
  "imports": {
    "@std/testing/": "jsr:@std/testing@^0.218.0/",
    "chai": "npm:chai@^4.3.7"
  }
}
```

This makes these dependencies available to all workspace members without needing to redefine them.

### Managing version conflicts

When resolving dependencies, workspace members can override dependencies defined in the root. If both the root and a member specify different versions of the same dependency, the member's version will be used when resolving within that member's folder. This allows individual packages to use specific dependency versions when needed.

However, member-specific dependencies are scoped only to that member's folder. Outside of member folders, or when working with files at the workspace root level, the workspace root's import map will be used for resolving dependencies (including JSR and HTTPS dependencies).

### Interdependent workspace members

As shown in the earlier example with the `add` and `subtract` modules, workspace members can depend on each other. This enables a clean separation of concerns while maintaining the ability to develop and test interdependent modules together.

The `subtract` module imports functionality from the `add` module, demonstrating how workspace members can build upon each other:

subtract/mod.ts

```ts
import { add } from "@scope/add";

export function subtract(a: number, b: number): number {
  return add(a, b * -1);
}
```

This approach allows you to:

1.  Break down complex projects into manageable, single-purpose packages
2.  Share code between packages without publishing to a registry
3.  Test and develop interdependent modules together
4.  Gradually migrate monolithic codebases to modular architecture

## Using workspace protocol in package.json

Deno supports workspace protocol specifiers in `package.json` files. These are useful when you have npm packages that depend on other packages within the workspace:

package.json

```json
{
  "name": "my-npm-package",
  "dependencies": {
    "another-workspace-package": "workspace:*"
  }
}
```

The following workspace protocol specifiers are supported:

*   `workspace:*` - Use the latest version available in the workspace
*   `workspace:~` - Use the workspace version with only patch-level changes
*   `workspace:^` - Use the workspace version with semver-compatible changes

## npm and pnpm workspace compatibility

Deno works seamlessly with standard npm workspaces defined in `package.json`:

package.json

```json
{
  "workspaces": ["packages/*"]
}
```

For pnpm users, Deno supports typical pnpm workspace configurations. However, if you're using a `pnpm-workspace.yaml` file, you'll need to migrate to a `deno.json` workspace configuration:

pnpm-workspace.yaml (to be replaced)

```yaml
packages:
  - "packages/*"
```

Should be converted to:

deno.json

```json
{
  "workspace": ["packages/*"]
}
```

This allows for smooth integration between Deno and npm/pnpm ecosystems during migration or in hybrid projects.

For more information on configuring your project, check out the [Configuration with deno.json](/examples/configuration_with_deno_json/) tutorial.
