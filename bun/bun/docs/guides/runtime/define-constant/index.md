---
title: "Define and replace static globals & constants"
source: "https://bun.com/docs/guides/runtime/define-constant"
canonical_url: "https://bun.com/docs/guides/runtime/define-constant"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:26.105Z"
content_hash: "3d66aef2eb8f7312f01e79f8b3b2d36ec6cbc378408396ba2fac52ff89e7f550"
menu_path: ["Define and replace static globals & constants"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/runtime/codesign-macos-executable/index.md", "title": "Codesign a single-file JavaScript executable on macOS"}
nav_next: {"path": "bun/bun/docs/guides/runtime/delete-directory/index.md", "title": "Delete directories"}
---

# JSON
bun --define AWS='{"ACCESS_KEY":"abc","SECRET_KEY":"def"}' src/index.ts
```

Those will be transformed into the equivalent JavaScript code. From:

```
console.log(AWS.ACCESS_KEY); // => "abc"
```

To:

```
console.log("abc");
```

### 

[​

](#replace-values-with-other-properties)

Replace values with other properties

You can also pass properties to the `--define` flag. For example, to replace all usages of `console.write` with `console.log`, you can use the following command

```
bun --define console.write=console.log src/index.ts
```

That transforms the following input:

```
console.write("Hello, world!");
```

Into the following output:

```
console.log("Hello, world!");
```

## 

[​

](#how-is-this-different-than-setting-a-variable)

How is this different than setting a variable?

You can also set `process.env.NODE_ENV` to `"production"` in your code, but that won’t help with dead code elimination. In JavaScript, property accesses can have side effects. Getters & setters can be functions, and even dynamically defined (due to prototype chains and Proxy). Even if you set `process.env.NODE_ENV` to `"production"`, on the next line, it is not safe for static analysis tools to assume that `process.env.NODE_ENV`is`"production"`.

## 

[​

](#how-is-this-different-than-find-and-replace-or-string-replacement)

How is this different than find-and-replace or string replacement?

The `--define` flag operates on the AST (Abstract Syntax Tree) level, not on the text level. It happens during the transpilation process, which means it can be used in optimizations like dead code elimination. String replacement tools tend to have escaping issues and replace unintended parts of the code.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/define-constant.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/define-constant>)

[

Build-time constants with --define

Previous

](/docs/guides/runtime/build-time-constants)[

Install and run Bun in GitHub Actions

Next

](/docs/guides/runtime/cicd)


