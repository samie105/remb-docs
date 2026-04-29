---
title: "deno fmt"
source: "https://docs.deno.com/runtime/reference/cli/fmt/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/fmt/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:29:29.883Z"
content_hash: "98158520ba8d7518de848f33752f8993a6c0e04f4a0f6ef9bf7e9909978c904f"
menu_path: ["deno fmt"]
section_path: []
content_language: "en"
nav_prev: {"path": "../eval/index.md", "title": "deno eval"}
nav_next: {"path": "../info/index.md", "title": "deno info"}
---

# deno-fmt-ignore aaaaaa: bbbbbbb
```

Command line usage:

```
deno fmt [OPTIONS] [files]...
```

Auto-format various file types.

```
deno fmt myfile1.ts myfile2.ts
```

Supported file types are:

```
JavaScript, TypeScript, Markdown, JSON(C) and Jupyter Notebooks
```

Supported file types which are behind corresponding unstable flags (see formatting options):

```
HTML, CSS, SCSS, SASS, LESS, YAML, Svelte, Vue, Astro and Angular
```

Format stdin and write to stdout:

```
cat file.ts | deno fmt -
```

Check if the files are formatted:

```
deno fmt --check
```

Ignore formatting code by preceding it with an ignore comment:

```
// deno-fmt-ignore
```

Ignore formatting a file by adding an ignore comment at the top of the file:

```
// deno-fmt-ignore-file
```

## Options

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--no-config`

Disable automatic loading of the configuration file.

`--permit-no-files`

Don't return an error code if no files were found.

## Formatting options

`--check`

Check if the source files are formatted.

`--ext`<ext>

Set content type of the supplied file.

`--fail-fast`

Stop checking files on first format error.

`--ignore`<ignore>

Ignore formatting particular source files.

`--indent-width`<indent-width>

Define indentation width \[default: 2\]

`--line-width`<line-width>

Define maximum line width \[default: 80\]

`--no-semicolons`<no-semicolons>optional

Don't use semicolons except where necessary \[default: false\]

`--prose-wrap`<prose-wrap>

Define how prose should be wrapped \[default: always\]

`--single-quote`<single-quote>optional

Use single quotes \[default: false\]

`--unstable-component`

Enable formatting Svelte, Vue, Astro and Angular files.

`--unstable-sql`

Enable formatting SQL files.

`--use-tabs`<use-tabs>optional

Use tabs instead of spaces for indentation \[default: false\]

## File watching options

`--no-clear-screen`

Do not clear terminal screen when under watch mode.

`--watch`

Watch for file changes and restart process automatically. Only local files from entry point module graph are watched.

`--watch-exclude`<FILES>optional

Exclude provided files/patterns from watch mode.
