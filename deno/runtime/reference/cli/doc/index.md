---
title: "deno doc"
source: "https://docs.deno.com/runtime/reference/cli/doc/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/doc/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:28:36.896Z"
content_hash: "903d7f75964f365c73ddcd950d943cf1fbc2a5301ba17caa9c6b4885bb3cb6cd"
menu_path: ["deno doc"]
section_path: []
content_language: "en"
nav_prev: {"path": "../deploy/index.md", "title": "deno deploy"}
nav_next: {"path": "../eval/index.md", "title": "deno eval"}
---

**On this page**

-   [Examples](#examples)
-   [Linting](#linting)
-   [Supported JSDoc features and tags](#supported-jsdoc-features-and-tags)
    -   [Supported Tags](#supported-tags)
    -   [Inline Linking](#inline-linking)
-   [HTML output](#html-output)
-   [JSON output](#json-output)
-   [Dependency management options](#dependency-management-options)
-   [Options](#options)
-   [Documentation options](#documentation-options)

## Examples

`deno doc` followed by a list of one or more source files will print the JSDoc documentation for each of the module's **exported** members.

For example, given a file `add.ts` with the contents:

```ts
/**
 * Adds x and y.
 * @param {number} x
 * @param {number} y
 * @returns {number} Sum of x and y
 */
export function add(x: number, y: number): number {
  return x + y;
}
```

Running the Deno `doc` command prints the function's JSDoc comment to `stdout`:

\>\_

```sh
deno doc add.ts
function add(x: number, y: number): number
  Adds x and y. @param {number} x @param {number} y @returns {number} Sum of x and y
```

## Linting

You can use `--lint` flag to check for problems in your documentation while it's being generated. `deno doc` will point out three kinds of problems:

1.  Error for an exported type from the root module referencing a non-exported type.
    -   Ensures API consumers have access to all the types the API uses. This can be suppressed by exporting the type from a root module (one of the files specified to `deno doc` on the command line) or by marking the type with an `@internal` jsdoc tag.
2.  Error for missing return type or property type on a **public** type.
    -   Ensures `deno doc` displays the return/property type and helps improve type checking performance.
3.  Error for missing JS doc comment on a **public** type.
    -   Ensures the code is documented. Can be suppressed by adding a jsdoc comment, or via an `@ignore` jsdoc tag to exclude it from the documentation. Alternatively, add an `@internal` tag to keep it in the docs, but signify it's internal.

For example:

/mod.ts

```ts
interface Person {
  name: string;
  // ...
}

export function getName(person: Person) {
  return person.name;
}
```

\>\_

```sh
deno doc --lint mod.ts
Type 'getName' references type 'Person' which is not exported from a root module.
Missing JS documentation comment.
Missing return type.
    at file:///mod.ts:6:1
```

These lints are meant to help you write better documentation and speed up type-checking in your projects. If any problems are found, the program exits with non-zero exit code and the output is reported to standard error.

## Supported JSDoc features and tags

Deno implements a large set of JSDoc tags, but does not strictly adhere to the JSDoc standard, but rather align with sensible standards and features provided by widely used tools and ecosystems in the same feature-space, like [TSDoc](https://tsdoc.org/) and [TypeDoc](https://typedoc.org/).

For any free-form text places, ie the main description of a JSDoc comment, the description of a parameter, etc. accept markdown.

### Supported Tags

The following tags are supported, being a selection of tags used and specified by JSDoc, TSDoc and TypeDoc:

-   [`constructor`/`class`](https://jsdoc.app/tags-class): mark a function to be a constructor.
-   [`ignore`](https://jsdoc.app/tags-ignore): ignore a symbol to be included in the output.
-   internal: mark a symbol to be used only for internal. In the HTML generator, the symbol will not get a listed entry, however it will still be generated and can be reached if a non-internal symbol links to it.
-   [`public`](https://jsdoc.app/tags-public): treat a symbol as public API. Equivalent of TypeScript `public` keyword.
-   [`private`](https://jsdoc.app/tags-private): treat a symbol as private API. Equivalent of TypeScript `private` keyword.
-   [`protected`](https://jsdoc.app/tags-protected): treat a property or method as protected API. Equivalent of TypeScript `protected` keyword.
-   [`readonly`](https://jsdoc.app/tags-readonly): mark a symbol to be readonly, meaning that it cannot be overwritten.
-   [`experimental`](https://tsdoc.org/pages/tags/experimental): mark a symbol as experimental, meaning that the API might change or be removed, or behaviour is not well-defined.
-   [`deprecated`](https://jsdoc.app/tags-deprecated): mark a symbol as deprecated, meaning that it is not supported anymore and might be removed in a future version.
-   [`module`](https://jsdoc.app/tags-module): this tag can be defined on a top-level JSDoc comment, which will treat that comment to be for the file instead of the subsequent symbol. A value can be specified, which will use the value as an identifier for the module (ie for default exports).
-   `category`/`group`: mark a symbol to be of a specific category/group. This is useful for grouping together various symbols together.
-   [`see`](https://jsdoc.app/tags-see): define an external reference related to the symbol.
-   [`example`](https://jsdoc.app/tags-example): define an example for the symbol. Unlike JSDoc, code examples need to be wrapped in triple backtick (markdown-style codeblocks), which aligns more with TSDoc than JSDoc.
-   `tags`: define additional custom labels for a symbol, via a comma separated list.
-   [`since`](https://jsdoc.app/tags-since): define since when the symbol has been available.
-   [`callback`](https://jsdoc.app/tags-callback): define a callback.
-   [`template`/`typeparam`/`typeParam`](https://tsdoc.org/pages/tags/typeparam): define a generic parameter.
-   [`prop`/`property`](https://jsdoc.app/tags-property): define a property on a symbol.
-   [`typedef`](https://jsdoc.app/tags-typedef): define a type.
-   [`param`/`arg`/`argument`](https://jsdoc.app/tags-param): define a parameter on a function.
-   [`return`/`returns`](https://jsdoc.app/tags-returns): define the return type and/or comment of a function.
-   [`throws`/`exception`](https://jsdoc.app/tags-throws): define what a function throws when called.
-   [`enum`](https://jsdoc.app/tags-enum): define an object to be an enum.
-   [`extends`/`augments`](https://jsdoc.app/tags-augments): define a type that a function extends on.
-   [`this`](https://jsdoc.app/tags-this): define what the `this` keyword refers to in a function.
-   [`type`](https://jsdoc.app/tags-type): define the type of a symbol.
-   [`default`](https://jsdoc.app/tags-default): define the default value for a variable, property or field.

### Inline Linking

Inline links let you specify links to other parts of the page, other symbols, or modules. Besides just supporting markdown-style links, [JSDoc style inline-links](https://jsdoc.app/tags-inline-link) are also supported.

For example, you can do`{@link https://docs.deno.com}`, which will be rendered as the following '[https://docs.deno.com](https://docs.deno.com)'. `{@linkcode https://docs.deno.com}` can also be used, to make it in a monospace font, and will be rendered roughly like this: '`https://docs.deno.com`'.

You can also specify a replacement label, via `{@link https://docs.deno.com | Deno Docs}`, which will use the text after `|` as the text to display instead of the link. The previous example would render as '[Deno Docs](https://docs.deno.com)'.

You can add inline links in your descriptions to other symbols via `{@link MySymbol}`.

For module linking, the same applies, but you use the `{@link [myModule]}` syntax. You can also link to symbols in a different module via `{@link [myModule].mysymbol}`.

## HTML output

Use the `--html` flag to generate a static site with documentation.

\>\_

```sh
deno doc --html --name="My library" ./mod.ts

deno doc --html --name="My library" --output=./documentation/ ./mod.ts

deno doc --html --name="My library" ./sub1/mod.ts ./sub2/mod.ts
```

The generated documentation is a static site with multiple pages that can be deployed to any static site hosting service.

A client-side search is included in the generated site, but is not available if user's browser has JavaScript disabled.

## JSON output

Use the `--json` flag to output the documentation in JSON format. This JSON format is consumed by the [deno doc website](https://github.com/denoland/docland) and is used to generate module documentation.

Command line usage:

```
deno doc [OPTIONS] [source_file]...
```

Show documentation for a module.

Output documentation to standard output:

```
deno doc ./path/to/module.ts
```

Output documentation in HTML format:

```
deno doc --html --name="My library" ./path/to/module.ts
```

Lint a module for documentation diagnostics:

```
deno doc --lint ./path/to/module.ts
```

Target a specific symbol:

```
deno doc ./path/to/module.ts MyClass.someField
```

Show documentation for runtime built-ins:

```
deno doc
```

```
deno doc --filter Deno.Listener
```

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

`--reload, -r`<CACHE\_BLOCKLIST>optional

Reload source code cache (recompile TypeScript) no value Reload everything jsr:@std/http/file-server,jsr:@std/assert/assert-equals Reloads specific modules npm: Reload all npm modules npm:chalk Reload specific npm module.

## Options

`--allow-import, -I`<IP\_OR\_HOSTNAME>optional

Allow importing from remote hosts. Optionally specify allowed IP addresses and host names, with ports as necessary. Default value: deno.land:443,[jsr.io:443](http://jsr.io:443),[esm.sh:443](http://esm.sh:443),[raw.esm.sh:443](http://raw.esm.sh:443),[cdn.jsdelivr.net:443](http://cdn.jsdelivr.net:443),[raw.githubusercontent.com:443](http://raw.githubusercontent.com:443),[gist.githubusercontent.com:443](http://gist.githubusercontent.com:443).

`--deny-import`<IP\_OR\_HOSTNAME>optional

Deny importing from remote hosts. Optionally specify denied IP addresses and host names, with ports as necessary.

## Documentation options

`--category-docs`<category-docs>

Path to a JSON file keyed by category and an optional value of a markdown doc.

`--default-symbol-map`<default-symbol-map>

Uses the provided mapping of default name to wanted name for usage blocks.

`--filter`<filter>

Dot separated path to symbol.

`--html`

Output documentation in HTML format.

`--json`

Output documentation in JSON format.

`--lint`

Output documentation diagnostics.

`--name`<name>

The name that will be used in the docs (ie for breadcrumbs).

`--output`<output>

Directory for HTML documentation output.

`--private`

Output private documentation.

`--strip-trailing-html`

Remove trailing .html from various links. Will still generate files with a .html extension.

`--symbol-redirect-map`<symbol-redirect-map>

Path to a JSON file keyed by file, with an inner map of symbol to an external link.
