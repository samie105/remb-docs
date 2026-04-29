---
title: "Module Resolution"
source: "https://bun.com/docs/runtime/module-resolution"
canonical_url: "https://bun.com/docs/runtime/module-resolution"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:41.445Z"
content_hash: "d9ef5c93f8bf861137645ee6c45dbd5e8b2b5ee05602a9cee287e5ab5b64ad71"
menu_path: ["Module Resolution"]
section_path: []
nav_prev: {"path": "../markdown/index.md", "title": "Markdown"}
nav_next: {"path": "../networking/dns/index.md", "title": "DNS"}
---

# Use it with bun build:
bun build --conditions="react-server" --target=bun ./app/foo/route.js

# Use it with bun's runtime:
bun --conditions="react-server" ./app/foo/route.js
```

You can also use `conditions` programmatically with `Bun.build`:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)build.ts

```
await Bun.build({
  conditions: ["react-server"],
  target: "bun",
  entryPoints: ["./app/foo/route.js"],
});
```

* * *

## Path re-mapping

Bun supports import path re-mapping through TypeScript’s [`compilerOptions.paths`](https://www.typescriptlang.org/tsconfig#paths) in `tsconfig.json`, which works well with editors. If you aren’t a TypeScript user, you can achieve the same behavior by using a [`jsconfig.json`](https://code.visualstudio.com/docs/languages/jsconfig) in your project root.

tsconfig.json

```
{
  "compilerOptions": {
    "paths": {
      "config": ["./config.ts"], // map specifier to file
      "components/*": ["components/*"] // wildcard matching
    }
  }
}
```

Bun also supports [Node.js-style subpath imports](https://nodejs.org/api/packages.html#subpath-imports) in `package.json`, where mapped paths must start with `#`. This approach doesn’t work as well with editors, but both options can be used together.

package.json

```
{
  "imports": {
    "#config": "./config.ts", // map specifier to file
    "#components/*": "./components/*" // wildcard matching
  }
}
```

Low-level details of CommonJS interop in Bun

Bun’s JavaScript runtime has native support for CommonJS. When Bun’s JavaScript transpiler detects usages of `module.exports`, it treats the file as CommonJS. The module loader will then wrap the transpiled module in a function shaped like this:

```
(function (module, exports, require) {
  // transpiled module
})(module, exports, require);
```

`module`, `exports`, and `require` are very much like the `module`, `exports`, and `require` in Node.js. These are assigned via a [`with scope`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with) in C++. An internal `Map` stores the `exports` object to handle cyclical `require` calls before the module is fully loaded.Once the CommonJS module is successfully evaluated, a Synthetic Module Record is created with the `default` ES Module [export set to `module.exports`](https://github.com/oven-sh/bun/blob/9b6913e1a674ceb7f670f917fc355bb8758c6c72/src/bun.js/bindings/CommonJSModuleRecord.cpp#L212-L213) and keys of the `module.exports` object are re-exported as named exports (if the `module.exports` object is an object).When using Bun’s bundler, this works differently. The bundler will wrap the CommonJS module in a `require_${moduleName}` function which returns the `module.exports` object.

* * *

The `import.meta` object is a way for a module to access information about itself. It’s part of the JavaScript language, but its contents are not standardized. Each “host” (browser, runtime, etc) is free to implement any properties it wishes on the `import.meta` object. Bun implements the following properties.

/path/to/project/file.ts

```
import.meta.dir; // => "/path/to/project"
import.meta.file; // => "file.ts"
import.meta.path; // => "/path/to/project/file.ts"
import.meta.url; // => "file:///path/to/project/file.ts"

import.meta.main; // `true` if this file is directly executed by `bun run`
// `false` otherwise

import.meta.resolve("zod"); // => "file:///path/to/project/node_modules/zod/index.js"
```

Property

Description

`import.meta.dir`

Absolute path to the directory containing the current file, e.g. `/path/to/project`. Equivalent to `__dirname` in CommonJS modules (and Node.js)

`import.meta.dirname`

An alias to `import.meta.dir`, for Node.js compatibility

`import.meta.env`

An alias to `process.env`.

`import.meta.file`

The name of the current file, e.g. `index.tsx`

`import.meta.path`

Absolute path to the current file, e.g. `/path/to/project/index.ts`. Equivalent to `__filename` in CommonJS modules (and Node.js)

`import.meta.filename`

An alias to `import.meta.path`, for Node.js compatibility

`import.meta.main`

Indicates whether the current file is the entrypoint to the current `bun` process. Is the file being directly executed by `bun run` or is it being imported?

`import.meta.resolve`

Resolve a module specifier (e.g. `"zod"` or `"./file.tsx"`) to a url. Equivalent to [`import.meta.resolve` in browsers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#resolve). Example: `import.meta.resolve("zod")` returns `"file:///path/to/project/node_modules/zod/index.ts"`

`import.meta.url`

A `string` url to the current file, e.g. `file:///path/to/project/index.ts`. Equivalent to [`import.meta.url` in browsers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#url)
