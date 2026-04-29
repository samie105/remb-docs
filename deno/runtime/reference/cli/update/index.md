---
title: "deno update"
source: "https://docs.deno.com/runtime/reference/cli/update/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/update/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:34:38.731Z"
content_hash: "dbc576d5bdf6f5c50a3ac639fe3bef610006cc15a86f04fda59a0ef6b117029c"
menu_path: ["deno update"]
section_path: []
content_language: "en"
nav_prev: {"path": "../uninstall/index.md", "title": "deno uninstall"}
nav_next: {"path": "../upgrade/index.md", "title": "deno upgrade"}
---

**On this page**

-   [Updating dependencies](#updating-dependencies)
-   [Selecting packages](#selecting-packages)
    -   [Updating to specific versions](#updating-to-specific-versions)
-   [Workspaces](#workspaces)
-   [Options](#options)
-   [Dependency management options](#dependency-management-options)

`deno update` updates dependencies in your [`deno.json`](/runtime/fundamentals/configuration/) or `package.json`. See [Modules](/runtime/fundamentals/modules/) for more about managing dependencies.

## Updating dependencies

By default, the `update` subcommand will only update dependencies to semver-compatible versions (i.e. it won't update to a breaking version).

\>\_

```sh
deno update
Updated 1 dependency:
 - jsr:@std/fmt 1.0.0 -> 1.0.3
```

To update to the latest versions (regardless of whether it's semver compatible), pass the `--latest` flag.

\>\_

```sh
deno update --latest
Updated 3 dependencies:
 - jsr:@std/async 1.0.1 -> 1.0.8
 - jsr:@std/fmt   1.0.0 -> 1.0.3
 - npm:chalk      4.1.2 -> 5.3.0
```

## Selecting packages

The `update` subcommand also supports selecting which packages to operate on.

\>\_

```sh
deno update --latest chalk
Updated 1 dependency:
 - npm:chalk 4.1.2 -> 5.3.0
```

Multiple selectors can be passed, and wildcards (`*`) or exclusions (`!`) are also supported.

For instance, to update all packages with the `@std` scope, except for `@std/fmt`:

\>\_

```sh
deno update --latest "@std/*" "!@std/fmt"
Updated 1 dependency:
 - jsr:@std/async 1.0.1 -> 1.0.8
```

Note that if you use wildcards, you will probably need to surround the argument in quotes to prevent the shell from trying to expand them.

### Updating to specific versions

You can also select a specific version to update to by appending it after `@`.

\>\_

```sh
deno update chalk@5.2 @std/async@1.0.6
Updated 2 dependencies:
 - jsr:@std/async 1.0.1 -> 1.0.6
 - npm:chalk      4.1.2 -> 5.2.0
```

## Workspaces

In a workspace setting, by default `update` will only operate on the _current_ workspace member.

For instance, given a workspace:

deno.json

```json
{
  "workspace": ["./member-a", "./member-b"]
}
```

Running

\>\_

```sh
deno update
```

from the `./member-a` directory will only update dependencies listed in `./member-a/deno.json` or `./member-a/package.json`.

To include all workspace members, pass the `--recursive` flag (the `-r` shorthand is also accepted).

\>\_

```sh
deno update --recursive
deno update --latest -r
```

Command line usage:

```
deno update [OPTIONS] [filters]...
```

Update outdated dependencies.

Update dependencies to the latest semver compatible versions:

```
deno update
```

Update dependencies to the latest versions, ignoring semver requirements:

```
deno update --latest
```

This command is an alias of deno outdated --update

Filters can be used to select which packages to act on. Filters can include wildcards (\*) to match multiple packages.

```
deno update --latest "@std/*"
```

```
deno update --latest "react*"
```

Note that filters act on their aliases configured in deno.json / package.json, not the actual package names: Given "foobar": "npm:react@17.0.0" in deno.json or package.json, the filter "foobar" would update npm:react to the latest version.

```
deno update --latest foobar
```

Filters can be combined, and negative filters can be used to exclude results:

```
deno update --latest "@std/*" "!@std/fmt*"
```

Specific version requirements to update to can be specified:

```
deno update @std/fmt@^1.0.2
```

## Options

`--compatible`

Only consider versions that satisfy semver requirements.

`--interactive, -i`

Interactively select which dependencies to update.

`--latest`

Consider the latest version, regardless of semver constraints.

`--lockfile-only`

Install only updating the lockfile.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--recursive, -r`

Include all workspace members.

## Dependency management options

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.
