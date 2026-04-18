---
title: "bun update"
source: "https://bun.com/docs/pm/cli/update"
canonical_url: "https://bun.com/docs/pm/cli/update"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:42.531Z"
content_hash: "8beb02b017784d2a3f7023178922549bf971af071fda917c268e131dc09e2fa5"
menu_path: ["bun update"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/publish/index.md", "title": "bun publish"}
nav_next: {"path": "bun/bun/docs/pm/cli/why/index.md", "title": "bun why"}
---

To update all dependencies to the latest version:

terminal

```
bun update
```

To update a specific dependency to the latest version:

terminal

```
bun update [package]
```

## `--interactive`

For a more controlled update experience, use the `--interactive` flag to select which packages to update:

terminal

```
bun update --interactive
bun update -i
```

This launches an interactive terminal interface that shows all outdated packages with their current and target versions. You can then select which packages to update.

### Interactive Interface

The interface displays packages grouped by dependency type:

```
? Select packages to update - Space to toggle, Enter to confirm, a to select all, n to select none, i to invert, l to toggle latest

  dependencies                Current  Target   Latest
    □ react                   17.0.2   18.2.0   18.3.1
    □ lodash                  4.17.20  4.17.21  4.17.21

  devDependencies             Current  Target   Latest
    □ typescript              4.8.0    5.0.0    5.3.3
    □ @types/node             16.11.7  18.0.0   20.11.5

  optionalDependencies        Current  Target   Latest
    □ some-optional-package   1.0.0    1.1.0    1.2.0
```

**Sections:**

*   Packages are grouped under section headers: `dependencies`, `devDependencies`, `peerDependencies`, `optionalDependencies`
*   Each section shows column headers aligned with the package data

**Columns:**

*   **Package**: Package name (may have suffix like `dev`, `peer`, `optional` for clarity)
*   **Current**: Currently installed version
*   **Target**: Version that would be installed (respects semver constraints)
*   **Latest**: Latest available version

### Keyboard Controls

**Selection:**

*   **Space**: Toggle package selection
*   **Enter**: Confirm selections and update
*   **a/A**: Select all packages
*   **n/N**: Select none
*   **i/I**: Invert selection

**Navigation:**

*   **↑/↓ Arrow keys** or **j/k**: Move cursor
*   **l/L**: Toggle between target and latest version for current package

**Exit:**

*   **Ctrl+C** or **Ctrl+D**: Cancel without updating

### Visual Indicators

*   **☑** Selected packages (will be updated)
*   **□** Unselected packages
*   **\>** Current cursor position
*   **Colors**: Red (major), yellow (minor), green (patch) version changes
*   **Underlined**: Currently selected update target

### Package Grouping

Packages are organized in sections by dependency type:

*   **dependencies** - Regular runtime dependencies
*   **devDependencies** - Development dependencies
*   **peerDependencies** - Peer dependencies
*   **optionalDependencies** - Optional dependencies

Within each section, individual packages may have additional suffixes ( `dev`, `peer`, `optional`) for extra clarity.

## `--recursive`

Use the `--recursive` flag with `--interactive` to update dependencies across all workspaces in a monorepo:

terminal

```
bun update --interactive --recursive
bun update -i -r
```

This displays an additional “Workspace” column showing which workspace each dependency belongs to.

## `--latest`

By default, `bun update` will update to the latest version of a dependency that satisfies the version range specified in your `package.json`. To update to the latest version, regardless of if it’s compatible with the current version range, use the `--latest` flag:

terminal

```
bun update --latest
```

In interactive mode, you can toggle individual packages between their target version (respecting semver) and latest version using the **l** key. For example, with the following `package.json`:

package.json

```
{
  "dependencies": {
    "react": "^17.0.2"
  }
}
```

*   `bun update` would update to a version that matches `17.x`.
*   `bun update --latest` would update to a version that matches `18.x` or later.

* * *

## CLI Usage

terminal

```
bun update <package> <version>
```

### Update Strategy

\--force

boolean

Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

\--latest

boolean

Update packages to their latest versions

### Dependency Scope

\--production

boolean

Don’t install devDependencies. Alias: `-p`

\--global

boolean

Install globally. Alias: `-g`

\--omit

string

Exclude `dev`, `optional`, or `peer` dependencies from install

### Project File Management

\--yarn

boolean

Write a `yarn.lock` file (yarn v1). Alias: `-y`

\--no-save

boolean

Don’t update `package.json` or save a lockfile

\--save

boolean

default:"true"

Save to `package.json` (true by default)

\--frozen-lockfile

boolean

Disallow changes to lockfile

\--save-text-lockfile

boolean

Save a text-based lockfile

\--lockfile-only

boolean

Generate a lockfile without installing dependencies

### Network & Registry

\--ca

string

Provide a Certificate Authority signing certificate

\--cafile

string

Same as `—ca`, but as a file path to the certificate

\--registry

string

Use a specific registry by default, overriding `.npmrc`, `bunfig.toml` and environment variables

\--network-concurrency

number

default:"48"

Maximum number of concurrent network requests (default 48)

### Caching

\--cache-dir

string

Store & load cached data from a specific directory path

\--no-cache

boolean

Ignore manifest cache entirely

### Output & Logging

\--silent

boolean

Don’t log anything

\--verbose

boolean

Excessively verbose logging

\--no-progress

boolean

Disable the progress bar

\--no-summary

boolean

Don’t print a summary

### Script Execution

\--ignore-scripts

boolean

Skip lifecycle scripts in the project’s `package.json` (dependency scripts are never run)

\--concurrent-scripts

number

default:"5"

Maximum number of concurrent jobs for lifecycle scripts (default 5)

### Installation Controls

\--no-verify

boolean

Skip verifying integrity of newly downloaded packages

\--trust

boolean

Add to `trustedDependencies` in the project’s `package.json` and install the package(s)

\--backend

string

default:"clonefile"

Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default), `hardlink`, `symlink`, `copyfile`

### General & Environment

\--config

string

Specify path to config file (`bunfig.toml`). Alias: `-c`

\--dry-run

boolean

Don’t install anything

\--cwd

string

Set a specific cwd

\--help

boolean

Print this help menu. Alias: `-h`
