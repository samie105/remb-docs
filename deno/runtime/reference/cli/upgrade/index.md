---
title: "deno upgrade"
source: "https://docs.deno.com/runtime/reference/cli/upgrade/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/upgrade/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:14.757Z"
content_hash: "30a285360520788cca9121bf45c931f61524fd64cfa5bd3ed7bc4e43ae0a5d40"
menu_path: ["deno upgrade"]
section_path: []
---
On this page

*   [Examples](#examples)
    *   [Upgrade to the latest version](#upgrade-to-the-latest-version)
    *   [Upgrade to a specific version](#upgrade-to-a-specific-version)
    *   [Check available upgrade without installing](#check-available-upgrade-without-installing)
*   [\--quiet flag](#--quiet-flag)
*   [Cached downloads](#cached-downloads)
*   [Checksum verification](#checksum-verification)
*   [Canary build](#canary-build)
*   [Upgrade options](#upgrade-options)
*   [Options](#options)

## Examples

### Upgrade to the latest version

Use this command without any options to upgrade Deno to the latest available version:

\>\_

```sh
deno upgrade
Checking for latest version
Version has been found
Deno is upgrading to version 1.38.5
downloading https://github.com/denoland/deno/releases/download/v1.38.5/deno-x86_64-apple-darwin.zip
downloading 100%
Upgrade done successfully
```

### Upgrade to a specific version

You can specify a particular version to upgrade to:

\>\_

```sh
deno upgrade --version 1.37.0
Checking for version 1.37.0
Version has been found
Deno is upgrading to version 1.37.0
downloading https://github.com/denoland/deno/releases/download/v1.37.0/deno-x86_64-apple-darwin.zip
downloading 100%
Upgrade done successfully
```

### Check available upgrade without installing

Use the `--dry-run` flag to see what would be upgraded without actually performing the upgrade:

\>\_

```sh
deno upgrade --dry-run
Checking for latest version
Version has been found
Would upgrade to version 1.38.5
```

## \--quiet flag

The `--quiet` flag suppresses diagnostic output during the upgrade process. When used with `deno upgrade`, it will hide progress indicators, download information, and success messages.

\>\_

```sh
deno upgrade --quiet
```

This is useful for scripting environments or when you want cleaner output in CI pipelines.

## Cached downloads

Downloaded Deno binaries are cached in `$DENO_DIR/dl/`. If you reinstall the same version later, the cached archive is reused instead of re-downloading. For canary builds, old entries are automatically removed, keeping only the 10 most recent versions.

## Checksum verification

Use the `--checksum` flag to verify a downloaded binary against a known SHA-256 hash. This protects against tampering in CI environments and security-sensitive setups:

\>\_

```sh
deno upgrade --checksum=<sha256-hash> 2.7.0
```

SHA-256 checksums are published as `.sha256sum` files alongside release archives on GitHub:

\>\_

```sh
curl -sL https://github.com/denoland/deno/releases/download/v2.7.0/deno-x86_64-unknown-linux-gnu.zip.sha256sum
```

## Canary build

By default, Deno will upgrade from the official GitHub releases. You can specify the `--canary` build flag for the latest canary build:

\>\_

```sh
# Upgrade to the latest canary build
deno upgrade --canary
```

Command line usage:

```
deno upgrade [OPTIONS] [VERSION]...
```

Upgrade deno executable to the given version.

### Latest

```
deno upgrade
```

### Specific version

```
deno upgrade 1.45.0
```

```
deno upgrade 1.46.0-rc.1
```

```
deno upgrade 9bc2dd29ad6ba334fd57a20114e367d3c04763d4
```

### Channel

```
deno upgrade stable
```

```
deno upgrade alpha
```

```
deno upgrade beta
```

```
deno upgrade rc
```

```
deno upgrade canary
```

The version is resolved via `https://dl.deno.land` and then downloaded from either there or GitHub releases, replacing the current executable.

If you want to not replace the current Deno executable but instead download an update to a different location, use the `--output` flag:

```
deno upgrade --output $HOME/my_deno
```

## Upgrade options

`--checksum`<checksum>

Verify the downloaded archive against the provided SHA256 checksum.

`--dry-run`

Perform all checks without replacing old exe.

`--force, -f`

Replace current exe even if not out-of-date.

`--output`<output>

The path to output the updated version to.

## Options

`--cert`<FILE>

Load certificate authority from PEM encoded file.
