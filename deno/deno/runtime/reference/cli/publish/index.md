---
title: "deno publish"
source: "https://docs.deno.com/runtime/reference/cli/publish/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/publish/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:55.802Z"
content_hash: "c452f940aa6d50a388d801d4cd76c182db72eb16857eb36d16d2fae978154184"
menu_path: ["deno publish"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/outdated/index.md", "title": "deno outdated"}
nav_next: {"path": "deno/deno/runtime/reference/cli/lsp/index.md", "title": "deno lsp"}
---

On this page

*   [Package Requirements](#package-requirements)
*   [Examples](#examples)
*   [Publishing options](#publishing-options)
*   [Options](#options)
*   [Type checking options](#type-checking-options)

`deno publish` publishes your package to the [JSR](https://jsr.io/) registry.

## Package Requirements

Your package must have a `name` and `version` and an `exports` field in its [`deno.json`](/runtime/fundamentals/configuration/) or `jsr.json` file.

*   The `name` field must be unique and follow the `@<scope_name>/<package_name>` convention.
*   The `version` field must be a valid semver version.
*   The `exports` field must point to the main entry point of the package. The exports field can either be specified as a single string, or as an object mapping entrypoint names to paths in your package.

Example:

deno.json

```json
{
  "name": "@scope_name/package_name",
  "version": "1.0.0",
  "exports": "./main.ts"
}
```

Before you publish your package, you must create it in the registry by visiting [JSR - Publish a package](https://jsr.io/new).

## Examples

Publish your current workspace

\>\_

```sh
deno publish
```

Publish your current workspace with a specific token, bypassing interactive authentication

\>\_

```sh
deno publish --token c00921b1-0d4f-4d18-b8c8-ac98227f9275
```

Publish and check for errors in remote modules

\>\_

```sh
deno publish --check=all
```

Perform a dry run to simulate publishing.

\>\_

```sh
deno publish --dry-run
```

Publish using settings from a specific configuration file

\>\_

```sh
deno publish --config custom-config.json
```

Command line usage:

```
deno publish [OPTIONS]
```

Publish the current working directory's package or workspace to JSR

## Publishing options

`--allow-dirty`

Allow publishing if the repository has uncommitted changed.

`--allow-slow-types`

Allow publishing with slow types.

`--dry-run`

Prepare the package for publishing performing all checks and validations without uploading.

`--no-provenance`

Disable provenance attestation. Enabled by default on Github actions, publicly links the package to where it was built and published from.

`--set-version`<VERSION>

Set version for a package to be published. This flag can be used while publishing individual packages and cannot be used in a workspace.

`--token`<token>

The API token to use when publishing. If unset, interactive authentication is be used.

## Options

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--no-config`

Disable automatic loading of the configuration file.

## Type checking options

`--check`<CHECK\_TYPE>optional

Set type-checking behavior. This subcommand type-checks local modules by default, so adding `--check` is redundant If the value of "all" is supplied, remote modules will be included. Alternatively, the 'deno check' subcommand can be used.

`--no-check`<NO\_CHECK\_TYPE>optional

Skip type-checking. If the value of "remote" is supplied, diagnostic errors from remote modules will be ignored.
