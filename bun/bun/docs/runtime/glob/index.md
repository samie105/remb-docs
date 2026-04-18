---
title: "Glob"
source: "https://bun.com/docs/runtime/glob"
canonical_url: "https://bun.com/docs/runtime/glob"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:44.418Z"
content_hash: "352fa52b352d0880c4a1eabaa08a8c894f078d0f59119dfb05e8cd901abbdf54"
menu_path: ["Glob"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/file-system-router/index.md", "title": "File System Router"}
nav_next: {"path": "bun/bun/docs/runtime/file-types/index.md", "title": "File Types"}
---

## Quickstart

**Scan a directory for files matching `*.ts`**:

```
import { Glob } from "bun";

const glob = new Glob("**/*.ts");

// Scans the current working directory and each of its sub-directories recursively
for await (const file of glob.scan(".")) {
  console.log(file); // => "index.ts"
}
```

**Match a string against a glob pattern**:

```
import { Glob } from "bun";

const glob = new Glob("*.ts");

glob.match("index.ts"); // => true
glob.match("index.js"); // => false
```

`Glob` is a class which implements the following interface:

```
class Glob {
  scan(root: string | ScanOptions): AsyncIterable<string>;
  scanSync(root: string | ScanOptions): Iterable<string>;

  match(path: string): boolean;
}

interface ScanOptions {
  /**
   * The root directory to start matching from. Defaults to `process.cwd()`
   */
  cwd?: string;

  /**
   * Allow patterns to match entries that begin with a period (`.`).
   *
   * @default false
   */
  dot?: boolean;

  /**
   * Return the absolute path for entries.
   *
   * @default false
   */
  absolute?: boolean;

  /**
   * Indicates whether to traverse descendants of symbolic link directories.
   *
   * @default false
   */
  followSymlinks?: boolean;

  /**
   * Throw an error when symbolic link is broken
   *
   * @default false
   */
  throwErrorOnBrokenSymlink?: boolean;

  /**
   * Return only files.
   *
   * @default true
   */
  onlyFiles?: boolean;
}
```

## Supported Glob Patterns

Bun supports the following glob patterns:

### `?` - Match any single character

```
const glob = new Glob("???.ts");
glob.match("foo.ts"); // => true
glob.match("foobar.ts"); // => false
```

### `*` - Matches zero or more characters, except for path separators (`/` or `\`)

```
const glob = new Glob("*.ts");
glob.match("index.ts"); // => true
glob.match("src/index.ts"); // => false
```

### `**` - Match any number of characters including `/`

```
const glob = new Glob("**/*.ts");
glob.match("index.ts"); // => true
glob.match("src/index.ts"); // => true
glob.match("src/index.js"); // => false
```

### `[ab]` - Matches one of the characters contained in the brackets, as well as character ranges

```
const glob = new Glob("ba[rz].ts");
glob.match("bar.ts"); // => true
glob.match("baz.ts"); // => true
glob.match("bat.ts"); // => false
```

You can use character ranges (e.g `[0-9]`, `[a-z]`) as well as the negation operators `^` or `!` to match anything _except_ the characters contained within the braces (e.g `[^ab]`, `[!a-z]`)

```
const glob = new Glob("ba[a-z][0-9][^4-9].ts");
glob.match("bar01.ts"); // => true
glob.match("baz83.ts"); // => true
glob.match("bat22.ts"); // => true
glob.match("bat24.ts"); // => false
glob.match("ba0a8.ts"); // => false
```

### `{a,b,c}` - Match any of the given patterns

```
const glob = new Glob("{a,b,c}.ts");
glob.match("a.ts"); // => true
glob.match("b.ts"); // => true
glob.match("c.ts"); // => true
glob.match("d.ts"); // => false
```

These match patterns can be deeply nested (up to 10 levels), and contain any of the wildcards from above.

### `!` - Negates the result at the start of a pattern

```
const glob = new Glob("!index.ts");
glob.match("index.ts"); // => false
glob.match("foo.ts"); // => true
```

### `\` - Escapes any of the special characters above

```
const glob = new Glob("\\!index.ts");
glob.match("!index.ts"); // => true
glob.match("index.ts"); // => false
```

## Node.js `fs.glob()` compatibility

Bun also implements Node.js’s `fs.glob()` functions with additional features:

```
import { glob, globSync, promises } from "node:fs";

// Array of patterns
const files = await promises.glob(["**/*.ts", "**/*.js"]);

// Exclude patterns
const filtered = await promises.glob("**/*", {
  exclude: ["node_modules/**", "*.test.*"],
});
```

All three functions (`fs.glob()`, `fs.globSync()`, `fs.promises.glob()`) support:

*   Array of patterns as the first argument
*   `exclude` option to filter results


