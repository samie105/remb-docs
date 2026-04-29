---
title: "deno upgrade"
source: "https://docs.deno.com/runtime/reference/cli/upgrade/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/upgrade/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:34:59.240Z"
content_hash: "bc05a12a8d681baaab60bedec314377619946e9b3a13e8f86f07617bed2eaf20"
menu_path: ["deno upgrade"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/update/index.md", "title": "deno update"}
nav_next: {"path": "deno/runtime/reference/cli/unstable_flags/index.md", "title": "Unstable feature flags"}
---

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
