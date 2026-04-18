---
title: "deno outdated"
source: "https://docs.deno.com/runtime/reference/cli/outdated/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/outdated/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:55.663Z"
content_hash: "f288ed0354a46d82fb42503082d0fab1257c5334648e67b2bdc2b485df6ccd04"
menu_path: ["deno outdated"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/lint/index.md", "title": "deno lint"}
nav_next: {"path": "deno/deno/runtime/reference/cli/publish/index.md", "title": "deno publish"}
---

On this page

*   [Checking for outdated dependencies](#checking-for-outdated-dependencies)
*   [Updating dependencies](#updating-dependencies)
*   [Selecting packages](#selecting-packages)
    *   [Updating to specific versions](#updating-to-specific-versions)
*   [Workspaces](#workspaces)
*   [Options](#options)
*   [Dependency management options](#dependency-management-options)

## Checking for outdated dependencies

The `outdated` subcommand checks for new versions of NPM and JSR dependencies listed in [`deno.json`](/runtime/fundamentals/configuration/) or `package.json` files, and displays dependencies that could be updated. Workspaces are fully supported, including workspaces where some members use `package.json` and others use `deno.json`.

For example, take a project with a `deno.json` file:

deno.json

```json
{
  "imports": {
    "@std/fmt": "jsr:@std/fmt@^1.0.0",
    "@std/async": "jsr:@std/async@1.0.1",
    "chalk": "npm:chalk@4"
  }
}
```

and a lockfile that has `@std/fmt` at version `1.0.0`.

\>\_

```sh
deno outdated
┌────────────────┬─────────┬────────┬────────┐
│ Package        │ Current │ Update │ Latest │
├────────────────┼─────────┼────────┼────────┤
│ jsr:@std/fmt   │ 1.0.0   │ 1.0.3  │ 1.0.3  │
├────────────────┼─────────┼────────┼────────┤
│ jsr:@std/async │ 1.0.1   │ 1.0.1  │ 1.0.8  │
├────────────────┼─────────┼────────┼────────┤
│ npm:chalk      │ 4.1.2   │ 4.1.2  │ 5.3.0  │
└────────────────┴─────────┴────────┴────────┘
```

The `Update` column lists the newest semver-compatible version, while the `Latest` column lists the latest version.

Notice that `jsr:@std/async` is listed, even though there is no semver-compatible version to update to. If you would prefer to only show packages that have new compatible versions you can pass the `--compatible` flag.

\>\_

```sh
deno outdated --compatible
┌────────────────┬─────────┬────────┬────────┐
│ Package        │ Current │ Update │ Latest │
├────────────────┼─────────┼────────┼────────┤
│ jsr:@std/fmt   │ 1.0.0   │ 1.0.3  │ 1.0.3  │
└────────────────┴─────────┴────────┴────────┘
```

`jsr:@std/fmt` is still listed, since it could be compatibly updated to `1.0.3`, but `jsr:@std/async` is no longer shown.

## Updating dependencies

The `outdated` subcommand can also update dependencies with the `--update` flag. By default, it will only update dependencies to semver-compatible versions (i.e. it won't update to a breaking version).

\>\_

```sh
deno outdated --update
Updated 1 dependency:
 - jsr:@std/fmt 1.0.0 -> 1.0.3
```

To update to the latest versions (regardless of whether it's semver compatible), pass the `--latest` flag.

\>\_

```sh
deno outdated --update --latest
Updated 3 dependencies:
 - jsr:@std/async 1.0.1 -> 1.0.8
 - jsr:@std/fmt   1.0.0 -> 1.0.3
 - npm:chalk      4.1.2 -> 5.3.0
```

## Selecting packages

The `outdated` subcommand also supports selecting which packages to operate on. This works with or without the `--update` flag.

\>\_

```sh
deno outdated --update --latest chalk
Updated 1 dependency:
 - npm:chalk 4.1.2 -> 5.3.0
```

Multiple selectors can be passed, and wildcards (`*`) or exclusions (`!`) are also supported.

For instance, to update all packages with the `@std` scope, except for `@std/fmt`:

\>\_

```sh
deno outdated --update --latest "@std/*" "!@std/fmt"
Updated 1 dependency:
 - jsr:@std/async 1.0.1 -> 1.0.8
```

Note that if you use wildcards, you will probably need to surround the argument in quotes to prevent the shell from trying to expand them.

### Updating to specific versions

You can also select a specific version to update to by appending it after `@`.

\>\_

```sh
deno outdated --update chalk@5.2 @std/async@1.0.6
Updated 2 dependencies:
 - jsr:@std/async 1.0.1 -> 1.0.6
 - npm:chalk      4.1.2 -> 5.2.0
```

## Workspaces

In a workspace setting, by default `outdated` will only operate on the _current_ workspace member.

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
deno outdated
```

from the `./member-a` directory will only check for outdated dependencies listed in `./member-a/deno.json` or `./member-a/package.json`.

To include all workspace members, pass the `--recursive` flag (the `-r` shorthand is also accepted).

\>\_

```sh
deno outdated --recursive
deno outdated --update --latest -r
```

Command line usage:

```
deno outdated [OPTIONS] [filters]...
```

Find and update outdated dependencies. By default, outdated dependencies are only displayed.

Display outdated dependencies:

```
deno outdated
```

```
deno outdated --compatible
```

Update dependencies to the latest semver compatible versions:

```
deno outdated --update
```

Update dependencies to the latest versions, ignoring semver requirements:

```
deno outdated --update --latest
```

Filters can be used to select which packages to act on. Filters can include wildcards (\*) to match multiple packages.

```
deno outdated --update --latest "@std/*"
```

```
deno outdated --update --latest "react*"
```

Note that filters act on their aliases configured in deno.json / package.json, not the actual package names: Given "foobar": "npm:react@17.0.0" in deno.json or package.json, the filter "foobar" would update npm:react to the latest version.

```
deno outdated --update --latest foobar
```

Filters can be combined, and negative filters can be used to exclude results:

```
deno outdated --update --latest "@std/*" "!@std/fmt*"
```

Specific version requirements to update to can be specified:

```
deno outdated --update @std/fmt@^1.0.2
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

`--update, -u`

Update dependency versions.

## Dependency management options

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.
