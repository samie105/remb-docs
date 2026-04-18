---
title: "deno info"
source: "https://docs.deno.com/runtime/reference/cli/info/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/info/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:42.705Z"
content_hash: "35b05fcac8f7faa21124ebef506ee2d6c7e5adab8c178c12a96146ebd390ab64"
menu_path: ["deno info"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/fmt/index.md", "title": "deno fmt"}
nav_next: {"path": "deno/deno/runtime/reference/cli/init/index.md", "title": "deno init"}
---

On this page

*   [Example](#example)
*   [JSON output](#json-output)
*   [Cache location](#cache-location)
*   [Options](#options)
*   [Dependency management options](#dependency-management-options)

`deno info` displays information about a module's dependency tree. See [Modules](/runtime/fundamentals/modules/) for more about how Deno resolves and caches dependencies.

## Example

\>\_

```sh
deno info jsr:@std/http/file-server
local: /home/user/.cache/deno/deps/https/jsr.io/...
type: TypeScript
dependencies: 40 unique
size: 326.42KB

https://jsr.io/@std/http/1.0.0-rc.5/file_server.ts (24.74KB)
├─┬ https://jsr.io/@std/path/1.0.1/posix/join.ts (862B)
│ ├── https://jsr.io/@std/path/1.0.1/_common/assert_path.ts (307B)
│ └─┬ https://jsr.io/@std/path/1.0.1/posix/normalize.ts (1.31KB)
│   ├─┬ https://jsr.io/@std/path/1.0.1/_common/normalize.ts (263B)
│   │ └── https://jsr.io/@std/path/1.0.1/_common/assert_path.ts *
│   ├─┬ https://jsr.io/@std/path/1.0.1/_common/normalize_string.ts (2.25KB)
│   │ └── https://jsr.io/@std/path/1.0.1/_common/constants.ts (1.97KB)
│   └─┬ https://jsr.io/@std/path/1.0.1/posix/_util.ts (391B)
│     └── https://jsr.io/@std/path/1.0.1/_common/constants.ts *
├── https://jsr.io/@std/path/1.0.1/posix/normalize.ts *
├─┬ https://jsr.io/@std/path/1.0.1/extname.ts (906B)
│ ├── https://jsr.io/@std/path/1.0.1/_os.ts (736B)
│ ├─┬ https://jsr.io/@std/path/1.0.1/posix/extname.ts (2.28KB)
│ │ ├── https://jsr.io/@std/path/1.0.1/_common/constants.ts *
│ │ ├── https://jsr.io/@std/path/1.0.1/_common/assert_path.ts *
│ │ └── https://jsr.io/@std/path/1.0.1/posix/_util.ts *
│ └─┬ https://jsr.io/@std/path/1.0.1/windows/extname.ts (2.5KB)
│   ├── https://jsr.io/@std/path/1.0.1/_common/constants.ts *
│   ├── https://jsr.io/@std/path/1.0.1/_common/assert_path.ts *
│   └─┬ https://jsr.io/@std/path/1.0.1/windows/_util.ts (828B)
│     └── https://jsr.io/@std/path/1.0.1/_common/constants.ts *
├─┬ https://jsr.io/@std/path/1.0.1/join.ts (926B)
│ ├── https://jsr.io/@std/path/1.0.1/_os.ts *
│ ├── https://jsr.io/@std/path/1.0.1/posix/join.ts *
│ └─┬ https://jsr.io/@std/path/1.0.1/windows/join.ts (2.41KB)
│   ├── https://jsr.io/@std/path/1.0.1/_common/assert_path.ts *
│   ├── https://jsr.io/@std/path/1.0.1/windows/_util.ts *
│   └─┬ https://jsr.io/@std/path/1.0.1/windows/normalize.ts (3.84KB)
│     ├── https://jsr.io/@std/path/1.0.1/_common/normalize.ts *
│     ├── https://jsr.io/@std/path/1.0.1/_common/constants.ts *
│     ├── https://jsr.io/@std/path/1.0.1/_common/normalize_string.ts *
│     └── https://jsr.io/@std/path/1.0.1/windows/_util.ts *
├─┬ https://jsr.io/@std/path/1.0.1/relative.ts (1.08KB)
│ ├── https://jsr.io/@std/path/1.0.1/_os.ts *
│ ├─┬ https://jsr.io/@std/path/1.0.1/posix/relative.ts (3.25KB)
│ │ ├── https://jsr.io/@std/path/1.0.1/posix/_util.ts *
│ │ ├─┬ https://jsr.io/@std/path/1.0.1/posix/resolve.ts (1.84KB)
│ │ │ ├── https://jsr.io/@std/path/1.0.1/_common/normalize_string.ts *
│ │ │ ├── https://jsr.io/@std/path/1.0.1/_common/assert_path.ts *
│ │ │ └── https://jsr.io/@std/path/1.0.1/posix/_util.ts *
│ │ └─┬ https://jsr.io/@std/path/1.0.1/_common/relative.ts (287B)
│ │   └── https://jsr.io/@std/path/1.0.1/_common/assert_path.ts *
│ └─┬ https://jsr.io/@std/path/1.0.1/windows/relative.ts (4.24KB)
│   ├── https://jsr.io/@std/path/1.0.1/_common/constants.ts *
│   ├─┬ https://jsr.io/@std/path/1.0.1/windows/resolve.ts (5.02KB)
│   │ ├── https://jsr.io/@std/path/1.0.1/_common/constants.ts *
│   │ ├── https://jsr.io/@std/path/1.0.1/_common/normalize_string.ts *
│   │ ├── https://jsr.io/@std/path/1.0.1/_common/assert_path.ts *
│   │ └── https://jsr.io/@std/path/1.0.1/windows/_util.ts *
│   └── https://jsr.io/@std/path/1.0.1/_common/relative.ts *
├─┬ https://jsr.io/@std/path/1.0.1/resolve.ts (1.02KB)
│ ├── https://jsr.io/@std/path/1.0.1/_os.ts *
│ ├── https://jsr.io/@std/path/1.0.1/posix/resolve.ts *
│ └── https://jsr.io/@std/path/1.0.1/windows/resolve.ts *
├─┬ https://jsr.io/@std/path/1.0.1/constants.ts (705B)
│ └── https://jsr.io/@std/path/1.0.1/_os.ts *
├─┬ https://jsr.io/@std/media-types/1.0.2/content_type.ts (3.09KB)
│ ├─┬ https://jsr.io/@std/media-types/1.0.2/parse_media_type.ts (3.54KB)
│ │ └── https://jsr.io/@std/media-types/1.0.2/_util.ts (3.18KB)
│ ├─┬ https://jsr.io/@std/media-types/1.0.2/get_charset.ts (1.45KB)
│ │ ├── https://jsr.io/@std/media-types/1.0.2/parse_media_type.ts *
│ │ ├── https://jsr.io/@std/media-types/1.0.2/_util.ts *
│ │ └─┬ https://jsr.io/@std/media-types/1.0.2/_db.ts (1.34KB)
│ │   ├── https://jsr.io/@std/media-types/1.0.2/vendor/db.ts (190.69KB)
│ │   └── https://jsr.io/@std/media-types/1.0.2/_util.ts *
│ ├─┬ https://jsr.io/@std/media-types/1.0.2/format_media_type.ts (2.45KB)
│ │ └── https://jsr.io/@std/media-types/1.0.2/_util.ts *
│ ├── https://jsr.io/@std/media-types/1.0.2/_db.ts *
│ └─┬ https://jsr.io/@std/media-types/1.0.2/type_by_extension.ts (1.15KB)
│   └── https://jsr.io/@std/media-types/1.0.2/_db.ts *
├─┬ https://jsr.io/@std/http/1.0.0-rc.5/etag.ts (6.46KB)
│ └─┬ https://jsr.io/@std/encoding/1.0.1/base64.ts (3.18KB)
│   └── https://jsr.io/@std/encoding/1.0.1/_validate_binary_like.ts (798B)
├── https://jsr.io/@std/http/1.0.0-rc.5/status.ts (13.39KB)
├── https://jsr.io/@std/streams/1.0.0-rc.4/byte_slice_stream.ts (2.57KB)
├── https://jsr.io/@std/cli/1.0.0/parse_args.ts (21.94KB)
├── https://jsr.io/@std/http/1.0.0-rc.5/deno.json (415B)
├── https://jsr.io/@std/fmt/1.0.0-rc.1/bytes.ts (5.3KB)
└── https://jsr.io/@std/net/1.0.0-rc.2/get_network_address.ts (1.68KB)
```

Dependency inspector works with any local or remote ES modules.

## JSON output

Use `--json` to get machine-readable output, useful for tooling and CI:

\>\_

```sh
deno info --json main.ts
```

## Cache location

`deno info` can be used to display information about cache location:

\>\_

```sh
deno info
DENO_DIR location: "/Users/deno/Library/Caches/deno"
Remote modules cache: "/Users/deno/Library/Caches/deno/deps"
TypeScript compiler cache: "/Users/deno/Library/Caches/deno/gen"
```

Command line usage:

```
deno info [OPTIONS] [file]
```

Show information about a module or the cache directories.

Get information about a module:

```
deno info jsr:@std/http/file-server
```

The following information is shown: local: Local path of the file type: JavaScript, TypeScript, or JSON emit: Local path of compiled source code (TypeScript only) dependencies: Dependency tree of the source file

## Options

`--allow-import, -I`<IP\_OR\_HOSTNAME>optional

Allow importing from remote hosts. Optionally specify allowed IP addresses and host names, with ports as necessary. Default value: deno.land:443,[jsr.io:443](http://jsr.io:443),[esm.sh:443](http://esm.sh:443),[raw.esm.sh:443](http://raw.esm.sh:443),[cdn.jsdelivr.net:443](http://cdn.jsdelivr.net:443),[raw.githubusercontent.com:443](http://raw.githubusercontent.com:443),[gist.githubusercontent.com:443](http://gist.githubusercontent.com:443).

`--cert`<FILE>

Load certificate authority from PEM encoded file.

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--deny-import`<IP\_OR\_HOSTNAME>optional

Deny importing from remote hosts. Optionally specify denied IP addresses and host names, with ports as necessary.

`--json`

UNSTABLE: Outputs the information in JSON format.

`--location`<HREF>

Show files used for origin bound APIs like the Web Storage API when running a script with `--location=<HREF>`.

`--no-config`

Disable automatic loading of the configuration file.

## Dependency management options

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`[--import-map](< https://docs.deno.com/runtime/manual/basics/import_maps>)`<FILE>

Load import map file from local file or remote URL.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.

`--no-npm`

Do not resolve npm modules.

`--no-remote`

Do not resolve remote modules.

`--node-modules-dir`<MODE>optional

Sets the node modules management mode for npm packages.

`--reload, -r`<CACHE\_BLOCKLIST>optional

Reload source code cache (recompile TypeScript) no value Reload everything jsr:@std/http/file-server,jsr:@std/assert/assert-equals Reloads specific modules npm: Reload all npm modules npm:chalk Reload specific npm module.

`--vendor`<vendor>optional

Toggles local vendor folder usage for remote modules and a node\_modules folder for npm packages.

