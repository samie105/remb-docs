---
title: "Auto-install"
source: "https://bun.com/docs/runtime/auto-install"
canonical_url: "https://bun.com/docs/runtime/auto-install"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:36.457Z"
content_hash: "7cc35998886c1993e709589f6221e03ee572674089cd2417c28fda9617e6b057"
menu_path: ["Auto-install"]
section_path: []
nav_prev: {"path": "bun/docs/runtime/archive/index.md", "title": "Archive"}
nav_next: {"path": "bun/docs/runtime/binary-data/index.md", "title": "Binary Data"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

If no `node_modules` directory is found in the working directory or higher, Bun will abandon Node.js-style module resolution in favor of the **Bun module resolution algorithm**. Under Bun-style module resolution, all imported packages are auto-installed on the fly into a [global module cache](/docs/pm/global-cache) during execution (the same cache used by [`bun install`](/docs/pm/cli/install)).

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import { foo } from "foo"; // install `latest` version

foo();
```

The first time you run this script, Bun will auto-install `"foo"` and cache it. The next time you run the script, it will use the cached version.

* * *

## 

[​

](#version-resolution)

Version resolution

To determine which version to install, Bun follows the following algorithm:

1.  Check for a `bun.lock` file in the project root. If it exists, use the version specified in the lockfile.
2.  Otherwise, scan up the tree for a `package.json` that includes `"foo"` as a dependency. If found, use the specified semver version or version range.
3.  Otherwise, use `latest`.

* * *

## 

[​

](#cache-behavior)

Cache behavior

Once a version or version range has been determined, Bun will:

1.  Check the module cache for a compatible version. If one exists, use it.
2.  When resolving `latest`, Bun will check if `package@latest` has been downloaded and cached in the last _24 hours_. If so, use it.
3.  Otherwise, download and install the appropriate version from the `npm` registry.

* * *

## 

[​

](#installation)

Installation

Packages are installed and cached into `<cache>/<pkg>@<version>`, so multiple versions of the same package can be cached at once. Additionally, a symlink is created under `<cache>/<pkg>/<version>` to make it faster to look up all versions of a package that exist in the cache.

* * *

## 

[​

](#version-specifiers)

Version specifiers

This entire resolution algorithm can be short-circuited by specifying a version or version range directly in your import statement.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import { z } from "zod@3.0.0"; // specific version
import { z } from "zod@next"; // npm tag
import { z } from "zod@^3.20.0"; // semver range
```

* * *

## 

[​

](#benefits)

Benefits

This auto-installation approach is useful for a few reasons:

*   **Space efficiency** — Each version of a dependency only exists in one place on disk. This is a huge space and time savings compared to redundant per-project installations.
*   **Portability** — To share simple scripts and gists, your source file is _self-contained_. No need to `zip` together a directory containing your code and config files. With version specifiers in `import` statements, even a `package.json` isn’t necessary.
*   **Convenience** — There’s no need to run `npm install` or `bun install` before running a file or script. Run it with `bun run`.
*   **Backwards compatibility** — Because Bun still respects the versions specified in `package.json` if one exists, you can switch to Bun-style resolution with a single command: `rm -rf node_modules`.

* * *

## 

[​

](#limitations)

Limitations

*   No Intellisense. TypeScript auto-completion in IDEs relies on the existence of type declaration files inside `node_modules`. We are investigating various solutions to this.
*   No [patch-package](https://github.com/ds300/patch-package) support

* * *

## 

[​

](#faq)

FAQ

How is this different from what pnpm does?

With pnpm, you have to run `pnpm install`, which creates a `node_modules` folder of symlinks for the runtime to resolve. By contrast, Bun resolves dependencies on the fly when you run a file; there’s no need to run any `install` command ahead of time. Bun also doesn’t create a `node_modules` folder.

How is this different from Yarn Plug'N'Play does?

With Yarn, you must run `yarn install` before you run a script. By contrast, Bun resolves dependencies on the fly when you run a file; there’s no need to run any `install` command ahead of time.Yarn Plug’N’Play also uses zip files to store dependencies. This makes dependency loading [slower at runtime](https://twitter.com/jarredsumner/status/1458207919636287490), as random access reads on zip files tend to be slower than the equivalent disk lookup.

How is this different from what Deno does?

Deno requires an `npm:` specifier before each npm `import`, lacks support for import maps via `compilerOptions.paths` in `tsconfig.json`, and has incomplete support for `package.json` settings. Unlike Deno, Bun does not currently support URL imports.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/auto-install.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/auto-install>)

[

JSX

Previous

](/docs/runtime/jsx)[

Plugins

Next

](/docs/runtime/plugins)
