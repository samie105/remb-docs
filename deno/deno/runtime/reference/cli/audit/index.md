---
title: "deno audit"
source: "https://docs.deno.com/runtime/reference/cli/audit/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/audit/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:49.503Z"
content_hash: "1a8cdf69a7aa9d43487eba50f278cdcd275428d4ee8327bcb8d41359516dabd4"
menu_path: ["deno audit"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/approve_scripts/index.md", "title": "deno approve-scripts"}
nav_next: {"path": "deno/deno/runtime/reference/cli/bench/index.md", "title": "deno bench"}
---

On this page

*   [Examples](#examples)
*   [Dependency management options](#dependency-management-options)
*   [Options](#options)

The `deno audit` command checks your project's dependencies for known security vulnerabilities. It reads your lock file and reports any advisories found in vulnerability databases.

## Examples

Audit all dependencies:

\>\_

```sh
deno audit
```

Show only high and critical severity vulnerabilities:

\>\_

```sh
deno audit --level=high
```

Check against the [socket.dev](https://socket.dev/) vulnerability database:

\>\_

```sh
deno audit --socket
```

Ignore specific CVEs (useful for suppressing false positives or accepted risks):

\>\_

```sh
deno audit --ignore=CVE-2024-12345,CVE-2024-67890
```

Ignore advisories that have no available fix:

\>\_

```sh
deno audit --ignore-unfixable
```

Don't error if the audit data can't be retrieved from the registry:

\>\_

```sh
deno audit --ignore-registry-errors
```

Command line usage:

```
deno audit [OPTIONS]
```

Audit currently installed dependencies.

```
deno audit
```

Show only high and critical severity vulnerabilities

```
deno audit --level=high
```

Check against socket.dev vulnerability database

```
deno audit --socket
```

Don't error if the audit data can't be retrieved from the registry

```
deno audit --ignore-registry-errors
```

## Dependency management options

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.

## Options

`--ignore`<CVE>

Ignore advisories matching the given CVE IDs.

`--ignore-registry-errors`

Return exit code 0 if remote service(s) responds with an error.

`--ignore-unfixable`

Ignore advisories that don't have any actions to resolve them.

`--level`<level>

Only show advisories with severity greater or equal to the one specified.

`--socket`

Check against socket.dev vulnerability database.

