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
---
**On this page**

-   [Basic usage](#basic-usage)
-   [Watch mode](#watch-mode)
-   [Check formatting in CI](#check-formatting-in-ci)
-   [Formatting stdin](#formatting-stdin)
-   [Configuring the formatter](#configuring-the-formatter)
-   [Including and excluding files](#including-and-excluding-files)
-   [Supported file types](#supported-file-types)
-   [Ignoring code](#ignoring-code)
    -   [JavaScript / TypeScript / JSONC](#javascript-%2F-typescript-%2F-jsonc)
    -   [Markdown / HTML / CSS](#markdown-%2F-html-%2F-css)
    -   [YAML](#yaml)
-   [Options](#options)
-   [Formatting options](#formatting-options)
-   [File watching options](#file-watching-options)

Deno ships with a built-in code formatter based on [dprint](https://dprint.dev/) that auto-formats your code to a consistent style. For a broader overview, see [Linting and Formatting](/runtime/fundamentals/linting_and_formatting/).

## Basic usage

Format all supported files in the current directory:

\>\_

```sh
deno fmt
```

Format specific files or directories:

\>\_

```sh
deno fmt main.ts src/
```

## Watch mode

Automatically re-format files when they change:

\>\_

```sh
deno fmt --watch
```

## Check formatting in CI

Use `--check` to verify files are formatted without modifying them. The command exits with a non-zero status code if any files are unformatted:

\>\_

```sh
deno fmt --check
```

Add `--fail-fast` to stop on the first unformatted file instead of reporting all of them, which is useful in large codebases:

\>\_

```sh
deno fmt --check --fail-fast
```

## Formatting stdin

Format code piped through stdin — useful for editor integrations:

\>\_

```sh
cat main.ts | deno fmt -
```

## Configuring the formatter

Customize formatting options in your `deno.json`:

deno.json

```json
{
  "fmt": {
    "useTabs": false,
    "lineWidth": 80,
    "indentWidth": 2,
    "semiColons": true,
    "singleQuote": false,
    "proseWrap": "preserve"
  }
}
```

See the [Configuration](/runtime/fundamentals/configuration/#formatting) page for all available options.

## Including and excluding files

Specify which files to format in `deno.json`:

deno.json

```json
{
  "fmt": {
    "include": ["src/"],
    "exclude": ["src/testdata/", "src/generated/**/*.ts"]
  }
}
```

You can also exclude files from the command line:

\>\_

```sh
deno fmt --ignore=dist/,build/
```

## Supported file types

| File Type | Extension | Notes |
| --- | --- | --- |
| JavaScript | `.js`, `.cjs`, `.mjs` |  |
| TypeScript | `.ts`, `.mts`, `.cts` |  |
| JSX | `.jsx` |  |
| TSX | `.tsx` |  |
| Markdown | `.md`, `.mkd`, `.mkdn`, `.mdwn`, `.mdown`, `.markdown` |  |
| JSON | `.json` |  |
| JSONC | `.jsonc` |  |
| CSS | `.css` |  |
| HTML | `.html` |  |
| [Nunjucks](https://mozilla.github.io/nunjucks/) | `.njk` |  |
| [Vento](https://github.com/ventojs/vento) | `.vto` |  |
| YAML | `.yml`, `.yaml` |  |
| Sass | `.sass` |  |
| SCSS | `.scss` |  |
| LESS | `.less` |  |
| Jupyter Notebook | `.ipynb` |  |
| Astro | `.astro` | Requires `--unstable-component` flag or `"unstable": ["fmt-component"]` config option. |
| Svelte | `.svelte` | Requires `--unstable-component` flag or `"unstable": ["fmt-component"]` config option. |
| Vue | `.vue` | Requires `--unstable-component` flag or `"unstable": ["fmt-component"]` config option. |
| SQL | `.sql` | Requires `--unstable-sql` flag or `"unstable": ["fmt-sql"]` config option. |

Note

**`deno fmt` can format code snippets in Markdown files.** Snippets must be enclosed in triple backticks and have a language attribute.

## Ignoring code

### JavaScript / TypeScript / JSONC

Ignore formatting code by preceding it with a `// deno-fmt-ignore` comment:

```ts
// deno-fmt-ignore
export const identity = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1,
];
```

Or ignore an entire file by adding a `// deno-fmt-ignore-file` comment at the top of the file.

### Markdown / HTML / CSS

Ignore formatting next item by preceding it with `<!--- deno-fmt-ignore -->` comment:

HTML

```html
<html>
  <body>
    <p>
      Hello there
      <!-- deno-fmt-ignore -->
    </p>
  </body>
</html>
```

To ignore a section of code, surround the code with `<!-- deno-fmt-ignore-start -->` and `<!-- deno-fmt-ignore-end -->` comments.

Or ignore an entire file by adding a `<!-- deno-fmt-ignore-file -->` comment at the top of the file.

### YAML

Ignore formatting next item by preceding it with `# deno-fmt-ignore` comment:

HTML

```html
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
