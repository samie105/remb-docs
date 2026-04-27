---
title: "deno audit"
source: "https://docs.deno.com/runtime/reference/cli/audit/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/audit/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:25:55.260Z"
content_hash: "6a2e252dc6e0a5b71599c8737263f157f10e31cb98b561323f5c5f378b654ca1"
menu_path: ["deno audit"]
section_path: []
content_language: "en"
---
**On this page**

-   [Examples](#examples)
-   [Dependency management options](#dependency-management-options)
-   [Options](#options)

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
