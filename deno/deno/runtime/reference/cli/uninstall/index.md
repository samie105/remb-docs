---
title: "deno uninstall"
source: "https://docs.deno.com/runtime/reference/cli/uninstall/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/uninstall/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:40.658Z"
content_hash: "7f56671d370507eb37ee7d124593a8ef8d4a55cdc61c41d1b3bc6209739e98c1"
menu_path: ["deno uninstall"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/types/index.md", "title": "deno types"}
nav_next: {"path": "deno/deno/runtime/reference/cli/update/index.md", "title": "deno update"}
---

On this page

*   [deno uninstall \[PACKAGES\]](#deno-uninstall-%5Bpackages%5D)
*   [deno uninstall --global \[SCRIPT\_NAME\]](#deno-uninstall---global-%5Bscript_name%5D)
*   [Options](#options)
*   [Dependency management options](#dependency-management-options)

## `deno uninstall [PACKAGES]`

Remove dependencies specified in [`deno.json`](/runtime/fundamentals/configuration/) or `package.json`:

\>\_

```sh
deno add npm:express
Add npm:express@5.0.0

cat deno.json
{
  "imports": {
    "express": "npm:express@5.0.0"
  }
}
```

\>\_

```sh
deno uninstall express
Removed express

cat deno.json
{
  "imports": {}
}
```

Tip

You can also use `deno remove` which is an alias to `deno uninstall [PACKAGES]`

You can remove multiple dependencies at once:

\>\_

```sh
deno add npm:express jsr:@std/http
Added npm:express@5.0.0
Added jsr:@std/http@1.0.7

cat deno.json
{
  "imports": {
    "@std/http": "jsr:@std/http@^1.0.7",
    "express": "npm:express@^5.0.0",
  }
}
```

\>\_

```sh
deno remove express @std/http
Removed express
Removed @std/http

cat deno.json
{
  "imports": {}
}
```

Info

While dependencies are removed from the `deno.json` and `package.json` they still persist in the global cache for future use.

If your project contains `package.json`, `deno uninstall` can work with it too:

\>\_

```sh
cat package.json
{
  "dependencies": {
    "express": "^5.0.0"
  }
}

deno remove express
Removed express

cat package.json
{
  "dependencies": {}
}
```

## `deno uninstall --global [SCRIPT_NAME]`

Uninstall `serve`

\>\_

```sh
deno uninstall --global serve
```

Uninstall `serve` from a specific installation root

\>\_

```sh
deno uninstall -g --root /usr/local/bin serve
```

Command line usage:

```
deno uninstall [OPTIONS] [name-or-package] [additional-packages]...
```

Uninstalls a dependency or an executable script in the installation root's bin directory.

```
deno uninstall @std/dotenv chalk
```

```
deno uninstall --global file_server
```

To change the installation root, use `--root` flag:

```
deno uninstall --global --root /usr/local serve
```

The installation root is determined, in order of precedence:

*   `--root` option
*   `DENO_INSTALL_ROOT` environment variable
*   `$HOME/.deno`

## Options

`--global, -g`

Remove globally installed package or module.

`--lockfile-only`

Install only updating the lockfile.

`--root`<root>

Installation root.

## Dependency management options

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.

